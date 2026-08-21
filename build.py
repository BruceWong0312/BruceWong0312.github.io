#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build.py — 把 content/*.yml 渲染成 docs/index.html

用法：
    python build.py            # 渲染到 docs/
    python build.py --check    # 只校验 YAML，不渲染

依赖：PyYAML、Jinja2（conda base 已自带）
"""
import re
import sys
import shutil
import datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
ASSETS = ROOT / "assets"
DOCS = ROOT / "docs"

# 需要读取的内容文件 → 模板变量名
CONTENT_FILES = {
    "profile": "profile.yml",
    "education": "education.yml",
    "publications": "publications.yml",
    "projects": "projects.yml",
    "talks": "talks.yml",
    "skills": "skills.yml",
}

# 项目类型 → 页面上的分组标题与顺序
PROJECT_TYPES = [
    ("research", "科研项目"),
    ("service", "学术服务"),
    ("teaching", "教学助教"),
    ("survey", "调查实践"),
    ("other", "其他"),
]


def beijing_today() -> str:
    tz = datetime.timezone(datetime.timedelta(hours=8))
    return datetime.datetime.now(tz).strftime("%Y-%m-%d")


def load_yaml(path: Path):
    """读取 YAML；出错时打印文件名 + 行号后退出。"""
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        where = f"第 {mark.line + 1} 行，第 {mark.column + 1} 列" if mark else "位置未知"
        sys.exit(f"[YAML 错误] {path.relative_to(ROOT)} {where}\n{e}\n"
                 f"提示：值里含英文冒号/井号时请用双引号包起来；缩进用两个空格。")


def bold_self(text) -> Markup:
    """把 **xxx** 转成 <strong>xxx</strong>，其余内容做 HTML 转义。"""
    if not text:
        return Markup("")
    parts = re.split(r"\*\*(.+?)\*\*", str(text))
    out = []
    for i, part in enumerate(parts):
        out.append(f"<strong>{escape(part)}</strong>" if i % 2 else str(escape(part)))
    return Markup("".join(out))


def nonempty(value) -> bool:
    """列表/字符串是否非空（用于模板隐藏空板块）。"""
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return len(value) > 0


def group_projects(items):
    """按 type 分组，保持 PROJECT_TYPES 顺序；未知 type 归入"其他"。"""
    known = {k for k, _ in PROJECT_TYPES}
    groups = []
    for key, label in PROJECT_TYPES:
        rows = [p for p in (items or []) if (p.get("type") or "other") == key
                or (key == "other" and (p.get("type") or "other") not in known)]
        if rows:
            groups.append({"key": key, "label": label, "items": rows})
    return groups


def build(check_only: bool = False) -> None:
    data = {k: load_yaml(CONTENT / v) for k, v in CONTENT_FILES.items()}
    if check_only:
        print("YAML 全部通过校验。")
        return

    profile = data["profile"] or {}
    # 照片：文件存在用真图，否则用占位 SVG
    photo = profile.get("photo") or ""
    if not photo or not (ROOT / photo).exists():
        profile["photo"] = "assets/img/photo-placeholder.svg"
        profile["photo_is_placeholder"] = True
    # 链接：去掉空值
    links = profile.get("links") or {}
    profile["links"] = {k: v for k, v in links.items() if nonempty(v)}
    cv = profile["links"].get("cv")
    if cv and not (ROOT / cv).exists():
        print(f"[提示] CV 文件不存在：{cv}，导航中的 CV 链接暂不显示。")
        profile["links"].pop("cv")

    pubs = data["publications"] or {}
    ctx = {
        "p": profile,
        "education": data["education"] or [],
        "published": pubs.get("published") or [],
        "working": pubs.get("working") or [],
        "in_progress": pubs.get("in_progress") or [],
        "talks": data["talks"] or [],
        "project_groups": group_projects(data["projects"]),
        "skill_groups": (data["skills"] or {}).get("groups") or [],
        "training": (data["skills"] or {}).get("training") or [],
        "build_date": beijing_today(),
        "year": beijing_today()[:4],
    }

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["bold"] = bold_self
    env.tests["nonempty"] = nonempty

    html = env.get_template("index.html.j2").render(**ctx)

    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(html, encoding="utf-8", newline="\n")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    # 复制静态资源（排除 private 目录）
    shutil.copytree(
        ASSETS, DOCS / "assets", dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("private", "*.psd", "Thumbs.db"),
    )

    size_kb = (DOCS / "index.html").stat().st_size / 1024
    print(f"已生成 docs/index.html（{size_kb:.1f} KB），构建日期 {ctx['build_date']}。")
    print("本地预览：python -m http.server -d docs 8000  →  http://localhost:8000")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    build(check_only="--check" in sys.argv)
