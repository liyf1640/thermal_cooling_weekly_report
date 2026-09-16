---
name: weekly-briefing
description: 出「散热方案周报」下一期——五路定向检索 → 原文逐位核验 → 按既有模板成稿 → 更新跨期清单 → 开 PR 等人工核后合并。用户说「出周报 / 下一期 / 跑一下周报 / weekly briefing」，或每周 routine 触发时使用。
---

# 散热方案周报 · 每周出稿

本仓库是 MkDocs Material 知识库（https://liyf1640.github.io/thermal_cooling_weekly_report/）。
你的任务：产出下一期周报草稿，**开 PR 交人工核验**，绝不直接推 `main`。

覆盖面：**英文新闻 + 学术/会议论文 + 工业动态**，主题为**冷板设计仿真 · 制造工艺 · 前沿散热技术**。

开工前先读：

- `.claude/skills/weekly-briefing/rules.md` —— 核验与写作铁律（**每次必读，不得跳过**）
- `.claude/skills/weekly-briefing/TEMPLATE.md` —— 成稿骨架
- `drafts/reported-index.md` —— 跨期去重索引（第 1 步生成）

---

## 第 0 步 · 定位与定期号

```bash
cd <repo>            # 含 mkdocs.yml 的仓库根
git pull --ff-only origin main
python scripts/reported_index.py          # 生成 drafts/reported-index.md
```

读 `drafts/reported-index.md` 抬头，拿到：

- **本期期号** = 上期 + 1
- **时间窗** = 上期日期之后至今天（若距上期超过 2 周，时间窗照实写覆盖区间，不假装是一周）
- **期号日期** = 今天（`date +%F`）；用户显式指定日期时以用户为准

把 reported-index 的「已报论文卡 / arXiv id / DOI / URL / 公司 / 学者」整份读进来——**后面每一条候选都要对它查重**。

## 第 1 步 · 五路并行检索

用 `Agent` 工具一次发起 5 个 `thermal-scout` 子代理（**同一条消息里并发**），每个负责一个角度。
给每个 scout 的 prompt 里必须带上：本期时间窗、`drafts/reported-index.md` 的去重清单摘要、该角度的检索要点。

| # | 角度 | 检索要点 |
|---|---|---|
| A | **冷板仿真与设计** | 拓扑优化 / 生成式设计（扩散、GAN、VAE）/ 歧管微通道 MMC / 射流冲击 / 两相沸腾冷板 / ROM 代理模型 / 共轭传热 CFD。arXiv `physics.flu-dyn`、`cs.CE`、Crossref、IJHMT / ATE / ICHMT / Energy Conversion & Management |
| B | **冷板制造工艺** | **钎焊 brazing / skived 翅片 / 搅拌摩擦焊 FSW —— 长期缺口，每期专项硬检索**；外加 ECAM / LPBF / 扩散焊 / 微铣削。会议集 **ITherm / ECTC / SEMI-THERM / InterPACK** 也要扫 |
| C | **仿真方法** | ML-for-CFD、神经算子（FNO/DeepONet）、可微分求解器、湍流闭合学习、PINN、降阶模型。判据：对冷板内对流换热高保真快速建模**有方法学价值** |
| D | **中文学术** | CNKI / 万方「网络首发」、《电子机械工程》《空间电子技术》《化工学报》《工程热物理学报》等。检不到就如实写「本期未检出」 |
| E | **产业动态** | 近 2 周英文一手新闻：并购 / 新品 / 产能扩张 / 合作 / 部署。NVIDIA、CoolIT-Ecolab、Vertiv、nVent、Fabric8Labs-TDK、Boyd、ACT、LiquidStack、JetCool、Accelsius、Chilldyne 等。分析师/市场数字**单独收集**，不混入事实条 |

每个 scout 回传**候选清单**，不回传成稿；每条候选必须带原始 URL。

## 第 2 步 · 逐位核验

把 scout 回传的候选（去掉命中 reported-index 的）交给 `thermal-verifier` 子代理核。
**不信检索索引摘要**：一律用 `python scripts/fetch_source.py <arXiv id | DOI | URL>`
取原文紧凑元数据，逐位核作者、单位、数字、日期。该脚本把 arXiv abs 页从 ~43k 字符压到 ~2k，
是本流程最大的省 token 杠杆——**不要直接 curl 整页**。

- 核得实：进正文
- 核不到单位/职称：写「待确认」，**不臆测、不以人名猜单位**
- 核不实：丢弃；若此前期次报过错，在「方法与局限」里更正
- 厂商/分析师口径：标注来源口径，且**只能进第五节「前瞻 / 分析师数字」**

## 第 3 步 · 成稿

照 `TEMPLATE.md` 填 `drafts/<YYYY-MM-DD>.md`。要点：

- 论文卡**五段式**：研究团队 / 技术介绍（含性能数字）/ 技术优势（先进性）/ 技术局限 / 来源
- TL;DR 一段话串起本期全部实质新增，带 ①②③ 序号
- **缺口照实写缺**（例如制造工艺连续第 N 期未检出同行评审新文），**绝不凑数**
- 正文中文，专业术语保留英文原文 + 中文
- 末尾署名：`*—— Sage · 散热方案周报第 N 期（待核验稿）*`

## 第 4 步 · 更新跨期清单

本期出现的新公司 / 并购 / 产品 → `docs/notes/companies.md`（含「制造工艺覆盖 / 缺口」表）；
新学者 → `docs/notes/sg-scholars.md`；新缩写 → `docs/glossary.md`。
每行都要标「已覆盖期 + 出处」。缺口三项（钎焊 / skived / FSW）一旦检出擅长企业或新文，填进「擅长企业」列。

## 第 5 步 · 入库并开 PR

```bash
git checkout -b briefing/<YYYY-MM-DD>
python scripts/ingest_briefing.py drafts/<YYYY-MM-DD>.md --no-push
git add docs/notes docs/glossary.md          # 清单改动（若有）
git commit -m "notes: 第 N 期跨期清单更新" --allow-empty-message || true
git push -u origin briefing/<YYYY-MM-DD>
gh pr create --base main --title "briefing: 第 N 期 · <YYYY-MM-DD>" --body-file <PR 正文>
```

`ingest_briefing.py --no-push` 会复制稿件到 `docs/briefings/<年>/<日期>.md`、重建首页 AUTO 索引与
`mkdocs.yml` 侧栏 nav，并本地提交 `briefing: <日期>`。**务必带 `--no-push`**——不带会直接推 `main`。

推分支前本地验一次构建：`mkdocs build --strict`（失败就修到过）。

PR 正文写：本期期号/日期、TL;DR、**经核条目数与逐条来源**、**本期缺口与未核项**、需要人工重点复核的地方。

## 第 6 步 · 回报

输出：PR 链接 + 本期自评（几条经核、哪几个角度空窗、哪些标了「待确认」需人工定夺）。
PR 合并进 `main` 后 GitHub Actions 自动构建并部署 Pages，无需额外操作。

---

## 空窗周怎么办

某角度检不出东西是**正常且可接受**的结果。照实写「本期未检出窗口内新文」，在「开放问题 / 下期」里挂账，
下期继续专项。**宁可薄一期，也不拿旧文、营销稿、专利、分析师预测凑数**——这是本刊的立身之本。
