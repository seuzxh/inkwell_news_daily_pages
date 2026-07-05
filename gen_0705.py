#!/usr/bin/env python3
"""生成 0705 完整列表 + 精选简报"""

import json
from pathlib import Path

BASE = Path(__file__).parent
DATA = json.load(open(BASE / "0705_articles.json", encoding="utf-8"))

DATE = "2026-07-05"
YMD = "2026/07/05"

# 手写每篇一句话摘要（简短、中文），保留原始 inkwell 链接
SUMMARIES = {
    # AI & ML
    "art_b43739": "Simon Willison 转发 Iwo Kadziela（Codex 协作）的极客小品：仅 445 字节数据 + deflate 压缩 + 极短 JavaScript，即可生成可辨识的 ASCII 世界地图。首次演示 fetch() 可直接吞 data: URI + DecompressionStream，工程美学十足。",
    "art_66sjof": "Simon Willison 转 Armin Ronacher 观察：新款 Claude Opus 4.8 在 Pi 的 edit 工具嵌套 edits[] 数组里频繁凭空多塞字段，导致工具调用被拒。反直觉结论——「更强模型 ≠ 更稳工具调用」，schema 校验会随能力提升而更容易失效。",
    # Tech Culture
    "art_hpxijf": "John Gruber 从 2018 年 DF 存档翻出旧文重贴——那年他就警告 Electron 是原生应用体验的祸根，如今 Claude、Slack、VS Code 全线套壳，Mac 原生美感被稀释。历史坐标回望 8 年前判断精准兑现。",
    "art_542tod": "Flexibits 发布 Fantastical 4.1.15：新增 Calendar Mirroring，可把工作/私人两本日历打通，事件双向映射且完全本地处理、不经服务器。可选「详情或忙碌块」两档隐私粒度，是本地优先跨账号协作范例。",
    "art_heykmj": "shkspr.mobi 极客实验：把 1D UPC 条码嵌进 QR Code 中央区域，扫描器远看识别 QR、近看识别一维码。1970 年代条码 vs. 未来 QR 的过渡兼容方案，附完整生成脚本。",
    # History
    "art_99wmgd": "Construction Physics 每周阅读单 07/04/26：本周聚焦「无房主保险家庭比例、AI 芯片走私打击、日本双工频电网、Meta AI 算力生意」等主题，2/3 内容付费订户专享。基础设施+工业技术周度导航必读。",
    # Indie
    "art_z1k632": "nesbitt.io 第 7 周包管理周报：Hex 2.5.0 上线组织级依赖政策（HEX_POLICY），项目可从组织仓库拉取命名策略过滤高风险版本；APT 亦有多项更新。Erlang/Elixir 生态在供应链安全上再进一步。",
    # Essays
    "art_van2qt": "John D. Cook 一篇贝叶斯小品：「更多数据一定降低后验方差吗？」——答案是否定的。虽然一般情况下后验会收缩，但存在反例，新观测可能与先验冲突反而放大不确定性。附数值化推演，统计学直觉纠偏。",
    # Systems
    "art_9qdstu": "computer.rip 长文《megawatts by microwave》：从 1914 年内政部对哥伦比亚河的开发调研讲起，回顾大萧条时代 Grand Coulee 水坝供电大西北的经典史，为下一步「微波无线输电」远景铺陈历史脉络。",
    # Programming
    "art_d2ub3b": "Armin Ronacher 原文首发：Claude Opus 4.8 调用 Pi 的 edit 工具时凭空捏造嵌套字段（如 edits[].newContent 里多出 unknown key），导致工具因 schema 不匹配拒绝执行。作者两天调试后判定：模型能力提升带来副作用，参数捏造比幻觉输出更隐蔽、更致命。",
}

CATEGORY_ORDER = ["AI & ML", "Tech Culture", "Programming", "Systems", "History", "Indie", "Essays"]

# 精选简报选取：去重（art_66sjof=Simon转 art_d2ub3b=Armin原文），保留原文
# 10 篇原始 -> 9 条精选（严格筛选，不凑数）
HIGHLIGHT_IDS = {
    "AI & ML": [
        "art_b43739",  # 500字节世界地图
    ],
    "Tech Culture": [
        "art_hpxijf",  # DF 存档 Electron
        "art_542tod",  # Fantastical Calendar Mirroring
        "art_heykmj",  # 1D+2D 条码合并
    ],
    "Programming": [
        "art_d2ub3b",  # Armin: Better Models Worse Tools 原文
    ],
    "Systems": ["art_9qdstu"],  # 微波兆瓦
    "History": ["art_99wmgd"],  # Reading List 07/04
    "Indie": ["art_z1k632"],    # Package Management Weekly
    "Essays": ["art_van2qt"],   # 贝叶斯 posterior variance
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
    lines.append("**采集范围**: 2026-07-04 08:00 ~ 2026-07-05 08:00 (北京时间)")
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
    out = BASE / "data" / "2026" / "07" / "05_complete.md"
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
    lines.append("")
    lines.append("🔗 查看今日全部文章")
    lines.append(f"👉 https://seuzxh.github.io/inkwell_news_daily_pages/complete.html?date={DATE}")
    out = Path("/app/data/所有对话/主对话/InkWell简报") / f"简报_20260705.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"精选简报: {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    gen_complete()
    gen_highlights()
