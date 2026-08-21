# CLAUDE.md — 个人主页项目

## 项目目标
为黄允（南京大学政府管理学院博士生）制作极简学者主页（参考何国俊、王绍达），部署到 GitHub Pages。规划见 `PLAN.md`，任务见 `TODO.md`，留痕见 `CHANGELOG.md`。

## 技术栈
- 内容：`content/*.yml`（唯一数据源，用户会自己改）
- 构建：`python build.py`（PyYAML + Jinja2，conda base 已有）→ `docs/`
- 模板：`templates/index.html.j2`；样式：`assets/css/style.css`（CSS 变量）
- 部署：GitHub Pages，`main` 分支 `/docs` 目录，需 `docs/.nojekyll`

## 硬性约束
- 不引入外链字体 / CDN / JS 框架；字体用系统中文字体栈
- 公开内容禁止出现手机号、住址；`*.docx` 已 gitignore，不要取消
- 内容改动只改 YAML，不要在模板里写死文字
- 数据为空的板块在模板中自动隐藏
- 中文文案遵循 fix-chinese 规范（中英文之间加空格、去翻译腔）

## 工作流
1. 改动前读 `TODO.md` 找到对应任务；完成后勾选并注日期
2. 每次有意义的改动追加 `CHANGELOG.md`
3. 提交按类别分开：`content:` / `style:` / `build:` / `docs:` / `chore:` / `research:`，中文提交信息，不加 Co-Authored-By
4. 改完模板或样式必须重新 `python build.py` 并提交 `docs/`
5. 改技术方案或视觉规范 → 更新 `PLAN.md` 版本号与变更记录

## 常用命令
```bash
python build.py
python -m http.server -d docs 8000
python -c "import yaml,glob;[yaml.safe_load(open(f,encoding='utf-8')) for f in glob.glob('content/*.yml')];print('YAML OK')"
```
