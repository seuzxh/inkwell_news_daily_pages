#!/usr/bin/env python3
"""生成 0702 完整列表 + 精选简报"""

import json
from pathlib import Path

BASE = Path(__file__).parent
DATA = json.load(open(BASE / "0702_articles.json", encoding="utf-8"))

DATE = "2026-07-02"
YMD = "20260702"

# ---------- 完整列表 ----------
lines = []
lines.append("# 🗞️ Inkwell 24小时完整文章列表")
lines.append(f"**日期**: {DATE}  |  **来源**: inkwell.coze.site  |  **总数**: {DATA['total']} 篇 / {len(DATA['by_category'])} 分类")
lines.append("")
lines.append("---")
lines.append("")

# 按数量降序排列分类
cats_sorted = sorted(DATA["by_category"].items(), key=lambda x: -len(x[1]))
for cat, arts in cats_sorted:
    lines.append(f"## {cat} ({len(arts)})")
    lines.append("")
    for a in arts:
        lines.append(f"### {a['title']}")
        lines.append(f"- 分类: {cat}")
        lines.append(f"- 时间: {a['pubDate'][:16].replace('T', ' ')}")
        lines.append(f"- 来源: {a['source']}")
        if a.get("author"):
            lines.append(f"- 作者: {a['author']}")
        lines.append(f"- 摘要: {a['snippet'][:300]}")
        lines.append(f"- 原文: {a['url']}")
        lines.append("")
    lines.append("---")
    lines.append("")

complete_path = BASE / "data" / "2026" / "07" / "02_complete.md"
complete_path.parent.mkdir(parents=True, exist_ok=True)
complete_path.write_text("\n".join(lines), encoding="utf-8")
print(f"写入完整列表: {complete_path}  ({complete_path.stat().st_size} bytes)")
