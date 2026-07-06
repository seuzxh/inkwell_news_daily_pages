#!/usr/bin/env python3
"""生成 0706 完整列表 + 精选简报"""

import json
from pathlib import Path

BASE = Path(__file__).parent
DATA = json.load(open(BASE / "0706_articles.json", encoding="utf-8"))

DATE = "2026-07-06"

# 手写每篇一句话摘要（中文，50-100字），保留原始 inkwell 链接
SUMMARIES = {
    # AI & ML
    "art_f25dxd": "Simon Willison 分享 sqlite-utils 4.0rc2 稳定版收尾实战：借 Claude Fable Max 订阅到期前的算力窗口（累计花费 $149.25），让 Fable 全流程审查代码库，一次性揪出 5 个 release blocker，其中 delete_where() 未提交事务将永久污染连接、导致数据丢失。「LLM 兜底大版本 SemVer 审查」范式跑通。",
    "art_9b4ung": "Simon Willison 同日短讯：sqlite-utils 4.0rc2 已发布，正式指向前一篇 Claude Fable 协作长文。作为 SemVer 语义化版本正式候选，本轮为 4.0 stable 前最后一次收敛，无新破坏性变更。",
    # Programming
    "art_5wz4j5": "程序语言实现顶会 PLDI 2026 Boulder 现场手记：作者第四次参会，重点参加 EGRAPHS workshop，多次听到 Knuth-Bendix 完备化算法。含 e-graph 优化、编译器研究圈层社交观察，以及 Denver 机场到 Boulder 的通勤实录，PL 圈层内部生态窥探。",
}

CATEGORY_ORDER = ["AI & ML", "Programming"]

# 精选简报选取：art_9b4ung 是 art_f25dxd 的短讯转发，去重仅保留主文
# 3 篇原始 -> 2 条精选（严格筛选，不凑数）
HIGHLIGHT_IDS = {
    "AI & ML": [
        "art_f25dxd",  # sqlite-utils 4.0rc2 Claude Fable 协作长文
    ],
    "Programming": [
        "art_5wz4j5",  # PLDI 2026 Boulder 手记
    ],
}


def summary_for(a):
    s = SUMMARIES.get(a["id"])
    if s:
        return s
    return (a.get("snippet") or "")[:250]


def build_article_lookup():
    lookup = {}
    for cat, arts in DATA["by_category"].items():
        for a in arts:
            lookup[a["id"]] = (cat, a)
    return lookup


# === 1. 完整列表 ===
def gen_complete():
    lines = []
    lines.append(f"# InkWell 完整列表 · {DATE}")
    lines.append("")
    lines.append("**采集范围**: 2026-07-05 08:00 ~ 2026-07-06 08:00 (北京时间)")
    lines.append("**来源**: inkwell.coze.site")
    lines.append(f"**文章总数**: {DATA['total']} 篇 / {len(DATA['by_category'])} 个分类")
    lines.append("")
    lines.append("## 分类统计")
    lines.append("")
    lines.append("| 分类 | 数量 |")
    lines.append("|------|------|")
    cats_sorted = sorted(DATA["by_category"].items(), key=lambda x: -len(x[1]))
    for cat, arts in cats_sorted:
        lines.append(f"| {cat} | {len(arts)} |")
    lines.append(f"| **总计** | **{DATA['total']}** |")
    lines.append("")
    lines.append("---")
    lines.append("")
    for cat, arts in cats_sorted:
        lines.append(f"## {cat} ({len(arts)} 篇)")
        lines.append("")
        for a in arts:
            lines.append(f"**{a['title']}**")
            lines.append(f"▸ {summary_for(a)}")
            lines.append(f"🔗 {a['url']}")
            lines.append("")
    out = BASE / "data" / "2026" / "07" / "06_complete.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"完整列表: {out} ({out.stat().st_size} bytes)")


# === 2. 精选简报 ===
def gen_highlights():
    lookup = build_article_lookup()
    total = sum(len(v) for v in HIGHLIGHT_IDS.values())
    lines = []
    lines.append("# 🗞️ Inkwell 资讯简报")
    lines.append(f"**更新时间**: {DATE}  |  **来源**: inkwell.coze.site")
    lines.append("")
    lines.append("---")
    lines.append("")
    for cat in CATEGORY_ORDER:
        if cat not in HIGHLIGHT_IDS:
            continue
        ids = HIGHLIGHT_IDS[cat]
        if not ids:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        for aid in ids:
            if aid not in lookup:
                continue
            _, a = lookup[aid]
            lines.append(f"**{a['title']}**")
            lines.append(f"▸ {summary_for(a)}")
            lines.append(f"🔗 {a['url']}")
            lines.append("")
        lines.append("---")
        lines.append("")
    lines.append("📊 统计概览")
    lines.append(f"- 本期精选: {total} 条")
    lines.append(f"- 覆盖分类: {len(HIGHLIGHT_IDS)} 个")
    lines.append(f"- 说明: 24h 内 InkWell 新增 {DATA['total']} 篇（周日+周一凌晨为博客低产时段），严格筛选后交付")
    lines.append("")
    lines.append("🔗 查看今日全部文章")
    lines.append(f"👉 https://seuzxh.github.io/inkwell_news_daily_pages/complete.html?date={DATE}")
    out = Path("/app/data/所有对话/主对话/InkWell简报") / f"简报_20260706.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"精选简报: {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    gen_complete()
    gen_highlights()
