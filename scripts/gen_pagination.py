#!/usr/bin/env python3
"""为 /blog/ 生成分页页（_pages/blog-page-2.md、blog-page-3.md …）。

分页规则：每 `blog_paginate` 篇（_config.yml，默认 10）一页，最新的在前
（排序在 _layouts/blog.html 里做）。第 1 页就是 _pages/blog.md 本身
（permalink: /blog/），本脚本只生成第 2 页及以后，例如 25 篇文章：

    /blog/            10 篇
    /blog/page/2/     10 篇
    /blog/page/3/      5 篇

    python3 scripts/gen_pagination.py

GitHub Actions 在 `jekyll build` 之前会自动调用；本地预览前自己跑一次即可。
"""

import math
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_config.yml"
POSTS_DIR = ROOT / "_posts"
PAGES_DIR = ROOT / "_pages"

DEFAULT_PER_PAGE = 10
BLOG_TITLE = "Dajie's Blog"
BLOG_DESCRIPTION = "Recording learning and life"
BLOG_URL = "/blog/"
GENERATED_PREFIX = "blog-page-"

PER_PAGE_RE = re.compile(r"^blog_paginate\s*:\s*(\d+)\s*$", re.M)


def per_page():
    """每页文章数取自 _config.yml 的 blog_paginate，读不到时用 10。"""
    try:
        match = PER_PAGE_RE.search(CONFIG.read_text(encoding="utf-8"))
    except OSError:
        return DEFAULT_PER_PAGE
    if not match:
        return DEFAULT_PER_PAGE
    value = int(match.group(1))
    return value if value > 0 else DEFAULT_PER_PAGE


def collect_posts():
    """按 Jekyll 的规则数文章：文件名要带 YYYY-MM-DD，且日期不在未来。"""
    today = date.today()
    total, skipped, undated = 0, 0, 0
    for path in POSTS_DIR.rglob("*.md"):
        try:
            published = date.fromisoformat(path.name[:10])
        except ValueError:
            undated += 1
            continue
        if published > today:
            skipped += 1
            continue
        total += 1
    if undated:
        print("  警告：%d 个文件名没有 YYYY-MM-DD 前缀，已忽略" % undated, file=sys.stderr)
    if skipped:
        print("  注意：%d 篇文章日期在未来，Jekyll 默认不构建，已忽略" % skipped)
    return total


def render(number):
    return (
        "---\n"
        "layout: blog\n"
        'title: "%s"\n'
        'description: "%s"\n'
        "permalink: %spage/%d/\n"
        "paginate_page: %d\n"
        "---\n" % (BLOG_TITLE, BLOG_DESCRIPTION, BLOG_URL, number, number)
    )


def main():
    if not POSTS_DIR.is_dir():
        print("找不到 _posts 目录：%s" % POSTS_DIR, file=sys.stderr)
        return 1

    step = per_page()
    total = collect_posts()
    total_pages = max(1, math.ceil(total / step))

    PAGES_DIR.mkdir(exist_ok=True)
    expected = set()
    written = 0
    for number in range(2, total_pages + 1):
        path = PAGES_DIR / ("%s%d.md" % (GENERATED_PREFIX, number))
        expected.add(path.name)
        content = render(number)
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print("  生成第 %d 页 -> _pages/%s" % (number, path.name))

    # 目录里只留脚本生成的分页页，文章变少时清理掉多余的
    for stale in sorted(PAGES_DIR.glob(GENERATED_PREFIX + "*.md")):
        if stale.name not in expected:
            stale.unlink()
            print("  删除过期分页 _pages/%s" % stale.name)

    print(
        "%d 篇文章，每页 %d 篇，共 %d 页（第 1 页为 _pages/blog.md），新生成/更新 %d 个分页"
        % (total, step, total_pages, written)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
