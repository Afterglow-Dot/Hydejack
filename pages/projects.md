---
layout: page
title: Projects
description: 我的课程项目、科研工作和代码实践。
permalink: /projects/
---

{% assign projects = site.projects | sort: "importance" %}

{% if projects.size > 0 %}
<ul class="project-list">
{% for project in projects %}
  <li>
    <a href="{{ project.url | relative_url }}"><strong>{{ project.title }}</strong></a>{% if project.category %} <span class="project-category">· {{ project.category }}</span>{% endif %}
    <p>{{ project.description }}</p>
  </li>
{% endfor %}
</ul>
{% else %}
暂时还没有项目。
{% endif %}
