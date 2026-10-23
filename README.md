# Dajie's Homepage

李大杰的个人主页与博客，基于 [Hydejack](https://hydejack.com/)（Jekyll 主题）搭建，
内容迁移自 [afterglow-dot.github.io](https://afterglow-dot.github.io/)。

- 站点地址：<https://afterglow-dot.github.io/Hydejack/>
- 主题：`jekyll-theme-hydejack` 9.x（免费版）
- 语言：简体中文（`lang: zh-CN`）

## 目录结构

| 路径 | 说明 |
| --- | --- |
| `index.md` | 首页（`layout: about`）：作者简介 + 最新动态 + 最新文章 |
| `blog.md` | 文章列表 `/blog/`，含标签与分类入口 |
| `news.md` | 动态列表 `/news/` |
| `publications.md` | 论文列表 `/publications/`（目前为空） |
| `projects.md` | 项目列表 `/projects/`（`_projects/` 为空，页面显示占位文案） |
| `_posts/` | 博客正文，文件名格式 `YYYY-MM-DD-英文标题.md` |
| `_news/` | 动态条目（collection `news`，永久链接 `/news/:name/`） |
| `_projects/` | 项目条目（collection `projects`，永久链接 `/projects/:path/`） |
| `_featured_tags/` | 标签页，`slug` 与文章的 `tags` 对应 |
| `_featured_categories/` | 分类页，`slug` 与文章的 `categories` 对应 |
| `_layouts/blog.html` | 覆盖主题的 blog 布局，补上标题、描述与正文 |
| `_includes/news-list.html` | 首页「最新动态」列表 |
| `_data/authors.yml` | 作者信息（首页作者卡片、文章页脚使用） |
| `assets/img/` | 图片，`prof_pic.jpg` 为头像，`sidebar-bg.svg` 为侧栏背景 |
| `_sass/my-style.scss` | 自定义样式 |

## 写一篇新文章

在 `_posts/` 下新建 `2026-11-01-my-post.md`：

```yaml
---
layout: post
title: 文章标题
date: 2026-11-01 21:00:00 +0800
description: 一句话摘要。
tags: [随笔, 生活]
categories: [日常记录]
toc:
  sidebar: left
---
```

标签和分类如果想在 `/blog/` 顶部出现，需要在 `_featured_tags/`（标签）或
`_featured_categories/`（分类）里建一个同名文件，`slug` 填标签/分类名。
每个归档页都要写一个 ASCII 的 `permalink`，例如 `_featured_tags/随笔.md` 里的
`permalink: /blog/tag/essay/`——中文或空格 slug 直接当 URL 会被转义。

## 本地预览

需要 Ruby 3.2+：

```bash
bundle install
bundle exec jekyll serve
```

## 部署

推送到 `master` 分支后，GitHub Actions（`.github/workflows/pages.yml`）会自动构建并发布。
首次使用需要在仓库 **Settings → Pages → Build and deployment → Source** 中选择
**GitHub Actions**。

`_config.yml` 中的 `baseurl: '/Hydejack'` 对应仓库名；如果仓库改了名字，
需要同步修改，或改用工作流里的 `--baseurl "${{ steps.pages.outputs.base_path }}"`（已经是这样写的）。

## 许可

主题 [Hydejack](https://hydejack.com/) 版权归 Florian Klampfer 所有（GPL-3.0）；
本站内容（文章、图片）版权归李大杰所有。
