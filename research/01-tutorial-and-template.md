# 调研 01：连享会教程 + lianyujun 模板仓库

> 调研时间：2026-08-22 ｜ 来源：
> - 教程：https://www.lianxh.cn/details/1644.html （连小白，2025-07-18，《50 分钟搞定个人主页：Fork 模板 + GitHub Pages + Quarto 完整教程》，正文经 `/web-api/article?id=1644` 接口获取）
> - 模板：https://github.com/BruceWong0312/lianyujun.github.io （上游 https://github.com/lianyujun/lianyujun.github.io，再上游 https://github.com/chizapoth/chizapoth.github.io）
> - 本地克隆：`C:/Users/19068/AppData/Local/Temp/claude/D--cc-----/d64e2c82-caef-4eb0-b264-3c265d8d7f86/scratchpad/lianyujun-template`

## 1. 教程要点（lianxh 1644）

**技术路线**：GitHub Pages（托管）+ Quarto（静态站生成），不是 Jekyll/Hugo/纯 HTML。推荐直接 Fork `lianyujun/lianyujun.github.io` 模板（7 个 `.qmd` 静态页），或参考 chizapoth 等 Quarto 模板。主打理由：免费、无需服务器和域名、不写 HTML/CSS/JS、Markdown + YAML 即可维护。

**工具链**：GitHub 账号、GitHub Desktop（避免命令行）、VS Code + Quarto 插件 + Markdown All in One、Quarto CLI；安装后 `quarto check` 验证。

**部署步骤**：
1. Fork（或 Use this template）模板仓库，仓库名必须为 `yourusername.github.io`；
2. GitHub Desktop 克隆到本地；
3. 修改 `index.qmd`（个人介绍/头像/链接）、`_quarto.yml`（站点标题、导航栏、输出目录）、`publications.qmd`/`blog.qmd` 等子页面、替换 `images/` 下头像和 logo；
4. 终端执行 `quarto render`，HTML 输出到 `docs/`，双击 `docs/index.html` 本地预览；
5. GitHub Desktop 提交并 Push；
6. 仓库 Settings → Pages → Source 选 `main` 分支 + `/docs` 目录 → Save，几分钟后 `https://yourusername.github.io` 上线；
7. 可选：仓库 About 设置勾选 "Use your GitHub Pages website" 显示主页链接；
8. 更新维护 = 改文件 → `quarto render` → 提交推送。

**注意事项 / 坑**：
- 仓库名必须严格等于 `用户名.github.io`，否则不会自动部署到根域名；
- 多个 GitHub 账号时要在 GitHub Desktop 中切换到正确账号（File → Options → Accounts）；
- 新增页面必须同步加进 `_quarto.yml` 的 navbar，否则无入口；
- 自定义域名：仓库根目录加 `CNAME` 文件 + DNS 指向 GitHub，GitHub 自动配 HTTPS；
- 进阶：博客 `categories`/`tags` 分类（参考 chizapoth）、嵌入 R/Python 交互图表（参考 kazuyanagimoto）；
- 教程推荐的其他模板：chizapoth（清爽，适合学生）、valegiunchiglia（两栏 CV）、vbaliga（纯文字极简）、drganghe（多目录/实验室）、samanthacsik（多栏）、kazuyanagimoto（美观但复杂，不推荐初学者）；
- 教程未涉及：GitHub Actions 自动渲染、Google Analytics/访问统计、SEO、中文字体。

## 2. 模板仓库结构（lianyujun.github.io）

**技术栈判断**：Quarto website（Quarto 1.6.39，`docs/index.html` 的 `<meta name="generator" content="quarto-1.6.39">`）+ Bootstrap 5 + 自定义 SCSS 主题。依据：`_quarto.yml` 中 `project.type: website`、`output-dir: docs`、`format.html.theme: styles.scss`；内容文件全是 `.qmd`；根目录有 `.nojekyll`（告诉 GitHub Pages 不要跑 Jekyll）。**没有 `.github/workflows`**，发布方式是把渲染产物 `docs/` 直接提交进仓库，Pages 从 `main` + `/docs` 读取。仓库里还残留 blogdown/Hugo 时代遗物：`.Rprofile`（设置 Hugo 0.101.0）、`.hugo_build.lock`，以及未被任何页面使用的 `_extensions/coatless/webr` 扩展和 `_freeze/` 缓存。LICENSE 为 MIT（Chi Zhang, 2022）。

**目录树（关键文件）**：
```
lianyujun.github.io/
├── _quarto.yml          # 站点配置：标题、navbar、页脚、主题、TOC
├── index.qmd            # 首页：about 模板 trestles，头像 + 社交链接 + 简介 + Background
├── publications.qmd     # 论文列表（Markdown 无序列表硬编码）+ 科研项目（有序列表）
├── books.qmd            # 书稿封面图 + 链接
├── blog.qmd             # 推文列表（New 10 / Hot 10 / ALL，纯 Markdown 链接）
├── codes.qmd            # Stata 命令清单
├── Chinese.qmd          # 中文简历页（navbar 中的「中文」）
├── CV.md                # 与 Chinese.qmd 内容几乎相同，notes.txt 说明是用 Typora 导出 PDF 的源
├── CV.pdf               # navbar 直接链接的 PDF 简历（600 KB）
├── about.qmd            # 仅一行占位，未进 navbar
├── Teaching.md          # 空文件，未进 navbar（但 docs/ 里有 Teaching.html 旧产物）
├── styles.scss          # 自定义主题（颜色变量 + 字体 + 规则）
├── images/              # bio-photo.jpg, lianyujun_2025.png(388K), *_full.jpg(1.2MB 未用), site-logo.png
├── docs/                # quarto render 产物，Pages 发布目录（含 site_libs/、search.json、sitemap.xml）
├── .nojekyll / robots.txt / sitemap.xml / search.json
├── _extensions/coatless/webr/   # 未使用的 webR 扩展
├── _freeze/ .Rprofile .hugo_build.lock   # 历史残留
└── readme.md / LICENSE / notes.txt
```

**栏目与数据存放**：navbar 右侧 7 项：Home / Publications / Books / Blogs / Codes / 中文 / CV(PDF)。所有内容均**直接写在各 `.qmd` 的 Markdown 正文中**，没有 YAML/BibTeX/CSV 数据文件，没有 Quarto listing；论文条目是手写的 `- 作者. 题目. **期刊**, 年, 卷(期): 页. [Link](...) [PDF](...)` 列表。首页社交链接写在 `index.qmd` 的 YAML `about.links` 里（icon + text + href），这是唯一结构化的数据。

**样式特点**：
- 布局：整体单栏正文 + 右侧 TOC（`toc-position: right`）；首页用 Quarto 内置 `about: template: trestles`，桌面端左栏圆形头像 + 链接列表、右栏文字，移动端自动堆叠；
- 响应式：Bootstrap 5 + Quarto 默认，navbar 有折叠按钮，宽度自适应；
- 配色：`_quarto.yml` 设 navbar 背景 `#A9CCE3`（浅蓝），而 `styles.scss` 又设 `$navbar-bg` 深绿、`$link-color` 红色——两处重复定义，且 SCSS 的 `rules` 段再用 `body{color:#000}`、`a{color:#0066cc}` 覆盖前面的变量，整体是咖啡棕标题 + 黑正文 + 蓝链接，变量定义大部分实际未生效；
- 字体：`@import` 了 8 个 Google Fonts（Lato 正文、PT Serif 标题、Source Code Pro 等），未声明任何中文字体栈；
- 全站搜索（`search: true`）、页面右上 Edit/Issue 链接（`repo-actions`）、页脚左右两栏。

**修改难易度**：
- 改论文列表：只动 `publications.qmd`，纯 Markdown，零门槛；但中文简历页 `Chinese.qmd` 和 `CV.md` 里各有一份「部分论文」副本，需手动同步三处；
- 改个人信息/链接：`index.qmd` 的 YAML 头 + 正文；
- 改栏目：`_quarto.yml` navbar；新建页面需同时建 `.qmd` 并加 navbar；
- 每次修改后必须本地 `quarto render` 并把整个 `docs/` 一起提交，提交 diff 噪声大（search.json、sitemap 每次都变）；
- Fork 后必改项：`_quarto.yml` 的 `title`、`site-url`、`repo-url`（当前仍指向 lianyujun）、页脚、`images/`、`CV.pdf`，并清理 about.qmd/Teaching.md/CV.md 等半成品文件。

## 3. 对本项目的启示

**值得借鉴**：
1. Quarto + GitHub Pages 路线本身成熟、免费、对学术用户友好，且用户已熟悉 Markdown，维护成本最低；`main` + `/docs` 的发布方式不依赖 Actions，调试直观。
2. 首页用 `about: template: trestles`（或 `jolla`/`solana` 等内置模板）一行配置就能得到头像 + 社交链接 + 简介的标准学术首页，链接用 YAML `about.links` 结构化维护（邮箱、GitHub、Google Scholar、ORCID、知乎等）。
3. 中英双页结构（英文 Home + 「中文」页）适合国内博士生：英文面向国际审稿人/合作者，中文面向国内导师和招生。
4. 栏目设计 Home / Publications / Teaching / CV 的骨架可直接复用；CV 同时提供网页版和 PDF 下载链接。
5. `.nojekyll`、`robots.txt`、`sitemap.xml`、全站搜索这些 SEO/可用性细节 Quarto 默认就给，直接保留。

**不建议照搬**：
1. 论文/项目全部手写在 Markdown 里且三处重复（publications.qmd、Chinese.qmd、CV.md）——本项目应把论文做成单一数据源（YAML 或 BibTeX，用 Quarto listing 或 `{{< include >}}` 渲染），一处修改全站生效。
2. `styles.scss` 的 8 个 Google Fonts `@import` 在国内访问慢甚至阻塞渲染，且没有中文字体栈——应去掉外链字体，改用系统中文字体栈（如 `"Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif`），或自托管。
3. 仓库里的历史残留（`.Rprofile`、`.hugo_build.lock`、`_extensions/webr`、`_freeze`、空的 Teaching.md、占位 about.qmd、1.2 MB 未使用大图）和颜色变量的重复/互相覆盖——应从干净的 `quarto create project website` 起步，只抄结构和配置思路，不整仓 Fork。
4. 提交 `docs/` 渲染产物的方式虽简单，但长期会让仓库膨胀、diff 混乱；本项目可考虑 GitHub Actions（`quarto-dev/quarto-actions`）在云端渲染并发布到 `gh-pages`，本地只提交源文件。
