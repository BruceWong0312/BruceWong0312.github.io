# 调研 02：何国俊（Guojun He）个人主页
> 调研时间：2026-08-22 ｜ 来源 URL：
> - 港大经管学院页（中文版）：https://www.hkubs.hku.hk/sc/people/guojun-he/
> - 港大"出版物"子页：https://www.hkubs.hku.hk/sc/people/guojun-he/publications/
> - 独立个人网站：https://www.guojunhe.com/ （含 publications.html / working-papers.html / about.html / teaching.html / news.html / cv.html / 20013259913161620171.html 中文简介）
> - 说明：个人网站本机直连超时（curl、Chrome 均无法访问，疑似 Weebly 托管在大陆网络受限），内容经 Tavily 抓取获得；HKU 页已拿到完整 HTML 与 Chrome 计算样式。

## 1. 页面整体结构

### 1.1 港大经管学院官方页（机构模板页）
- 技术栈：WordPress + Elementor 3.33（`meta generator` 明确标注），另含 WPML 多语言、Slider Revolution、AIOSEO；Google Fonts 加载 Open Sans。
- 布局：单栏、内容容器宽 1140px（外层 1200px），顶部固定导航（高 95px，透明背景）；照片在左上、400×426px 显示（原图 940×1000）、圆角 10px；页面总高约 4800px。
- 栏目顺序：
  1. 页头横幅"团队"（h1，52px 白字压图）
  2. 身份区：姓名、学科标签（经济学 / 管理及商业策略）、头衔 4 行、电话 / 邮箱 / 办公室 / 个人网站链接
  3. Academic & Professional Qualification：仅两行（Ph.D. UC Berkeley / B.A. Peking University）
  4. Biography：3 段，约 230 词
  5. Teaching：2 门课名
  6. Selected Publications：21 条纯文本 `<li>`，无链接
  7. Recent Publications：其实是媒体专栏（信报、FT 中文网等）的卡片流，10 条，带日期与摘要，分页 4 页
  8. 学院 Newsletter 订阅表单 + 页脚社交图标
- 信息密度：前半部分极简（学历 2 行、教学 2 行），论文区密度高但无交互；后半部分是学院统一模板内容，与学者本人关系不大。

### 1.2 独立个人网站 guojunhe.com（本人维护）
- 技术栈：Weebly 建站平台。依据：图片路径 `uploads/1/1/7/9/117970477/img-8173_orig.jpg` 是 Weebly 上传目录格式；中文页 URL `20013259913161620171.html` 是 Weebly 对非 ASCII 标题的编码（20013=中、25991=文、31616=简、20171=介）；各页以 `.html` 结尾；PDF 托管在 `filesusr.com`（早期 Wix 遗留）。
- 布局：单栏、顶部水平导航（9 项：Home / News / Publications / Working Papers / Teaching / CV / Recruiting / About / 中文简介），页脚重复同一导航；首页为"左文右图"两列表格：左侧 7 条加粗头衔（每条带机构链接），右侧证件照。
- 栏目清单（按导航顺序）：
  1. Home：头衔块 + "Recent Research Highlights"（2×2 网格，每格 = 小标题 + 缩略图 + 一句话结论 + 指向 NBER / AEA 的链接）+ 底部三个入口（Citations→Google Scholar / Publications / Working Papers）
  2. News：按年份倒序（2025、2024）的新闻条目 + "Media Coverage"一节，用 `[[WSJ]] [[REUTERS]]` 式方括号链接串
  3. Publications：单一列表，按年份倒序，约 30 条，不分子类
  4. Working Papers：I. Working Papers（13 条）→ Resting Working Papers（2 条，附"为何不再投稿"的坦诚说明）→ II. Working in Progress（9 条仅主题）
  5. Teaching：I. 课程 → II. 学生（在读 / 去向）→ III. 给博士生的资料库（按 Research / Writing / Presenting / Publishing… 十余类分组，近百个外链）
  6. CV：直接嵌入 4 页 PDF
  7. Recruiting：仅一个标题"Post-Doc and PhD Recruitment"
  8. About：Short Version（4 句）+ Long Version（5 段）+ 联系方式
  9. 中文简介：中文版头衔 + 简介 + 微信公众号二维码 + 联系表单

## 2. 各栏目写法细节

### 2.1 个人简介（Bio）
- 第三人称（"Guojun HE is an economist working on…"），姓氏全大写。
- 提供长短两版：Short Version 4 句话——身份 / 研究所 / 研究主题 / 编辑职务；Long Version 5 段——身份与兼职 → 编辑职务与研究主题 → 发表与影响 → 荣誉 → 教育背景与经历、咨询。
- 突出顺序：职位与机构 → 研究主题（一句话"benefits and costs of environmental and development policies, with particular focus on how governance structures affect policy outcomes"）→ 期刊层级 → 奖项 → 学历。
- HKU 页的 Bio 是较旧的 3 段版，结构相同：身份 → 研究兴趣 → 奖项与兼职。

### 2.2 论文列表
- 排版格式（个人网站原文，Markdown 还原）：
  ```
  * He, Guojun, Shaoda Wang, and Bing Zhang. "[Watering Down Environmental Regulation in China](QJE 链接)," ***Quarterly Journal of Economics***, 2020, 135(4): 2315-2385.
    [[Research Summary]] [[研究概要]]
    [Gregory Chow Best Paper Award, Chinese Economists Society, 2018]
    [Masahiko Aoki Best Paper Nomination Award 2021]

  * Greenstone, Michael, Guojun He, Ruixue Jia, and Tong Liu. "[Can Technology Solve the Principal-Agent Problem? Evidence from China's War on Air Pollution](AER 链接)," ***American Economic Review: Insights***, 2022, 4(1): 54-70.
    [[Research Summary]]
    Best Paper Award for Sustainable Paths Toward Carbon Neutrality by CICC Global Institute (CGI) in 2021

  * He, Guojun*+, Yuhang Pan+, Albert Park+, Yasuyuki Sawada+, and Elaine S. Tan+. "[Reducing Single-Use Cutlery with Green Nudges: Evidence from China's Food Delivery Industry](Science 链接)," ***Science***, 8 Sep 2023, Vol 381, Issue 6662.
  ```
- 规则：第一作者"姓, 名"，其余"名 姓"；题目加引号且整题是超链接（指向期刊页而非本地 PDF）；期刊名加粗斜体；年、卷（期）：页码；作者不加粗（本人姓名不高亮）；附加行用双层方括号 `[[Research Summary]] [[Data Files]] [[AEA Research Highlights]]`，奖项用单层方括号独立成行。
- 分类：Publications 页不分 Published / Forthcoming / 领域，仅按年份倒序一列到底；Working Papers 单独成页。列表顶部有一条 Note 说明作者排序规则（经济学期刊按字母序；综合科学期刊用 * 标通讯作者、+ 标共同一作）。
- HKU 页同一列表的退化版：纯文本 `<li>`，仅期刊名 `<em>`，无任何链接、无奖项行。

### 2.3 其他栏目
- Working Papers：每条只有"题目 (with 合作者)"，不给链接、不给摘要；"Resting Working Papers"坦白写"Unfortunately, this paper cannot be published."。
- Teaching：课程写"课名 (课号), 学校"；学生去向写"姓名 (单位 职位)"一行排完。资料库是本页最重的部分，明显面向博士生读者。
- News：`**日期** — [标题](链接)` + 一段两三句摘要 + 来源链接串，按年分组。
- CV：直接放 PDF，不在网页重复内容。
- 中文简介：独立页面，而非中英切换；另加微信公众号二维码，面向国内读者。

## 3. 视觉风格
- HKU 页（Chrome 计算样式）：正文 Open Sans 16px / 行高 24px，正文色 `#344962`（深蓝灰），背景纯白，强调色 `#df3603`（橙红，用于按钮与少量标记），链接色与正文同色且无下划线，列表 `list-style: none`。留白大、分块清晰，但属于学院统一模板，个人辨识度低。
- 个人网站：Weebly 默认主题风格——白底、无衬线、顶部细导航、内容居中单栏；大量用水平分割线分段；整体"信息多于设计"，没有自定义配色。首页 Research Highlights 是唯一的图文卡片区。
- 响应式：HKU 页为 Elementor 断点 767px / 1140px，手机端单栏堆叠；Weebly 主题默认响应式，但表格式两列（头衔 / 照片）在窄屏会折行。

## 4. 对本项目的启示

### 值得借鉴
1. **长短两版 Bio**：首页放 4 句 Short Version（身份 → 研究主题一句话 → 方法 / 关注点 → 关键链接），About 页放 Long Version；博士生可把"研究主题一句话"写成类似"研究 X，尤其关注 Y 如何影响 Z"的句式。
2. **论文条目格式照搬**：作者全列、题目加引号并整题超链接、期刊加粗斜体、年卷期页；附加材料用方括号短标签独立一行（如 `[PDF] [Slides] [Data] [Code]`），奖项 / 媒体另起一行。分 Published / Working Papers 两块，块内按年份倒序即可，不必再按领域分。
3. **列表顶部一行 Note**：说明作者排序规则或标记含义（本人姓名是否加粗、* 通讯作者等），读者不用猜。
4. **首页"Research Highlights"**：每篇代表作一句话结论（"This study shows that…"）+ 链接，比直接堆标题更易读；博士生可放 2-3 篇工作论文的一句话卖点。
5. **News 写法**：`日期 — 标题 + 两句摘要 + 来源链接`，按年分组；CV 用 PDF 嵌入而非网页重写，减少维护点。

### 不适用于博士生主页
- 7 条头衔块、Recruiting 页、Students 去向、Media Coverage 链接串：博士生没有对应内容，硬放会显得空。
- 近百条"给博士生的资料"外链：维护成本高且与个人研究无关，至多放 5-10 条自己真用过的。
- Weebly 这类建站平台：大陆访问不稳定（本次直连即超时），且模板感强；建议用静态 HTML 或 Hugo/Jekyll 自托管，保留其"单栏 + 顶部导航 + 白底无衬线"的骨架即可。
- 中文简介单独成页的做法可以保留，但博士生可直接做中英双语首页，不必复制一整套页面。
