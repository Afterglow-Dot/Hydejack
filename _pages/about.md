---
layout: about
title: About
description: 我的个人主页：记录学习、科研和生活。
permalink: /
---

<!--author-->

大家好！我是一名合肥工业大学通信工程专业的硕士研究生，目前研一在读。

这里是我记录研究生学习和生活的小站。我会在这里分享：

- 📚 **学习笔记**：课程笔记、文献阅读、工具使用
- 💻 **项目实践**：实验记录、代码实践、论文写作
- 🌱 **生活随笔**：读研日常、心态变化、读书分享

欢迎交流，我的邮箱是：[2026170686@mail.hfut.edu.cn](mailto:2026170686@mail.hfut.edu.cn)

## 最新动态

{% include news-list.html %}

## 最新文章

<div class="news-list">
  <ul>
  {% for post in site.posts limit: 5 %}
    <li>
      <span class="news-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
  </ul>
</div>

[更多文章 →]({{ '/blog/' | relative_url }})
