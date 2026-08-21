# ✅ TODO — 个人主页任务清单

> 用法：完成一项把 `[ ]` 改成 `[x]` 并在行尾加日期；新任务直接追加到对应里程碑。
> 负责人：🤖 = Claude Code 执行 ｜ 🙋 = 需要黄允提供 / 确认 ｜ 🤝 = 协作

## M0 调研与规划（2026-08-22）
- [x] 🤖 提取简历内容 → `research/00-resume-extract.md`（已去隐私） — 08-22
- [x] 🤖 调研连享会教程 + lianyujun 模板 → `research/01-tutorial-and-template.md` — 08-22
- [x] 🤖 调研何国俊主页 → `research/02-guojun-he.md` — 08-22
- [x] 🤖 调研王绍达主页 → `research/03-shaoda-wang.md` — 08-22
- [x] 🤖 内容结构化为 `content/*.yml`（7 个文件）+ `content/README.md` — 08-22
- [x] 🤖 git 初始化、`.gitignore`（排除简历原件）、`.gitattributes`、`CHANGELOG.md` — 08-22
- [x] 🤖 `PLAN.md` / `TODO.md` / `README.md` / `CLAUDE.md` — 08-22

## M1 可预览原型（2026-08-22）
- [x] 🤖 `build.py`：读取 `content/*.yml` → Jinja2 渲染 → `docs/index.html`，复制 `assets/` 到 `docs/assets/`，页脚写入构建日期，YAML 报错时给出文件名 + 行号 — 08-22
- [x] 🤖 `templates/index.html.j2`：导航 + 7 个板块（Header / 简介 + 兴趣 / 教育 / 论文 / 会议 / 项目与服务 / 能力 + 培训）+ 页脚；荣誉奖项按要求不加 — 08-22
- [x] 🤖 `assets/css/style.css`：CSS 变量、760px 版心、系统中文字体栈（衬线标题 + 无衬线正文）、响应式断点 640px、论文三行结构样式、标签样式 — 08-22
- [x] 🤖 论文条目渲染规则：`**Huang, Y.**` → 加粗；有 `links` 则题目整体超链接到第一个链接，否则纯文本；`doi` 非空则追加 `[DOI]` — 08-22
- [x] 🤖 `docs/.nojekyll`、占位照片 `assets/img/photo-placeholder.svg` — 08-22
- [x] 🤖 本地预览并截图：`research/screenshots/m1-desktop-1280.png`、`m1-mobile-390.png` — 08-22
- [x] 🤖 提交：`build:` / `style:` / `content:` / `docs:` — 08-22

## M2 内容补全与打磨
- [ ] 🙋 提供照片 → `assets/img/photo.jpg`（建议 ≥ 400×500，JPG < 300KB）
- [ ] 🙋 提供不含手机号的 CV PDF → `assets/files/CV_YunHuang.pdf`
- [ ] 🙋 确认 / 补充：两篇论文 DOI、两次论坛年份、案例大赛年份（`content/` 里标 `# TODO` 处）
- [ ] 🙋 确认：是否显示 QQ 邮箱、导师姓名、博士在研课题；Google Scholar / ORCID / GitHub 链接
- [ ] 🤝 润色简介（第三人称、4–5 句、去 AI 味；参考何国俊 Short Version 结构：身份 → 研究主题一句话 → 方法 → 发表）
- [ ] 🤖 在研工作：若有 1–3 个在研题目，填入 `publications.yml: in_progress`
- [ ] 🤖 全页检查：无 "TODO" 字样、无空板块（数据为空的板块自动隐藏）、所有链接可点
- [ ] 🤖 可访问性与 SEO：`<title>`、`<meta description>`、`lang="zh-CN"`、图片 `alt`、Open Graph 基本标签
- [ ] 🤖 更新 `CHANGELOG.md`，提交 `content:` / `style:`

## M3 上线（GitHub Pages）
- [ ] 🙋 确认 GitHub 用户名（默认 `BruceWong0312`）；本机未装 `gh`，首次 push 会弹出浏览器授权
- [ ] 🤖 在 GitHub 新建公开仓库 `<用户名>.github.io`（空仓库，不勾 README）
- [ ] 🤖 `git remote add origin https://github.com/<用户名>/<用户名>.github.io.git` → `git push -u origin main`
- [ ] 🙋 仓库 Settings → Pages → Source: `Deploy from a branch` → Branch `main` / Folder `/docs` → Save
- [ ] 🤝 等待 1–3 分钟，访问 `https://<用户名>.github.io` 验证；手机端也打开一次
- [ ] 🤖 在 `README.md` 顶部写上线地址；`CHANGELOG.md` 记录上线日期

## M4 增强（可选，按需勾选）
- [ ] 英文版 `/en/index.html`：在 YAML 中增加 `*_en` 字段，`build.py` 渲染两套
- [ ] GitHub Actions：推送后云端执行 `build.py` 并发布，实现"在 GitHub 网页 / 手机上改 YAML 即更新"
- [ ] 自定义域名：购买域名 → 仓库根目录 `CNAME` → DNS CNAME 指向 `<用户名>.github.io`
- [ ] 访问统计：不蒜子（一行脚本）或自托管 Umami
- [ ] Google Scholar 个人主页建立并回链
- [ ] 论文摘要折叠（点击 [Abstract] 展开，≤ 20 行原生 JS）
- [ ] 把 LaTeX 简历改为从同一套 YAML 生成 PDF CV（pandoc + 模板），彻底单一数据源

## 🧾 变更日志（本文件）
- 2026-08-22：创建，M0 全部完成。
- 2026-08-22：M1 全部完成（荣誉奖项板块按用户要求移除，`content/awards.yml` 已删除）。
