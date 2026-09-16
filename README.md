# 散热方案周报 · Web 知识库

数据中心 / 电子散热方向每周简报的 Web 知识库，基于 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建。

## 本地预览

```bash
pip install -r requirements.txt
mkdocs serve        # 打开 http://127.0.0.1:8000
```

构建静态站点：

```bash
mkdocs build --strict
```

## 每周入库（每周一发布后运行一次）

每期简报经 Rey 周日核验、周一发布后，用一键助手把通过的 `.md` 入库：

```bash
python scripts/ingest_briefing.py <通过的稿件.md> --date YYYY-MM-DD
```

- `--date` 缺省时会从文件名或稿件标题自动推断，一般可省略。
- 助手会自动：`git pull` → 复制到 `docs/briefings/<年>/<日期>.md` → 更新首页
  "最新一期"/索引 + `mkdocs.yml` 侧栏 nav 的"周报"子树 → `commit "briefing: <日期>"` → `push` 到 `main`。
- **幂等**：索引与 nav 均由 `docs/briefings/` 内容重新生成（`AUTO` 标记区块），重复运行同一日期不会重复；无变更时跳过提交。
- 仓库已公开，`push` 到 `main` 会触发 Actions 自动构建并部署 Pages。

先验证不推送：

```bash
python scripts/ingest_briefing.py <稿件.md> --dry-run   # 只预览，不写文件
python scripts/ingest_briefing.py <稿件.md> --no-push   # 本地提交但不推送
```

> 前置：运行的机器需已 `git clone` 本仓库，且具备 owner（liyf1640）推送权限。

## 每周自动出稿（Agent）

每期周报由 `.claude/` 下的 agent 自动产出草稿并开 PR，人工核验后合并发布。

手动触发（在本仓库根目录）：

```bash
claude            # 进入会话后
/weekly-briefing  # 出下一期草稿并开 PR
```

云端每周定时由 Claude Code scheduled routine 触发同一技能，无需本机开机。

流程：

1. `scripts/reported_index.py` 生成 `drafts/reported-index.md` 跨期去重索引（已报标题 / arXiv id / DOI / URL / 公司 / 学者）
2. 并发 5 个 `thermal-scout` 子代理检索：冷板仿真与设计 · 制造工艺 · 仿真方法 · 中文学术 · 产业动态
3. `thermal-verifier` 子代理逐条用 `fetch_source.py` 取原文核作者 / 单位 / 数字 / 日期，判「通过 / 待确认 / 否决」
4. 按 `TEMPLATE.md` 成稿到 `drafts/<日期>.md`，同步更新 `notes/companies.md`、`notes/sg-scholars.md`、`glossary.md`
5. `ingest_briefing.py --no-push` 入库 → `mkdocs build --strict` 验证 → 推 `briefing/<日期>` 分支 → `gh pr create`

相关文件：

```
.claude/skills/weekly-briefing/SKILL.md      每周出稿运行手册（6 步）
.claude/skills/weekly-briefing/rules.md      核验与写作铁律（23 条，每次必读）
.claude/skills/weekly-briefing/TEMPLATE.md   成稿骨架 + 自检清单
.claude/agents/thermal-scout.md              单角度检索侦察兵（并发 5 个）
.claude/agents/thermal-verifier.md           对抗式核验员（curl 原文逐位核）
scripts/reported_index.py                    跨期去重索引生成器
scripts/fetch_source.py                      紧凑取源（arXiv/Crossref/URL），核验省 token 用
```

> **跳期**：定时跑时若上期 PR 仍未合并，或距上期不足 5 天（例如补发期之后紧跟的那次定时），agent 直接结束不出稿。
>
> agent **绝不直接推 `main`**：一律走 `briefing/<日期>` 分支 + PR，合并后 Actions 自动部署 Pages。

## 目录结构

```
docs/
  index.md                     首页（最新一期 + 索引，AUTO 区块由脚本生成）
  briefings/2026/2026-08-01.md 周报第 1 期
  notes/                       主题笔记（预留）
  decisions/                   决策记录（预留）
  glossary.md                  术语表
scripts/ingest_briefing.py     每周入库助手
.github/workflows/deploy.yml   构建 + Pages 部署（可一键切换）
mkdocs.yml                     站点配置
```

## 发布（Phase-2，一键切换）

当前为私有阶段，站点**不发布**。需要发布时：

1. 仓库 **Settings → Pages → Source** 选择 **GitHub Actions**。
2. 新增仓库变量 **Settings → Variables → Actions → `ENABLE_PAGES = true`**。
3. 取消 `mkdocs.yml` 中 `site_url` 的注释并填入 Pages 地址。

之后推送到 `main` 即自动构建并发布，无需改动 workflow 文件。私有阶段 `deploy` 任务会被跳过，无副作用。
