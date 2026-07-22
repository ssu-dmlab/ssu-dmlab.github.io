---
layout: article
permalink: /publications/
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* ==========================================================================
     ★ Publications 통합형 탭 및 모던 카드 레이아웃 스타일
     ========================================================================== */
  .pub-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px 0;
  }

  /* 상단 탭 디자인 */
  .pub-tabs {
    display: flex;
    gap: 12px;
    margin-bottom: 35px;
    padding-bottom: 12px;
  }
  .pub-tab-btn {
    padding: 10px 24px;
    text-decoration: none;
    color: #64748b;
    font-weight: 700;
    font-size: 1.05rem;
    border-radius: 6px;
    transition: all 0.25s ease;
    border: 1px solid transparent;
    cursor: pointer;
  }
  .pub-tab-btn:hover {
    background-color: #f1f5f9;
    color: #0f172a;
  }
  
  /* 활성화된 탭 스타일 */
  .pub-tab-btn.is-active {
    background-color: #0f172a !important;
    color: #ffffff !important;
  }

  .pub-content-section {
    display: none;
    opacity: 0;
    transition: opacity 0.25s ease-in-out;
  }

  /* 활성화되어 화면에 나타날 때의 스타일 */
  .pub-content-section.is-visible {
    display: block;
    opacity: 1;
  }

  /* 연도별 그룹 헤딩 */
  .pub-year-heading {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0f172a;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
  }

  /* 모던 카드 형태의 논문 리스트 프레임 */
  .pub-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
  }
  .pub-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 20px 24px;
    margin-bottom: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
    /* index.md와 동일하게 부드러운 cubic-bezier 애니메이션 적용 */
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .pub-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
    border-color: #00B4D8;
  }
  .pub-card:hover .pub-card-title {
    color: #1A365D !important;
    text-decoration: underline !important;
    text-decoration-color: #1A365D !important;
  }

  /* 카드 내부 텍스트 및 저자 요소 */
  .pub-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
  }
  /* [추가] 타이틀에도 부드러운 색상 변화를 위해 transition 추가 */
  .pub-card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.4;
    margin: 0 !important;
    transition: color 0.25s ease, text-decoration 0.25s ease;
  }
  .pub-venue-badge {
    display: inline-block;
    padding: 4px 10px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #2563eb;
    background: #eff6ff;
    border-radius: 4px;
    white-space: nowrap;
  }
  .pub-card-authors {
    font-size: 0.95rem;
    color: #475569;
    line-height: 1.5;
  }
  .pub-author-me {
    font-weight: 700;
    color: #0f172a;
    text-decoration: underline;
  }

  /* 푸터 및 링크 메타 정보 */
  .pub-card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 8px;
    padding-top: 12px;
    border-top: 1px dashed #e2e8f0;
  }
  .pub-meta-date {
    font-size: 0.85rem;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .pub-links-group {
    display: flex;
    gap: 8px;
  }
  .pub-btn-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    font-size: 0.85rem;
    font-weight: 600;
    color: #0f172a!important;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.2s ease;
  }
  .pub-btn-link:hover {
    background: #0f172a;
    color: #f1f5f9!important;
    border-color: #00B4D8;
  }
  .pub-modal {
    display: none; /* 기본 숨김 */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(15, 23, 42, 0.6); /* 뒷배경 어둡게 */
    backdrop-filter: blur(4px); /* 뒷배경 블러 처리 */
    z-index: 9999;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .pub-modal.is-active {
    display: flex;
    opacity: 1;
  }

  .pub-modal-content {
    background: #ffffff;
    border-radius: 12px;
    width: 90%;
    max-width: 700px;
    max-height: 85vh;
    overflow-y: auto;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.15), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    position: relative;
    transform: translateY(20px);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    padding: 35px;
    box-sizing: border-box;
  }

  .pub-modal.is-active .pub-modal-content {
    transform: translateY(0);
  }

  /* 닫기 버튼 */
  .pub-modal-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: none;
    border: none;
    font-size: 1.5rem;
    color: #64748b;
    cursor: pointer;
    transition: color 0.2s;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
  }
  .pub-modal-close:hover {
    background-color: #f1f5f9;
    color: #0f172a;
  }

  /* 모달 내부 타이틀 및 디테일 구역 */
  .pub-modal-venue {
    display: inline-block;
    padding: 4px 10px;
    font-size: 0.8rem;
    font-weight: 700;
    color: #2563eb;
    background: #eff6ff;
    border-radius: 4px;
    margin-bottom: 12px;
  }
  .pub-modal-title {
    font-size: 1.5rem;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.4;
    margin-top: 0;
    margin-bottom: 15px;
  }
  .pub-modal-authors {
    font-size: 1rem;
    color: #475569;
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 1px solid #e2e8f0;
  }
  .pub-modal-section {
    margin-bottom: 20px;
  }
  .pub-modal-section-title {
    font-size: 1rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .pub-modal-section-desc {
    font-size: 0.95rem;
    color: #334155;
    line-height: 1.6;
    margin: 0;
  }

  /* 카드 호버 시 클릭할 수 있음을 나타내는 커서 스타일 추가 */
  .pub-card {
    cursor: pointer;
  }

  @media (max-width: 640px) {
    /* 카드 내부 여백 및 간격 축소 */
    .pub-card {
      padding: 16px 18px;
      gap: 10px;
    }

    /* 헤더: 제목과 Badge가 작은 화면에서 자연스럽게 줄바꿈되도록 변경 */
    .pub-card-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 8px;
    }

    /* 푸터: 날짜와 링크 그룹을 수직(Column)으로 배치하여 겹침 차단 */
    .pub-card-footer {
      flex-direction: column;
      align-items: flex-start;
      gap: 12px;
    }

    /* 링크 버튼 그룹: 공간이 부족하면 자연스럽게 다음 줄로 내려가도록 줄바꿈 허용 */
    .pub-links-group {
      flex-wrap: wrap;
      gap: 6px;
      width: 100%;
    }

    /* 모바일에서 버튼 크기와 여백을 미세하게 조정하여 가독성 및 터치 영역 확보 */
    .pub-btn-link {
      padding: 5px 10px;
      font-size: 0.8rem;
    }
  }
</style>

<div class="pub-container">

  <div class="pub-tabs">
    <a href="#international" id="tab-btn-international" class="pub-tab-btn" onclick="setTimeout(handleTabChange, 0)">International</a>
    <a href="#domestic" id="tab-btn-domestic" class="pub-tab-btn" onclick="setTimeout(handleTabChange, 0)">Domestic</a>
  </div>

  {%- assign local_empty_array = "" | split: "," -%}
  {%- assign member_array = site.data.members | map: "name" | map: "en" -%}
  {%- assign years = "2026,2025,2024,2023,2022,2021,2020" | split: "," -%}

  <div id="pub-content-international" class="pub-content-section">
    {% for y in years %}
      {% assign has_paper_in_year = false %}
      {% for paper in site.data.international_journal %}{% if paper.Year == y or paper.Date contains y %}{% assign has_paper_in_year = true %}{% endif %}{% endfor %}
      {% for paper in site.data.international_conference %}{% if paper.Year == y or paper.Date contains y %}{% assign has_paper_in_year = true %}{% endif %}{% endfor %}

      {% if has_paper_in_year %}
        <div class="pub-year-heading">{{ y }}</div>
        <ul class="pub-list js-sortable-list">
          
          {% for paper in site.data.international_journal %}
            {% if paper.Year == y or paper.Date contains y %}
              {% assign sort_time = paper.Date | date: "%Y%m%d" %}
              <li class="pub-card" data-time="{{ sort_time | default: 0 }}">
                <div class="pub-card-header">
                  <h4 class="pub-card-title">{{ paper.Title.en | default: paper.Title.ko | default: paper.Title }}</h4>
                  <div class="pub-venue-badge">{{ paper.Venue.text | default: paper.Publisher | default: "Journal" }}</div>
                </div>
                <div class="pub-card-authors">
                  {% if paper.Authors %}
                    {% for author in paper.Authors %}
                      {% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
                      {% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
                      {% if forloop.last == true %}and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}{% else %}{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}, {% endif %}
                    {% endfor %}
                  {% else %}{{ paper.Author }}{% endif %}
                </div>
                <div class="pub-card-footer">
                  <div class="pub-meta-date"><i class="far fa-calendar-alt"></i> <span>{{ paper.Date | date: "%b %Y" }}</span></div>
                  <div class="pub-links-group">
                    {% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
                    {% if paper.BIB.url != nil %}<a href="{{ paper.BIB.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
                    {% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
                    {% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
                  </div>
                </div>
              </li>
            {% endif %}
          {% endfor %}

          {% for paper in site.data.international_conference %}
            {% if paper.Year == y or paper.Date contains y %}
              {% assign sort_time = paper.Date | date: "%Y%m%d" %}
              <li class="pub-card" data-time="{{ sort_time | default: 0 }}">
                <div class="pub-card-header">
                  <h4 class="pub-card-title">{{ paper.Title.en | default: paper.Title.ko | default: paper.Title }}</h4>
                  {% assign short_year = y | slice: 2, 2 %}
                  <div class="pub-venue-badge">{{ paper.Venue.text | default: paper.Publisher | default: "Conference" }} '{{ short_year }}</div>
                </div>
                <div class="pub-card-authors">
                  {% if paper.Authors %}
                    {% for author in paper.Authors %}
                      {% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
                      {% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
                      {% if forloop.last == true %}and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}{% else %}{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}, {% endif %}
                    {% endfor %}
                  {% else %}{{ paper.Author }}{% endif %}
                </div>
                <div class="pub-card-footer">
                  <div class="pub-meta-date"><i class="far fa-calendar-alt"></i> <span>{{ paper.Date | date: "%b %Y" }}</span></div>
                  <div class="pub-links-group">
                    {% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
                    {% if paper.BIB.url != nil %}<a href="{{ paper.BIB.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
                    {% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
                    {% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
                  </div>
                </div>
              </li>
            {% endif %}
          {% endfor %}

        </ul>
      {% endif %}
    {% endfor %}
  </div>

  <div id="pub-content-domestic" class="pub-content-section">
    {% for y in years %}
      {% assign has_paper_in_year = false %}
      {% for paper in site.data.domestic_journal %}{% if paper.Year == y or paper.Date contains y %}{% assign has_paper_in_year = true %}{% endif %}{% endfor %}
      {% for paper in site.data.domestic_conference %}{% if paper.Year == y or paper.Date contains y %}{% assign has_paper_in_year = true %}{% endif %}{% endfor %}

      {% if has_paper_in_year %}
        <div class="pub-year-heading">{{ y }}</div>
        <ul class="pub-list js-sortable-list">
          
          {% for paper in site.data.domestic_journal %}
            {% if paper.Year == y or paper.Date contains y %}
              {% assign sort_time = paper.Date | date: "%Y%m%d" %}
              <li class="pub-card" data-time="{{ sort_time | default: 0 }}">
                <div class="pub-card-header">
                  <h4 class="pub-card-title">{{ paper.Title.ko | default: paper.Title.en | default: paper.Title }}</h4>
                  <div class="pub-venue-badge">{{ paper.Venue.text | default: paper.Publisher | default: "Journal" }}</div>
                </div>
                <div class="pub-card-authors">
                  {% if paper.Authors %}
                    {% for author in paper.Authors %}
                      {% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
                      {% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
                      {% if forloop.last == true %}and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}{% else %}{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}, {% endif %}
                    {% endfor %}
                  {% else %}{{ paper.Author }}{% endif %}
                </div>
                <div class="pub-card-footer">
                  <div class="pub-meta-date"><i class="far fa-calendar-alt"></i> <span>{{ paper.Date | date: "%b %Y" }}</span></div>
                  <div class="pub-links-group">
                    {% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
                    {% if paper.BIB.url != nil %}<a href="{{ paper.BIB.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
                    {% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
                    {% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
                  </div>
                </div>
              </li>
            {% endif %}
          {% endfor %}

          {% for paper in site.data.domestic_conference %}
            {% if paper.Year == y or paper.Date contains y %}
              {% assign sort_time = paper.Date | date: "%Y%m%d" %}
              <li class="pub-card" data-time="{{ sort_time | default: 0 }}">
                <div class="pub-card-header">
                  <h4 class="pub-card-title">{{ paper.Title.ko | default: paper.Title.en | default: paper.Title }}</h4>
                  {% assign short_year = y | slice: 2, 2 %}
                  <div class="pub-venue-badge">{{ paper.Venue.text | default: paper.Publisher | default: "Conference" }} '{{ short_year }}</div>
                </div>
                <div class="pub-card-authors">
                  {% if paper.Authors %}
                    {% for author in paper.Authors %}
                      {% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
                      {% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
                      {% if forloop.last == true %}and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}{% else %}{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}, {% endif %}
                    {% endfor %}
                  {% else %}{{ paper.Author }}{% endif %}
                </div>
                <div class="pub-card-footer">
                  <div class="pub-meta-date"><i class="far fa-calendar-alt"></i> <span>{{ paper.Date | date: "%b %Y" }}</span></div>
                  <div class="pub-links-group">
                    {% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
                    {% if paper.BIB.url != nil %}<a href="{{ paper.BIB.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
                    {% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
                    {% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
                  </div>
                </div>
              </li>
            {% endif %}
          {% endfor %}

        </ul>
      {% endif %}
    {% endfor %}
  </div>

</div>
<!-- 논문 디테일 모달 팝업 구조 -->
<div id="pubDetailModal" class="pub-modal">
  <div class="pub-modal-content">
    <button class="pub-modal-close" id="modalCloseBtn">
      <i class="fas fa-times"></i>
    </button>
    <div id="modalVenue" class="pub-modal-badge"></div>
    <h3 id="modalTitle" class="pub-modal-title"></h3>
    <div id="modalAuthors" class="pub-modal-authors"></div>
    
    <div class="pub-modal-section">
      <div class="pub-modal-section-title"><i class="fas fa-align-left me-2"></i> Abstract</div>
      <p id="modalAbstract" class="pub-modal-section-desc"></p>
    </div>
    
    <div class="pub-modal-section">
      <div class="pub-modal-section-title"><i class="fas fa-award me-2"></i> Contribution</div>
      <p id="modalContribution" class="pub-modal-section-desc"></p>
    </div>
  </div>
</div>

<script>
  // DOM 정렬은 무거운 작업이므로 페이지 로드 시 딱 '한 번'만 실행하도록 플래그 설정
  var isSorted = false;

  function sortPublicationsByTime() {
    if (isSorted) return; // 이미 정렬되었다면 실행하지 않음
    
    document.querySelectorAll('.js-sortable-list').forEach(list => {
      const cards = Array.from(list.querySelectorAll('.pub-card'));
      
      cards.sort((a, b) => {
        const timeA = parseInt(a.getAttribute('data-time'), 10) || 0;
        const timeB = parseInt(b.getAttribute('data-time'), 10) || 0;
        return timeB - timeA;
      });
      
      cards.forEach(card => list.appendChild(card));
    });
    
    isSorted = true; // 정렬 완료 플래그 활성화
  }

  function handleTabChange(forcedHash) {
    var hash = forcedHash || window.location.hash || '#international';
    
    if (hash.indexOf('#') !== -1) {
      hash = '#' + hash.split('#')[1];
    }

    var intSection = document.getElementById('pub-content-international');
    var domSection = document.getElementById('pub-content-domestic');
    var intBtn = document.getElementById('tab-btn-international');
    var domBtn = document.getElementById('tab-btn-domestic');

    if (!intSection || !domSection || !intBtn || !domBtn) return;

    // 1. 기존 활성화 클래스 및 display 제거
    intSection.classList.remove('is-visible');
    domSection.classList.remove('is-visible');
    intSection.style.display = 'none';
    domSection.style.display = 'none';
    
    intBtn.classList.remove('is-active');
    domBtn.classList.remove('is-active');

    // 2. 대상 섹션 결정
    var targetSection = (hash === '#domestic') ? domSection : intSection;
    var targetBtn = (hash === '#domestic') ? domBtn : intBtn;

    // 3. 부드러운 페이드인 처리를 위한 브라우저 렌더링 큐 활용
    targetSection.style.display = 'block';
    targetBtn.classList.add('is-active');
    
    // display: block이 적용된 직후 opacity가 변해야 애니메이션이 먹히므로 requestAnimationFrame 사용
    requestAnimationFrame(() => {
      targetSection.classList.add('is-visible');
    });
  }

  window.addEventListener('hashchange', function() {
    handleTabChange();
  });

  window.addEventListener('DOMContentLoaded', () => {
    sortPublicationsByTime();
    handleTabChange();
  });

  // Pjax 및 네비게이션 클릭 리스너 (불필요한 중복 정렬 제거로 버벅임 해결)
  document.addEventListener('click', function(e) {
    const link = e.target.closest('a');
    if (!link) return;

    const href = link.getAttribute('href');
    if (!href) return;

    if (href.includes('#international') || href.includes('#domestic')) {
      const targetHash = href.includes('#domestic') ? '#domestic' : '#international';
      
      // 먼저 한 번 정렬을 확실히 보장한 후 전환
      sortPublicationsByTime();
      handleTabChange(targetHash);
      
      setTimeout(function() {
        handleTabChange(targetHash);
      }, 50);
    }
  }, true);
  // 팝업(모달) 제어 로직
  document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('pubDetailModal');
    var closeBtn = document.getElementById('modalCloseBtn');
    
    var modalVenue = document.getElementById('modalVenue');
    var modalTitle = document.getElementById('modalTitle');
    var modalAuthors = document.getElementById('modalAuthors');
    var modalAbstract = document.getElementById('modalAbstract');
    var modalContribution = document.getElementById('modalContribution');

    // 더미 데이터 생성 (실제 논문에서 개별 필드를 YAML 데이터로 관리하게 되면 나중에 연동할 수 있습니다)
    var dummyAbstract = "In this research, we propose a novel paradigm addressing key issues in standard machine learning models. By leveraging multi-modal representation frameworks and optimizing the underlying loss landscapes, our architecture achieves significantly higher generalization bounds compared to conventional models. We evaluate our method across extensive real-world datasets, demonstrating its effectiveness, lightweight footprint, and outstanding scalability.";
    var dummyContribution = "1. Designed and implemented a highly scalable algorithm capable of processing massive graph structures in real time.\n2. Introduced a dynamic pruning technique that reduces VRAM utilization by up to 45%.\n3. Demonstrated state-of-the-art (SOTA) performance across three main benchmark tasks.";

    // 1. 카드 클릭 시 팝업 열기 (이벤트 위임 방식으로 Pjax 및 동적 리스트 보장)
    document.addEventListener('click', function(e) {
      // PDF 파일 다운로드나 외부 코드 링크 등 카드 내부의 실제 '버튼/링크'를 클릭했을 때는 팝업이 뜨지 않도록 예외 처리
      if (e.target.closest('.pub-links-group') || e.target.closest('a')) {
        return;
      }

      var card = e.target.closest('.pub-card');
      if (!card) return;

      e.preventDefault();

      // 클릭한 카드 내부의 실제 데이터 파싱
      var titleText = card.querySelector('.pub-card-title').innerText;
      var authorsText = card.querySelector('.pub-card-authors').innerText;
      var venueText = card.querySelector('.pub-venue-badge').innerText;

      // 모달 엘리먼트에 내용 대입
      modalVenue.innerText = venueText;
      modalTitle.innerText = titleText;
      modalAuthors.innerText = authorsText;
      
      // 더미 텍스트 대입 (개행 문자는 <br> 태그 등으로 가독성 확보)
      modalAbstract.innerText = dummyAbstract;
      modalContribution.innerHTML = dummyContribution.replace(/\n/g, '<br>');

      // 모달 활성화 클래스 추가
      modal.classList.add('is-active');
      document.body.style.overflow = 'hidden'; // 뒷배경 스크롤 방지
    });

    // 2. 닫기 버튼 누르면 팝업 닫기
    if (closeBtn) {
      closeBtn.addEventListener('click', closeModal);
    }

    // 3. 팝업 바깥 어두운 배경(딤처리 구역) 클릭하면 닫기
    if (modal) {
      modal.addEventListener('click', function(e) {
        if (e.target === modal) {
          closeModal();
        }
      });
    }

    function closeModal() {
      modal.classList.remove('is-active');
      document.body.style.overflow = ''; // 스크롤 잠금 해제
    }

    // ESC 키 입력 시 팝업 닫기 지원
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && modal.classList.contains('is-active')) {
        closeModal();
      }
    });
  });
</script>