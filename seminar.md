---
layout: article
title: ""
---

<style>
  .seminar-year-toggle {
    margin-bottom: 1.5em;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 0.5em;
  }
  .seminar-year-toggle > summary {
    cursor: pointer;
    font-size: 1.15em;
    font-weight: 700;
    padding: 6px 0;
    list-style: none;
    display: flex;
    align-items: center;
    user-select: none;
    color: #0f172a;
  }
  .seminar-year-toggle > summary::-webkit-details-marker { display: none; }
  .seminar-year-toggle > summary::before {
    content: "▶";
    display: inline-block;
    margin-right: 8px;
    font-size: 0.7em;
    transition: transform 0.2s ease;
    color: #1A365D;
  }
  .seminar-year-toggle[open] > summary::before {
    transform: rotate(90deg);
  }
  .seminar-year-toggle > summary:hover {
    color: #00B4D8;
  }
  .seminar-year-toggle > summary:hover::before {
    color: #00B4D8;
  }
</style>

## About Seminar

In this seminar, we discuss diverse research topics such as data mining, graph machine learning, and applied data science including recommender systems. Here are the details of the seminar.

* Time: Every thursday
* Place: 숭실대학교 정보과학관 301호

## Seminar Information
{% assign now_in_seconds = site.time | date: '%s' | plus: 0 %}
{% assign one_week_from_now = now_in_seconds | plus: 604800 %}

{% assign today_start_sec = site.time | date: "%Y-%m-%d 00:00:00" | date: "%s" | plus: 0 %}
{% assign current_year = site.time | date: '%Y' %}

{% assign sorted_seminars = site.data.seminars | sort: "Date" | reverse %}
{% assign grouped_seminars = sorted_seminars | group_by_exp: "item", "item.Date | date: '%Y'" %}

{% for group in grouped_seminars %}

{% assign visible_count = 0 %}
{% for seminar in group.items %}
  {% assign target_date_seconds = seminar.Date | date: '%s' | plus: 0 %}
  {% if seminar.Title != "" and target_date_seconds <= one_week_from_now %}
    {% assign visible_count = visible_count | plus: 1 %}
  {% endif %}
{% endfor %}

{% if visible_count > 0 %}
{% if group.name == current_year %}
### {{ group.name }}

|Date|Title|Speaker|Slide|
|:---:|:---:|:---:|:---:|
    {% for seminar in group.items -%}
        {% assign target_date_seconds = seminar.Date | date: '%s' | plus: 0 -%}
        {% if target_date_seconds < today_start_sec and seminar.Title != "" -%}
|{{seminar.Date | date: "%y/%m/%d"}}|[{{seminar.Title}}]({{seminar.Paper.URL}})|{{seminar.Speaker}}| [[link]({{seminar.Slide.URL}})]|
        {% elsif target_date_seconds <= one_week_from_now and seminar.Title != "" -%}
|{{seminar.Date | date: "%y/%m/%d"}}|`Upcoming`<br> [{{seminar.Title}}]({{seminar.Paper.URL}})|{{seminar.Speaker}}| [[link]({{seminar.Slide.URL}})]|
        {% endif -%}
    {% endfor -%}
{% else %}
<details class="seminar-year-toggle" markdown="1">
<summary>{{ group.name }}</summary>

|Date|Title|Speaker|Slide|
|:---:|:---:|:---:|:---:|
    {% for seminar in group.items -%}
        {% assign target_date_seconds = seminar.Date | date: '%s' | plus: 0 -%}
        {% if target_date_seconds < today_start_sec and seminar.Title != "" -%}
|{{seminar.Date | date: "%y/%m/%d"}}|[{{seminar.Title}}]({{seminar.Paper.URL}})|{{seminar.Speaker}}| [[link]({{seminar.Slide.URL}})]|
        {% elsif target_date_seconds <= one_week_from_now and seminar.Title != "" -%}
|{{seminar.Date | date: "%y/%m/%d"}}|`Upcoming`<br> [{{seminar.Title}}]({{seminar.Paper.URL}})|{{seminar.Speaker}}| [[link]({{seminar.Slide.URL}})]|
        {% endif -%}
{% endfor %}
</details>
{% endif %}
{% endif %}
{% endfor %}