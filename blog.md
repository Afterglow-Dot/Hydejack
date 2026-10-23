---
layout: blog
title: Dajie's Blog
description: Recording learning and life
permalink: /blog/
---

{% assign tag_docs = site.featured_tags | where: "kind", "tag" | sort: "order" %}
{% assign cat_docs = site.featured_tags | where: "kind", "category" | sort: "order" %}

<p class="post-tags">
  <strong>Tags</strong>
  {% for doc in tag_docs %}<a href="{{ doc.url | relative_url }}">#{{ doc.title }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
  <br>
  <strong>Categories</strong>
  {% for doc in cat_docs %}<a href="{{ doc.url | relative_url }}">{{ doc.title }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
</p>
