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
