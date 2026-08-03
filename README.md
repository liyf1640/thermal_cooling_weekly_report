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

## 目录结构

```
docs/
  index.md                     首页（最新一期 + 索引）
  briefings/2026/2026-08-01.md 周报第 1 期
  notes/                       主题笔记（预留）
  decisions/                   决策记录（预留）
  glossary.md                  术语表
.github/workflows/deploy.yml   构建 + Pages 部署（可一键切换）
mkdocs.yml                     站点配置
```

## 发布（Phase-2，一键切换）

当前为私有阶段，站点**不发布**。需要发布时：

1. 仓库 **Settings → Pages → Source** 选择 **GitHub Actions**。
2. 新增仓库变量 **Settings → Variables → Actions → `ENABLE_PAGES = true`**。
3. 取消 `mkdocs.yml` 中 `site_url` 的注释并填入 Pages 地址。

之后推送到 `main` 即自动构建并发布，无需改动 workflow 文件。私有阶段 `deploy` 任务会被跳过，无副作用。
