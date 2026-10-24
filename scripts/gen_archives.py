#!/usr/bin/env python3
"""为所有标签 / 分类自动生成归档页（_featured_tags、_featured_categories）。

每次写新文章时，只要在 front matter 里写上 tags / categories，就不必再手工
新建归档页文件：构建前运行本脚本即可。

    python3 scripts/gen_archives.py

GitHub Actions 在 `jekyll build` 之前已经自动调用它，所以推送到 GitHub 之后
什么都不用管；只有本地预览时才需要自己跑一次。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"

# 中文 / 特殊字符标签对应的 URL 片段。没有列在这里的标签会自动使用
# 「把名字转成小写、用连字符连接」的规则；如果转不出纯 ASCII，就直接用原名
# （浏览时会被百分号编码，功能正常，只是网址不那么好看）。
SLUG_MAP = {
    "随笔": "essay",
    "生活": "life",
    "秋天": "autumn",
    "合肥": "hefei",
    "日常记录": "daily",
    "Daily Record": "daily-record",
    # 注意：下面这些是英文标签，本身就能直接用，列出来是为了固定顺序
    "Solitude": "solitude",
    "Life": "life-en",
    "Reflection": "reflection",
    "English": "english",
}

# 归档页顶部的展示顺序就是文件名顺序（即上面 slug 的字母序），不再手工指定。

FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)


def read_front_matter(text):
    match = FRONT_MATTER_RE.match(text)
    return match.group(1) if match else ""


def unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_list(front_matter, key):
    """读取 `tags: [a, b]` 或 `tags:` + 若干 `- a` 两种写法。"""
    lines = front_matter.splitlines()
    pattern = re.compile(r"^" + re.escape(key) + r"\s*:\s*(.*)$")
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if not match:
            continue
        rest = match.group(1).strip()
        if rest.startswith("["):
            inner = rest[1:]
            if inner.endswith("]"):
                inner = inner[:-1]
            return [unquote(item) for item in inner.split(",") if item.strip()]
        items = []
        for following in lines[index + 1:]:
            if not following.strip():
                continue
            item_match = re.match(r"^\s*-\s*(.+)$", following)
            if not item_match:
                break
            items.append(unquote(item_match.group(1)))
        return items
    return []


def make_slug(name):
    if name in SLUG_MAP:
        return SLUG_MAP[name]
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return ascii_slug or name


def collect():
    tags, categories = {}, {}
    posts = sorted(POSTS_DIR.rglob("*.md"))
    for post in posts:
        front_matter = read_front_matter(post.read_text(encoding="utf-8"))
        for name in parse_list(front_matter, "tags"):
            tags.setdefault(name, None)
        for name in parse_list(front_matter, "categories"):
            categories.setdefault(name, None)
    return sorted(tags), sorted(categories), len(posts)


def render(kind, name):
    if kind == "tag":
        description = "关于「%s」的文章。" % name
    else:
        description = "「%s」分类下的文章。" % name
    return (
        "---\n"
        "layout: blog\n"
        'title: "%s"\n'
        'slug: "%s"\n'
        "kind: %s\n"
        'description: "%s"\n'
        "---\n" % (name, name, kind, description)
    )


def write_archives(directory, kind, names):
    target = ROOT / directory
    target.mkdir(exist_ok=True)
    written = 0
    expected = set()
    for name in names:
        slug = make_slug(name)
        path = target / ("%s.md" % slug)
        expected.add(path.name)
        content = render(kind, name)
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print("  %-28s -> %s/%s.md" % (name, directory, slug))
    # 目录内容完全由本脚本生成，清掉已经不存在的标签 / 分类留下的旧页面
    for stale in sorted(target.glob("*.md")):
        if stale.name not in expected:
            stale.unlink()
            print("  删除过期归档页 %s/%s" % (directory, stale.name))
    return written


def main():
    if not POSTS_DIR.is_dir():
        print("找不到 _posts 目录：%s" % POSTS_DIR, file=sys.stderr)
        return 1

    tags, categories, post_count = collect()
    print("扫描到 %d 篇文章、%d 个标签、%d 个分类" % (post_count, len(tags), len(categories)))
    written = write_archives("_featured_tags", "tag", tags)
    written += write_archives("_featured_categories", "category", categories)
    print("已生成 / 更新 %d 个归档页" % written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
