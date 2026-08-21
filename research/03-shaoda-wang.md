# 调研 03：王绍达（Shaoda Wang）个人主页

> 调研时间：2026-08-22 ｜ 来源 URL：
> - http://www.sdwang.org/ （首页，Home）
> - http://www.sdwang.org/research.html
> - http://www.sdwang.org/cv.html
> - http://www.sdwang.org/teaching.html
> - http://www.sdwang.org/2001325991.html （"中文"页）
> - http://www.sdwang.org/files/main_style.css （主题样式表）
>
> 抓取方式：curl 抓取 HTML 源码 + 样式表全部成功；WebFetch 对 https 域名报 SSL 握手失败（站点仅 http 可靠），未影响结论。

## 1. 页面整体结构

**技术栈：Weebly 建站平台**（非 Jekyll/Hugo/手写）。依据：
- 页脚 "Proudly powered by Weebly"；CSS/JS 全部来自 `cdn*.editmysite.com`（Weebly 的 CDN）；`_W.configDomain = "www.weebly.com"`。
- 类名前缀清一色 `wsite-`（`wsite-multicol`、`wsite-menu-default`、`wsite-content-title`），正文是 Weebly 可视化编辑器生成的 `<div class="paragraph">` + 大量内联 `<font size="4" color="#2a2a2a">`，属于"所见即所得"拖拽生成的脏 HTML。
- jQuery 1.8.3、Google Analytics 老版 ga.js、Cloudflare 邮箱混淆。Weebly 主题是 "Birdseye/teal" 系列（`theme/teal_icons.png`）。

**布局：**
- 固定宽度 **960px** 居中（`#content-wrapper{width:960px;margin:auto}`），**无 @media 媒体查询**，手机端由 Weebly 另给 `?view=mobile` 版本。
- 顶部居中站名 "SHAODA WANG (王绍达)"（Raleway 36px 全大写），下方居中横向导航栏，导航两侧有一条 1px 灰线装饰（`ul:before/after` 伪元素）。
- 首页为**两栏表格布局**：左栏 33.8% 放照片，右栏 66.2% 放"Appointments"列表；下方再一段全宽自我介绍。
- 照片：原图 783×800 px 的 JPEG，`max-width:100%` 自适应栏宽（实际约 290px 宽），右对齐，无边框无圆角。

**页面清单（按导航顺序）：**
1. **Home**：照片 + 4 行职务 + 邮箱 + 一段约 120 词的第三人称简介。信息密度中等。
2. **Research**：全站核心，4 个分组共 28 条论文 + 3 条其他写作，每条附 PDF 与媒体报道链接。密度极高。
3. **CV**：仅一行链接 "CV (2026.04)" 指向 PDF。密度极低。
4. **Teaching**：两门课名 + 平均评教分 + 评教 PDF 下载框（Weebly 文件组件）。密度低。
5. **中文**：一张照片 + 一段中文第三人称简介（学历、职务、研究领域、代表期刊、斯隆奖）+ 邮箱。密度低。

## 2. 各栏目写法细节

**首页简介**
- 先用"标签块"：`Appointments:` 加粗，下列 4 行（Associate Professor / Deputy Faculty Director / NBER FRF / BREAD Affiliate），再 `Email:` 加粗 + 地址。全部用 `<font size="4">`（约 18px），行间用 `<br><br>` 空一行。
- 再接一段**第三人称**（"I am an Associate Professor..."——实为第一人称，"I"开头）两端对齐段落：职位 → 兼职 → 奖项（2026 Sloan Fellow）→ 研究领域一句话 → 学历 → 博后经历。没有 CV 链接，没有社交媒体，没有 Google Scholar。
- 首页不放任何论文，论文全部推到 Research 页。

**论文列表（Research 页）**
- 分组标题用 `<h2 class="wsite-content-title">`：`Publications:` / `Working Papers:` / `Selected Works in Progress:` / `Other Writings:`，标题后带冒号，组间用 `<br>` 空行分隔，无分隔线。
- 分组逻辑是**按状态**而非按年份；组内按时间倒序（最新在前）。没有编号，没有年份侧栏。
- 单条格式（原文示例）：

  > **"Court Capture, Local Protectionism, and Economic Integration: Evidence from China"** (with Ernest Liu, Yi Lu, and Wenwei Peng)
  > <u>*Review of Economics and Statistics*</u>, Forthcoming
  > • Media Coverage: VoxChina; VoxDev; SCCEI Brief

  > **"Policy Experimentation in China: The Political Economy of Policy Learning"** (with David Y. Yang)
  > <u>*Journal of Political Economy*</u>, 2025, vol133(7), pp.2180-2228.
  > • Media Coverage: The Economist; CATO Research Brief; VoxDev; BFI; BFI China (in Chinese); Econimate (video)

  > **"Campaigning for Extinction: Eradication of Sparrows and the Great Famine in China"** (with Eyal Frank, Qinyun Wang, Xuebin Wang, and Yang You)
  > Revise and Resubmit, <u>*Quarterly Journal of Economics*</u>
  > • Media Coverage: EPIC; The Economist; CATO Research Brief

- 排版规则总结：
  - **标题加粗 + 引号包裹 + 整个标题就是 PDF 超链接**（指向站内 `/uploads/.../xxx.pdf`，新窗口打开），没有单独的 [PDF] 标签。
  - 作者不加粗、不列本人，用 "(with A, B, and C)" 写法，紧跟标题同一行。
  - **期刊名斜体 + 下划线**，换行单独一行，后接年、卷(期)、页码。
  - 状态标注：Working paper 若有审稿进展，直接在期刊行写 `Revise and Resubmit, <期刊>` 或 `Reject and Resubmit, American Economic Review`；无进展的就只有标题 + 作者，不写 "under review"。
  - 媒体报道作为条目下的**一级无序列表**（`<ul><li>`），字号比正文小一号（`size="3"` 约 16px），各媒体名用分号分隔、均为外链。没有 [Slides]/[Appendix]/[Code]/[Abstract] 折叠，没有摘要。
  - 特殊说明用斜体括号，如 "(*invited paper for special issue on China's green transition*)"。
  - Works in Progress 只有标题 + 合作者，无链接。
  - Other Writings 收录政策简报与中文论文，格式略松散（作者在前、期刊名不斜体），并注明 "(in Chinese)"。

**其他页面**
- CV：一行 PDF 链接并在括号里写更新月份 "(2026.04)"，让访客知道新旧。
- Teaching：课名 + "(Average evaluation: 4.6/5)" 把评教分直接亮出来，附评教报告 PDF。
- 中文页：面向国内受众的简介镜像，顺序为职务 → 学历时间线 → 领域 → 顶刊名录 → 奖项 → 邮箱，另放一张不同的生活照。

## 3. 视觉风格

- **配色**：页面底 `#f9f9f9`，内容区白底；正文文字 `#2a2a2a`/`#3e3f3f`（作者用内联色手动加深，覆盖主题默认的灰 `#8e8e8e`）；标题 `#484848`；主题链接色为青蓝 `#5199a8`（hover `#8dc7d3`），但作者又用 `!important` 把正文链接强制改成 `#2a2a2a`——所以论文标题链接与正文同色，靠加粗区分，整体近乎**黑白灰单色**，没有任何强调色块。
- **字体**：正文 Open Sans（无衬线）15px 基准，作者用 `<font size="4">` 抬到约 18px；站名/导航 Raleway 全大写（导航 13px）；主题 h2 本应为 Alice（衬线）26px，但站点级 CSS 把 `#wsite-content h2` 强制成 **"Comic Sans MS" !important**——Research 页四个分组标题在装有该字体的电脑上会显示为 Comic Sans，属于明显的失误/随性之笔。
- **行距留白**：段落 `padding:.5em 0`，条目之间靠 `<br><br>` 手动空行；header 上下 52/25px，导航下 40px，页底 100px 留白。论文区两端对齐（`text-align:justify`）。
- **响应式**：主题 CSS 无媒体查询，桌面固定 960px；移动端依赖 Weebly 单独渲染的 mobile 视图，体验不可控。
- 总体观感：实用主义、信息优先、视觉质感一般；靠内容（QJE/AER/JPE/ReStat + 大量媒体报道）撑场面，而非设计。

## 4. 对本项目的启示

**值得借鉴：**
1. **论文条目的三行结构**：第 1 行加粗标题（本身就是 PDF 链接）+ "(with 合作者)"；第 2 行斜体期刊 + 年卷页 或 R&R 状态；第 3 行小字 "Media Coverage:" 列表。这个结构信息完整、扫读快，可直接照搬成 HTML/Markdown 模板。
2. **按状态分组、组内倒序**：Publications / Working Papers / Works in Progress 三段式，比按年份分组更适合产出量不大的学者；博士生可改为 Working Papers / Publications / Works in Progress（把在投工作放最前）。
3. **R&R 状态写在期刊行**，用 "Revise and Resubmit, *Journal*" 一句话表达，不另加图标或标签；没有审稿进展就只留标题，不写 "under review"，避免频繁改动。
4. **首页 "Appointments + Email" 标签块**：把身份与联系方式用加粗标签分行列在照片旁，访客 3 秒内得到关键信息；博士生可对应改为 "Ph.D. Candidate, 南京大学政府管理学院 / Advisor / Email / CV"。
5. **中文页单独成页**：中英简介不混排，导航直接放"中文"两个字，对面向国内学界的博士生尤其实用。

**不适用于博士生主页的地方：**
- 用 Weebly 这类拖拽平台生成的 HTML 充满 `<font>` 内联样式、固定 960px、无响应式，维护困难；本项目应用 Hugo/Jekyll/手写 HTML + CSS 变量实现同样的视觉效果并原生支持手机。
- 首页不放论文、不放 CV 链接、不放 Google Scholar/ORCID，对已有顶刊背书的教授无妨，但博士生需要在首页直接展示 1-3 篇代表作与 CV 入口，降低求职市场的访问成本。
- "Media Coverage" 列表是该站信息密度的主要来源；博士生通常没有媒体报道，可把这一行替换成 [PDF] [Slides] [Code] [Abstract] 等功能链接，否则条目会显得空。
- Comic Sans 标题、链接与正文同色（仅靠加粗区分）、评教分直接贴在课名旁——这些都不应沿用；链接需要可辨识的颜色或下划线，标题字体应与正文字体成体系。
- 全站 `text-align:justify` 在窄屏上会出现大空洞，博士生主页应左对齐。
