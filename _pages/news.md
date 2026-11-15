---
layout: page
title: News
description: 我的最新动态。
permalink: /news/
---

{% assign news_items = site.news | sort: "date" | reverse %}

<ul class="news-list">
{% for item in news_items %}
  <li>
    <span class="news-date">{{ item.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
  </li>
{% endfor %}
</ul>

