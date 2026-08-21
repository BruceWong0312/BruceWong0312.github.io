# ✏️ 如何修改网页内容

网页上的所有文字都来自本目录的 YAML 文件，**改这里 → 重新生成 → 提交**，三步完成。

| 文件 | 对应网页板块 | 常见修改 |
|---|---|---|
| `profile.yml` | 顶部姓名/单位/照片/简介/研究兴趣/链接 | 换简介、加 Google Scholar 链接 |
| `education.yml` | 教育经历 | 加导师、改年份 |
| `publications.yml` | 论文（已发表 / 工作论文 / 在研） | **新增论文：复制一整条，改字段** |
| `projects.yml` | 项目与学术服务 | 新增审稿、课题 |
| `talks.yml` | 学术会议 / 论坛 | 新增汇报 |
| `skills.yml` | 专业能力 + 学术培训 | 加工具、加暑期学校 |
| `awards.yml` | 荣誉奖项 | 加奖项 |

## 三步更新

```bash
# 1. 用任何文本编辑器改 content/*.yml（VS Code / 记事本都行）
# 2. 重新生成网页并本地预览
python build.py            # 生成 docs/index.html
python -m http.server -d docs 8000   # 浏览器打开 http://localhost:8000
# 3. 提交并推送（留痕）
git add -A && git commit -m "content: 新增 2025 年 xxx 论文" && git push
```

推送后 GitHub Pages 约 1 分钟内自动更新。

## YAML 三条规则（避免 90% 的报错）

1. **缩进用两个空格**，不要用 Tab。
2. 值里含英文冒号 `:`、井号 `#` 或以 `*`/`&` 开头时，**整段用英文双引号包起来**。
3. 列表每项以 `- ` 开头；想删掉某项就整条删掉，想隐藏某字段就留空 `""`。

检查语法：`python -c "import yaml,glob;[yaml.safe_load(open(f,encoding='utf-8')) for f in glob.glob('content/*.yml')];print('OK')"`

## 字段里的小技巧

- 作者串里 `**Huang, Y.**` 会在网页上加粗显示自己。
- `links: [{label: PDF, url: assets/files/xxx.pdf}]` 会生成 `[PDF]` 小链接；PDF 文件放到 `assets/files/`。
- 标了 `# TODO` 的字段是待补充项，补完把注释删掉即可。
