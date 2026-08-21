# 🏠 黄允 · 个人学术主页

> 🌐 上线地址：**https://brucewong0312.github.io** ｜ 源码：https://github.com/BruceWong0312/BruceWong0312.github.io
> 📐 风格：何国俊 / 王绍达式极简学者主页 —— 白底、单栏、内容优先
> 🛠️ 技术：`content/*.yml` → `build.py`（Python + Jinja2）→ `docs/index.html` → GitHub Pages

## 📂 文件导航

| 文件 / 目录 | 用途 |
|---|---|
| `content/` | ✏️ **日常只改这里**：姓名、简介、论文、项目、会议、能力（YAML） |
| `content/README.md` | 修改指南 + YAML 三条规则 |
| `build.py` | 一键生成网页：`python build.py` |
| `templates/index.html.j2` | 页面骨架（想调板块顺序改这里） |
| `assets/css/style.css` | 样式（颜色在顶部 CSS 变量） |
| `docs/` | 构建产物，GitHub Pages 发布目录，不要手改 |
| `PLAN.md` | 技术选型、页面结构、视觉规范、里程碑 |
| `TODO.md` | 任务清单（可勾选） |
| `CHANGELOG.md` | 留痕日志 |
| `research/` | 参考网站调研报告 |

## 🚀 三步更新

```bash
python build.py                          # 1. 生成
python -m http.server -d docs 8000       # 2. 预览 http://localhost:8000
git add -A && git commit -m "content: ..." && git push   # 3. 发布
```

## 🔒 隐私
公开页面只放邮箱；`简历.docx` 原件已在 `.gitignore` 中排除，不会进入仓库。
