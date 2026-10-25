---
layout: page
title: News
description: 我的最新动态。
permalink: /news/
---

{% assign news_items = site.news | sort: "date" | reverse %}

<ul class="news-list-full">
{% for item in news_items %}
  <li>
    <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
    <p class="news-date">{{ item.date | date: "%Y-%m-%d %H:%M" }}</p>
    {{ item.content }}
  </li>
{% endfor %}
</ul>

