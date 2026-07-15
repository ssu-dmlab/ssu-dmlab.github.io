---
layout: article
title: "News"
permalink: /news/
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
  /* 뉴스 Grid 시스템 */
  .news-grid-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px 15px;
  }
  
  .vslab-heading {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 30px;
    color: #0f172a;
    border-left: 5px solid #1e3a8a; /* 포인트 컬러 (필요시 수정) */
    padding-left: 15px;
  }

  .vslab-row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
  }

  /* 3열 카드 배치 (태블릿 이하에서는 1열) */
  .vslab-col-4 {
    flex: 0 0 33.3333%;
    max-width: 33.3333%;
    padding: 15px;
    box-sizing: border-box;
  }

  @media (max-width: 991px) {
    .vslab-col-4 {
      flex: 0 0 50%;
      max-width: 50%;
    }
  }

  @media (max-width: 767px) {
    .vslab-col-4 {
      flex: 0 0 100%;
      max-width: 100%;
    }
  }

  /* 카드 디자인 (index.md와 통일) */
  .news-card-wrapper {
    display: flex;
  }

  .news-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  .news-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
    border-color: #00B4D8;
  }

  /* 이미지 비율 16:9 유지 */
  .news-card-img-wrap {
    position: relative;
    width: 100%;
    padding-top: 56.25%; /* 16:9 */
    background-color: #f1f5f9;
    overflow: hidden;
  }

  .news-card-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: transform 0.3s ease;
  }

  .news-card:hover .news-card-bg {
    transform: scale(1.03);
  }

  /* 카드 텍스트 요소 */
  .news-card-body {
    padding: 20px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
  }

  .news-card-badge {
    display: inline-block;
    padding: 4px 10px;
    font-size: 0.75rem;
    font-weight: 600;
    border-radius: 6px;
    margin-bottom: 12px;
    width: fit-content;
    color: #ffffff;
  }

  /* 뱃지 테마 색상 */
  .bg-vslab-paper { background-color: #2563eb; }
  .bg-vslab-award { background-color: #eab308; }
  .bg-vslab-default { background-color: #64748b; }

  .news-card-text {
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.5;
    margin: 0 0 15px 0;
    color: #1e293b;
    flex-grow: 1;
  }

  .news-card-text a {
    color: inherit;
    text-decoration: none;
  }

  .news-card-text a:hover {
    color: inherit !important;
    text-decoration: underline;
  }

  .news-card-date {
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: auto;
  }
</style>

<div class="news-grid-container">
  <h2 class="vslab-heading">All News</h2>
  <div class="vslab-row">
    
    {% for news in site.data.news %}
    <div class="vslab-col-4 news-card-wrapper">
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
    
  </div>
</div>