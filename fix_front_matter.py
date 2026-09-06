# -*- coding: utf-8 -*-
"""
检查 source/_posts 下所有 Markdown 文章的 front-matter，
自动补全缺失字段：
  title      = 文件名（不含扩展名）
  author     = AUTHOR 常量
  comments   = false
  categories = 相对 _posts 的目录路径（多级目录则多级分类）
  tags       = 目录名（默认最后一级，可改 TAGS_FROM = "all"）
  date       = 文件最后修改时间

用法:
  python fix_front_matter.py          # 直接修复并打印改动
  python fix_front_matter.py --check  # 只检查，不修改
已存在的字段一律保留原值，只补缺失项；全部齐全的文件不会被改动。
"""
import os
import sys
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(ROOT, "source", "_posts")
AUTHOR = "zvozve"
TAGS_FROM = "last"          # "last" = 只用最后一级目录名; "all" = 完整路径各级
DATE_FMT = "%Y-%m-%d %H:%M:%S"
CHECK_ONLY = "--check" in sys.argv


def parse_front_matter(block_lines):
    """把 front-matter 块解析为 {key: {"inline": str|None, "items": [..]}}（按原顺序）。"""
    fields = {}
    order = []
    cur = None
    for line in block_lines:
        stripped = line.strip()
        head, sep, inline = line.partition(":")
        key = head.strip()
        if sep and key and " " not in key and not stripped.startswith("-"):
            cur = key
            if key not in fields:
                fields[key] = {"inline": inline.strip() or None, "items": []}
                order.append(key)
            else:
                fields[key]["inline"] = inline.strip() or None
        elif stripped.startswith("-") and cur:
            fields[cur]["items"].append(stripped[1:].strip())
        elif cur and stripped:
            fields[cur]["items"].append(stripped)
    return fields, order


def emit(key, fields, default_inline=None, default_items=None):
    """优先输出已有值，缺失时输出默认值。"""
    if key in fields:
        f = fields[key]
        if f["inline"] is not None:
            return ["%s: %s" % (key, f["inline"])]
        if f["items"]:
            return ["%s:" % key] + ["- %s" % i for i in f["items"]]
        return ["%s:" % key]
    if default_items:
        return ["%s:" % key] + ["- %s" % i for i in default_items]
    if default_inline is not None:
        return ["%s: %s" % (key, default_inline)]
    return ["%s:" % key]


def fix_file(path, rel_dir):
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    newline = "\r\n" if "\r\n" in content else "\n"
    lines = content.splitlines()

    # 定位 front-matter 块
    if lines and lines[0].strip() == "---":
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        except StopIteration:
            return "SKIP（front-matter 没有闭合 ---）"
        body = lines[end + 1:]
        fields, _ = parse_front_matter(lines[1:end])
        had_fm = True
    else:
        body = lines
        fields, order = {}, []
        had_fm = False

    rel = os.path.relpath(path, POSTS_DIR).replace("\\", "/")
    segments = rel_dir.split("/") if rel_dir else []
    stem = os.path.splitext(os.path.basename(path))[0]
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime(DATE_FMT)
    tag_segs = segments if TAGS_FROM == "all" else segments[-1:]

    missing = [k for k in ("title", "author", "comments", "categories", "tags", "date")
               if k not in fields]
    if had_fm and not missing:
        return None  # 全部齐全，不改动

    out = ["---"]
    out += emit("title", fields, default_inline=stem)
    out += emit("author", fields, default_inline=AUTHOR)
    out += emit("comments", fields, default_inline="false")
    out += emit("categories", fields, default_items=segments or None)
    out += emit("tags", fields, default_items=tag_segs or None)
    out += emit("date", fields, default_inline=mtime)
    # 保留 canonical 之外的其它字段（如 abbrlink 等）
    for key in (k for k in _order_of(fields) if k not in ("title", "author", "comments",
                                                          "categories", "tags", "date")):
        out += emit(key, fields)
    out.append("---")

    new_content = newline.join(out + body) + newline
    changed = "新建 front-matter" if not had_fm else "补全缺失: " + ", ".join(missing)
    if not CHECK_ONLY:
        with open(path, "w", encoding="utf-8", newline="") as fp:
            fp.write(new_content)
    return changed


def _order_of(fields):
    return list(fields.keys())


def main():
    if not os.path.isdir(POSTS_DIR):
        print("找不到目录:", POSTS_DIR)
        sys.exit(1)

    fixed, checked = 0, 0
    for cur, dirs, files in os.walk(POSTS_DIR):
        for name in files:
            if not name.lower().endswith(".md"):
                continue
            path = os.path.join(cur, name)
            rel_dir = os.path.relpath(cur, POSTS_DIR).replace("\\", "/")
            if rel_dir == ".":
                rel_dir = ""
            checked += 1
            result = fix_file(path, rel_dir)
            if result:
                prefix = "[待修复] " if CHECK_ONLY else "[已修复] "
                print(prefix + os.path.relpath(path, ROOT) + " -> " + result)
                fixed += 1
    mode = "检查完成" if CHECK_ONLY else "修复完成"
    print("%s：共 %d 篇，%d 篇 %s" % (
        mode, checked, fixed, "缺字段" if CHECK_ONLY else "已处理"))


if __name__ == "__main__":
    main()
