---
layout: article
---

<!-- Bootstrap 5 CSS 및 FontAwesome 로드 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* [공통 스타일 정의] */
  .vslab-container {
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 15px;
  }
  .vslab-heading {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
    margin-top: 40px;
    margin-bottom: 20px;
  }
  .rounded-box {
    border: 2px solid #cbd5e1;
    border-radius: 20px;
    background-color: #ffffff;
    padding: 30px;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
  }

  /* 1. 상단 Main Picture & Latest News 카드 슬라이더 */
  .carousel-news-container {
    margin-bottom: 40px;
  }
  .news-slide-card {
    position: relative;
    height: 380px;
    border-radius: 24px;
    overflow: hidden;
    border: 2px solid #cbd5e1;
    background-color: #0f172a;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  }
  .news-slide-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    filter: brightness(0.65);
    z-index: 1;
    transition: transform 0.5s ease;
  }
  .news-slide-card:hover .news-slide-bg {
    transform: scale(1.03);
  }
  .news-slide-content {
    position: relative;
    z-index: 2;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 40px;
    color: #ffffff;
  }
  .news-slide-meta {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
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
    color: #94a3b8;
  }
  .news-slide-title {
    font-size: 1.6rem;
    font-weight: 700;
    line-height: 1.4;
    margin-bottom: 0;
    max-width: 85%;
  }
  .carousel-control-prev, .carousel-control-next {
    width: 60px;
    z-index: 3;
  }
  .control-icon-bg {
    background-color: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.4);
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
    background-color: rgba(255, 255, 255, 0.4);
    transform: scale(1.1);
  }

  /* 2. 하단 가로형 뉴스 목록 카드 */
  .news-row-card {
    display: flex;
    align-items: center;
    border: 2px solid #cbd5e1;
    border-radius: 20px;
    padding: 20px 30px;
    margin-bottom: 16px;
    background-color: #ffffff;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  .news-row-card:hover {
    border-color: #3b82f6;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.08);
  }
  .news-row-left {
    min-width: 120px;
    max-width: 120px;
    height: 50px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    margin-right: 24px;
    text-transform: uppercase;
  }
  
  /* [동적 컬러 클래스 정의] */
  .bg-vslab-paper {
    background-color: #10b981 !important; /* 모던 그린 */
    border: 2px solid #047857 !important;
    color: #ffffff !important;
  }
  .bg-vslab-award {
    background-color: #3b82f6 !important; /* 모던 블루 */
    border: 2px solid #1d4ed8 !important;
    color: #ffffff !important;
  }
  .bg-vslab-default {
    background-color: #64748b !important; /* 기본 슬레이트 그레이 */
    border: 2px solid #475569 !important;
    color: #ffffff !important;
  }

  .news-row-center {
    flex-grow: 1;
    font-size: 1.02rem;
    font-weight: 500;
    color: #334155;
    line-height: 1.5;
  }
  .news-row-center a {
    color: #2563eb;
    font-weight: 600;
    text-decoration: underline;
  }
  .news-row-right {
    min-width: 110px;
    text-align: right;
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
    margin-left: 16px;
  }

  /* [반응형 모바일 미디어 쿼리] */
  @media (max-width: 768px) {
    .news-slide-card {
      height: 320px;
    }
    .news-slide-title {
      font-size: 1.25rem;
      max-width: 100%;
    }
    .news-slide-content {
      padding: 24px;
    }
    .news-row-card {
      flex-direction: column;
      align-items: flex-start;
      padding: 20px;
    }
    .news-row-left {
      margin-bottom: 12px;
      height: 40px;
    }
    .news-row-right {
      margin-top: 8px;
      text-align: left;
      margin-left: 0;
    }
  }
</style>

<div class="vslab-container">

  <!-- ================= [1] Main Picture & Latest News 슬라이더 ================= -->
  <div class="carousel-news-container">
    <div id="vslabMainCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
      <div class="carousel-inner">
        
        {% for news in site.data.news limit:5 %}
        <div class="carousel-item {% if forloop.first %}active{% endif %}" data-bs-interval="4000">
          <div class="news-slide-card">
            
            <div class="news-slide-bg" {% if news.image %} style="background-image: url('{{ news.image }}');" {% endif %}></div>
            
            <div class="news-slide-content">
              <div class="news-slide-meta">
                <!-- 조건문에 따라 상단 배지 배경색 변경 -->
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
                {%   elsif news.link != nil %}
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


  <!-- ================= [2] Announcement 박스 영역 ================= -->
  <h2 class="vslab-heading">Announcement</h2>
  <div class="rounded-box">
    {% for welcome in site.data.welcome %}
    <div class="d-flex align-items-center mb-3">
      <img width="45" src="/assets/images/logo/newlogo.svg" class="me-3" alt="Logo"/>
      <h4 class="m-0 fw-bold text-dark">{{ welcome.headline }}</h4>
    </div>
    <p class="m-0 text-secondary" style="line-height: 1.7; text-align: justify; font-size: 1.05rem;">
      {{ welcome.description }}
    </p>
    {% endfor %}
  </div>


  <!-- ================= [3] News 리스트 영역 (배경색 조건 분기 완료) ================= -->
  <h2 class="vslab-heading">News</h2>
  <div class="news-list-wrapper">
    
    {% for news in site.data.news %}
    <div class="news-row-card">
      <!-- 조건문에 따라 하단 좌측 박스 배경색 변경 -->
      <div class="news-row-left 
        {% if news.keyword == 'Paper' %} bg-vslab-paper 
        {% elsif news.keyword == 'Award' %} bg-vslab-award 
        {% else %} bg-vslab-default {% endif %}">
        {{ news.keyword }}
      </div>
      
      <div class="news-row-center">
        {{ news.content }}
      </div>
      
      <div class="news-row-right">
        {{ news.date }}
      </div>
    </div>
    {% endfor %}
    
  </div>

</div>

<!-- 부트스트랩 JS 로드 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>