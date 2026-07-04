# InkWell 完整列表 · 2026-07-04

**采集范围**: 2026-07-03 08:00 ~ 2026-07-04 08:00 (北京时间)
**来源**: inkwell.coze.site
**文章总数**: 14 篇 / 6 个分类

## 分类统计

| 分类 | 数量 |
|------|------|
| AI & ML | 7 |
| Tech Culture | 2 |
| History | 2 |
| Systems | 1 |
| Indie | 1 |
| Security | 1 |
| **总计** | **14** |

---

## AI & ML (7 篇)

**Open Source AI Gap Map**
▸ Current AI 非营利联盟发布 Open Source AI Gap Map v0.1，深入索引 421 个开源 AI 产品（266 工具+85 模型+50 数据集+20 硬件），并把 1184 份 YAML 全部放到 MIT 许可的 GitHub 仓库，另有 24400 长尾条目待挖。首个真正意义上的开源 AI 生态版图。
🔗 https://inkwell.coze.com/article/art_pqmshf

**Quoting Josh W. Comeau**
▸ Josh W. Comeau 反馈：新课 Whimsical Animations 销量仅为往年 1/3，同行普遍营收下滑 50%+。原因是双重打击——开发者担心岗位消失不愿投资学习，能学的人又转向 LLM 一对一辅导。开发者教育市场正被 AI 结构性冲击。
🔗 https://inkwell.coze.com/article/art_1rgac3

**Fable's judgement**
▸ Simon Willison 从 Claude Code 团队 Cat Wu / Thariq 处获得核心 tip：与其规定 Fable 何时写测试，不如让它「自行判断」。他进一步在 memory file 里写入「所有编码任务，用你的判断分派给合适的低算力子 Agent」，一举压低 Fable 昂贵 token 消耗。
🔗 https://inkwell.coze.com/article/art_ugh2rl

**June 2026 newsletter**
▸ Simon Willison 6 月付费月报出炉：本期覆盖 Claude Fable 5、GPT-5.6、美国出口管制，重点判定 GLM-5.2 为当前最强开源权重模型，同时宣告「Tokenmaxxing 时代已过」——效率不再靠堆 token。付费墙 10 美元/月，比公开版早一个月。
🔗 https://inkwell.coze.com/article/art_t5n040

**Google DeepMind and A24 announce first-of-its-kind research partnership**
▸ Google DeepMind 与好莱坞制片厂 A24 官宣联合科研合作——AI 巨头首次与顶级独立影视厂建立研究伙伴关系，方向指向下一代生成式影像。为 Gen-AI 内容工业化落地打开电影级样本入口。
🔗 https://inkwell.coze.com/article/art_yq0lin

**AIEWF Daily Dispatch: The great loops debate and the state of AI engineering**
▸ AIEWF 收官日 Loop 大辩论：Ralph Loop 作者 Geoffrey Huntley、Keycard 的 Ian Livingstone 力挺自动化软件工厂「已不可逆」，HumanLayer 的 Dex Horthy、Subroutine 的 Greg Pstrucha 反问理想与现实差距。可验证性成为 loop 派唯一底线。
🔗 https://inkwell.coze.com/article/art_uyevgc

**Vercel's Andrew Qu on why agents are a new kind of software**
▸ Vercel Chief of Software Andrew Qu 详解：Agents 是全新形态的软件，不只是 UI 上加个聊天框。Vercel 自研 MCP 库、skills.sh 和 eve 框架，公司正在把自身「Agent 化」。这是 Vercel 从 web 部署平台向 Agent 底座转型的官方宣言。
🔗 https://inkwell.coze.com/article/art_tjallb

## Tech Culture (2 篇)

**★ Claude’s Criminally Bad Electron Mac App Is an Inside Job**
▸ John Gruber 猛批 Anthropic Claude Mac 桌面应用——Electron 套壳、体验拉垮已两年，讽刺意味在于 Anthropic 自家 Claude Code 已能自动生成原生 SwiftUI 代码。用不用 Claude Code 造 Claude for Mac，成为 Anthropic 工程文化的公开测试。
🔗 https://inkwell.coze.com/article/art_dbcjgm

**Pluralistic: CARDiac, syntax coloring, view source and vibe code (03 Jul 2026)**
▸ Cory Doctorow 新篇：从 1970 年代纸板计算机 CARDiac 讲到 vibe coding，直击当代抽象层过厚导致「查看源代码」失灵、隐性认知损耗剧增，抽象越强代价越大。他警告：程序员正把可解释性主权交给不透明系统。
🔗 https://inkwell.coze.com/article/art_2e4yvt

## History (2 篇)

**The Life and Times of Maxis, Part 1: SimEverything**
▸ Filfre 长篇史料级连载启动《Maxis 兴衰史》第一集 SimEverything：从 Will Wright 到大陆漂移的痴迷，追述 Maxis 如何造出一整套模拟宇宙。是继 Infocom 系列后又一次经典游戏史级研究。
🔗 https://inkwell.coze.com/article/art_hcvxub

**The Fall and Rise of Screwworm**
▸ Construction Physics 长文回顾灭而复现的螺旋蝇（Screwworm）：6 月 3 日德州再度发现、数十例已蔓延至新墨西哥，冷战时用不育昆虫技术根除的经典公卫案例正被复刻。全球昆虫防治体系被再次检验。
🔗 https://inkwell.coze.com/article/art_tcpqfn

## Systems (1 篇)

**How did we conclude that CcNamespace.dll was the ringleader of a group of DLLs that unloaded prematurely?**
▸ Raymond Chen 追加案例：如何在崩溃 dump 里定位到 CcNamespace.dll 是一群 CloudNs 系列 DLL 提前卸载的元凶——利用 Windows 卸载 DLL 环形历史 + 命名族群，反推第三方 DLL 生命周期漏洞。经典调试思路教材。
🔗 https://inkwell.coze.com/article/art_g4tqqu

## Indie (1 篇)

**Midnight Train to Stockholm**
▸ Copenhagen 程序员 Mat Duggan 从马尔默夜车赴斯德哥尔摩，实地写了瑞典高铁 vs. 飞行 vs. 夜卧的选择分析——工程师视角评估欧洲城际交通体验，附中年出差实操心得。
🔗 https://inkwell.coze.com/article/art_xmes9e

## Security (1 篇)

**Swimming Pools, Pee, and Trying to Delete Your Data From the Internet**
▸ Troy Hunt（HIBP 创办人）用「往泳池里撒尿再想捞回来」比喻个人数据一旦泄露不可逆，正面回应各类「帮你删除个人信息」商业服务的营销骚扰。GDPR 时代必读的隐私边界现实主义警示。
🔗 https://inkwell.coze.com/article/art_t3vc7k
