---
layout: article
---

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* [폰트 및 초기화] */
  body {
    font-family: 'Inter', 'Pretendard', -apple-system, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
  }

  /* 1. 가로 전체를 채우는 Full-width Hero Carousel */
  .full-width-hero {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-bottom: 80px;
    overflow: hidden;
  }
  .hero-slide {
    position: relative;
    height: 550px; /* MILAB 스타일의 시원하고 깊은 높이감 */
    background-color: #0b1329;
  }
  .hero-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: brightness(0.45); /* 텍스트 가독성을 위한 최적화 어둡기 */
    z-index: 1;
    transition: transform 0.6s ease-in-out;
  }
  .carousel-item:hover .hero-bg {
    transform: scale(1.02);
  }
  .hero-content-wrapper {
    position: relative;
    z-index: 2;
    height: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #ffffff;
  }
  .hero-title {
    font-size: 2.75rem;
    font-weight: 800;
    line-height: 1.25;
    margin-bottom: 20px;
    letter-spacing: -0.03em;
  }
  .hero-desc {
    font-size: 1.15rem;
    color: #cbd5e1;
    max-width: 750px;
    margin-bottom: 35px;
    line-height: 1.6;
  }
  
  /* 미니멀 시크 버튼 스타일 (MILAB 감성) */
  .btn-hero {
    background-color: transparent;
    color: #ffffff;
    font-weight: 600;
    font-size: 0.95rem;
    padding: 12px 30px;
    border: 2px solid #ffffff;
    border-radius: 4px; /* 칼각 스타일 혹은 미세 라운딩 */
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    width: fit-content;
    letter-spacing: 0.05em;
  }
  .btn-hero:hover {
    background-color: #ffffff;
    color: #0b1329;
  }

  /* 부드러운 슬라이드 컨트롤 UI */
  .control-icon-bg {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 14px;
    border-radius: 50%;
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
  }
  .carousel-control-prev:hover .control-icon-bg,
  .carousel-control-next:hover .control-icon-bg {
    background-color: rgba(255, 255, 255, 0.25);
  }

  /* [콘텐츠 공통 컨테이너] */
  .vslab-container {
    max-width: 1240px;
    margin: 0 auto;
    padding: 0 24px;
  }
  .vslab-heading {
    font-size: 1.75rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 35px;
    letter-spacing: -0.02em;
    text-transform: uppercase;
  }

  /* 2. News 카드 그리드 영역 (3개씩 2줄 배치) */
  .news-grid-container {
    margin-bottom: 80px;
  }
  .news-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .news-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
    border-color: #cbd5e1;
  }
  .news-card-badge {
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 4px;
    width: fit-content;
    margin-bottom: 16px;
    text-transform: uppercase;
  }
  .bg-vslab-paper { background-color: #e6f4ea !important; color: #137333 !important; }
  .bg-vslab-award { background-color: #e8f0fe !important; color: #1a73e8 !important; }
  .bg-vslab-default { background-color: #f1f5f9 !important; color: #475569 !important; }

  .news-card-text {
    font-size: 1rem;
    font-weight: 500;
    color: #334155;
    line-height: 1.5;
    margin-bottom: 20px;
  }
  .news-card-text a {
    color: #0f172a;
    text-decoration: none;
  }
  .news-card-text a:hover { text-decoration: underline; }
  
  .news-card-date {
    font-size: 0.85rem;
    color: #94a3b8;
    font-weight: 500;
  }

  /* 3. 하단 레이아웃 (Publications / Contact 좌우 분할) */
  .bottom-split-container {
    margin-bottom: 100px;
  }
  .pub-row {
    border-bottom: 1px solid #f1f5f9;
    padding: 16px 0;
  }
  .pub-row:last-child { border-bottom: none; }
  .pub-title {
    font-size: 1rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 4px;
  }
  .pub-meta {
    font-size: 0.88rem;
    color: #64748b;
  }

  /* 우측 Contact 카드 스타일 */
  .contact-info-box {
    background-color: #f8fafc;
    border-radius: 16px;
    padding: 35px;
    height: 100%;
  }
  .contact-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
  }
  .contact-item:last-child { margin-bottom: 0; }
  .contact-icon {
    font-size: 1.2rem;
    color: #64748b;
    margin-right: 16px;
    margin-top: 2px;
    width: 24px;
    text-align: center;
  }
  .contact-detail-title {
    font-weight: 700;
    color: #0f172a;
    font-size: 0.95rem;
    margin-bottom: 2px;
  }
  .contact-detail-text {
    font-size: 0.95rem;
    color: #475569;
    line-height: 1.5;
  }

  /* [반응형 화면 대응] */
  @media (max-width: 992px) {
    .hero-slide { height: 460px; }
    .hero-title { font-size: 2rem; }
    .hero-desc { font-size: 1rem; }
    .contact-info-box { margin-top: 40px; }
  }
</style>

<div class="full-width-hero">
  <div id="milabStyleCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
    <div class="carousel-inner">
      
      <div class="carousel-item active" data-bs-interval="6000">
        <div class="hero-slide">
          <div class="hero-bg" style="background-image: url('/assets/images/hero/slide_main.jpg');"></div>
          <div class="hero-content-wrapper">
            <h1 class="hero-title">Data Mining & Machine Learning Lab</h1>
            <p class="hero-desc">We investigate cutting-edge algorithms to solve real-world complexities. Our core research spans across fundamental machine learning methodologies and innovative data science applications.</p>
            <a href="/contact" class="btn-hero">CONTACT US</a>
          </div>
        </div>
      </div>

      <div class="carousel-item" data-bs-interval="5000">
        <div class="hero-slide">
          <div class="hero-bg" style="background-image: url('/assets/images/hero/slide_research1.jpg');"></div>
          <div class="hero-content-wrapper">
            <h1 class="hero-title">AI for Healthcare & Bio-informatics</h1>
            <p class="hero-desc">Developing advanced deep learning architectures for early-stage epidemic forecasts, precision patient screening, and multimodal medical image diagnostics.</p>
            <a href="/research" class="btn-hero">VIEW RESEARCH</a>
          </div>
        </div>
      </div>

      <div class="carousel-item" data-bs-interval="5000">
        <div class="hero-slide">
          <div class="hero-bg" style="background-image: url('/assets/images/hero/slide_research2.jpg');"></div>
          <div class="hero-content-wrapper">
            <h1 class="hero-title">Next-Gen Computer Vision & Automation</h1>
            <p class="hero-desc">Empowering machines to interpret the dynamic world through continuous object tracking, complex context understanding, and spatial generative models.</p>
            <a href="/research" class="btn-hero">VIEW RESEARCH</a>
          </div>
        </div>
      </div>

      <div class="carousel-item" data-bs-interval="5000">
        <div class="hero-slide">
          <div class="hero-bg" style="background-image: url('/assets/images/hero/slide_research3.jpg');"></div>
          <div class="hero-content-wrapper">
            <h1 class="hero-title">Trustworthy Large Language Models</h1>
            <p class="hero-desc">Exploring structural fine-tuning parameters, contextual alignment, and systematic bias mitigation for highly dependable corporate and logical NLP engines.</p>
            <a href="/research" class="btn-hero">VIEW RESEARCH</a>
          </div>
        </div>
      </div>
      
    </div>
    
    <button class="carousel-control-prev" type="button" data-bs-target="#milabStyleCarousel" data-bs-slide="prev">
      <div class="control-icon-bg"><span class="carousel-control-prev-icon" aria-hidden="true"></span></div>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#milabStyleCarousel" data-bs-slide="next">
      <div class="control-icon-bg"><span class="carousel-control-next-icon" aria-hidden="true"></span></div>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</div>


<div class="vslab-container">

  <div class="news-grid-container">
    <h2 class="vslab-heading">Latest News</h2>
    <div class="row g-4">
      
      {% for news in site.data.news limit:6 %}
      <div class="col-md-6 col-lg-4">
        <div class="news-card">
          <div>
            <div class="news-card-badge 
              {% if news.keyword == 'Paper' %} bg-vslab-paper 
              {% elsif news.keyword == 'Award' %} bg-vslab-award 
              {% else %} bg-vslab-default {% endif %}">
              {{ news.keyword }}
            </div>
            <p class="news-card-text">
              {% if news.keyword == "Paper" %}
                <a href="/publications">{{ news.content | strip_html | truncate: 100 }}</a>
              {% elsif news.link != nil %}
                <a href="{{ news.link }}" target="_blank">{{ news.content | strip_html | truncate: 100 }}</a>
              {% else %}
                {{ news.content | strip_html | truncate: 100 }}
              {% endif %}
            </p>
          </div>
          <div class="news-card-date">
            <i class="far fa-calendar-alt me-1"></i> {{ news.date }}
          </div>
        </div>
      </div>
      {% endfor %}
      
    </div>
  </div>


  <div class="row bottom-split-container">
    
    <div class="col-lg-7">
      <h2 class="vslab-heading">Recent Publications</h2>
      <div class="pe-lg-4">
        
        {% assign count = 0 %}
        {% for news in site.data.news %}
          {% if news.keyword == 'Paper' and count < 4 %}
          <div class="pub-row">
            <h4 class="pub-title">
              <a href="/publications" class="text-decoration-none text-dark-hover">{{ news.content | strip_html | truncate: 110 }}</a>
            </h4>
            <div class="pub-meta">
              <span>Accepted at Top-tier Venue</span> &bull; <span class="text-primary fw-medium">{{ news.date }}</span>
            </div>
          </div>
          {% assign count = count | plus: 1 %}
          {% endif %}
        {% endfor %}
        
      </div>
    </div>

    <div class="col-lg-5">
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
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
