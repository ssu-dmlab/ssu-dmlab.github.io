import hashlib
import mimetypes
import os
import re
from datetime import datetime

import requests
import yaml

'''
Google Sheet(Apps Script) 에서 데이터를 받아 _data/*.yml 로 저장하는 스크립트.

- Publications(International Conference/Journal, Domestic Conference)의 Image 링크는
  다운로드해서 저장소(assets/images/publications/)에 커밋하고, yml 에는 로컬 경로를 저장한다.
- Publications의 Description 컬럼(논문 설명 .txt 파일의 Drive 링크, 선택)은 내용을 받아와서
  "Abstract:" / "Contribution:" 구분자로 섹션을 나눠 각 논문 항목의 Abstract/Contribution 필드로 저장한다.
  -> publications.md 팝업에서 실제 내용으로 보여주려면 별도로 publications.md 수정이 필요함(채팅 참고).
- News 탭 데이터를 받아 실제 news.md / index.md 가 기대하는 소문자 스키마
  (date, title, content, keyword, link, image)로 변환해 _data/news.yml 로 저장한다.

** ssu-dmlab.github.io 저장소 실측 기준 **
- toyaml.py는 리포 루트에서 실행되고(.github/workflows/update_data.yml), _data/*.yml 을 커밋한다.
- 이미지 경로 컨벤션은 assets/img/ 가 아니라 assets/images/ 이다 (assets/images/news, /paper, /hero 등 기존 사용 확인).
- _data/news.yml은 news.md, index.md 에서 news.date / news.title / news.content / news.keyword / news.link /
  news.image 필드명(소문자)으로 카드+팝업을 렌더링하므로, Apps Script가 돌려주는 키(헤더 그대로, 대문자 포함)를
  이 스키마에 맞게 변환해야 한다.
'''

PAPER_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwdXZXgYgRf-t5uqe3RBTwOLR9F0sbu0DBylDI7Y-upzzFA3-CDr4kWqrbbp4ZKoZ-Pww/exec"
SEMINAR_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzkHvVaplMOJp9tkEoJTX7-X0hy6o6IQz94tm4xyUBaA-Pf50LuEtwqOCgbHmModBDc5A/exec"

IMAGE_DIR_PUBLICATIONS = "assets/images/publications"
IMAGE_DIR_NEWS = "assets/images/news"


def fetch_sheet(sheet_name):
    resp = requests.get(PAPER_SCRIPT_URL, params={"sheet": sheet_name})
    resp.raise_for_status()
    return resp.json()


def extract_text(field):
    """Apps Script의 default 케이스는 셀에 하이퍼링크가 있으면 {"text":..,"url":..},
    없으면 순수 문자열을 돌려준다. 두 경우 모두에서 '보여줄 텍스트'를 뽑아낸다."""
    if isinstance(field, dict):
        return field.get("text") or field.get("url") or ""
    return field or ""


def extract_url(field):
    """위와 동일한 두 형태에서 '실제 링크(URL)'를 뽑아낸다."""
    if isinstance(field, dict):
        return field.get("url") or field.get("text") or ""
    return field or ""


def to_drive_direct_url(url):
    """Google Drive 공유 링크를 직접 다운로드 가능한 링크로 변환한다."""
    if "drive.google.com" not in url:
        return url
    m = re.search(r"/d/([a-zA-Z0-9_-]+)", url) or re.search(r"[?&]id=([a-zA-Z0-9_-]+)", url)
    if not m:
        return url
    return f"https://drive.google.com/uc?export=download&id={m.group(1)}"


def fetch_drive_text(url):
    """Google Drive에 올린 순수 텍스트(.txt) 파일의 내용을 그대로 가져온다.
    (Google Docs 문서가 아니라, 진짜 .txt 파일을 업로드하고 '링크가 있는 모든 사용자 - 뷰어'로
    공유해야 동작한다. 이미지 다운로드와 접근 권한 요구사항이 동일하다.)"""
    if not url:
        return ""
    try:
        resp = requests.get(to_drive_direct_url(url), timeout=30, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[warn] failed to fetch description text: {url} ({e})")
        return ""
    if not resp.encoding:
        resp.encoding = "utf-8"
    return resp.text


# txt 파일 안에서 이 이름으로 시작하는 줄을 섹션 구분자로 인식한다 (대소문자, 콜론 유무 무관).
# 예: "Abstract:" / "abstract" / "Contribution:" 모두 인식됨.
DESCRIPTION_SECTIONS = ["Abstract", "Contribution"]
_SECTION_RE = re.compile(r"^\s*(" + "|".join(DESCRIPTION_SECTIONS) + r")\s*:?\s*$", re.IGNORECASE)


def parse_description_sections(text):
    """'Abstract:\\n...\\n\\nContribution:\\n...' 형태의 텍스트를
    {"Abstract": "...", "Contribution": "..."} 로 나눈다."""
    sections = {}
    current_key = None
    buf = []
    for line in text.splitlines():
        m = _SECTION_RE.match(line)
        if m:
            if current_key:
                sections[current_key] = "\n".join(buf).strip()
            current_key = m.group(1).capitalize()
            buf = []
        else:
            buf.append(line)
    if current_key:
        sections[current_key] = "\n".join(buf).strip()
    return sections


def slugify(text, max_len=40):
    """사람이 봐서 어떤 항목인지 알 수 있게, 파일명에 쓸 짧은 표시용 문자열을 만든다.
    한글/영문/숫자만 남기고 나머지는 '-'로 바꾼 뒤 길이를 제한한다."""
    if not text:
        return ""
    text = str(text).strip().lower()
    text = re.sub(r"[^\w\-]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_len].rstrip("-")


def paper_title_text(entry):
    """논문 Title 필드(문자열 또는 {"en":..,"kr":..})에서 표시용 제목 텍스트를 뽑아낸다."""
    t = entry.get("Title")
    if isinstance(t, dict):
        return t.get("en") or t.get("kr") or ""
    return t or ""


def download_image(url, image_dir, slug=""):
    """url의 이미지를 image_dir 에 다운로드하고, 사이트에서 쓸 절대경로(/assets/...)를 반환한다.
    파일명은 "{slug}-{url 해시}.확장자" 형태로 만든다 (slug가 없으면 해시만 사용).
    - 논문: slug = 논문 제목 앞부분 (예: our-work-on-lightweight-tensor-com-4a1b2c3d4e5f.png)
    - 뉴스: slug = 날짜 (예: 2026-01-13-4a1b2c3d4e5f.png)
    중복 체크는 slug가 아니라 'url 해시가 파일명에 포함되어 있는지'로 하기 때문에,
    나중에 논문 제목/날짜가 바뀌어도(=slug가 바뀌어도) 같은 이미지를 다시 받지는 않는다.
    다만 그 경우 파일명은 예전 slug 그대로 남아있으니, 참고로만 알아두면 된다."""
    if not url:
        return ""

    # "link"처럼 실제 URL이 아닌 텍스트가 셀에 잘못 들어간 경우: 요청을 시도하지 않고 바로 빈 값 처리.
    if not re.match(r"^https?://", url.strip(), re.IGNORECASE):
        print(f"[warn] not a valid image URL, skipping: {url!r}")
        return ""

    os.makedirs(image_dir, exist_ok=True)
    url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()[:12]

    for fname in os.listdir(image_dir):
        if fname.startswith(url_hash + ".") or f"-{url_hash}." in fname:
            return f"/{image_dir}/{fname}"

    try:
        resp = requests.get(to_drive_direct_url(url), timeout=30, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[warn] failed to download image: {url} ({e})")
        return ""  # 실패한 원본 URL을 그대로 남기지 않고 빈 값으로 → placeholder로 안전하게 폴백

    content_type = resp.headers.get("Content-Type", "").split(";")[0].strip()
    ext = mimetypes.guess_extension(content_type) or ".jpg"
    if ext == ".jpe":
        ext = ".jpg"

    fname = f"{slug}-{url_hash}{ext}" if slug else f"{url_hash}{ext}"
    with open(os.path.join(image_dir, fname), "wb") as f:
        f.write(resp.content)

    return f"/{image_dir}/{fname}"


def localize_publication_images(entries):
    """각 논문 항목의 Image 필드(구글시트 'Image' 컬럼)를 다운로드해 로컬 경로로 치환한다.
    파일명은 "논문 제목-해시.확장자" 형태로 저장해서 어떤 논문 이미지인지 알아보기 쉽게 한다.
    주의: publications.md가 아직 paper.Image 를 화면에 그리지 않으므로, 지금 단계에서는
    '다운로드해서 저장소에 반영'까지만 하고 실제 카드에 썸네일로 보여주는 건 별도 작업이다."""
    for entry in entries:
        if "Image" in entry:
            src = extract_url(entry["Image"])
            slug = slugify(paper_title_text(entry))
            entry["Image"] = download_image(src, IMAGE_DIR_PUBLICATIONS, slug=slug)
    return entries


# 논문 설명 txt 파일의 Drive 링크를 넣는 컬럼 이름으로 이 중 아무거나 인식한다.
# (시트에 "Description"이든 "Abstract"든 편한 이름으로 만들어도 되도록 유연하게 처리)
DESCRIPTION_LINK_COLUMNS = ["Description", "Abstract", "Content", "Details"]


def attach_paper_description(entries):
    """논문 설명 txt 파일의 Drive 링크(구글시트의 Description/Abstract 등 컬럼)를 받아서
    Abstract / Contribution 두 필드로 나눠 entry에 채워 넣는다.
    해당 컬럼이 없거나 값이 비어있으면 그냥 건너뛴다(빈 문자열로 채워짐).
    주의: 링크가 들어있던 원래 컬럼 값(예: Abstract 컬럼에 있던 링크 텍스트)은
    파싱된 실제 Abstract 텍스트로 덮어써진다."""
    for entry in entries:
        url = ""
        for col in DESCRIPTION_LINK_COLUMNS:
            if col in entry:
                url = extract_url(entry[col])
                if url:
                    break

        entry["Abstract"] = ""
        entry["Contribution"] = ""
        if not url:
            continue

        text = fetch_drive_text(url)
        if not text:
            continue

        sections = parse_description_sections(text)
        entry["Abstract"] = sections.get("Abstract", "")
        entry["Contribution"] = sections.get("Contribution", "")
    return entries


def save_yaml(data, path):
    with open(path, "w", encoding="utf8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


def format_display_date(iso_date):
    """Apps Script가 돌려주는 ISO 문자열('2026-01-13T00:00:00.000Z')을
    기존 _data/news.yml 표기 방식인 'Jan 13, 2026' 형태로 바꾼다.
    (news.md/index.md는 date 필드에 별도 Liquid date 필터 없이 그대로 출력하기 때문에,
    여기서 미리 사람이 읽기 좋은 문자열로 만들어둬야 한다.)"""
    if not iso_date:
        return ""
    try:
        dt = datetime.strptime(str(iso_date)[:10], "%Y-%m-%d")
    except ValueError:
        return str(iso_date)
    return f"{dt.strftime('%b')} {dt.day}, {dt.year}"


'''
Publications
'''
international_conference = attach_paper_description(localize_publication_images(fetch_sheet("International Conference")))
international_journal = attach_paper_description(localize_publication_images(fetch_sheet("International Journal")))
domestic_conference = attach_paper_description(localize_publication_images(fetch_sheet("Domestic Conference")))

save_yaml(international_conference, "_data/international_conference.yml")
save_yaml(international_journal, "_data/international_journal.yml")
save_yaml(domestic_conference, "_data/domestic_conference.yml")

'''
Seminars
'''
seminars = requests.get(SEMINAR_SCRIPT_URL).json()
save_yaml(seminars, "_data/seminars.yml")

'''
News

Google Sheet "News" 탭 컬럼 구성(권장):
  Date, Title(선택), Content, Keyword, Link(선택), Image(선택)
  - Date: 날짜 셀(구글시트 Date 타입)로 입력 -> Apps Script가 ISO로 파싱, 여기서 "Jan 13, 2026" 형태로 재포맷
  - Title: 카드/팝업 제목으로 쓸 짧은 텍스트. 비워두면 news.md/index.md가 Content를 대신 제목으로 사용한다
    (`news.title | default: news.content` 폴백 방식).
  - Content: 카드/팝업에 보여줄 본문 텍스트 (news.md, index.md 둘 다 HTML 태그는 strip해서 보여줌)
  - Keyword: "Paper" / "Award" 로 쓰면 전용 배지 색상+아이콘이 붙고, 그 외 값은 기본(공지) 배지로 표시됨
  - Link: 카드 클릭 시 이동할 외부/내부 링크 (Keyword가 Paper면 /publications로 자동 연결되어 비워둬도 됨)
  - Image: 카드 썸네일. 비워두면 news.md/index.md가 기본 이미지(/assets/images/news/default_news169.png)를 사용

_data/news.yml은 news.md / index.md 에서 news.date / news.title / news.content / news.keyword / news.link /
news.image (소문자) 필드로 이미 카드+팝업 UI가 구현되어 있으므로, 그 스키마에 맞춰 변환한다.
'''
raw_news = fetch_sheet("News")

news = []
for item in raw_news:
    iso_date = item.get("Date", "")
    image_url = extract_url(item.get("Image")) if item.get("Image") else ""
    date_slug = str(iso_date)[:10] if iso_date else ""  # 예: "2026-01-13"
    news.append({
        "date": format_display_date(iso_date),
        "_sort_date": str(iso_date),  # 정렬 전용, 저장 직전에 제거
        "title": extract_text(item.get("Title")) if item.get("Title") else "",
        "content": extract_text(item.get("Content")),
        "keyword": extract_text(item.get("Keyword")),
        "link": extract_url(item.get("Link")) if item.get("Link") else "",
        "image": download_image(image_url, IMAGE_DIR_NEWS, slug=date_slug) if image_url else "",
    })

# news.md/index.md는 파일에 저장된 순서를 그대로 사용하므로(별도 sort 없음),
# 여기서 최신순으로 정렬해서 저장해야 한다.
news.sort(key=lambda x: x["_sort_date"], reverse=True)
for n in news:
    del n["_sort_date"]

save_yaml(news, "_data/news.yml")