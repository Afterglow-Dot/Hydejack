# 我的个人网站（Hydejack 版）

这是我的个人网站仓库，基于 [jekyll-theme-hydejack](https://github.com/hydecorp/hydejack) 主题搭建。  
网站用于记录研究生期间的学习、科研和生活，也会分享读书笔记、代码实践和日常思考。

- 🌐 网站地址：<https://afterglow-dot.github.io/Hydejack/>
- 📝 定位：研究生在读，通信工程，记录学习和生活。

---

## 📁 项目结构

| 目录 / 文件          | 作用                                                         |
| :------------------- | :----------------------------------------------------------- |
| `_config.yml`        | 网站全局配置：标题、作者、URL、baseurl、菜单、集合、主题开关 |
| `_pages/`            | 独立页面：首页、动态、博客、论文、项目、404         |
| `_posts/`            | 博客文章                                                     |
| `_news/`             | 动态：显示在首页和 `/news/`                     |
| `_projects/`         | 我的项目                                             |
| `_layouts/`          | 覆盖/补充主题布局                                   |
| `_includes/`         | 渲染首页动态                        |
| `_sass/`             | 自定义样式                           |
| `_data/`             | 数据文件：作者和社交链接、界面文案、字号和断点等变量         |
| `scripts/`           | 构建前运行的 Python 脚本：生成博客归档页, 并进行分页          |
| `assets/`            | 头像、侧栏背景图等静态资源                                   |
| `.github/workflows/` | GitHub Actions 自动部署配置                                  |

---

## 🚀 部署方式

每次向 `main` 分支推送代码，GitHub Actions 都会自动构建网站并部署到 GitHub Pages。不需要手动操作。

- 构建流程：生成归档页 → 生成分页 → Jekyll 构建 → 发布 Pages。
- 查看部署状态：进入 GitHub 仓库的 **Actions** 页面。
- 如果 Actions 显示红色叉号，点进去查看报错日志。

---

## 🧩 自定义部分

- **归档自动生成**：`scripts/gen_archives.py` 扫描所有文章的 `tags`、`categories`，自动产出 `/blog/tag/…`、`/blog/category/…` 页面，不用手动创建文件。中文标签的网址片段在脚本顶部的 `SLUG_MAP` 里配置。
- **博客分页**：`scripts/gen_pagination.py` 按 `blog_paginate` 分页，第 1 页是 `_pages/blog.md`，之后生成 `blog-page-N.md`。修改每页篇数只改 `_config.yml` 一处。
- **博客列表布局**：`_layouts/blog.html` 在主题基础上补了标题、描述和正文，并支持按标签/分类过滤。
- **数学公式**：用 kramdown 内置的 MathJax 渲染，构建时不需要 Node 环境。
- **界面文案**：全部软编码在 `_data/strings.yml`，想改「继续阅读」「上一篇」这类措辞直接修改这里即可。

---

## 📄 许可证与致谢

- 主题：[jekyll-theme-hydejack](https://github.com/hydecorp/hydejack)（免费版），遵循 GPL-3.0 许可证。
- 本站内容（博客文章、图片等）版权归 Dajie Li 所有，未经允许请勿转载。

---

© 2026 Dajie Li. 保留所有权利。
