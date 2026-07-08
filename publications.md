---
layout: article
title: "Publications"
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* ==========================================================================
     ★ Publications 전용 모던 카드 리스트 CSS (격리 설계)
     ========================================================================== */
  .pub-section-title {
    font-size: 1.75rem;
    font-weight: 800;
    color: #0f172a;
    margin-top: 2.5rem;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
  }
  .pub-year-heading {
    font-size: 1.15rem;
    font-weight: 600;
    color: #64748b;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
  }
  
  /* 카드 형태의 논문 리스트 프레임 */
  .pub-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 20px 24px;
    margin-bottom: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
    position: relative;
    box-sizing: border-box;
    transition: all 0.25s ease;
  }
  .pub-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.04);
  }

  /* 상단 타이틀 및 배지 영역 레이아웃 */
  .pub-card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
    width: 100%;
    margin-bottom: 6px;
  }
  .pub-card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.4;
    margin: 0 !important;
  }
  
  /* 우측 저널/학회 약어 및 연도 배지 */
  .pub-venue-badge {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 14px;
    font-size: 0.9rem;
    font-weight: 700;
    color: #475569;
    white-space: nowrap;
    text-align: center;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  /* 저자 표시 스타일 */
  .pub-card-authors {
    font-size: 1rem;
    color: #475569;
    margin-bottom: 14px;
    line-height: 1.4;
  }
  .pub-author-me {
    text-decoration: underline;
    font-weight: 600;
  }

  /* 하단 메타 정보 및 리소스 링크 바 */
  .pub-card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: auto;
    border-top: 1px solid #f1f5f9;
    padding-top: 12px;
  }
  .pub-meta-date {
    font-size: 0.85rem;
    color: #94a3b8;
    font-weight: 500;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  
  .pub-links-group {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  
  /* 리소스 에셋 소형 버튼 컴포넌트 */
  .pub-btn-link {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background-color: #f1f5f9;
    color: #475569 !important;
    font-size: 0.82rem;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 4px;
    text-decoration: none !important;
    transition: all 0.2s ease;
  }
  .pub-btn-link:hover {
    background-color: #e2e8f0;
    color: #1e293b !important;
  }
</style>

{% assign member_array = site.data.members | map: "name" | map: "en" %}

{% if site.data.preprints != blank %}
<h2 class="pub-section-title">Preprints</h2>
{% endif %}

{% assign current_year = "" %}
{% for paper in site.data.preprints %}
{% if paper.international == true %}
{% if paper.year != current_year %}
<div class="pub-year-heading">{{ paper.year }}</div>
{% assign current_year = paper.year %}
{% endif %}
<div class="pub-card">
<div class="pub-card-top">
<h4 class="pub-card-title">{{ paper.title }}</h4>
<div class="pub-venue-badge">
{% if paper.type == "arxiv" %}<i class="fas fa-globe"></i>{% endif %}
{{ paper.publisher.venue }}
</div>
</div>
<div class="pub-card-authors">
{% for author in paper.authors %}
{% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
{% assign is_co_first = false %}{% if paper.first.size > 1 and paper.first contains author %}{% assign is_co_first = true %}{% endif %}
{% if forloop.last == true %}
and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}
{% else %}
{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %},
{% endif %}
{% endfor %}
</div>
<div class="pub-card-footer">
<div class="pub-meta-date">
<i class="far fa-calendar-alt"></i> {{ paper.month }} {{ paper.year }}
</div>
<div class="pub-links-group">
{% if paper.pdf != nil %}<a href="{{ paper.pdf }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
{% if paper.bib != nil %}<a href="{{ paper.bib }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
{% if paper.slide != nil %}<a href="{{ paper.slide }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
{% if paper.code != nil %}<a href="{{ paper.code }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
</div>
</div>
</div>
{% endif %}
{% endfor %}


<h2 class="pub-section-title">International Conference</h2>

{% assign current_year = "" %}
{% assign sorted_IC = site.data.international_conference | sort: 'Date' | reverse %}
{% for paper in sorted_IC %}
{% if paper.Year != current_year %}
<div class="pub-year-heading">{{ paper.Year }}</div>
{% assign current_year = paper.Year %}
{% endif %}
<div class="pub-card">
<div class="pub-card-top">
<h4 class="pub-card-title">{{ paper.Title }}</h4>
<div class="pub-venue-badge">
{{ paper.Venue.text | default: "Conference" }} {{ paper.Year }}
</div>
</div>
<div class="pub-card-authors">
{% for author in paper.Authors %}
{% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
{% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
{% if forloop.last == true %}
and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}
{% else %}
{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %},
{% endif %}
{% endfor %}
</div>
<div class="pub-card-footer">
<div class="pub-meta-date">
<i class="far fa-calendar-alt"></i> {{ paper.Date | date: "%b %Y" }}
</div>
<div class="pub-links-group">
{% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
{% if paper.BIB.url != nil %}<a href="{{ paper.BIB.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
{% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
{% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
</div>
</div>
</div>
{% endfor %}


<h2 class="pub-section-title">International Journal</h2>

{% assign current_year = "" %}
{% assign sorted_IJ = site.data.international_journal | sort: 'Date' | reverse %}
{% for paper in sorted_IJ %}
{% if paper.Year != current_year %}
<div class="pub-year-heading">{{ paper.Year }}</div>
{% assign current_year = paper.Year %}
{% endif %}
<div class="pub-card">
<div class="pub-card-top">
<h4 class="pub-card-title">{{ paper.Title }}</h4>
<div class="pub-venue-badge">
{{ paper.Venue.text | default: "Journal" }} {{ paper.Year }}
</div>
</div>
<div class="pub-card-authors">
{% for author in paper.Authors %}
{% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
{% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
{% if forloop.last == true %}
and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}
{% else %}
{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %},
{% endif %}
{% endfor %}
</div>
<div class="pub-card-footer">
<div class="pub-meta-date">
<i class="far fa-calendar-alt"></i> {{ paper.Date | date: "%b %Y" }}
</div>
<div class="pub-links-group">
{% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
{% if paper.BIB.url != nil %}<a href="{{ paper.BIB.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-import"></i> BibTex</a>{% endif %}
{% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
{% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
</div>
</div>
</div>
{% endfor %}


<h2 class="pub-section-title">Domestic Conference</h2>

{% assign current_year = "" %}
{% assign sorted_DC = site.data.domestic_conference | sort: 'Date' | reverse %}
{% for paper in sorted_DC %}
{% if paper.Year != current_year %}
<div class="pub-year-heading">{{ paper.Year }}</div>
{% assign current_year = paper.Year %}
{% endif %}
<div class="pub-card">
<div class="pub-card-top">
<h4 class="pub-card-title">{{ paper.Title.en | default: paper.Title }}</h4>
<div class="pub-venue-badge">
{{ paper.Venue.text | default: "Domestic" }} {{ paper.Year }}
</div>
</div>
<div class="pub-card-authors">
{% for author in paper.Authors %}
{% if member_array contains author %}{% assign is_member = true %}{% else %}{% assign is_member = false %}{% endif %}
{% assign is_co_first = false %}{% if paper.First.size > 1 and paper.First contains author %}{% assign is_co_first = true %}{% endif %}
{% if forloop.last == true %}
and {% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %}
{% else %}
{% if is_member %}<span class="pub-author-me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% if is_co_first %}<sup>*</sup>{% endif %},
{% endif %}
{% endfor %}
</div>
<div class="pub-card-footer">
<div class="pub-meta-date">
<i class="far fa-calendar-alt"></i> {{ paper.Date | date: "%b %Y" }}
</div>
<div class="pub-links-group">
{% if paper.Paper.url != nil %}<a href="{{ paper.Paper.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-pdf"></i> Paper</a>{% endif %}
{% if paper.Slide.url != nil %}<a href="{{ paper.Slide.url }}" class="pub-btn-link" target="_blank"><i class="fas fa-file-powerpoint"></i> Slide</a>{% endif %}
{% if paper.Code.url != nil %}<a href="{{ paper.Code.url }}" class="pub-btn-link" target="_blank"><i class="fab fa-github"></i> Code</a>{% endif %}
</div>
</div>
</div>
{% endfor %}