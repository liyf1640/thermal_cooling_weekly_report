#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the cross-issue "reported index" used for de-duplication.

Scans every archived briefing under docs/briefings/ and emits a compact digest
of what has already been reported: paper-card titles, arXiv ids, DOIs, every
cited URL, and the company / scholar rows tracked in docs/notes/.

The weekly agent reads this file BEFORE drafting, so a candidate that already
appeared in an earlier issue is dropped instead of being re-reported.

Usage:
    python scripts/reported_index.py                 # write drafts/reported-index.md
    python scripts/reported_index.py --stdout        # print instead of writing
    python scripts/reported_index.py -o <path>       # custom output path
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BRIEFINGS = REPO / "docs" / "briefings"
NOTES = REPO / "docs" / "notes"
DEFAULT_OUT = REPO / "drafts" / "reported-index.md"

DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
ISSUE_RE = re.compile(r"第\s*(\d+)\s*期")
CARD_RE = re.compile(r"^###\s+(?:\S+\s+)?论文(?:卡|\s*\d+)\s*[·・]\s*(.+?)\s*$", re.M)
URL_RE = re.compile(r"https?://[^\s\)\]，、。；」）]+")
ARXIV_RE = re.compile(r"arXiv[:\s]*(\d{4}\.\d{4,5})", re.I)
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
ROW_RE = re.compile(r"^\|\s*\*{0,2}([^|*]+?)\*{0,2}\s*\|", re.M)


def issues():
    """Yield {date, issue, text} for every archived briefing, newest first."""
    found = []
    for path in sorted(BRIEFINGS.rglob("*.md")):
        if not DATE_RE.fullmatch(path.stem):
            continue
        text = path.read_text(encoding="utf-8")
        m = ISSUE_RE.search(text)
        found.append({
            "date": path.stem,
            "issue": m.group(1) if m else "?",
            "text": text,
            "path": path.relative_to(REPO).as_posix(),
        })
    found.sort(key=lambda x: x["date"], reverse=True)
    return found


def table_keys(path):
    """First column of every markdown table row in a notes page (skips headers)."""
    if not path.is_file():
        return []
    keys, seen = [], set()
    for raw in ROW_RE.findall(path.read_text(encoding="utf-8")):
        key = raw.strip()
        if not key or key.startswith("-") or key in {"公司", "姓名", "工艺", "缩写"}:
            continue
        if key not in seen:
            seen.add(key)
            keys.append(key)
    return keys


def render(items):
    out = ["# reported-index（跨期去重索引 · 自动生成，勿手改）", ""]
    if not items:
        out += ["_暂无已归档周报_", ""]
        return "\n".join(out)

    latest = items[0]
    out += [
        f"已归档 **{len(items)}** 期，最新为 **第 {latest['issue']} 期 · {latest['date']}**。",
        f"下一期应为 **第 {int(latest['issue']) + 1 if latest['issue'].isdigit() else '?'} 期**，"
        f"时间窗覆盖 **{latest['date']} 之后**的新增。",
        "",
        "> 用法：起草前先读本页。命中以下任一 **标题 / arXiv id / DOI / URL** 的候选 = 已报过，"
        "本期不再重复报道（仅在有实质进展时以「进展更新」一句话提及）。",
        "",
        "---",
        "",
        "## 一、已报论文卡（按期倒序）",
        "",
    ]
    for it in items:
        cards = CARD_RE.findall(it["text"])
        out.append(f"### 第 {it['issue']} 期 · {it['date']}")
        out.append("")
        out += [f"- {c}" for c in cards] or ["- _该期无论文卡_"]
        out.append("")

    ids = sorted({a for it in items for a in ARXIV_RE.findall(it["text"])})
    dois = sorted({d.rstrip(".,)") for it in items for d in DOI_RE.findall(it["text"])})
    urls = sorted({u.rstrip(".,)") for it in items for u in URL_RE.findall(it["text"])})

    out += ["---", "", "## 二、已引用 arXiv id", ""]
    out += [f"- arXiv:{a}" for a in ids] or ["- _无_"]
    out += ["", "## 三、已引用 DOI", ""]
    out += [f"- {d}" for d in dois] or ["- _无_"]
    out += ["", "## 四、已引用 URL（全部）", ""]
    out += [f"- {u}" for u in urls] or ["- _无_"]

    out += ["", "---", "", "## 五、跨期清单已收录条目", "",
            "**公司 / 工艺**（docs/notes/companies.md）：", ""]
    out += [f"- {k}" for k in table_keys(NOTES / "companies.md")] or ["- _无_"]
    out += ["", "**学者**（docs/notes/sg-scholars.md）：", ""]
    out += [f"- {k}" for k in table_keys(NOTES / "sg-scholars.md")] or ["- _无_"]
    out += ["", "**术语表已有缩写**（docs/glossary.md）：", ""]
    out += [f"- {k}" for k in table_keys(REPO / "docs" / "glossary.md")] or ["- _无_"]
    out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Build the cross-issue de-dup index")
    ap.add_argument("-o", "--out", default=str(DEFAULT_OUT), help="output path")
    ap.add_argument("--stdout", action="store_true", help="print instead of writing")
    args = ap.parse_args()

    body = render(issues())
    if args.stdout:
        sys.stdout.write(body)
        return
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    print(f"Wrote {out.relative_to(REPO) if out.is_relative_to(REPO) else out}")


if __name__ == "__main__":
    main()
