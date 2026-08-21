# 📋 PLAN — 黄允个人学术主页

> 版本：v1.0 ｜ 创建：2026-08-22 ｜ 状态：M0 完成，待执行 M1
> 配套文件：`TODO.md`（任务清单）· `CHANGELOG.md`（留痕）· `research/`（调研原始报告）· `content/`（全部可编辑内容）

## 0. 一句话目标

做一个**何国俊 / 王绍达式的极简学者主页**：白底、单栏、无衬线、信息优先，内容只保留博士阶段、论坛、项目经验、论文、专业能力、研究兴趣六块；所有文字放在 YAML 里随时可改，整个制作过程用 git + CHANGELOG 留痕，最终部署到 GitHub Pages。

## 1. 调研结论（详见 `research/0x-*.md`）

| 来源 | 技术 | 值得借鉴 | 不照搬 |
|---|---|---|---|
| 连享会教程 1644 | Quarto + GitHub Pages（`main` + `/docs`） | 部署流程：仓库名必须是 `用户名.github.io`；Pages 从 `/docs` 读；加 `.nojekyll`；自定义域名用 `CNAME` | Quarto 需额外安装；模板论文手写三处重复；外链 8 个 Google Fonts 且无中文字体栈 |
| lianyujun 模板仓库 | Quarto 1.6 + Bootstrap 5 | 中英双页思路；`about.links` 结构化社交链接 | 残留 Hugo 文件、颜色变量互相覆盖、每次提交整个 `docs/` 噪声大 |
| 何国俊 | HKU 页 WordPress；个人站 Weebly | **长短两版 Bio**；论文条目"作者全列 + 引号题目超链接 + 加粗斜体期刊 + 年卷页"；列表顶部一行 Note 说明加粗/标记含义；首页 Research Highlights 一句话卖点 | 7 行头衔、招生页、近百条外链资料库；Weebly 大陆访问超时 |
| 王绍达 | Weebly，固定 960px | **论文三行结构**（加粗题目即 PDF 链接 / 斜体期刊或 R&R 状态 / 小字链接行）；按状态分组（Published / Working / In Progress）组内倒序；"中文"单独成页；近乎黑白灰单色 | 无响应式；链接与正文同色；`text-align: justify`；Comic Sans 标题 |

**共同点**：两位老师的页面都是"内容 > 设计"——白底、无衬线、单栏、几乎没有装饰色块、论文是页面的重心。本项目照这个骨架做，但用现代 CSS 实现响应式，并把内容从 HTML 里抽离成数据文件。

## 2. 技术选型

### 2.1 决策：纯静态 HTML + Python 构建脚本 + GitHub Pages

```
content/*.yml  ──►  build.py（Jinja2 模板渲染）  ──►  docs/index.html + docs/assets/
                                                          │
                                                   git push ─► GitHub Pages
```

| 方案 | 本机可用 | 改内容难度 | 样式控制 | 结论 |
|---|---|---|---|---|
| **A. 纯 HTML + Python 构建（选定）** | ✅ Python 3.12 / Jinja2 3.1 / PyYAML 6.0 已装 | 改 YAML，一处改全站生效 | 完全可控，可精确复刻极简风 | **采用** |
| B. Quarto（教程路线） | ❌ 未安装，需另装 CLI | 改 .qmd Markdown | Bootstrap 默认样式，要去壳 | 备选；如需博客 / R 图表再迁 |
| C. Jekyll（GitHub 原生） | ❌ 无 Ruby，本地不能预览 | 改 `_data/*.yml` | 可控 | 不选 |
| D. Hugo | ❌ 未安装 | 改 YAML/MD | 可控但模板语法陡 | 不选 |

选 A 的理由：① 不引入新工具链，用户本身熟悉 Python；② 调研发现两位老师的页面本质上就是一页静态 HTML，自己写 CSS 比去掉 Bootstrap 的壳更省事；③ 内容与样式彻底分离——论文列表只维护 `content/publications.yml` 一份；④ 构建产物是一个 HTML 文件，没有 `search.json` / `sitemap` 之类的提交噪声。

### 2.2 约束
- **零外部依赖运行时**：不加载 Google Fonts / CDN JS（大陆访问慢）。字体用系统中文字体栈：`"Noto Sans SC", "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif`。
- **无 JS 框架**：最多一段 20 行原生 JS（移动端导航折叠、平滑滚动）。
- **隐私**：公开页只放邮箱，不放手机号、住址；`简历.docx` 原件已被 `.gitignore` 排除。
- **单一数据源**：网页 / 中文页 / 英文页都从同一套 YAML 渲染。

## 3. 站点结构

### 3.1 页面
- `/`（`docs/index.html`）：中文单页主页，顶部锚点导航 —— **一期**
- `/en/`：英文版（同一数据的 `*_en` 字段渲染）—— **二期，可选**
- `/assets/files/CV_YunHuang.pdf`：简历 PDF（导航直链）

### 3.2 首页板块（自上而下）

| # | 板块 | 数据来源 | 写法要点（来自调研） |
|---|---|---|---|
| 0 | 顶部导航 | 固定 | 姓名 + 6 个锚点 + CV / English 链接；移动端折叠成一行 |
| 1 | **Header** | `profile.yml` | 左：姓名（中 + 英）、身份、单位、邮箱、链接行（CV · Google Scholar · GitHub · ORCID）；右：照片 ≈ 160–180px，方角或 4px 圆角 |
| 2 | **简介 + 研究兴趣** | `profile.yml` | 第三人称 4–5 句"短版 Bio"（何国俊）；下方兴趣用小标签列出（"喜好的领域"） |
| 3 | **教育经历** | `education.yml` | 三行时间线，博士在读置顶，可加导师 / 研究课题（"博士阶段"） |
| 4 | **论文** | `publications.yml` | 分"已发表 / 工作论文 / 在研"三组，组内倒序；条目三行：**题目**（有 PDF 则整题超链接）+ 作者（本人加粗）/ *期刊* 年卷页 或 状态 / 小字 `[PDF] [Slides] [DOI]`；顶部一行 Note："加粗为本人；† 通讯作者" |
| 5 | **学术会议** | `talks.yml` | `年份 · 口头汇报 / 海报 · 会议名（主办方）` + 论文题目 |
| 6 | **项目与学术服务** | `projects.yml` | 按类型分组：科研项目 / 学术服务（审稿、推文）/ 助教 / 调查；每条"时间 · 角色 · 项目名 + 一句话" |
| 7 | **专业能力** | `skills.yml` | 三行标签：研究方法 / 编程与软件 / 语言；下方小节"学术培训" |
| 8 | **荣誉奖项** | `awards.yml` | 年份 + 奖项名，一行一条 |
| 9 | 页脚 | 自动 | "最后更新：YYYY-MM-DD"（构建时写入）· © 黄允 · 源码链接 |

### 3.3 视觉规范
- 版心最大宽度 **760px**，左右内边距 24px；`< 640px` 时照片移到姓名上方居中。
- 字号：正文 16px / 行高 1.75；h1 28px；h2 20px（带 1px 浅灰下边线）；小字 13–14px。
- 颜色（CSS 变量，`assets/css/style.css` 顶部集中定义，改一处全站变）：
  `--bg #fff` · `--text #1f2328` · `--muted #6b7280` · `--link #1d4e89` · `--link-hover #0b3a6b` · `--rule #e5e7eb` · `--tag-bg #f3f4f6`
- 链接：与正文区分（深蓝）+ hover 下划线——吸取王绍达页"链接与正文同色"的教训。
- 文字左对齐，不用 justify。
- 不做暗色模式、不加动画（极简优先）。

## 4. 目录结构（目标态）

```
个人主页/
├── PLAN.md  TODO.md  CHANGELOG.md  README.md  CLAUDE.md
├── content/                # ★ 你日常只改这里
│   ├── README.md           # 修改指南
│   ├── profile.yml  education.yml  publications.yml  projects.yml
│   └── talks.yml  skills.yml  awards.yml
├── templates/
│   └── index.html.j2       # Jinja2 模板（页面骨架）
├── assets/
│   ├── css/style.css       # 唯一样式表
│   ├── img/photo.jpg       # 照片
│   └── files/CV_YunHuang.pdf
├── build.py                # python build.py → 渲染到 docs/
├── docs/                   # GitHub Pages 发布目录（构建产物 + assets 副本）
│   ├── index.html  .nojekyll  assets/
├── research/               # 调研留痕（00 简历提取 / 01–03 参考站分析）
└── .gitignore  .gitattributes
```

## 5. 留痕机制

| 层次 | 工具 | 规则 |
|---|---|---|
| 代码级 | `git log` | 每次改动按类别分开提交：`content:` / `style:` / `build:` / `docs:` / `chore:` / `research:`；提交信息写中文、说清"改了什么" |
| 项目级 | `CHANGELOG.md` | 每个工作日 / 里程碑一条，记"做了什么、为什么、影响哪些文件" |
| 任务级 | `TODO.md` | 勾选 `[x]` 并在行尾注日期；新需求直接追加 |
| 决策级 | `PLAN.md` + `research/` | 改技术方案或设计规范时在本文件顶部 bump 版本并在 §9 写"变更记录" |
| 产物级 | 页脚"最后更新" | `build.py` 自动写入构建日期，访客可见 |
| 云端 | GitHub 提交历史 | 推送后公开可查，天然备份 |

## 6. "随时修改"工作流

```bash
# ① 改内容：编辑 content/*.yml（见 content/README.md，新增论文 = 复制一条改字段）
# ② 重新生成 + 本地预览
python build.py
python -m http.server -d docs 8000      # 浏览器打开 http://localhost:8000
# ③ 留痕 + 发布
git add -A && git commit -m "content: 新增 xxx 论文" && git push
# GitHub Pages 约 1 分钟后更新
```
- 改样式：只动 `assets/css/style.css`（颜色在顶部 CSS 变量里）。
- 改板块顺序 / 增删板块：动 `templates/index.html.j2`，每个板块是一个 `<section id="...">` 块，可整段剪切。
- 二期可加 GitHub Actions：推送后云端自动运行 `build.py`，这样在 GitHub 网页端直接改 YAML 也能生效（手机上也能更新）。

## 7. 里程碑

| 里程碑 | 内容 | 验收标准 | 预计 |
|---|---|---|---|
| **M0 调研与规划** | 4 项调研、内容 YAML、PLAN / TODO、git 初始化 | 本文件 + `TODO.md` 提交 | ✅ 2026-08-22 |
| **M1 可预览原型** | `build.py` + 模板 + CSS，渲染全部 8 个板块 | `python build.py` 无报错；本地浏览器桌面 / 手机宽度均正常 | 08-22 ~ 08-23 |
| **M2 内容补全与打磨** | 补 TODO 字段（照片、CV PDF、DOI、年份、导师）、文案润色 | 页面无 "TODO" 字样；论文条目有可点链接 | 08-23 ~ 08-25 |
| **M3 上线** | 建 `BruceWong0312.github.io` 仓库、推送、开启 Pages | `https://brucewong0312.github.io` 电脑与手机均可访问 | 08-25 ~ 08-26 |
| **M4 增强（可选）** | 英文版 `/en/`、GitHub Actions 自动构建、Google Scholar 链接、自定义域名、访问统计 | 按需 | 之后 |

## 8. 待确认事项（不阻塞 M1，默认按括号内假设推进）

1. GitHub 账号是否为 `BruceWong0312`（假设是；对应仓库名 `BruceWong0312.github.io`）
2. 主页主语言：中文优先、英文二期（假设是）
3. 照片与 CV PDF 由你提供，放入 `assets/img/photo.jpg`、`assets/files/CV_YunHuang.pdf`
4. 是否展示 QQ 邮箱、导师姓名、博士在研课题（默认只显示 NJU 邮箱，其余留空不显示）
5. 两篇论文的 DOI、两次论坛的年份（`content/` 里标了 `# TODO`）

## 9. 变更记录
- v1.0（2026-08-22）：初版。
