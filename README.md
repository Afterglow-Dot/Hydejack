# Dajie's Homepage

李大杰的个人主页与博客，基于 [Hydejack](https://hydejack.com/)（Jekyll 主题）搭建，
内容迁移自 [afterglow-dot.github.io](https://afterglow-dot.github.io/)。

- 站点地址：<https://afterglow-dot.github.io/Hydejack/>
- 主题：`jekyll-theme-hydejack` 9.x（免费版）
- 语言：简体中文（`lang: zh-CN`）

## 目录结构

| 路径 | 说明 |
| --- | --- |
| `_pages/index.md` | 首页（`layout: about`）：作者简介 + 最新动态 + 最新文章 |
| `_pages/blog.md` | 文章列表 `/blog/`，含标签与分类入口 |
| `_pages/news.md` | 动态列表 `/news/` |
| `_pages/publications.md` | 论文列表 `/publications/`（目前为空） |
| `_pages/projects.md` | 项目列表 `/projects/`（`_projects/` 为空，页面显示占位文案） |
| `_pages/404.md` | 404 页面（`permalink: 404.html`） |
| `_posts/` | 博客正文，文件名格式 `YYYY-MM-DD-英文标题.md` |
| `_news/` | 动态条目（collection `news`，永久链接 `/news/:name/`） |
| `_projects/` | 项目条目（collection `projects`，永久链接 `/projects/:path/`） |
| `scripts/gen_archives.py` | 扫描文章，自动生成标签 / 分类归档页（构建前运行） |
| `_featured_tags/` | 标签归档页（**自动生成，不入库**） |
| `_featured_categories/` | 分类归档页（**自动生成，不入库**） |
| `_layouts/blog.html` | 覆盖主题的 blog 布局，补上标题、描述与正文 |
| `_includes/news-list.html` | 首页「最新动态」列表 |
| `_data/authors.yml` | 作者信息（首页作者卡片、文章页脚使用） |
| `assets/img/` | 图片，`prof_pic.jpg` 为头像，`sidebar-bg.svg` 为侧栏背景 |
| `_sass/my-style.scss` | 自定义样式 |
| `_data/strings.yml` | 界面文案（当前为英文，与原站一致） |

> `_pages/` 是 Jekyll 的 `pages` collection（在 `_config.yml` 里声明，见 al-folio 原站同样的约定）：
> 目录以下划线开头，Jekyll 才不会把它当成普通目录、把 `_pages/foo.md` 映射成 `/pages/foo/`。
> 6 个页面都写了显式 `permalink`（`/`、`/blog/`、`/news/`、`/publications/`、`/projects/`、`404.html`），
> 所以文件位置与网址无关；**新增页面时记得写 `permalink`**，否则会按 `/pages/...`（collection 默认）生成。

> 主题自带的 `_data/social.yml`（社交平台图标对照表）已删除：本站只用到 GitHub 和邮箱，
> 而主题的 `social-list-item.html` 对 github / email / twitter 内置了图标与链接前缀。
> 以后要加 LinkedIn、RSS 等平台时，用 `git show fbf41f5:_data/social.yml > _data/social.yml` 恢复即可。

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

标签和分类**不需要手工建文件**：构建之前 `scripts/gen_archives.py` 会扫描所有文章的
`tags` 与 `categories`，自动在 `_featured_tags/`、`_featured_categories/` 里生成对应的归档页
（已有的一律覆盖，删掉的标签也会自动消失）。GitHub Actions 已经替你跑这一步，推送即可；
只有本地预览时才需要手动执行一次：

```bash
python3 scripts/gen_archives.py
```

中文标签的网址片段在脚本顶部的 `SLUG_MAP` 里维护（例如 `随笔 → /blog/tag/essay/`）；
没有登记的标签会自动取其英文小写连字符形式，转不出纯 ASCII 就直接用原名当网址。

## 本地预览

需要 Ruby 3.3+（版本写在 `.ruby-version`，GitHub Actions 也读这个文件）：

```bash
bundle install
bundle exec jekyll serve
```

## 部署

推送到 `master` 分支后，GitHub Actions（`.github/workflows/pages.yml`）会自动构建并发布，
构建产物随后由 `actions/deploy-pages` 部署到 <https://afterglow-dot.github.io/Hydejack/>。

仓库已在 **Settings → Pages → Build and deployment → Source** 里选好 **GitHub Actions**，
日常只需要提交并推送即可；构建状态可以在 <https://github.com/Afterglow-Dot/Hydejack/actions> 查看。

`_config.yml` 中的 `baseurl: '/Hydejack'` 对应仓库名；如果仓库改了名字，
需要同步修改，或改用工作流里的 `--baseurl "${{ steps.pages.outputs.base_path }}"`（已经是这样写的）。

## 许可

主题 [Hydejack](https://hydejack.com/) 版权归 Florian Klampfer 所有（GPL-3.0）；
本站内容（文章、图片）版权归李大杰所有。
