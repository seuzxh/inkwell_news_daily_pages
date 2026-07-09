# InkWell 完整列表 · 2026-07-09

**采集范围**: 2026-07-08 08:00 ~ 2026-07-09 08:00 (北京时间)
**来源**: inkwell.coze.site
**文章总数**: 22 篇 / 9 个分类

## 分类统计

| 分类 | 数量 |
|------|------|
| Tech Culture | 8 |
| AI & ML | 4 |
| Indie | 3 |
| Security | 2 |
| Web & Design | 1 |
| Essays | 1 |
| Systems | 1 |
| Hardware | 1 |
| Programming | 1 |
| **总计** | **22** |

---

## Tech Culture (8 篇)

**'PARRY Encounters the DOCTOR' — 1973 年的聊天机器人对聊天机器人**
▸ John Gruber 挖出 1973 年 RFC 439：Kenneth Colby 的偏执型精神分裂模拟机器人 PARRY，被人接入 ELIZA/DOCTOR，两个 AI 现场互怼——由 Vint Cerf 记录成 RFC。Vint Cerf 上周从 Google 退休，享年 83。适合作为"AI 对话史"的历史锚点。
🔗 https://inkwell.coze.com/article/art_tkw8yd

**Mac App 逃离 Squircle Jail 的方式**
▸ Tyler Hall 揭示：macOS Tahoe 强制第三方 App 走 squircle 图标模具，但**只要 App 不上 Mac App Store**，就能通过 `NSDockTilePlugIn` API 保留自定义图标。Iris 已内置该逃逸路径。是 App Store 与非 Store 应用体验持续分化的又一个信号。
🔗 https://inkwell.coze.com/article/art_o5enkm

**'Searching for SmarterChild' 纪录片 Kickstarter**
▸ Gruber 支持：Lindsey Sitz 和 Zan Gillies 众筹一部纪念 SmarterChild 的纪录片。SmarterChild 是 2000 年代 AOL Instant Messenger 上的爆款聊天机器人，全盛期拥有 3000 万"好友"，可视为消费级 chatbot 的鼻祖之一。
🔗 https://inkwell.coze.com/article/art_qojtp8

**我和 ELIZA 的对话**
▸ Gruber 在 ELIZA Archeology Team 复刻的网页版上重跑经典 60 年代对话机器人，全程展示"if/then 语法解析"的机械感。核心结论：**ELIZA 的历史地位与实际交互能力相差极大**——它更多是个文化符号而非技术标杆。对当下 LLM 的"人格化"讨论是一个反向参照。
🔗 https://inkwell.coze.com/article/art_ao6pt0

**The ELIZA Archaeology Project**
▸ MIT Project MAC 时代 Joseph Weizenbaum 原始 ELIZA 的考古复刻项目，提供精准还原实现 + 计划出版的书稿。呼应 Weizenbaum 后来警告"不要把机器当人对待"的立场——AI 伦理讨论的历史源头。
🔗 https://inkwell.coze.com/article/art_knmtnu

**初代 Macintosh 的 App 图标设计传统**
▸ Dr. Drang 密集展示原始 Macintosh 一位（1-bit）图标：Apple 用"倾斜矩形 + 手形"标记 App，直立矩形 + 折角标记文档，形成早期视觉语言。TeachText 一开始就没有手（用铅笔），是"应用即工具"图标语言的前奏。当下 squircle 争议的历史参照。
🔗 https://inkwell.coze.com/article/art_4abfcl

**[Sponsor] WorkOS Pipes：一次 API 调用完成集成**
▸ 广告位：WorkOS Pipes 把 GitHub/Slack/Salesforce/Google Drive 等 100+ 第三方 OAuth 集成收敛成一次 API 调用，处理 token 刷新和凭证存储。Agent 时代减少 integration 工作量的典型基础设施。
🔗 https://inkwell.coze.com/article/art_5tadvf

**一个只影响左撇子用户的 Bug**
▸ @edent 用中世纪风格记录 WordPress 站点的一个 bug：JS 精简后，右滑触发的"回复"按钮位于左侧，只有左手拇指滑动的用户会误触弹出评论框。作者是右撇子所以从没复现过——**"设备/习惯的隐性 monoculture"如何造出无形 bug**，是无障碍/可用性测试的经典案例。
🔗 https://inkwell.coze.com/article/art_ur67lb

## AI & ML (4 篇)

**OpenAI 发布 GPT-Live**
▸ Simon Willison 预览：ChatGPT 语音模式底层模型终于从 GPT-4o 时代升级为 GPT-Live（背后跑 GPT-5.5）。核心特性：**边说话边把重活派发给 GPT-5.5**——遇到需要 web search、深度推理或复杂任务时，实时把工作卸载到前沿模型，返回结果后无缝继续对话。语音助手可用性大幅提升的分水岭。
🔗 https://inkwell.coze.com/article/art_pid361

**AI 基础设施为什么必须为 Agent Experience 演进 —— Modal CTO 访谈**
▸ Latent Space Agent Cloud 系列收官访谈 Modal（刚拿 3.55 亿美元 C 轮）。**核心论点：老一代云是为"能读文档、会看 dashboard 的人类开发者"设计的；Agent 没有这个奢侈品**。Agent 需要能写代码、跑代码、看输出、改环境、debug 失败并快速迭代——sandbox 化基础设施是关键。对国内做 AI 中台的团队有参考价值。
🔗 https://inkwell.coze.com/article/art_8qoumj

**Kenton Varda 引言：禁用 AI 写 PR/Commit 描述**
▸ Cloudflare Workers 之父 Kenton Varda 在团队内下达 moratorium：**AI 写的 change description 比没有还糟**——只会复读"代码里显然可见的细节"，却漏掉真正需要的高层动机与设计取舍。Simon Willison 收录。对研发流程中"AI 参与哪些环节"的边界思考有参考。
🔗 https://inkwell.coze.com/article/art_cf2l8v

**[AINews] Lilian Weng 总结 35 篇 Harness Engineering for RSI 论文**
▸ Latent Space 快讯：Meta Superintelligence 抢占图像/视频模型 Top 2/3（Muse Image/Video 无 paper）；Lilian Weng 罕见发长文综述 harness 工程与递归自我改进（RSI）——**未来 RSI 有多依赖 harness 尚难预测，但 harness 工程会朝自我改进方向进化，反过来又让模型更聪明**。是 Agent 层演进的重要理论坐标。
🔗 https://inkwell.coze.com/article/art_9d1gk1

## Indie (3 篇)

**从零手写 LLM 第 34b 部分 —— 用 JAX 实现 GPT-2**
▸ Giles Thomas 自 2024 年 12 月开始的长跑系列收官。**规则：只按自己的笔记从零搭 LLM，不看 Raschka 原书代码，也不看之前的 PyTorch 版本，改用 JAX 强制自己不"复述"记忆**。这套"再造轮子验证掌握"的学习法适合任何深度技术复盘。
🔗 https://inkwell.coze.com/article/art_ti14xt

**然后那个亿万富翁替我们付了 5.5 亿美元的账**
▸ idiallo.com：Snap CEO Evan Spiegel 夫妇捐 5.5 亿美元给 Undue Medical Debt，替加州人偿还医疗债务。作者不否认善行，但提醒"公开善举往往不像它看起来的样子"——**从盖茨的捐赠承诺到 TV 改造节目背后，都存在被光环遮蔽的结构性问题**。是慈善叙事的冷思考。
🔗 https://inkwell.coze.com/article/art_thjzhp

**如何重振社会结构？**
▸ Henrik Karlsson 新文（内容需订阅）+ Jockum Nordström 手绘配图。社会资本/社群维系是他近期核心议题——对判断"AI 会加速还是修补社会原子化"的读者值得追踪。
🔗 https://inkwell.coze.com/article/art_1pgsiz

## Security (2 篇)

**Weekly Update 511：Troy Hunt 在马拉喀什直播**
▸ Have I Been Pwned 创始人 Troy Hunt 本周核心议题：**打捞泳池里的尿——试图从合法数据经纪商那里"擦除"用户数据的服务，本质上是徒劳**。他不质疑动机，但对相关厂商反复找上门做 product placement 的营销机制发出警告。数据合规视角的一手观察。
🔗 https://inkwell.coze.com/article/art_razcz7

**罪犯与欺诈者兜售进攻型网络安全公司**
▸ Krebs on Security 深度调查：X 上号称在 McLean 出百万美元收购 0day 漏洞的 IRIS C2（@C2IRIS，4000+ 关注），实际由两名极右阴谋论者和被判过刑的欺诈者运营，前科包括虚假情报公司和已倒闭的 AI 游说平台。**主动漏洞市场的合规风险与信誉核查**警示。
🔗 https://inkwell.coze.com/article/art_5i9xzb

## Web & Design (1 篇)

**家庭大对抗：Mac 味 Mac App 版**
▸ Jim Nielsen 用 Family Feud 综艺格式吐槽：全球最有资格做"世界级 Mac 味 Mac App"的公司是谁？答案 Apple 之后，Anthropic 拿 Claude Desktop 上了 Electron，Adobe/Google 也没戏。**Electron 化时代，"原生 Mac App"越来越像绝迹的手工艺**——设计价值观 vs 跨平台效率的持续拉扯。
🔗 https://inkwell.coze.com/article/art_o5h9zi

## Essays (1 篇)

**越轨行为的衰退 2**
▸ Adam Mastroianni《The Decline of Deviance》续篇。原文核心：**1990 年代以来风险偏好和规则破坏在下降——好处是犯罪减少，坏处是创新也在减少**；根源是繁荣升高了"可失去的东西"。续篇收集大量反馈后推进讨论：为什么孩子们不再抽烟没人在乎、系列续集为何泛滥。是理解代际创新意愿变化的长文。
🔗 https://inkwell.coze.com/article/art_nzhsl7

## Systems (1 篇)

**另一种 Control Flow Guard 检查：合并验证与调用**
▸ Raymond Chen 深挖 Windows CFG：`LdrpValidateUserCallTarget` 除了纯验证版本，还有一个"验证后直接调用"的合并版本——因为验证完函数指针基本都会立即调用，合并可省寄存器保存成本，但代价是**调用约定必须变**（参数寄存器不能与 call target 用的重叠）。x86-64 汇编级细节，操作系统安全实现参考。
🔗 https://inkwell.coze.com/article/art_d3axlc

## Hardware (1 篇)

**Special Value Pi 4：昙花一现的"低价版"**
▸ Jeff Geerling 收到罕见的 Raspberry Pi 4 "Value Edition"：只保证 1.25 GHz（零售版 1.8 GHz，通常还能超频）。Reseller 上架后迅速下架，产品页 404。Pi 硬件产线上"筛选品"暗流的一角。
🔗 https://inkwell.coze.com/article/art_fb1xep

## Programming (1 篇)

**Agent 是 Monad（但不是那种）**
▸ Xe Iaso 提出：**AI Agent 的本质是它的 state——把 state 剥掉，剩下的不是弱化的 Agent，而只是底模**。这里的 hyle（质料，模型权重）与 pneuma（灵魂，Agent 状态）截然不同。Cat-theory 的 monad 是 blind to state 的抽象，而 Agent 的 monad 更像莱布尼茨的单子（Monad）——每一个都有具体状态。给 Agent 系统建模的哲学视角。
🔗 https://inkwell.coze.com/article/art_vr5pwa
