---
layout: blog
title: Blog
description: Recording learning and life
permalink: /blog/
paginate_page: 1
---

{% comment %} 归档页顺序 = 按照文件名（slug）字母序。 {% endcomment %}
{% assign tag_docs = site.featured_tags | where: "kind", "tag" %}
{% assign cat_docs = site.featured_categories %}

<p class="post-tags">
  <strong>Tags</strong>
  {% for doc in tag_docs %}<a href="{{ doc.url | relative_url }}">#{{ doc.title }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
  <br>
  <strong>Categories</strong>
  {% for doc in cat_docs %}<a href="{{ doc.url | relative_url }}">{{ doc.title }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
</p>
