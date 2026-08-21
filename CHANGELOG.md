# 📜 CHANGELOG — 个人主页制作留痕

> 记录每一次有意义的改动：做了什么、为什么、影响哪些文件。
> 时间均为北京时间。细粒度记录见 `git log`。

## [Unreleased]

### 2026-08-22 · M1 可预览原型
- **构建脚本** `build.py`：PyYAML 读取 `content/*.yml`，Jinja2 渲染 `templates/index.html.j2` 到 `docs/index.html`；复制 `assets/`；页脚自动写入北京时间构建日期；YAML 出错时提示文件名 + 行号；照片 / CV 文件缺失时自动降级（占位图 / 隐藏链接）。
- **模板**：7 个板块（Header、简介 + 研究兴趣、教育、论文、学术会议、项目与学术服务、专业能力 + 学术培训），数据为空的板块自动隐藏；论文采用"题目 / 作者（本人加粗）/ 期刊·年卷页 + 小字链接"三行结构。
- **样式** `assets/css/style.css`：白底单栏 760px，衬线标题（宋体栈）+ 无衬线正文，墨蓝链接色，零外链字体、零 JS；640px 以下照片上移、时间线单列。
- **内容调整**：按用户要求**不加荣誉奖项**，删除 `content/awards.yml`；`profile.yml` 新增 `repo_url`；`projects.yml` 组内按时间倒序。
- **自检**：Chrome 1280 / 390 宽度全页截图存 `research/screenshots/`，控制台无报错。

### 2026-08-22 · 项目启动
- **调研**：抓取并分析 4 个参考资源（连享会教程 1644、lianyujun 模板仓库、何国俊主页、王绍达主页），结论存于 `research/01~03-*.md`。
- **内容结构化**：从 `简历.docx` 提取信息（`research/00-resume-extract.md`，已去除手机号/地址），拆成 7 个可编辑的 YAML 文件放在 `content/`，并写 `content/README.md` 说明修改方法。
- **留痕机制**：初始化 git 仓库；`.gitignore` 排除含隐私的简历原件；建立本文件。
- **规划**：产出 `PLAN.md`（技术选型、页面结构、设计规范、部署方案）与 `TODO.md`（可勾选任务清单）。
