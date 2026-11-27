---
name: briefing-ppt
description: 把「散热方案周报」若干期的亮点做成汇报用 .pptx——研究侧一篇一页（标题栏 + 7/3 圆角红虚线框：左技术介绍+原文图，右研究团队/技术优势/当前状态/业务建议/信息来源），产业侧合成一页带来源链接。先查 OA 下全文、按全文细化并补图，出入写进演讲者备注。用户说「做成 PPT / 出汇报 / 周报要点 PPT」时使用。
---

# 周报要点 PPT

把已发布周报（`docs/briefings/`）里有价值的条目做成固定版式的汇报 PPT。版式、配色、流程都已和维护者定死，**照做，不重新设计**。

## 0. 工作目录与依赖

- 工作目录放在会话 scratchpad（下称 `$WD`），不要放进仓库。
- `cd $WD && npm install pptxgenjs@4`（本机未预装；`gen.js` 从**当前工作目录**的 node_modules 加载）。
- Python 需 `python-pptx`、`Pillow`、`pymupdf`；字宽估算用 `C:/Windows/Fonts/msyh.ttc` / `msyhbd.ttc`。
- 本技能脚本目录记为 `$S = .claude/skills/briefing-ppt/scripts`（用绝对路径调用）。

## 1. 先查开放获取、下全文（每次第一步）

对每篇研究论文：

1. `curl -s https://api.openalex.org/works/doi:<DOI>`，看 `open_access.is_oa`、`best_oa_location.pdf_url`，Crossref `license` 交叉核对。**不用 Unpaywall**（要邮箱）。
2. 是 OA 就下载到仓库 `pdfs/<年份>/`（文件名用论文标题），核对文件头是 `%PDF`、标题对得上。机构库作者版（如 Ghent biblio）也算。
3. 下载不了（出版商拦脚本，如 MDPI 返回 Access Denied；或闭源 IEEE）→ 删掉错误文件，**列链接给用户手动下载**，不绕拦截。
4. 有全文：PyMuPDF 抽文本通读，300 dpi 裁关键图（PIL trim 白边）存 `$WD/paperN/figX.png`，记下像素宽高填 `px`。许可允许（CC BY、作者版等）才放图；IEEE 版权的在信息来源框注「版权归 IEEE，仅供内部参考」。
5. 没全文：维持摘要层面，左侧用图片预留位（不给 `images` 即可）。

## 2. 写 content.json

从 `templates/content.template.json` 起步；完整实例见 `templates/example-issue13-14.json`（第 13–14 期，图片路径指向当时的 scratchpad，仅作写法参考）。

**文本标记**（`gen.js` 解析）：

| 写法 | 效果 |
|---|---|
| `- ` 开头 | 一个项目符号段落（红色符号）。**一个要点 = 一段 = 一个符号**，同一句不拆行 |
| 段首 `**问题**：` | 引导词红色粗体（问题：/方法：/工况：…） |
| 句中 `**关键词**` | 高饱和蓝色粗体 `0055E6` |
| `##数字##` | 同上（蓝色粗体），用于数字 |
| `[文字](url)` | 蓝色可点击链接（产业侧每条必带） |

- 标记**不要嵌套**（`**降 ##3 倍##**` 会坏）；中文与标记之间的空格会自动去掉，数字前的空格保留。
- 研究页字段：`title` `intro[]` `images[]`（`path` 相对 content.json、`px`、`caption`）`team` `advantage` `status` `suggestion` `source` `notes`；可调 `introH`（默认 2.55in）`introSize` `introSpace` `rightWeights`（五框高度权重）。
- 产业页：`"type": "industry"`，`items`（≤4 个，2×2）每条写**完整句子**并附链接；右侧 `suggestion` / `source`。

**内容口径**：数字照周报原文 / 全文，厂商数字标「厂商宣称」；技术介绍精简、直击重点。全文与已发布周报的出入、补齐的缺口写进 `notes`，以「【全文补充】」开头——**不进下一期周报、不回改前期**。作者单位、通讯作者等若据全文补全，可提议同步 `docs/notes/` 下的清单（须用户同意再改）。

## 3. 生成 → 后处理 → 检查

```bash
cd $WD
node $S/gen.js content.json deck.pptx
python $S/postprocess.py deck.pptx deck_clean.pptx      # 项目符号染红 + 去 ZIP 目录条目
PYTHONIOENCODING=utf-8 python $S/fitcheck.py deck_clean.pptx   # 按雅黑字宽估算溢出
python <pptx 技能>/scripts/office/validate.py deck_clean.pptx
cp deck_clean.pptx "C:/Users/lyf_7683/Desktop/liyf/<文件名>.pptx"
```

- `fitcheck` 偏保守约 15–25%：报「溢出」但超出 ≤ ~15% 的可接受（维护者已认可）；明显超出的删字或调 `rightWeights` / `introH`。
- 本机没有 LibreOffice / pdftoppm，PowerPoint COM 导出会被拦 → **视觉 QA 交给用户预审**，交付时说明。
- Windows 下 Python 打印中文要设 `PYTHONIOENCODING=utf-8`，且先写文件再打印，避免编码报错丢写入。

## 版式规则（已定，勿改）

- 画布 16:9 宽屏 13.333 × 7.5 in；字体 **Microsoft YaHei**；黑色为主；正文约 11pt（技术介绍 11–12，右框 10.5，信息来源 9），标题 22pt。
- **红色 `C00000` 只给**：题目、小标题 / 框标签、项目符号、段首引导词。其余加粗一律蓝色。
- 所有框为**小圆角红色虚线框**；标题栏右上角**不放**期号 / 日期标签。
- 图注只写图的内容，**不写「原文 Fig. XX」**，出处放信息来源框。
