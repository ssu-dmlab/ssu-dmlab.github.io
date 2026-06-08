---
layout: article
---

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* [공통 스타일 정의] */
  .vslab-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
  }
  .vslab-heading {
    font-size: 1.6rem;
    font-weight: 700;
    color: #1e293b;
    margin-top: 50px;
    margin-bottom: 25px;
    position: relative;
    padding-bottom: 8px;
  }
  
  /* 1. 상단 Hero Carousel 영역 개선 */
  .carousel-news-container {
    margin-bottom: 50px;
  }
  .news-slide-card {
    position: relative;
    height: 420px; /* 조금 더 시원한 개방감을 위해 높이 상향 */
    border-radius: 24px;
    overflow: hidden;
    background-color: #0f172a;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  }
  .news-slide-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    filter: brightness(0.55);
    z-index: 1;
    transition: transform 0.5s ease;
  }
  .news-slide-card:hover .news-slide-bg {
    transform: scale(1.02);
  }
  .news-slide-content {
    position: relative;
    z-index: 2;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center; /* 랩실 메인 정보 소개를 위해 중앙 정렬 배치 스타일 혼용 */
    padding: 50px;
    color: #ffffff;
  }
  .content-bottom {
    justify-content: flex-end;
  }
  .news-slide-meta {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
  }
  .slide-badge {
    font-size: 0.8rem;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 30px;
    text-transform: uppercase;
    color: #ffffff !important;
  }
  .slide-date {
    font-size: 0.9rem;
    color: #cbd5e1;
  }
  .news-slide-title {
    font-size: 2rem;
    font-weight: 800;
    line-height: 1.4;
    margin-bottom: 15px;
    max-width: 85%;
  }
  .news-slide-desc {
    font-size: 1.1rem;
    color: #94a3b8;
    margin-bottom: 25px;
    max-width: 70%;
  }
  
  /* 버튼 스타일 */
  .btn-vslab-primary {
    background-color: #ffffff;
    color: #0f172a;
    font-weight: 600;
    padding: 12px 28px;
    border-radius: 30px;
    border: none;
    transition: all 0.2s ease;
    text-decoration: none;
    display: inline-block;
    width: fit-content;
  }
  .btn-vslab-primary:hover {
    background-color: #f1f5f9;
    transform: translateY(-2px);
    color: #0f172a;
  }

  .carousel-control-prev, .carousel-control-next {
    width: 60px;
    z-index: 3;
  }
  .control-icon-bg {
    background-color: rgba(255, 255, 255, 0.15);
    padding: 12px;
    border-radius: 50%;
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
  }
  .carousel-control-prev:hover .control-icon-bg,
  .carousel-control-next:hover .control-icon-bg {
    background-color: rgba(255, 255, 255, 0.3);
  }

  /* 2. Research Highlights (중간 3단 카드 레이아웃) */
  .highlight-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    overflow: hidden;
    height: 100%;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  .highlight-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 20px rgba(0,0,0,0.05);
  }
  .highlight-img-box {
    height: 180px;
    background-color: #f8fafc;
    background-size: cover;
    background-position: center;
  }
  .highlight-body {
    padding: 24px;
  }
  .highlight-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 10px;
  }
  .highlight-text {
    font-size: 0.95rem;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 0;
  }

  /* 3. 하단 리스트 영역 및 가로형 뉴스 카드 */
  .news-row-card {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #e2e8f0;
    padding: 16px 0;
    background-color: #ffffff;
  }
  .news-row-left {
    min-width: 90px;
    max-width: 90px;
    height: 32px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.75rem;
    margin-right: 20px;
    text-transform: uppercase;
  }
  
  /* 동적 컬러 클래스 */
  .bg-vslab-paper { background-color: #e6f4ea !important; color: #137333 !important; }
  .bg-vslab-award { background-color: #e8f0fe !important; color: #1a73e8 !important; }
  .bg-vslab-default { background-color: #f1f5f9 !important; color: #475569 !important; }

  .news-row-center {
    flex-grow: 1;
    font-size: 0.98rem;
    color: #334155;
    line-height: 1.5;
  }
  .news-row-center a {
    color: #1a73e8;
    text-decoration: none;
    font-weight: 500;
  }
  .news-row-center a:hover { text-decoration: underline; }
  
  .news-row-right {
    min-width: 90px;
    text-align: right;
    font-size: 0.9rem;
    color: #94a3b8;
  }

  /* [반응형 모바일 미디어 쿼리] */
  @media (max-width: 992px) {
    .news-slide-card { height: 360px; }
    .news-slide-title { font-size: 1.5rem; }
    .news-slide-desc { font-size: 1rem; max-width: 90%; }
    .news-slide-content { padding: 30px; }
  }
  @media (max-width: 768px) {
    .news-row-card {
      flex-direction: column;
      align-items: flex-start;
      padding: 15px 0;
    }
    .news-row-left { margin-bottom: 8px; }
    .news-row-right { text-align: left; margin-top: 4px; }
  }
</style>

<div class="vslab-container">

  <div class="carousel-news-container">
    <div id="vslabMainCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
      <div class="carousel-inner">
        
        <div class="carousel-item active" data-bs-interval="5000">
          <div class="news-slide-card">
            <div class="news-slide-bg" style="background-image: url('/assets/images/logo/hero_bg.jpg');"></div>
            <div class="news-slide-content">
              <h1 class="news-slide-title">DMLAB @ SSU</h1>
              <p class="news-slide-desc">Advancing AI, Machine Learning, and Data Science for a Better World. We focus on innovative solutions for healthcare, computer vision, and large language models.</p>
              <a href="/contact" class="btn-vslab-primary">EXPLORE OUR WORK</a>
            </div>
          </div>
        </div>

        {% for news in site.data.news limit:5 %}
        <div class="carousel-item" data-bs-interval="4000">
          <div class="news-slide-card">
            
            <div class="news-slide-bg" {% if news.image %} style="background-image: url('{{ news.image }}');" {% endif %}></div>
            
            <div class="news-slide-content content-bottom">
              <div class="news-slide-meta">
                <span class="slide-badge 
                  {% if news.keyword == 'Paper' %} bg-vslab-paper 
                  {% elsif news.keyword == 'Award' %} bg-vslab-award 
                  {% else %} bg-vslab-default {% endif %}">
                  {{ news.keyword }}
                </span>
                <span class="slide-date"><i class="far fa-calendar-alt me-1"></i>{{ news.date }}</span>
              </div>
              
              <h2 class="news-slide-title">
                {% if news.keyword == "Paper" %}
                  <a href="/publications" style="color: inherit; text-decoration: none;">{{ news.content | strip_html | truncate: 120 }}</a>
                {% elsif news.link != nil %}
                  <a href="{{ news.link }}" target="_blank" style="color: inherit; text-decoration: none;">{{ news.content | strip_html | truncate: 120 }}</a>
                {% else %}
                  {{ news.content | strip_html | truncate: 120 }}
                {% endif %}
              </h2>
            </div>
            
          </div>
        </div>
        {% endfor %}
        
      </div>
      
      <button class="carousel-control-prev" type="button" data-bs-target="#vslabMainCarousel" data-bs-slide="prev">
        <div class="control-icon-bg">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        </div>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#vslabMainCarousel" data-bs-slide="next">
        <div class="control-icon-bg">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
        </div>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>


  <h2 class="vslab-heading">Research Highlights</h2>
  <div class="row g-4">
    <div class="col-md-4">
      <div class="highlight-card">
        <div class="highlight-img-box" style="background-image: url('/assets/images/highlights/healthcare.jpg');"></div>
        <div class="highlight-body">
          <h3 class="highlight-title">AI for Healthcare</h3>
          <p class="highlight-text">Leveraging deep learning for early disease diagnosis and personalized medical data analysis.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="highlight-card">
        <div class="highlight-img-box" style="background-image: url('/assets/images/highlights/vision.jpg');"></div>
        <div class="highlight-body">
          <h3 class="highlight-title">Computer Vision Applications</h3>
          <p class="highlight-text">Real-world solutions in object detection, video surveillance, and automation systems.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="highlight-card">
        <div class="highlight-img-box" style="background-image: url('/assets/images/highlights/nlp.jpg');"></div>
        <div class="highlight-body">
          <h3 class="highlight-title">Large Language Models</h3>
          <p class="highlight-text">Investigating efficient training methods, alignment engineering, and bias mitigation in LLMs.</p>
        </div>
      </div>
    </div>
  </div>


  <div class="row">
    
    <div class="col-lg-7">
      <h2 class="vslab-heading">Recent Publications</h2>
      <div class="pe-lg-3">
        {% for news in site.data.news %}
          {% if news.keyword == 'Paper' %}
          <div class="news-row-card">
            <div class="news-row-center">
              <span class="fw-bold text-dark d-block mb-1">{{ news.content | strip_html | truncate: 80 }}</span>
              <small class="text-secondary">Authors, Conference/Journal Year</small>
            </div>
            <div class="news-row-right">
              <span class="badge bg-light text-primary border border-primary-subtle">Full Paper</span>
            </div>
          </div>
          {% endif %}
        {% endfor %}
      </div>
    </div>

    <div class="col-lg-5">
      <h2 class="vslab-heading">Latest News</h2>
      <div class="ps-lg-2">
        {% for news in site.data.news limit:4 %}
        <div class="news-row-card">
          <div class="news-row-left 
            {% if news.keyword == 'Paper' %} bg-vslab-paper 
            {% elsif news.keyword == 'Award' %} bg-vslab-award 
            {% else %} bg-vslab-default {% endif %}">
            {{ news.keyword }}
          </div>
          <div class="news-row-center">
            {{ news.content | truncate: 60 }}
          </div>
          <div class="news-row-right">
            {{ news.date }}
          </div>
        </div>
        {% endfor %}
      </div>
    </div>

  </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>