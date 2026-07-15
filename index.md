---
layout: article
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* ==========================================================================
     ★ 깜빡임 박멸: 전역 간섭 없는 순수 CSS 격리형 페이드 카루셀 시스템
     ========================================================================== */
  .custom-carousel { 
    position: relative; 
    width: 100%; 
    overflow: hidden; 
  }
  .custom-carousel-inner { 
    position: relative; width: 100%; height: 100%;
  }
  .custom-carousel-item { 
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; z-index: 1; transition: opacity 0.8s ease-in-out; pointer-events: none;
  }
  .custom-carousel-item.vslab-active { 
    position: relative; display: block; opacity: 1; z-index: 2; pointer-events: auto;
  }
  
  #pubMiniCarousel .custom-carousel-item { position: absolute; }
  #pubMiniCarousel .custom-carousel-item.vslab-active { position: relative; }

  /* 컨트롤 인터페이스 기본 제어 (공통 기본값 초기화) */
  .custom-carousel-control-prev, .custom-carousel-control-next { 
    position: absolute; z-index: 10; display: flex; align-items: center; justify-content: center; padding: 0; background: none; border: 0; opacity: 0.7; transition: opacity .15s ease; cursor: pointer;
  }
  .custom-carousel-control-prev:hover, .custom-carousel-control-next:hover { opacity: 1; }
  
  /* 테마 규격 격리형 순수 하단 배치용 그리드 시스템 (Row / Col 독립 구현) */
  .vslab-row { display: flex; flex-wrap: wrap; margin-right: -12px; margin-left: -12px; }
  .vslab-row > * { box-sizing: border-box !important; flex-shrink: 0; width: 100%; max-width: 100%; padding-right: 12px; padding-left: 12px; margin-top: 0; margin-bottom: 0; }
  .vslab-col-6 { width: 50%; }
  .vslab-col-4 { width: 33.33333333%; }
  @media (max-width: 992px) {
    .vslab-col-md-12 { width: 100% !important; }
  }

  /* ==========================================================================
     3. 연구실 메인 테마 핏 레이아웃
     ========================================================================== */
  .vslab-container { width: 100%; margin: 0 auto; padding: 0; }
  .vslab-heading { 
    font-size: 1.75rem; 
    font-weight: 800; 
    color: #0f172a; 
    margin-top: 1.5rem; 
    margin-bottom: 35px; 
    letter-spacing: -0.02em; 
    text-transform: uppercase; 
    border-bottom: 2px solid #1A365D !important;
  }

  /* Main Hero Carousel 외부 프레임 */
  .container-hero { margin-top: 10px; margin-bottom: 80px; overflow: hidden; border-radius: 8px; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08); position: relative; }
  .hero-slide-link { display: block; text-decoration: none; color: inherit; }
  .hero-slide { position: relative; width: 100%; height: 480px; background-color: #f8fafc; overflow: hidden; }
  .main-hero-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: linear-gradient(to right, rgba(15, 23, 42, 0.9) 35%, rgba(15, 23, 42, 0.4) 100%), url('/assets/images/hero/slide_main.jpg'); background-size: cover; background-position: center; z-index: 1; }
  .main-hero-wrapper { position: relative; z-index: 2; height: 100%; padding: 60px; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; max-width: 850px; }
  .main-hero-content { color: #ffffff !important; text-shadow: 0 2px 15px rgba(0, 0, 0, 0.6); }
  .main-hero-content .hero-title { font-size: 2.85rem; font-weight: 800; margin-top: 0; margin-bottom: 20px; letter-spacing: -0.03em; color: #ffffff !important; }
  .main-hero-content .hero-desc { font-size: 1.15rem; line-height: 1.65; color: #cbd5e1 !important; margin-bottom: 32px; display: block; }
  
  .tb-hero-container { display: flex; flex-direction: column; width: 100%; height: 100%; }
  .tb-hero-img { width: 100%; height: 300px; background-size: cover; background-position: center; background-repeat: no-repeat; background-color: #f8fafc; position: relative; }
  
  /* [변경] 버튼 배치를 위해 position: relative 추가 및 우측 패딩 조정 */
  .tb-hero-text { width: 100%; height: 180px; background-color: #0f172a; padding: 20px 100px 20px 30px; display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; position: relative; }
  .tb-hero-text .hero-title { font-size: 1.75rem; font-weight: 800; line-height: 1.3; margin-top: 0px; margin-bottom: 0px; letter-spacing: -0.02em; color: #ffffff !important; }
  .tb-hero-text .hero-badge { font-size: 0.7rem; letter-spacing: 0.05em; display:block; margin-bottom: 6px; }
  /* [추가] 마우스를 올렸을 때(hover) 제목을 제외한 모든 하위 요소의 밑줄을 강제로 제거 */
  .hero-slide-link:hover,
  .hero-slide-link:hover *,
  .pub-slider-link:hover,
  .pub-slider-link:hover * {
    text-decoration: none !important;
  }
  .hero-slide-link:hover .hero-title,
  .pub-slider-link:hover .pub-hero-title {
    color: #ffffff !important;
    text-decoration-line: underline !important;
    text-decoration-color: #00B4D8 !important;
  }
  
  .btn-hero { background-color: #ffffff !important; color: #0f172a !important; font-weight: 600; font-size: 0.85rem; padding: 8px 24px; border: 2px solid #ffffff !important; border-radius: 4px; transition: all 0.3s ease; text-decoration: none; display: inline-block; width: fit-content; letter-spacing: 0.05em; }
  .btn-hero:hover { background-color: transparent !important; color: #ffffff !important; }
  .main-hero-content .btn-hero { margin-top: 0px; padding: 12px 30px; font-size: 0.95rem; }
  .tb-hero-text .btn-hero { margin-top: 14px; }

  /* ==========================================================================
     ★ 내비게이션 버튼 우하단 정밀 재배치 (Hero & Publications 공통 적용)
     ========================================================================== */
  .control-icon-bg { background-color: rgba(255, 255, 255, 0.85); padding: 8px; border-radius: 50%; box-shadow: 0 2px 6px rgba(0,0,0,0.15); display: flex; align-items: center; justify-content: center; transition: all 0.2s; }
  .control-icon-bg:hover { background-color: #ffffff; transform: scale(1.05); }
  
  .carousel-prev-icon-svg, .carousel-next-icon-svg { width: 0.85rem; height: 0.85rem; display: inline-block; background-size: 100% 100%; }
  .carousel-prev-icon-svg { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e"); }
  .carousel-next-icon-svg { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e"); }

  /* 1. Main Hero Carousel 버튼 위치 (첫 번째 슬라이드 포함 일괄 적용) */
  #milabStyleCarousel .custom-carousel-control-prev,
  #milabStyleCarousel .custom-carousel-control-next { top: auto !important; bottom: 20px !important; width: auto !important; height: auto !important; }
  #milabStyleCarousel .custom-carousel-control-prev { right: 64px !important; left: auto !important; }
  #milabStyleCarousel .custom-carousel-control-next { right: 20px !important; left: auto !important; }

  /* 첫 번째 슬라이드(전체 배경형)일 때 버튼 디자인 다크 테마에 맞춰 소폭 최적화 */
  .is-first-slide .control-icon-bg { background-color: rgba(255, 255, 255, 0.2) !important; border: 1px solid rgba(255, 255, 255, 0.3); box-shadow: none !important; }
  .is-first-slide .carousel-prev-icon-svg { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e"); }
  .is-first-slide .carousel-next-icon-svg { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e"); }

  /* ==========================================================================
     ★ Latest News 결합형 카드 디자인 리뉴얼 
     ========================================================================== */
  .news-grid-container { margin-bottom: 80px; }
  .news-card-wrapper { margin-bottom: 24px; }
  
  .news-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px; 
    height: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden; 
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    box-sizing: border-box;
  }
  .news-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
    border-color: #00B4D8;
  }
  .news-card:hover .news-card-text a {
    color: #1A365D; /* 호버 시 제목 글자색을 Deep Navy로 강조 */
  }

  .news-card-img-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9; 
    overflow: hidden;
    background-color: #f1f5f9; 
    border-bottom: 1px solid #e2e8f0;
  }
  .news-card-bg {
    width: 100%;
    height: 100%;
    background-size: cover; 
    background-position: center;
    background-repeat: no-repeat;
  }

  .news-card-body {
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex-grow: 1; 
  }

  .news-card-badge {
    display: inline-block;
    padding: 6px 12px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    border-radius: 6px !important;
    margin-bottom: 12px;
    width: fit-content;
    color: #ffffff !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* 키워드별 고유 배경색 */
  .bg-vslab-paper { 
    background-color: #0056b3 !important; /* 파란색 */
  }
  .bg-vslab-award { 
    background-color: #f39c12 !important; /* 골드/노란색 */
  }
  .bg-vslab-default { 
    background-color: #7f8c8d !important; /* 기본 회색 */
  }
  .news-card-text { 
    font-size: 1.05rem; 
    font-weight: 700; 
    color: #1e293b; 
    line-height: 1.45; 
    margin-top: 0px !important;
    margin-bottom: 16px; 
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    word-break: break-word;
  }
  .news-card-text a { color: #0f172a; text-decoration: none; }
  .news-card-text a:hover { text-decoration: underline; }
  
  .news-card-date { 
    font-size: 0.85rem; 
    color: #94a3b8; 
    font-weight: 500; 
    margin-top: auto; 
  }

  /* Recent Publications */
  .bottom-split-container { 
    margin-bottom: 100px; 
  }
  .pub-slider-link {
    display: block; text-decoration: none; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.06); transition: transform 0.3s ease; 
  }
  /* [수정] 호버 시 하단 그림자를 #00B4D8 색상으로 변경 */
  .pub-slider-link:hover { 
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2) 
  }
  .pub-mini-hero { 
    width: 100%; position: relative; background-color: #ffffff; 
  }
  .pub-hero-img-wrap { 
    position: relative; width: 100%; aspect-ratio: 16 / 9; overflow: hidden; background-color: #f8fafc; 
  }
  .pub-hero-bg { 
    width: 100%; height: 100%; background-size: contain; background-position: center; background-repeat: no-repeat; 
  }
  
  /* [변경] 버튼 배치를 위해 position: relative 추가 및 우측 패딩 조정 */
  .pub-hero-text-wrap { background-color: #1e293b; padding: 20px 100px 20px 20px; min-height: 165px; display: flex; flex-direction: column; justify-content: flex-start; box-sizing: border-box; position: relative; }
  .pub-hero-badge { font-size: 0.72rem; letter-spacing: 0.05em; display: block; line-height: 1.1; margin-top: 0px; margin-bottom: 8px; }
  .pub-hero-title { font-size: 1.2rem; font-weight: 700; line-height: 1.4; color: #ffffff !important; margin-top: 0px !important; margin-bottom: 12px !important; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; text-overflow: ellipsis; word-break: break-word; }
  .pub-hero-meta { font-size: 0.88rem; color: #94a3b8 !important; display: flex; flex-direction: column; gap: 5px; margin-top: auto; }
  .pub-hero-meta div { color: #94a3b8 !important; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  
  /* 2. Recent Publications Carousel 버튼 위치 정의 */
  .pub-mini-hero .custom-carousel-control-prev,
  .pub-mini-hero .custom-carousel-control-next { top: auto !important; bottom: 20px !important; z-index: 10 !important; }
  .pub-mini-hero .custom-carousel-control-prev { right: 64px !important; left: auto !important; }
  .pub-mini-hero .custom-carousel-control-next { right: 20px !important; left: auto !important; }

  /* Contact Box */
  .contact-info-box { background-color: #f8fafc; border-radius: 2px; padding: 35px; height: 100%; box-sizing: border-box;}
  .contact-item { display: flex; align-items: flex-start; margin-bottom: 20px; }
  .contact-item:last-child { margin-bottom: 0; }
  .contact-icon { font-size: 1.2rem; color: #64748b; margin-right: 16px; margin-top: 2px; width: 24px; text-align: center; }
  .contact-detail-title { font-weight: 700; color: #0f172a; font-size: 0.95rem; margin-bottom: 2px; }
  .contact-detail-text { font-size: 0.95rem; color: #475569; line-height: 1.5; }

  @media (max-width: 992px) {
    .hero-slide { height: auto; min-height: 440px; }
    .main-hero-content .hero-title { font-size: 2.0rem; }
    .main-hero-wrapper { padding: 30px; }
    .pub-slider-link { margin-bottom: 40px; }
    .contact-info-box { margin-top: 0px; }
    /* 모바일 환경에서 첫 화면 버튼 위치 보정 */
    .is-first-slide .custom-carousel-control-prev, .is-first-slide .custom-carousel-control-next { bottom: 20px !important; }
  }
</style>

<div class="vslab-container">
  
  <div class="container-hero" id="heroContainerFrame">
    <div id="milabStyleCarousel" class="custom-carousel">
      <div class="custom-carousel-inner">
        
        <div class="custom-carousel-item vslab-active" data-interval="6000">
          <div class="hero-slide">
            <div class="main-hero-bg"></div>
            <div class="main-hero-wrapper">
              <div class="main-hero-content">
                <h1 class="hero-title">Data Mining & Machine Learning Lab</h1>
                <p class="hero-desc">We investigate cutting-edge algorithms to solve real-world complexities. Our core research spans across fundamental machine learning methodologies and innovative data science applications.</p>
                <a href="/contact" class="btn-hero">CONTACT US</a>
              </div>
            </div>
          </div>
        </div>

        <div class="custom-carousel-item" data-interval="5000">
          <a href="/research" class="hero-slide-link">
            <div class="hero-slide">
              <div class="tb-hero-container">
                <div class="tb-hero-img" style="background-image: url('/assets/images/researches/pml.png'); background-size: contain;"></div>
                <div class="tb-hero-text">
                  <span class="text-success fw-bold uppercase hero-badge">RESEARCH TOPIC 01</span>
                  <h4 class="hero-title">Personalized Machine Learning and Recommender Systems</h4>
                  <div><span class="btn-hero">LEARN MORE</span></div>
                </div>
              </div>
            </div>
          </a>
        </div>

        <div class="custom-carousel-item" data-interval="5000">
          <a href="/research" class="hero-slide-link">
            <div class="hero-slide">
              <div class="tb-hero-container">
                <div class="tb-hero-img" style="background-image: url('/assets/images/researches/graph.gif'); background-size: contain;"></div>
                <div class="tb-hero-text">
                  <span class="text-success fw-bold uppercase hero-badge">RESEARCH TOPIC 02</span>
                  <h4 class="hero-title">Graph Machine Learning</h4>
                  <div><span class="btn-hero">LEARN MORE</span></div>
                </div>
              </div>
            </div>
          </a>
        </div>

        <div class="custom-carousel-item" data-interval="5000">
          <a href="/research" class="hero-slide-link">
            <div class="hero-slide">
              <div class="tb-hero-container">
                <div class="tb-hero-img" style="background-image: url('/assets/images/researches/large.png'); background-size: contain;"></div>
                <div class="tb-hero-text">
                  <span class="text-success fw-bold uppercase hero-badge">RESEARCH TOPIC 03</span>
                  <h4 class="hero-title">Lightweight and Scalable Data Mining</h4>
                  <div><span class="btn-hero">LEARN MORE</span></div>
                </div>
              </div>
            </div>
          </a>
        </div>
        
      </div>
      
      <button class="custom-carousel-control-prev" type="button" id="mainCarouselPrev">
        <div class="control-icon-bg"><span class="carousel-prev-icon-svg"></span></div>
      </button>
      <button class="custom-carousel-control-next" type="button" id="mainCarouselNext">
        <div class="control-icon-bg"><span class="carousel-next-icon-svg"></span></div>
      </button>
    </div>
  </div>

  <div class="news-grid-container">
    <h2 class="vslab-heading">Latest News</h2>
    <div class="vslab-row">
      
      {% for news in site.data.news limit:5 %}
      <div class="vslab-col-4 vslab-col-md-12 news-card-wrapper">
        <div class="news-card">
          
          <div class="news-card-img-wrap">
            <div class="news-card-bg" style="background-image: url('{% if news.image %}{{ news.image }}{% else %}/assets/images/news/default_news169.png{% endif %}');"></div>
          </div>
          
          <div class="news-card-body">
            <div class="news-card-badge 
              {% if news.keyword == 'Paper' or news.keyword == 'paper' %} bg-vslab-paper 
              {% elsif news.keyword == 'Award' or news.keyword == 'award' %} bg-vslab-award 
              {% else %} bg-vslab-default {% endif %}">
              
              {% if news.keyword == 'Paper' or news.keyword == 'paper' %}
                <i class="far fa-file-alt me-1"></i> {% elsif news.keyword == 'Award' or news.keyword == 'award' %}
                <i class="fas fa-trophy me-1"></i> {% else %}
                <i class="fas fa-bullhorn me-1"></i> {% endif %}
              
              {{ news.keyword }}
            </div>
            
            <h4 class="news-card-text">
              {% if news.keyword == "Paper" %}
                <a href="/publications">{{ news.content | strip_html }}</a>
              {% elsif news.link != nil %}
                <a href="{{ news.link }}" target="_blank">{{ news.content | strip_html }}</a>
              {% else %}
                {{ news.content | strip_html }}
              {% endif %}
            </h4>
            
            <div class="news-card-date">
              <i class="far fa-calendar-alt me-1"></i> {{ news.date }}
            </div>
          </div>

        </div>
      </div>
      {% endfor %}

      <div class="vslab-col-4 vslab-col-md-12 news-card-wrapper">
        <a href="/news" style="text-decoration: none; display: block; height: 100%;">
          <div class="news-card" style="background: #f8fafc; border-style: dashed; border-width: 2px; align-items: center; justify-content: center; min-height: 300px;">
            <div class="news-card-body" style="justify-content: center; align-items: center; text-align: center; width: 100%;">
              <div style="font-size: 2.5rem; color: #64748b; margin-bottom: 15px;">
                <i class="fas fa-arrow-circle-right"></i>
              </div>
              <h4 class="news-card-text" style="font-size: 1.3rem; color: #0f172a; margin-bottom: 8px;">
                More News
              </h4>
              <p style="font-size: 0.9rem; color: #64748b; margin: 0;">
                Click to view past news
              </p>
            </div>
          </div>
        </a>
      </div>
      
    </div>
  </div>

  <div class="vslab-row bottom-split-container">
    
    <div class="vslab-col-6 vslab-col-md-12" style="width: 58.33333333%;">
      <h2 class="vslab-heading">Recent Publications</h2>
      <div style="padding-right: 1.5rem;">
        
        {% assign all_papers = site.data.domestic_conference | concat: site.data.international_conference | concat: site.data.international_journal %}
        {% assign sorted_papers = all_papers | sort: "Date" | reverse %}
        
        {% if sorted_papers.size > 0 %}
          <a href="/publications" class="pub-slider-link">
            <div class="pub-mini-hero">
              <div id="pubMiniCarousel" class="custom-carousel">
                <div class="custom-carousel-inner">
                  
                  {% for paper in sorted_papers limit:5 %}
                  <div class="custom-carousel-item {% if forloop.first %}vslab-active{% endif %}" data-interval="4500">
                    
                    <div class="pub-hero-img-wrap">
                      <div class="pub-hero-bg" style="background-image: url('/assets/images/paper/slide_research{{ forloop.index }}.png');"></div>
                    </div>
                    
                    <div class="pub-hero-text-wrap">
                      <span class="text-success fw-bold uppercase pub-hero-badge">RECENT {{ forloop.index }} PUBLICATION</span>
                      
                      <h4 class="pub-hero-title">
                        {% if paper.Title.en %}
                          {{ paper.Title.en | strip_html }}
                        {% elsif paper.Title.kr %}
                          {{ paper.Title.kr | strip_html }}
                        {% else %}
                          {{ paper.Title | strip_html }}
                        {% endif %}
                      </h4>
                      
                      <div class="pub-hero-meta">
                        <div>
                          <i class="fas fa-bookmark me-1 opacity-75"></i>
                          {% if paper.FullVenue %} {{ paper.FullVenue }}
                          {% elsif paper.FullVenue.en %} {{ paper.FullVenue.en }}
                          {% elsif paper.Publisher %} {{ paper.Publisher }}
                          {% else %} Accepted Venue {% endif %}
                        </div>
                        <div>
                          <i class="far fa-calendar me-1 opacity-75"></i>{{ paper.Date | date: "%Y-%m-%d" }}
                        </div>
                      </div>
                    </div>

                  </div>
                  {% endfor %}
                  
                </div>
                
                <button class="custom-carousel-control-prev" type="button" id="pubCarouselPrev">
                  <div class="control-icon-bg"><span class="carousel-prev-icon-svg"></span></div>
                </button>
                <button class="custom-carousel-control-next" type="button" id="pubCarouselNext">
                  <div class="control-icon-bg"><span class="carousel-next-icon-svg"></span></div>
                </button>
              </div>
            </div>
          </a>
        {% else %}
          <p class="text-muted">등록된 최신 논문이 없습니다.</p>
        {% endif %}
        
      </div>
    </div>

    <div class="vslab-col-6 vslab-col-md-12" style="width: 41.66666667%;">
      <h2 class="vslab-heading">Contact Us</h2>
      <div class="contact-info-box">
        
        <div class="contact-item">
          <div class="contact-icon"><i class="fas fa-map-marker-alt"></i></div>
          <div>
            <div class="contact-detail-title">Lab Location</div>
            <div class="contact-detail-text">Room 225, Information Science Building, 50, Sadang-ro, Dongjak-gu, Seoul</div>
          </div>
        </div>

        <div class="contact-item">
          <div class="contact-icon"><i class="fas fa-envelope"></i></div>
          <div>
            <div class="contact-detail-title">Email Contact</div>
            <div class="contact-detail-text">jinhong@ssu.ac.kr </div>
          </div>
        </div>

        <div class="contact-item">
          <div class="contact-icon"><i class="fas fa-phone-alt"></i></div>
          <div>
            <div class="contact-detail-title">Office Phone</div>
            <div class="contact-detail-text">+82–02–820–0909 </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    
    function initCustomCarousel(carouselId, prevBtnId, nextBtnId) {
      var carousel = document.getElementById(carouselId);
      if (!carousel) return;
      
      var items = carousel.querySelectorAll('.custom-carousel-item');
      var currentIndex = 0;
      var timer = null;
      var containerFrame = document.getElementById('heroContainerFrame');

      // 초기화 시 첫 슬라이드 감지 클래스 적용
      if (carouselId === 'milabStyleCarousel' && containerFrame && currentIndex === 0) {
        containerFrame.classList.add('is-first-slide');
      }

      function showSlide(index) {
        items[currentIndex].classList.remove('vslab-active');
        currentIndex = (index + items.length) % items.length;
        items[currentIndex].classList.add('vslab-active');
        
        if (carouselId === 'milabStyleCarousel' && containerFrame) {
          if (currentIndex === 0) {
            containerFrame.classList.add('is-first-slide');
          } else {
            containerFrame.classList.remove('is-first-slide');
          }
        }
        resetTimer();
      }

      function nextSlide() { showSlide(currentIndex + 1); }
      function prevSlide() { showSlide(currentIndex - 1); }

      function resetTimer() {
        clearInterval(timer);
        var interval = parseInt(items[currentIndex].getAttribute('data-interval')) || 5000;
        timer = setInterval(nextSlide, interval);
      }

      var prevBtn = document.getElementById(prevBtnId);
      var nextBtn = document.getElementById(nextBtnId);
      
      if(prevBtn) prevBtn.addEventListener('click', function(e) { e.preventDefault(); prevSlide(); });
      if(nextBtn) nextBtn.addEventListener('click', function(e) { e.preventDefault(); nextSlide(); });

      resetTimer();
    }

    initCustomCarousel('milabStyleCarousel', 'mainCarouselPrev', 'mainCarouselNext');
    initCustomCarousel('pubMiniCarousel', 'pubCarouselPrev', 'pubCarouselNext');
  });
</script>