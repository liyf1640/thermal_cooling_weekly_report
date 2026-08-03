#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""周报入库助手 / Weekly briefing ingest helper.

把一期"通过核验"的周报 Markdown 入库到私有 KB 仓库：放置文件、重新生成首页
索引、提交并推送。仓库保持私有，不改动 Pages 开关（ENABLE_PAGES）。

用法（每周一发布后运行一次）：
    python scripts/ingest_briefing.py <稿件.md> [--date YYYY-MM-DD]

常用可选项：
    --date YYYY-MM-DD   指定期号日期；缺省时从文件名或稿件内容自动推断
    --dry-run           只预览将发生的改动，不写文件、不做任何 git 操作
    --no-push           完成放置/索引/提交，但不 push（本地验证用）

动作顺序：git pull --ff-only → 复制到 docs/briefings/<YEAR>/<DATE>.md →
重新生成 docs/index.md 的"最新一期"与"全部周报"区块 → git add -A →
git commit -m "briefing: <DATE>" → git push origin main。

幂等：索引由 briefings 目录内容重新生成，重复运行同一日期不会产生重复行；
若无实际变更则跳过提交，不会空提交。
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
BRIEFINGS = DOCS / "briefings"
INDEX = DOCS / "index.md"

LATEST_START = "<!-- AUTO:LATEST:START -->"
LATEST_END = "<!-- AUTO:LATEST:END -->"
INDEX_START = "<!-- AUTO:INDEX:START -->"
INDEX_END = "<!-- AUTO:INDEX:END -->"

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
ISSUE_RE = re.compile(r"第\s*(\d+)\s*期")
TOPIC_RE = re.compile(r"^\*\*主题\*\*[：:]\s*(.+?)\s*$", re.M)


def die(msg):
    print(f"错误：{msg}", file=sys.stderr)
    sys.exit(1)


def git(*args, capture=False):
    """在仓库根目录运行 git；失败即报错退出。"""
    result = subprocess.run(
        ["git", *args], cwd=REPO,
        capture_output=capture, text=True, encoding="utf-8",
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        die(f"git {' '.join(args)} 失败：{detail}")
    return (result.stdout or "").strip() if capture else ""


def valid_date(s):
    m = DATE_RE.fullmatch(s)
    if not m:
        die(f"日期格式应为 YYYY-MM-DD，收到：{s}")
    return s


def infer_date(source: Path, arg_date):
    if arg_date:
        return valid_date(arg_date)
    m = DATE_RE.search(source.name)
    if m:
        return m.group(0)
    m = DATE_RE.search(source.read_text(encoding="utf-8"))
    if m:
        return m.group(0)
    die("无法推断日期，请用 --date YYYY-MM-DD 指定")


def parse_meta(text, date):
    """从稿件文本提取 期号 与 主题，用于索引展示。"""
    issue = ISSUE_RE.search(text)
    topic = TOPIC_RE.search(text)
    return (
        issue.group(1) if issue else None,
        topic.group(1).strip() if topic else "",
    )


def label(issue, date):
    return f"第 {issue} 期 · {date}" if issue else date


def entry_line(issue, date, topic):
    year = date[:4]
    link = f"briefings/{year}/{date}.md"
    text = f"[{label(issue, date)}]({link})"
    return f"- {text} — {topic}" if topic else f"- {text}"


def collect_briefings():
    """扫描 briefings/ 下所有 <YYYY-MM-DD>.md，返回按日期倒序的元数据列表。"""
    items = []
    for p in sorted(BRIEFINGS.rglob("*.md")):
        m = DATE_RE.fullmatch(p.stem)
        if not m:
            continue
        date = p.stem
        issue, topic = parse_meta(p.read_text(encoding="utf-8"), date)
        items.append({"date": date, "issue": issue, "topic": topic})
    items.sort(key=lambda x: x["date"], reverse=True)
    return items


def render_latest(items):
    if not items:
        return "_暂无周报_"
    it = items[0]
    year = it["date"][:4]
    link = f"briefings/{year}/{it['date']}.md"
    line = f"**[{label(it['issue'], it['date'])}]({link})**"
    return f"{line} — {it['topic']}" if it["topic"] else line


def render_index(items):
    if not items:
        return "_暂无周报_"
    by_year = {}
    for it in items:
        by_year.setdefault(it["date"][:4], []).append(it)
    blocks = []
    for year in sorted(by_year, reverse=True):
        lines = [f"### {year}", ""]
        lines += [entry_line(i["issue"], i["date"], i["topic"]) for i in by_year[year]]
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def replace_region(text, start, end, body):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        die(f"index.md 缺少标记 {start} ... {end}，无法更新")
    return pattern.sub(lambda _: f"{start}\n{body}\n{end}", text, count=1)


def build_index(items):
    text = INDEX.read_text(encoding="utf-8")
    text = replace_region(text, LATEST_START, LATEST_END, render_latest(items))
    text = replace_region(text, INDEX_START, INDEX_END, render_index(items))
    return text


def main():
    ap = argparse.ArgumentParser(description="周报入库助手")
    ap.add_argument("source", help="通过核验的周报 .md 路径")
    ap.add_argument("--date", help="期号日期 YYYY-MM-DD（缺省自动推断）")
    ap.add_argument("--dry-run", action="store_true", help="只预览，不写文件、不做 git 操作")
    ap.add_argument("--no-push", action="store_true", help="提交但不 push（本地验证用）")
    args = ap.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.is_file():
        die(f"找不到稿件：{source}")

    date = infer_date(source, args.date)
    year = date[:4]
    dest = BRIEFINGS / year / f"{date}.md"

    content = source.read_text(encoding="utf-8")
    issue, topic = parse_meta(content, date)
    print(f"期号：{label(issue, date)}")
    if topic:
        print(f"主题：{topic}")
    print(f"目标：{dest.relative_to(REPO)}")

    existed = dest.exists()
    if existed and dest.resolve() == source:
        print("提示：稿件已在目标位置，仅重建索引。")

    if args.dry_run:
        # 预览：用内存中的内容模拟入库后的索引
        preview = [i for i in collect_briefings() if i["date"] != date]
        preview.append({"date": date, "issue": issue, "topic": topic})
        preview.sort(key=lambda x: x["date"], reverse=True)
        print("\n--- [dry-run] 首页索引预览 ---")
        print("最新一期：", render_latest(preview))
        print(render_index(preview))
        print("\n[dry-run] 未写入任何文件，未做 git 操作。")
        return

    # 1) 先同步远端，避免落后导致 push 冲突
    if not args.no_push:
        git("pull", "--ff-only", "origin", "main")

    # 2) 放置稿件（逐字复制，不改动内容）
    dest.parent.mkdir(parents=True, exist_ok=True)
    action = "更新" if existed else "新增"
    if dest.resolve() != source:
        shutil.copyfile(source, dest)

    # 3) 重新生成首页索引
    INDEX.write_text(build_index(collect_briefings()), encoding="utf-8")

    # 4) 提交（只暂存本次已知的两个路径，避免把工作区游离文件裹入 briefing 提交）
    git("add", "--", str(dest.relative_to(REPO)), str(INDEX.relative_to(REPO)))
    staged = git("diff", "--cached", "--name-only", capture=True)
    if not staged:
        print("无变更（该期内容与仓库一致），跳过提交。")
        return
    print(f"{action}并提交：\n  " + "\n  ".join(staged.splitlines()))
    git("commit", "-m", f"briefing: {date}")

    # 5) 推送
    if args.no_push:
        print("已提交（--no-push，未推送）。确认无误后运行： git push origin main")
        return
    git("push", "origin", "main")
    print(f"完成：{label(issue, date)} 已入库并推送到 main。仓库保持私有，未触发 Pages。")


if __name__ == "__main__":
    main()
