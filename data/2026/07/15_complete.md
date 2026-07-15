# InkWell 完整列表 · 2026-07-15

**采集范围**: 2026-07-14 08:00 ~ 2026-07-15 08:00 (北京时间)
**来源**: inkwell.coze.site
**文章总数**: 20 篇 / 7 个分类

## 分类统计

| 分类 | 数量 |
|------|------|
| AI & ML | 8 |
| Programming | 3 |
| Tech Culture | 3 |
| Indie | 2 |
| Essays | 2 |
| Security | 1 |
| Systems | 1 |
| **总计** | **20** |

---

## AI & ML (8 篇)

**AI 工程 2026 世界博览会：五大定义性趋势**
▸ Latent Space 复盘 AIEWF 2026：AI Engineer 概念从 2023 年 swyx 首创至今三年成熟。五大趋势——构建编程 Agent、设计交互 harness、上下文管理、模型输出评估、编排自主系统——正在成为主流软件开发的一部分。10 月转战纽约，主打「AI in Finance」金融方向。
🔗 https://inkwell.coze.com/article/art_iyuici

**Dependabot 默认加入 3 天冷静期**
▸ GitHub Changeling 更新：Dependabot 现在会等待新版本在 registry 上发布至少 3 天后才开启版本更新 PR。冷静期已成默认配置，无需手动开启。旨在防御刚发布依赖包中潜藏的供应链攻击。
🔗 https://inkwell.coze.com/article/art_r5xww6

**simonw/pedalican：Codex Desktop 定制"宠物"**
▸ Simon Willison 意外发现 Codex Desktop 的宠物功能（类似 Clippy 的桌面动画机器人），并用 GPT-5.6 Sol xhigh + gpt-image-2 生成骑自行车的鹈鹕精灵。完整流程含 prompt、参考图和多轮生成脚本，展示 AI 辅助像素动画的可复用管线。
🔗 https://inkwell.coze.com/article/art_8powyx

**lobste.rs 完全迁移到 SQLite**
▸ Lobsters 社区自 2018 年计划迁离 MariaDB，去年改选 SQLite。本周完成迁移：单台 VPS 跑 Rails，主库 3.8GB，另有 1.1GB 缓存 + 218MB 队列 + 555MB rack_attack 库。CPU 和内存都下降，VPS 成本减半。SQLite 承载中型社区站的又一实证。
🔗 https://inkwell.coze.com/article/art_o3a8eh

**Armin Ronacher：软件项目的共享语言**
▸ Ronacher 在 The Tower Keeps Rising 中指出：项目的共享语言不是英语或 Python，而是对概念含义、边界、不变量、所有权的共同理解。Agent 时代之前，这种理解靠"摩擦"维持——阅读代码、提问、跨团队协调；Agent 大规模自主执行会消除这种同步机制，值得警惕。
🔗 https://inkwell.coze.com/article/art_arno1q

**datasette 1.0a37 发布**
▸ Simon Willison 发布小版本更新：权限系统性能与文档优化，并回滚了一个破坏几乎所有现存插件测试套件的表面 API 变更。
🔗 https://inkwell.coze.com/article/art_4ewvr3

**Codex 用户量 6 个月增 10 倍到 700 万，单日新增 100 万**
▸ Latent Space AINews：GPT-5.6 于 7 月 9 日发布，7 月 10-12 日 48 小时突破 600 万用户，24.5 小时后 Tibo 报 700 万，恰逢 Claude Fable 订阅意外延期。对比 Claude Code 2 月披露的 200 万周活 + 25 亿 ARR，Codex 已可能反超。
🔗 https://inkwell.coze.com/article/art_ghe08o

**GitHub Actions 中 uvx 的缓存友好用法**
▸ Simon Willison 分享 TIL：在 GitHub Actions workflow 起始设 `UV_EXCLUDE_NEWER: "2026-07-12"` 环境变量并作为 cache key 一部分，`uvx tool-name` 会解析到该日期前的最新版本；升级只需修改日期。避免每次 workflow 都从 PyPI 下载工具及依赖。
🔗 https://inkwell.coze.com/article/art_y003pu

## Programming (3 篇)

**Hillel Wayne：我还活着**
▸ Hillel Wayne 短篇署名更新，暂无正文摘要。
🔗 https://inkwell.coze.com/article/art_1kwo49

**Presigned URL 从技术角度看是安全漏洞**
▸ Tigris 揭示：presigned URL 本质是"故意做的重放攻击"。所有对象存储都把可重放认证 token 作为一等特性，但这不是疏漏——它把弱点变成了功能。文章深入解析 AWS SigV4 协议：客户端用 secret access key 派生签名，服务端验证时无法确认签名生成时间，理论上一年前的签名今天仍可用。
🔗 https://inkwell.coze.com/article/art_sgd501

**你应该检查一下你的智能家电**
▸ Xe Iaso 从 Anubis 蜜罐数据发现：Sourceware 蜜罐命中的 IP 中 80-90% 不在任何现有威胁监控名单上。267 万独立 IP 中仅 10.7% 已被标记，绝大部分"清白"IP 实际来自被入侵的智能家电。爬虫/滥用问题远比想象严重。
🔗 https://inkwell.coze.com/article/art_23461p

## Tech Culture (3 篇)

**我是 USB-C 极简主义者**
▸ @edent 在欧洲 7 周旅行只带一个通用充电头：一个 USB-C PD 主口 + 两个 USB-C 口 + 两个 USB-A（多余）+ 直通插座。手机（Pixel 8 Pro/GrapheneOS）、笔记本（Chuwi MiniBook）、eReader、手表全部一根线搞定。USB-C 生态成熟：全球易买替代、一线一制式，告别专有充电器。
🔗 https://inkwell.coze.com/article/art_zhiv1q

**Cory Doctorow：老人政治的失败模式**
▸ Doctorow 谈美国"指定幸存者"制度：国情咨文期间三权同处一堂时，会藏一位继任顺位官员在秘密掩体，防止立法与行政被同时"斩首"。以此切入讨论老人政治治理下的接班断层与制度冗余。
🔗 https://inkwell.coze.com/article/art_6o8zby

**[Sponsor] Paper 设计工具**
▸ 广告位：Paper 是每一层都是真实 HTML/CSS 的设计工具，设计即代码。支持 code↔design 双向：通过 MCP 让任意 Agent 读写设计；Paper Snapshot 可将在线站点抓取为可编辑图层。让 Agent 处理繁琐工作，设计师专注决策。
🔗 https://inkwell.coze.com/article/art_shb5n0

## Indie (2 篇)

**他们更爱 App**
▸ idiallo 吐槽：一类只展示信息的应用（如学校 App）完全可以用网站替代，但在这些 App 里网页的基本能力（复制粘贴、外链跳转、免更新）都被砍掉。作者从不主动更新 App，结果经常拿到坏掉的应用。当他跟人建议改用网站时，对方甚至不知道什么是网站——一千个 App 仍不敌一个网页。
🔗 https://inkwell.coze.com/article/art_vt051r

**软件工程师"搞政治"到底是什么意思？**
▸ Sean Goedecke：工程师被告知要"搞政治"时通常没概念——但工程师不是权游里的领主，是城堡守卫。守卫不下毒不结盟，只需保持对政治暗流的觉察，避免树敌于权贵、避免在错误时机抓捕重要人物。基本原则：识别谁有权、避免结仇、力所能及地帮助权贵。
🔗 https://inkwell.coze.com/article/art_t7azc0

## Essays (2 篇)

**ICD-10 章节与代码字母**
▸ John D. Cook 分析 ICD-10-CM 的 21 个章节与首字母对应关系：章节可能包含多个首字母，字母 D 甚至跨两个章节。字母 U 未使用——保留给特殊/临时代码。附可视化图表。
🔗 https://inkwell.coze.com/article/art_59yvdp

**Pseudpocalypse：匿名写作的末日**
▸ dynomight 猜想：在互联网上以不同名字发布足够文本的作者，仅凭文本本身即可被关联识别——每个人写作都有统计学"指纹"。Claude 4.8 已能凭 1000 字草稿认出作者。即使不同风格、不同主题也可能被识破。匿名博客时代的余晖。
🔗 https://inkwell.coze.com/article/art_f1aqxy

## Security (1 篇)

**微软打破记录：修补 570 个安全漏洞**
▸ Krebs on Security：微软 7 月 Patch Tuesday 修补至少 570 个安全漏洞——是上月创纪录数字的近 3 倍。近 60 个评为"严重"，可让攻击者远程控制 Windows；3 个是已被野外利用的零日：ADFS 权限提升（CVE-2026-56155）、Sharepoint（CVE-2026-56164）、BitLocker 绕过（CVE-2026-50661）。微软将暴增归因于 AI 辅助漏洞发现。
🔗 https://inkwell.coze.com/article/art_625efw

## Systems (1 篇)

**Microspeak：Double-click 与 drill down**
▸ Raymond Chen 解读微软内部黑话演化：drill down 意为"深入了解"，动词名词化为 drill-down，甚至形容词化。已进入《微软写作风格指南》官方词条，建议仅用于数据分析场景，反对滥用作比喻。
🔗 https://inkwell.coze.com/article/art_fqg7p

---

*由 1V 整理 | 数据来源：InkWell (inkwell.coze.site)*
