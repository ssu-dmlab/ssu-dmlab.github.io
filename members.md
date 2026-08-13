---
layout: article
title: ""
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

{% raw %}
<style>
  /* ==========================================================================
     Members page — visual language matched to index.md (vslab theme)
     ========================================================================== */
  .vslab-container { width: 100%; margin: 0 auto; padding: 0; }
  .vslab-heading {
    font-size: 1.75rem;
    font-weight: 800;
    color: #0f172a;
    margin-top: 1.5rem;
    margin-bottom: 35px;
    letter-spacing: -0.02em;
    border-bottom: 2px solid #1A365D !important;
  }
  .mem-section { margin-bottom: 70px; }

  /* Director card */
  .director-card {
    display: flex;
    align-items: center;
    gap: 32px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 32px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    text-decoration: none !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  a.director-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
    border-color: #00B4D8;
    text-decoration: none !important;
  }
  .director-avatar {
    flex-shrink: 0;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background-size: cover;
    background-position: center;
    border: 3px solid #e2e8f0;
  }
  .director-info { flex: 1; min-width: 0; }
  .director-name, a .director-name { font-size: 1.4rem; font-weight: 800; color: #0f172a !important; margin: 0 0 4px 0; text-decoration: none !important; }
  a.director-card:hover .director-name {
    color: #1A365D !important;
    text-decoration-line: underline !important;
    text-decoration-color: #1A365D !important;
  }
  .director-role, a .director-role { font-size: 0.92rem; font-weight: 600; color: #00B4D8 !important; margin: 0 0 14px 0; line-height: 1.5; text-decoration: none !important; }
  .director-contact { display: flex; flex-direction: column; gap: 4px; }
  .director-contact div, a .director-contact div { font-size: 0.88rem; color: #334155 !important; text-decoration: none !important; }
  .director-contact i { color: #64748b !important; width: 18px; margin-right: 6px; }

  /* Announcement (matches index.md) */
  .announcement-container { margin-bottom: 50px; }
  .announcement-item {
    display: flex;
    align-items: center;
    background: #f8fafc;
    border-radius: 4px;
    padding: 16px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  .announcement-item .item__content { flex: 1; }
  .announcement-btn {
    display: inline-block;
    background-color: #00B4D8;
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.8rem;
    padding: 4px 10px;
    border-radius: 4px;
    text-decoration: none;
    margin-right: 8px;
  }
  .announcement-btn:hover { background-color: #0077b6; }
  .announcement-text { font-size: 0.95rem; color: #334155; font-weight: 500; }

  /* Member card grid — 4 per row */
  .mem-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
  }
  .mem-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 28px 20px 24px 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    box-sizing: border-box;
  }
  .mem-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
    border-color: #00B4D8;
  }
  .mem-avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin: 0 auto 20px auto;
    background-size: cover;
    background-position: center;
    border: 3px solid #e2e8f0;
  }
  .mem-name { font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 8px; }
  .mem-meta { font-size: 0.85rem; color: #475569; line-height: 1.6; word-break: break-word; margin-bottom: 4px; }
  .mem-meta:last-of-type { margin-bottom: 18px; }

  .mem-icon-row { display: flex; justify-content: center; gap: 10px; }
  .mem-icon-btn, .mem-icon-btn:visited {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: #f1f5f9;
    color: #334155 !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.95rem;
    text-decoration: none !important;
    transition: all 0.2s ease;
  }
  .mem-icon-btn i { color: inherit !important; }
  .mem-icon-btn:hover, .mem-icon-btn:hover i { background: #00B4D8; color: #ffffff !important; text-decoration: none !important; }

  /* Alumni (compact) card */
  .alumni-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
  }
  .alumni-card, .alumni-card:hover {
    display: flex;
    align-items: center;
    gap: 12px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px 16px;
    text-decoration: none !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    transition: all 0.25s ease;
    box-sizing: border-box;
  }
  a.alumni-card:hover { border-color: #00B4D8; box-shadow: 0 6px 14px rgba(0, 180, 216, 0.15); }
  a.alumni-card:hover .alumni-name {
    color: #1A365D !important;
    text-decoration-line: underline !important;
    text-decoration-color: #1A365D !important;
  }
  .alumni-avatar {
    flex-shrink: 0;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background-size: cover;
    background-position: center;
    border: 2px solid #e2e8f0;
  }
  .alumni-info { min-width: 0; }
  .alumni-name, a .alumni-name { font-size: 0.9rem; font-weight: 700; color: #0f172a !important; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-decoration: none !important; }
  .alumni-badge, a .alumni-badge { font-size: 0.78rem; color: #64748b !important; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-decoration: none !important; }

  @media (max-width: 992px) {
    .mem-grid { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 576px) {
    .director-card { flex-direction: column; text-align: center; }
    .director-contact { align-items: center; }
    .mem-grid { grid-template-columns: 1fr; }
    .mem-avatar { width: 130px; height: 130px; }
    .alumni-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }
  }
</style>
{% endraw %}

<div class="vslab-container">

<div class="mem-section">
<h2 class="vslab-heading">Director</h2>
{% assign member = site.data.members[0] %}
{% if member.link %}
<a href="{{ member.link }}" target="_blank" class="director-card">
{% else %}
<div class="director-card">
{% endif %}
  {% if member.img %}
    <div class="director-avatar" style="background-image: url('/assets/images/profile/{{ member.img }}');"></div>
  {% else %}
    <div class="director-avatar" style="background-image: url('/assets/images/profile/default-{{ member.gender }}.png');"></div>
  {% endif %}
  <div class="director-info">
    <div class="director-name">{{ member.name.en }}</div>
    {% if member.affiliation %}<div class="director-role">{{ member.affiliation }}</div>{% endif %}
    <div class="director-contact">
      {% if member.email %}<div><i class="fas fa-envelope"></i>{{ member.email }}</div>{% endif %}
    </div>
  </div>
{% if member.link %}
</a>
{% else %}
</div>
{% endif %}
</div>

<div class="announcement-container">
  <div class="announcement-item">
    <div class="item__content">
      <a class="announcement-btn" href="/recruitments" target="_blank">Join Our Lab</a>
      We are looking for graduate students who are enthusiastically interested in artificial intelligence and machine learning for data science. Please click <a href="/recruitments" target="_blank">[link]</a> if you're interested!
    </div>
  </div>
</div>

<div class="mem-section">
<h2 class="vslab-heading">Graduate Students</h2>
<div class="mem-grid">
  {% for member in site.data.members %}
  {% if member.type == "grad" %}
  <div class="mem-card">
    {% if member.img %}
      <div class="mem-avatar" style="background-image: url('/assets/images/profile/{{ member.img }}');"></div>
    {% else %}
      <div class="mem-avatar" style="background-image: url('/assets/images/profile/default-{{ member.gender }}.png');"></div>
    {% endif %}
    <div class="mem-name">{{ member.name.en }}</div>
    {% if member.email %}<div class="mem-meta">{{ member.email }}</div>{% endif %}
    {% if member.affiliation %}<div class="mem-meta">{{ member.affiliation }}</div>{% endif %}
    <div class="mem-icon-row">
      {% if member.email %}<a class="mem-icon-btn" href="mailto:{{ member.email }}" title="Email"><i class="fas fa-envelope"></i></a>{% endif %}
      {% if member.link %}
        <a class="mem-icon-btn" href="{{ member.link }}" target="_blank" title="Link">
          {% if member.link contains "github" %}<i class="fab fa-github"></i>
          {% elsif member.link contains "linkedin" %}<i class="fab fa-linkedin-in"></i>
          {% elsif member.link contains "notion" %}<i class="fas fa-file-alt"></i>
          {% else %}<i class="fas fa-link"></i>
          {% endif %}
        </a>
      {% endif %}
    </div>
  </div>
  {% endif %}
  {% endfor %}
</div>
</div>

<div class="mem-section">
<h2 class="vslab-heading">Undergraduate Students</h2>
<div class="mem-grid">
  {% for member in site.data.members %}
  {% if member.type == "undergrad" %}
  <div class="mem-card">
    {% if member.img %}
      <div class="mem-avatar" style="background-image: url('/assets/images/profile/{{ member.img }}');"></div>
    {% else %}
      <div class="mem-avatar" style="background-image: url('/assets/images/profile/default-{{ member.gender }}.png');"></div>
    {% endif %}
    <div class="mem-name">{{ member.name.en }}</div>
    {% if member.email %}<div class="mem-meta">{{ member.email }}</div>{% endif %}
    {% if member.affiliation %}<div class="mem-meta">{{ member.affiliation }}</div>{% endif %}
    <div class="mem-icon-row">
      {% if member.email %}<a class="mem-icon-btn" href="mailto:{{ member.email }}" title="Email"><i class="fas fa-envelope"></i></a>{% endif %}
      {% if member.link %}
        <a class="mem-icon-btn" href="{{ member.link }}" target="_blank" title="Link">
          {% if member.link contains "github" %}<i class="fab fa-github"></i>
          {% elsif member.link contains "linkedin" %}<i class="fab fa-linkedin-in"></i>
          {% elsif member.link contains "notion" %}<i class="fas fa-file-alt"></i>
          {% else %}<i class="fas fa-link"></i>
          {% endif %}
        </a>
      {% endif %}
    </div>
  </div>
  {% endif %}
  {% endfor %}
</div>
</div>

<div class="mem-section">
<h2 class="vslab-heading">Past Members</h2>
<div class="alumni-grid">
  {% for member in site.data.members %}
  {% if member.type == "alumni" %}
  {% if member.link %}<a href="{{ member.link }}" target="_blank" class="alumni-card">{% else %}<div class="alumni-card">{% endif %}
    {% if member.img %}
      <div class="alumni-avatar" style="background-image: url('/assets/images/profile/{{ member.img }}');"></div>
    {% else %}
      <div class="alumni-avatar" style="background-image: url('/assets/images/profile/default-{{ member.gender }}.png');"></div>
    {% endif %}
    <div class="alumni-info">
      <div class="alumni-name">{{ member.name.en }}</div>
      {% if member.affiliation %}<div class="alumni-badge">{{ member.affiliation }}</div>{% endif %}
    </div>
  {% if member.link %}</a>{% else %}</div>{% endif %}
  {% endif %}
  {% endfor %}
</div>
</div>

</div>