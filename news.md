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
    border-left: 5px solid #1e3a8a;
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
    .vslab-col-4 { flex: 0 0 50%; max-width: 50%; }
  }

  @media (max-width: 767px) {
    .vslab-col-4 { flex: 0 0 100%; max-width: 100%; }
  }

  /* 카드 디자인 */
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
    cursor: pointer; /* 클릭 가능 표시 */
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

  .news-card-date {
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: auto;
  }

  /* ================= 팝업 (Modal) 스타일 ================= */
  .news-modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(4px);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    padding: 20px;
    box-sizing: border-box;
  }

  .news-modal-overlay.active {
    display: flex;
  }

  .news-modal-content {
    background: #ffffff;
    border-radius: 16px;
    max-width: 650px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    animation: modalFadeIn 0.2s ease-out;
  }

  @keyframes modalFadeIn {
    from { opacity: 0; transform: translateY(10px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
  }

  .news-modal-close {
    position: absolute;
    top: 15px;
    right: 15px;
    background: rgba(255, 255, 255, 0.85);
    border: none;
    font-size: 1.25rem;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    cursor: pointer;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #475569;
    transition: background 0.2s;
  }

  .news-modal-close:hover {
    background: #e2e8f0;
    color: #0f172a;
  }

  .modal-body {
    padding: 24px;
  }

  .modal-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #0f172a;
    margin-top: 15px;
    margin-bottom: 12px;
    line-height: 1.4;
  }

  .modal-meta-info {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 0.85rem;
    color: #64748b;
  }

  .modal-content-text {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #334155;
    margin-bottom: 24px;
    white-space: pre-line;
  }

  .modal-link-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 18px;
    background-color: #1e3a8a;
    color: #ffffff !important;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9rem;
    transition: background-color 0.2s;
  }

  .modal-link-btn:hover {
    background-color: #00B4D8;
  }
</style>

<div class="news-grid-container">
  <h2 class="vslab-heading">All News</h2>
  <div class="vslab-row">
    
    <!-- 원래의 Jekyll 데이터 루프 구조 그대로 유지 -->
    {% for news in site.data.news %}
    {% assign news_img = news.image | default: '/assets/images/news/default_news169.png' %}
    {% assign news_title = news.title | default: news.content | strip_html %}
    
    <div class="vslab-col-4 news-card-wrapper">
      <div class="news-card" 
           onclick="openNewsModal(this)"
           data-title="{{ news_title | escape }}"
           data-content="{{ news.content | strip_html | escape }}"
           data-image="{{ news_img }}"
           data-date="{{ news.date }}"
           data-keyword="{{ news.keyword }}"
           data-link="{% if news.keyword == 'Paper' or news.keyword == 'paper' %}/publications{% else %}{{ news.link }}{% endif %}">
        
        <div class="news-card-img-wrap">
          <div class="news-card-bg" style="background-image: url('{{ news_img }}');"></div>
        </div>
        
        <div class="news-card-body">
          <div class="news-card-badge 
              {% if news.keyword == 'Paper' or news.keyword == 'paper' %} bg-vslab-paper 
              {% elsif news.keyword == 'Award' or news.keyword == 'award' %} bg-vslab-award 
              {% else %} bg-vslab-default {% endif %}">
              
              {% if news.keyword == 'Paper' or news.keyword == 'paper' %}
                <i class="far fa-file-alt me-1"></i>
              {% elsif news.keyword == 'Award' or news.keyword == 'award' %}
                <i class="fas fa-trophy me-1"></i>
              {% else %}
                <i class="fas fa-bullhorn me-1"></i>
              {% endif %}
              
              {{ news.keyword }}
          </div>
          
          <h4 class="news-card-text">
            {{ news_title }}
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

<!-- 뉴스 팝업 (Modal) -->
<div class="news-modal-overlay" id="newsModal" onclick="closeNewsModal(event)">
  <div class="news-modal-content" onclick="event.stopPropagation()">
    <button class="news-modal-close" onclick="closeNewsModal()"><i class="fas fa-times"></i></button>
    
    <!-- 16:9 Image -->
    <div class="news-card-img-wrap">
      <div class="news-card-bg" id="modalImg"></div>
    </div>
    
    <div class="modal-body">
      <!-- Badge & Date -->
      <div class="modal-meta-info">
        <span id="modalBadge" class="news-card-badge"></span>
        <span><i class="far fa-calendar-alt me-1"></i> <span id="modalDate"></span></span>
      </div>
      
      <!-- Title -->
      <h3 class="modal-title" id="modalTitle"></h3>
      
      <!-- Content -->
      <p class="modal-content-text" id="modalContent"></p>
      
      <!-- Link -->
      <div id="modalLinkContainer"></div>
    </div>
  </div>
</div>

<script>
  function openNewsModal(cardElement) {
    // 카드 element의 data-* 속성에서 데이터 읽어오기
    const title = cardElement.getAttribute('data-title');
    const content = cardElement.getAttribute('data-content');
    const image = cardElement.getAttribute('data-image');
    const date = cardElement.getAttribute('data-date');
    const keyword = cardElement.getAttribute('data-keyword');
    const link = cardElement.getAttribute('data-link');

    // Modal 엘리먼트에 채워넣기
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalContent').innerText = content;
    document.getElementById('modalDate').innerText = date;
    document.getElementById('modalImg').style.backgroundImage = `url('${image}')`;

    // 뱃지 아이콘 및 클래스 설정
    const badgeEl = document.getElementById('modalBadge');
    const kwLower = keyword ? keyword.toLowerCase() : '';
    let iconHTML = '<i class="fas fa-bullhorn me-1"></i>';
    let badgeClass = 'bg-vslab-default';

    if (kwLower === 'paper') {
      iconHTML = '<i class="far fa-file-alt me-1"></i>';
      badgeClass = 'bg-vslab-paper';
    } else if (kwLower === 'award') {
      iconHTML = '<i class="fas fa-trophy me-1"></i>';
      badgeClass = 'bg-vslab-award';
    }

    badgeEl.className = `news-card-badge ${badgeClass}`;
    badgeEl.innerHTML = `${iconHTML} ${keyword}`;

    // 링크 버튼 처리
    const linkContainer = document.getElementById('modalLinkContainer');
    if (link && link.trim() !== '') {
      const isExternal = link.startsWith('http');
      const targetAttr = isExternal ? 'target="_blank"' : '';
      
      linkContainer.innerHTML = `
        <a href="${link}" ${targetAttr} class="modal-link-btn">
          관련 페이지 바로가기 <i class="fas fa-external-link-alt"></i>
        </a>
      `;
    } else {
      linkContainer.innerHTML = '';
    }

    // Modal 활성화
    document.getElementById('newsModal').classList.add('active');
    document.body.style.overflow = 'hidden'; // 배경 스크롤 차단
  }

  function closeNewsModal(event) {
    document.getElementById('newsModal').classList.remove('active');
    document.body.style.overflow = 'auto'; // 스크롤 원복
  }

  // ESC 키 클릭 시 모달 닫기
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeNewsModal();
  });
</script>