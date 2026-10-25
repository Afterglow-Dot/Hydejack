---
# ============================================================================
# 项目页模板（Hydejack 版）
# ============================================================================
# 这个文件用来展示你做过的课程项目、科研工作或代码实践。
# 每个项目一个 .md 文件。
#
# 用法：
#   1. 复制本文件到同一目录，重命名去掉开头的下划线，例如 1_my-project.md
#      （文件名以下划线开头的会被 Jekyll 跳过，不会发布，所以本模板不会被渲染）
#   2. 填好下面 front matter 的 title、description、category
#   3. 删掉这整段注释
#
# 注意：本目录的 permalink 是 /projects/:path/，:path 就是文件名（不含扩展名），
# 所以 1_my-project.md 的网址是 /projects/1_my-project/。
# 如果希望网址干净，文件名可以不带数字前缀，排序交给下面的 importance 控制。
#
# 【字段说明】
# layout: page         —— 固定写法，用主题自带的 page 布局，不要改成 post。
# title:               —— 项目卡片上显示的标题。
# description:         —— 卡片上的一句话简介，会显示在标题下方。
# importance:          —— 排序，数字越小越靠前（_pages/projects.md 按这个排序）。
# category:            —— 分类标签，会以“· 分类名”的形式显示在标题后面，随意起名。
# img:                 —— 预留字段。当前 /projects/ 是纯文字列表，不会显示图片；
#                         写了也不报错，等以后改成卡片式布局再启用。
# github:              —— 预留字段，同上。目前想在页面上露出仓库链接，
#                         请在正文里自己写一个 Markdown 链接。
# redirect:            —— 不使用：Hydejack 没有这个跳转机制，请直接在正文写链接。
# ============================================================================

layout: page
title: 示例项目
description: 一句话说明这个项目做什么。这段文字会显示在项目卡片上。
importance: 1
category: 科研项目
---

这是一个模板文件，演示项目页可以怎么写。内容确定后，修改标题、描述和分类，
改名成 `1_你的项目名.md`（去掉开头的下划线），或者直接删掉这个文件。

## 项目背景

说明项目要解决的问题。比如：这个项目是课程大作业，还是实验室的科研任务？

## 我负责的部分

- 具体工作一（例如：负责算法仿真）
- 具体工作二（例如：撰写实验报告）

## 结果

写下结论、指标或者收获。比如：实现了什么功能，取得了什么数据，学到了什么。

---

### 写项目卡片要用的 front matter

| 字段 | 作用 | 是否生效 |
| --- | --- | --- |
| `title` | 卡片标题 | 生效 |
| `description` | 卡片上的一句话简介 | 生效 |
| `category` | 分类标签，显示在标题后 | 生效 |
| `importance` | 排序，数字越小越靠前 | 生效 |
| `layout` | 固定写 `page` | 生效 |
| `img` | 卡片背景图 | 预留，当前列表不显示 |
| `github` | 仓库链接 | 预留，当前不生成按钮 |
| `redirect` | 点击卡片跳转 | 不支持 |

### 在正文里放图片

先把图片放到 `assets/img/` 下。**路径必须用 Liquid 的 `relative_url` 包一层**，
因为本站在子路径 `/Hydejack/` 下，直接写 `/assets/img/xxx.jpg` 会 404：

```markdown
{% raw %}![图片说明]({{ '/assets/img/prof_pic.jpg' | relative_url }}){% endraw %}
```

（示例外层包了 `raw` 标签，只是为了让 Liquid 表达式原样显示；自己写正文时不要带这个标签。）

想加图注可以让图片单独成段并在下一行写斜体：

```markdown
{% raw %}![图片说明]({{ '/assets/img/prof_pic.jpg' | relative_url }})

*图 1：这里写图注。*{% endraw %}
```

### 并排放两张图

Hydejack 没有 Bootstrap，所以不要用 `row` / `col-sm` 栅格类。直接连着写两张图，
它们会各自占满一行；确实要并排，用一小段内联样式即可：

```html
{% raw %}<div style="display: flex; gap: 1rem;">
  <img src="{{ '/assets/img/a.jpg' | relative_url }}" alt="左图" style="width: 50%;">
  <img src="{{ '/assets/img/b.jpg' | relative_url }}" alt="右图" style="width: 50%;">
</div>{% endraw %}
```
