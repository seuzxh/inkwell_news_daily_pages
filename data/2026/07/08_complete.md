# InkWell 完整列表 · 2026-07-08

**采集范围**: 2026-07-07 08:00 ~ 2026-07-08 08:00 (北京时间)
**来源**: inkwell.coze.site
**文章总数**: 13 篇 / 4 个分类

## 分类统计

| 分类 | 数量 |
|------|------|
| AI & ML | 6 |
| Tech Culture | 3 |
| Systems | 2 |
| Indie | 2 |
| **总计** | **13** |

---

## AI & ML (6 篇)

**sqlite-utils 4.0, now with database schema migrations**
▸ Simon Willison 发布 sqlite-utils 4.0，是继 2020 年 11 月 3.0 之后的首次主版本升级，也是该项目第 124 次发布。三大新特性：数据库 schema migrations（迁移可追踪已应用记录）、通过 `db.atomic()` 支持嵌套事务、复合外键。破坏性变更集中在 upgrade guide。`table.transform()` 提供超越 SQLite `ALTER TABLE` 的能力。
🔗 https://inkwell.coze.com/article/art_elsy0h

**sqlite-migrate 0.2**
▸ 独立的 sqlite-migrate 库正式退休，本次 0.2 版本改为对 sqlite-utils 4.0 内建 migrations 的兼容 shim。功能收敛回 sqlite-utils 主库。
🔗 https://inkwell.coze.com/article/art_p45z18

**github-code Web Component**
▸ Simon Willison 用 GPT-5.5 vibe-code 出一个 Web Component `<github-code href="...">`，可把 GitHub 代码链接 embed 为带行号的代码块（通过 raw.githubusercontent.com fetch 指定行范围）。展示"提示词→Web Component"这类小工具的开发范式。
🔗 https://inkwell.coze.com/article/art_6tt847

**sqlite-utils 4.0**
▸ 稳定版发布公告，指向"sqlite-utils 4.0, now with database schema migrations"细节文章。
🔗 https://inkwell.coze.com/article/art_2akv9y

**sqlite-utils 4.0rc4**
▸ 4.0 稳定版之前的最后一个 RC，主要吸收了 Claude Fable 5 的详细代码 review 反馈。
🔗 https://inkwell.coze.com/article/art_idghw1

**[AINews] The Field Guide to Fable**
▸ Latent Space 快讯：General Intuition 和姚顺雨（Shunyu Yao）都发了新模型，业界等待 GPT-5.6 Sol Ultra 发布，而 Fable 5 的订阅补贴即将结束。Thariq 连夜把 keynote 转成 Fable 使用指南：模型约束往往来自 US（harness/prompt），碰到新模型应主动解除旧约束。
🔗 https://inkwell.coze.com/article/art_gv4y70

## Tech Culture (3 篇)

**Let AI Burn**
▸ Ed Zitron（wheresyoured.at）发布本周长文预告：本周刊出《Hater's Guide to Softbank》深度扒孙正义作为"科技圈最堕落赌徒"如何为 AI 泡沫最大规模的崩塌埋下基础；周五将深入记忆芯片行业。付费订阅 $70/年，每期 5000-18000 词。AI 泡沫论重要视角。
🔗 https://inkwell.coze.com/article/art_hu4mf5

**OS 27 Developer Beta 3 Enables New 'Pace' and 'Expressivity' Sliders for Siri's New Voices**
▸ iOS 27 开发者 Beta 3 启用 Siri 语音的"节奏（Pace）"和"表现力（Expressivity）"两个滑块（此前标记为 Coming soon）。John Gruber 已把主力 iPhone 17 Pro 全线切到 Beta，表示稳定性和 Siri AI 实用性都足够，公共 Beta 预计临近。
🔗 https://inkwell.coze.com/article/art_xe0aak

**Pluralistic: How US states and international trustbusters can beat Big Tech (07 Jul 2026)**
▸ Cory Doctorow 每日专栏，主推文《美国各州与国际反垄断机构如何击败大科技》——共同敌人是特朗普政府和其扶持的科技巨头。附大量"Object permanence"链接和文化观察。
🔗 https://inkwell.coze.com/article/art_2idlyd

## Systems (2 篇)

**How did Windows 95 decide that a setup program ran?**
▸ Raymond Chen 揭秘 Windows 95 判定"某程序是不是安装程序"的猜启发式：程序名中包含 setup/install/inst/imposta（意）/ayarla（土）/felrak（匈）等魔法词即被判为 setup。install 和 inst 并列冗余是历史遗留。适合了解早期 OS 设计的经验主义思路。
🔗 https://inkwell.coze.com/article/art_lgat3u

**Kort geding aandeelhouders Solvinity**
▸ Bert Hubert 荷兰语记录 Solvinity（DigiD 背后公司）股东状告国务秘书的紧急听证：荷兰政府拒收购、又阻止 Solvinity 出售给美国公司。数字经济与主权命题的现场记录，媒体报道多有遗漏。
🔗 https://inkwell.coze.com/article/art_yrz8ey

## Indie (2 篇)

**Content addressing in package managers**
▸ 系统梳理"内容寻址"（用数据的加密哈希而非名字或位置来标识）在包管理器各层的落点：一个端到端内容寻址的包管理器，其 registry index、metadata、artifact、artifact 内文件都以哈希命名，可从任意源获取并本地校验。回顾多个已部分实现该思路的系统。
🔗 https://inkwell.coze.com/article/art_1uzwlr

**Blog about things you don't understand yet**
▸ Sean Goedecke 写作观：每篇发出去的文章至少代表两件学到的东西——写作动机 + 写作过程中学到的东西。如果写作过程本身没学到新东西，说明这个话题不值得发。写作是学习的强制机制。
🔗 https://inkwell.coze.com/article/art_qgqvu4
