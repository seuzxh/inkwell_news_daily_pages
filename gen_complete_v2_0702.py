#!/usr/bin/env python3
"""重新生成 0702 完整列表 - 使用 add_news.py 兼容格式"""

import json
from pathlib import Path

BASE = Path(__file__).parent
DATA = json.load(open(BASE / "0702_articles.json", encoding="utf-8"))

DATE = "2026-07-02"

# 手写每篇一句话摘要（简短、中文），保留原始 inkwell 链接
SUMMARIES = {
    "art_5z8ok8": "Cursor 首位 FDE VP Pauline Brunet 详解如何把 Agent 塞进企业软件全生命周期。Forward Deployed Engineering 已成企业 AI 落地最热岗位，介于工程/产品/客户成功三者之间。",
    "art_p8cswm": "Genesis Molecular AI 用扩散模型做分子设计，Latent Space 揭示 Diffusion 在 LLM 之外的更大天地。播客还爆料 Evan Feinberg 差点成为 Genesis 一号员工的反事实故事。",
    "art_96wxju": "Warp 从 CLI 工具进化为 agentic 编程平台，创始人 Zach Lloyd 在 AIEWF 提出「software factory」概念——Agent 循环运行、按需交付软件，工程师从写代码转向管理工厂。",
    "art_fqh4z9": "AI Engineer 世界博览会首个正会日，「loop」一词贯穿全场。Agents 从聊天助手转向流水线角色，与 FDE、软件工厂形成企业 AI 落地三角，是本届大会的核心叙事。",
    "art_c2v3ye": "Anthropic 今日发布 Sonnet 5，性能接近 Opus 4.8 但更便宜；Fable/Mythos 5 也在与美国政府沟通后获准重新发布。Sonnet 5 效率讨论是 AI Engineer World's Fair 第二日主线话题。",
    "art_qpclo8": "Sierra Agent Engineering 负责人 Natalie Meurer 领 120+ 工程师团队构建对话式 AI，解释 FDE 为何是软件工程的未来——工程师直接参与客户实施与迭代。",
    "art_3i65av": "John Gruber 指出：主机厂靠 PS Plus（$11-20/月）和 Xbox Game Pass（$10-23/月）订阅回血，几年即超过硬件补贴总额，Steam 联机不收费，Valve 商业模式反而更透明。",
    "art_4mrv6g": "Valve 向 The Verge 解释拒绝赔本卖 Steam Deck / Steam Machine：主机行业以硬件亏损换软件抽成的模式已被 PS/Xbox 订阅费严重扭曲，Valve 坚守 PC 兼容策略。",
    "art_sg7mw0": "John Moltz 回归 The Talk Show 播客，讨论 Apple 硬件涨价应对全球 RAM/SSD 短缺，并畅谈 macOS 下一代 UI 更新中值得肯定的部分。",
    "art_j6ojso": "Pluralistic 新篇 Technocarcinization：平台老化是一种「技术癌变」，从消费者到监管者到员工被同一套操纵手法收割。Doctorow 把 enshittification 上升为跨行业结构性规律。",
    "art_lvazcl": "404 Media 披露 iCloud Hide My Email 存在可将匿名转发地址反解为真实邮箱的漏洞，漏洞至今可被利用，媒体已隐去技术细节等待 Apple 修复。隐私功能反成隐私风险。",
    "art_l5zsm": "老牌 Old New Thing 专栏本期案例：安全报告称改注册表可绕过安全策略。Raymond Chen 反驳——攻击者已获管理员权限时，任何后续动作都属预期行为，「气密舱另一侧」原则不适用。",
    "art_4vm8fb": "荷兰新调查报告 PDF 揭示两大情报机构 AIVD/MIVD 在处理涉及数百万无辜公民的批量数据集时草率甚至违法。berthub.eu 深入剖析监督失效与法律真空，欧洲情报监管再度承压。",
    "art_rlmnjm": "Eli Bendersky 2026 年 Q2 阅读总结：涵盖《纽伦堡审判》历史巨著、编程与哲学多本书目，评点各书亮点与阅读收获，季度阅读清单久负盛名。",
    "art_mi26yk": "从事可观测性十年的老兵 Mat Duggan 复盘 Datadog / Splunk / Elastic 疲态：Clickhouse 以列式 + 高压缩成为日志/指标/追踪三合一底座，Uber、eBay、Cloudflare 均已迁移，市场格局重排在即。",
    "art_og7uf7": "Andrew Nesbitt 在 UN Open Source Week 后撰文：欧盟 Cyber Resilience Act 被反复标榜为「解决开源安全」的方案，但实际针对的是商业软件供应链，把开源当挡箭牌反而误导监管重点。",
    "art_2g5g9t": "John D. Cook 把 DNA 序列比对映射到国王在棋盘上的斜向走法，用中心 Delannoy 数 D_n 统计路径数量。生物信息学的经典动态规划原来是国王走法的组合展开。",
    "art_rbf1vz": "jyn.dev 短文：作者坦承只能靠讲故事解释自己，因为「有些东西大于我能说出的部分」。程序员常见的沟通问题——技术之外还有大量隐性上下文，故事是唯一携带载体。",
}


def summary_for(a):
    s = SUMMARIES.get(a["id"])
    if s:
        return s
    return (a.get("snippet") or "")[:250]


# 生成 md
lines = []
lines.append(f"# InkWell 完整列表 · {DATE}")
lines.append("")
lines.append(f"**采集范围**: 2026-07-01 08:00 ~ 2026-07-02 08:00 (北京时间)")
lines.append(f"**来源**: inkwell.coze.site")
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

out_path = BASE / "data" / "2026" / "07" / "02_complete.md"
out_path.write_text("\n".join(lines), encoding="utf-8")
print(f"重写完整列表: {out_path}  ({out_path.stat().st_size} bytes)")
