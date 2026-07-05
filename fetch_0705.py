#!/usr/bin/env python3
"""获取 InkWell 过去24小时的新增文章 (0704 08:00 → 0705 08:00)"""

import json
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path

TZ = timezone(timedelta(hours=8))
NOW = datetime(2026, 7, 5, 8, 0, tzinfo=TZ)
CUTOFF = NOW - timedelta(hours=24)
API = "https://inkwell.coze.com/api/articles?limit=50&page={}"


def parse_pub(s: str) -> datetime:
    return datetime.fromisoformat(s)


def strip_html(html: str, max_len: int = 400) -> str:
    if not html:
        return ""
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = unescape(txt)
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt[:max_len]


def fetch_page(page: int):
    req = urllib.request.Request(
        API.format(page),
        headers={"User-Agent": "Mozilla/5.0 InkWell-Archive/1V"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    collected = []
    seen_ids = set()
    for page in range(1, 8):
        try:
            data = fetch_page(page)
        except Exception as e:
            print(f"page {page} failed: {e}")
            break
        arts = data.get("articles", [])
        if not arts:
            break
        stop = False
        for a in arts:
            pub = parse_pub(a["pubDate"])
            if pub < CUTOFF:
                stop = True
                continue
            if pub > NOW:
                continue
            if a["id"] in seen_ids:
                continue
            seen_ids.add(a["id"])
            collected.append(a)
        print(f"page {page}: got {len(arts)} articles, kept {len(collected)} total")
        if stop and parse_pub(arts[-1]["pubDate"]) < CUTOFF:
            break

    by_cat = {}
    for a in collected:
        cat = a.get("category") or "Uncategorized"
        by_cat.setdefault(cat, []).append(a)

    for k in by_cat:
        by_cat[k].sort(key=lambda x: x["pubDate"], reverse=True)

    print(f"\n=== 过去 24h ({CUTOFF.strftime('%Y-%m-%d %H:%M')} → {NOW.strftime('%Y-%m-%d %H:%M')}) ===")
    print(f"共 {len(collected)} 篇，{len(by_cat)} 个分类")
    for c, l in sorted(by_cat.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(l)}")

    out = {
        "total": len(collected),
        "cutoff": CUTOFF.isoformat(),
        "now": NOW.isoformat(),
        "by_category": {
            c: [
                {
                    "id": a["id"],
                    "title": a["title"],
                    "link": a["link"],
                    "url": f"https://inkwell.coze.com/article/{a['id']}",
                    "pubDate": a["pubDate"],
                    "source": a.get("source", ""),
                    "author": a.get("author", ""),
                    "snippet": (a.get("contentSnippet") or "")[:800],
                    "content_text": strip_html(a.get("content", ""), 1200),
                }
                for a in l
            ]
            for c, l in by_cat.items()
        },
    }
    out_path = Path(__file__).parent / "0705_articles.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n写入: {out_path}")


if __name__ == "__main__":
    main()
