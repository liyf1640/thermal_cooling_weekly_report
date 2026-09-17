#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch a source's metadata in compact form, for verification.

Raw arXiv/journal pages are ~10k tokens of HTML each; dumping them into an
agent's context is the single biggest token cost of a briefing run. This prints
only the fields the briefing actually needs -- title, authors, affiliations,
dates, abstract -- typically under 400 tokens.

Usage:
    python scripts/fetch_source.py 2608.22787              # arXiv id
    python scripts/fetch_source.py 10.1016/j.ijheatmasstransfer.2026.1234   # DOI
    python scripts/fetch_source.py https://example.com/news  # any URL -> text
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request

# Console on Windows may be cp1252; source text is often non-ASCII.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

UA = {"User-Agent": "thermal-weekly-briefing/1.0 (+https://github.com/liyf1640)"}
ARXIV_RE = re.compile(r"^(?:arxiv:)?(\d{4}\.\d{4,5})(v\d+)?$", re.I)
DOI_RE = re.compile(r"^(?:doi:|https?://(?:dx\.)?doi\.org/)?(10\.\d{4,9}/\S+)$", re.I)


RETRY_CODES = {406, 429, 500, 502, 503, 504}  # arXiv answers 406/503 when rate-limited


def get(url, timeout=30, attempts=4):
    """GET with backoff; arXiv asks for >=3 s between API calls."""
    for i in range(attempts):
        req = urllib.request.Request(url, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code not in RETRY_CODES or i == attempts - 1:
                raise
            wait = 3 * 2 ** i
            print(f"(HTTP {e.code}, retrying in {wait}s)", file=sys.stderr)
            time.sleep(wait)


def show(label, value):
    if value:
        print(f"{label}: {value}")


def from_arxiv(arxiv_id):
    """arXiv Atom API -- compact XML, includes per-author affiliation when set."""
    body = get(f"https://export.arxiv.org/api/query?id_list={arxiv_id}")
    entry = re.search(r"<entry>(.*?)</entry>", body, re.S)
    if not entry:
        sys.exit(f"arXiv: no entry for {arxiv_id}")
    e = entry.group(1)

    def tag(name):
        m = re.search(rf"<{name}>(.*?)</{name}>", e, re.S)
        return html.unescape(" ".join(m.group(1).split())) if m else ""

    authors = []
    for block in re.findall(r"<author>(.*?)</author>", e, re.S):
        name = re.search(r"<name>(.*?)</name>", block, re.S)
        aff = re.search(r"<arxiv:affiliation[^>]*>(.*?)</arxiv:affiliation>", block, re.S)
        if name:
            n = html.unescape(" ".join(name.group(1).split()))
            authors.append(f"{n} ({html.unescape(aff.group(1).strip())})" if aff else n)

    print(f"SOURCE: arXiv:{arxiv_id}")
    show("URL", f"https://arxiv.org/abs/{arxiv_id}")
    show("TITLE", tag("title"))
    show("AUTHORS", "; ".join(authors))
    show("PUBLISHED", tag("published"))
    show("UPDATED", tag("updated"))
    show("DOI", tag("arxiv:doi"))
    show("JOURNAL_REF", tag("arxiv:journal_ref"))
    show("COMMENT", tag("arxiv:comment"))
    print(f"ABSTRACT: {tag('summary')}")
    if not any("(" in a for a in authors):
        print("NOTE: no affiliation in arXiv metadata -- read the PDF or mark it unconfirmed.")


def from_doi(doi):
    """Crossref -- authoritative for peer-reviewed work, often carries affiliations."""
    data = json.loads(get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"))["message"]
    authors = []
    for a in data.get("author", []):
        name = " ".join(filter(None, [a.get("given"), a.get("family")])) or a.get("name", "")
        affs = "; ".join(x.get("name", "") for x in a.get("affiliation", []) if x.get("name"))
        authors.append(f"{name} ({affs})" if affs else name)

    def date(key):
        parts = data.get(key, {}).get("date-parts", [[]])[0]
        return "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts))

    print(f"SOURCE: DOI {doi}")
    show("URL", data.get("URL"))
    show("TITLE", " ".join(data.get("title", [""])))
    show("AUTHORS", "; ".join(authors))
    show("CONTAINER", " ".join(data.get("container-title", [""])))
    show("TYPE", data.get("type"))
    show("PUBLISHED", date("published") or date("published-online") or date("published-print"))
    show("PUBLISHER", data.get("publisher"))
    abstract = data.get("abstract", "")
    if abstract:
        print(f"ABSTRACT: {html.unescape(re.sub(r'<[^>]+>', ' ', abstract)).strip()}")
    if not any("(" in a for a in authors):
        print("NOTE: Crossref carries no affiliation -- read the paper or mark it unconfirmed.")


def from_url(url, limit):
    """Strip a page down to readable text -- for news / vendor releases."""
    body = get(url)
    body = re.sub(r"(?is)<(script|style|nav|footer|header|svg)[^>]*>.*?</\1>", " ", body)
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", body)
    date = re.search(r'(?i)<meta[^>]+(?:published_time|pubdate|article:published)[^>]+'
                     r'content="([^"]+)"', body)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text).strip()

    print(f"SOURCE: {url}")
    show("TITLE", html.unescape(title.group(1).strip()) if title else "")
    show("PUBLISHED_META", date.group(1) if date else "")
    print(f"TEXT ({min(len(text), limit)} of {len(text)} chars):")
    print(text[:limit])
    if len(text) > limit:
        print(f"... [truncated; rerun with --limit {limit * 2} if the fact you need is missing]")


def main():
    ap = argparse.ArgumentParser(description="Fetch compact source metadata for verification")
    ap.add_argument("target", help="arXiv id, DOI, or URL")
    ap.add_argument("--limit", type=int, default=6000, help="max chars of page text (URL mode)")
    args = ap.parse_args()

    target = args.target.strip()
    try:
        m = ARXIV_RE.match(target)
        if m:
            return from_arxiv(m.group(1))
        m = DOI_RE.match(target)
        if m:
            return from_doi(m.group(1))
        if target.startswith(("http://", "https://")):
            return from_url(target, args.limit)
        sys.exit(f"Unrecognized target: {target} (expected arXiv id, DOI, or URL)")
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} fetching {target}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error fetching {target}: {e.reason}")


if __name__ == "__main__":
    import urllib.parse  # noqa: E402  (used only in from_doi)
    main()
