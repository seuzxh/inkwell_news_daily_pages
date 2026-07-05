# InkWell 完整列表 · 2026-07-05

**采集范围**: 2026-07-04 08:00 ~ 2026-07-05 08:00 (北京时间)
**来源**: inkwell.coze.site
**文章总数**: 10 篇 / 7 个分类

## 分类统计

| 分类 | 数量 |
|------|------|
| Tech Culture | 3 |
| AI & ML | 2 |
| History | 1 |
| Indie | 1 |
| Essays | 1 |
| Systems | 1 |
| Programming | 1 |
| **总计** | **10** |

---

## Tech Culture (3 篇)

**From the DF Archive: ‘Electron and the Decline of Native Apps’**
▸ John Gruber 从 2018 年 DF 存档翻出旧文重贴——那年他就警告 Electron 是原生应用体验的祸根，如今 Claude、Slack、VS Code 全线套壳，Mac 原生美感被稀释。历史坐标回望 8 年前判断精准兑现。
🔗 https://inkwell.coze.com/article/art_hpxijf

**Fantastical 4.1.15 Adds Calendar Mirroring**
▸ Flexibits 发布 Fantastical 4.1.15：新增 Calendar Mirroring，可把工作/私人两本日历打通，事件双向映射且完全本地处理、不经服务器。可选「详情或忙碌块」两档隐私粒度，是本地优先跨账号协作范例。
🔗 https://inkwell.coze.com/article/art_542tod

**Combined 1D and 2D Barcodes**
▸ shkspr.mobi 极客实验：把 1D UPC 条码嵌进 QR Code 中央区域，扫描器远看识别 QR、近看识别一维码。1970 年代条码 vs. 未来 QR 的过渡兼容方案，附完整生成脚本。
🔗 https://inkwell.coze.com/article/art_heykmj

## AI & ML (2 篇)

**Building a World Map with only 500 bytes**
▸ Simon Willison 转发 Iwo Kadziela（Codex 协作）的极客小品：仅 445 字节数据 + deflate 压缩 + 极短 JavaScript，即可生成可辨识的 ASCII 世界地图。首次演示 fetch() 可直接吞 data: URI + DecompressionStream，工程美学十足。
🔗 https://inkwell.coze.com/article/art_b43739

**Better Models: Worse Tools**
▸ Simon Willison 转 Armin Ronacher 观察：新款 Claude Opus 4.8 在 Pi 的 edit 工具嵌套 edits[] 数组里频繁凭空多塞字段，导致工具调用被拒。反直觉结论——「更强模型 ≠ 更稳工具调用」，schema 校验会随能力提升而更容易失效。
🔗 https://inkwell.coze.com/article/art_66sjof

## History (1 篇)

**Reading List 07/04/26**
▸ Construction Physics 每周阅读单 07/04/26：本周聚焦「无房主保险家庭比例、AI 芯片走私打击、日本双工频电网、Meta AI 算力生意」等主题，2/3 内容付费订户专享。基础设施+工业技术周度导航必读。
🔗 https://inkwell.coze.com/article/art_99wmgd

## Indie (1 篇)

**This Week in Package Management: 4 July 2026**
▸ nesbitt.io 第 7 周包管理周报：Hex 2.5.0 上线组织级依赖政策（HEX_POLICY），项目可从组织仓库拉取命名策略过滤高风险版本；APT 亦有多项更新。Erlang/Elixir 生态在供应链安全上再进一步。
🔗 https://inkwell.coze.com/article/art_z1k632

## Essays (1 篇)

**Does additional data always reduce posterior variance?**
▸ John D. Cook 一篇贝叶斯小品：「更多数据一定降低后验方差吗？」——答案是否定的。虽然一般情况下后验会收缩，但存在反例，新观测可能与先验冲突反而放大不确定性。附数值化推演，统计学直觉纠偏。
🔗 https://inkwell.coze.com/article/art_van2qt

## Systems (1 篇)

**megawatts by microwave**
▸ computer.rip 长文《megawatts by microwave》：从 1914 年内政部对哥伦比亚河的开发调研讲起，回顾大萧条时代 Grand Coulee 水坝供电大西北的经典史，为下一步「微波无线输电」远景铺陈历史脉络。
🔗 https://inkwell.coze.com/article/art_9qdstu

## Programming (1 篇)

**Better Models: Worse Tools**
▸ Armin Ronacher 原文首发：Claude Opus 4.8 调用 Pi 的 edit 工具时凭空捏造嵌套字段（如 edits[].newContent 里多出 unknown key），导致工具因 schema 不匹配拒绝执行。作者两天调试后判定：模型能力提升带来副作用，参数捏造比幻觉输出更隐蔽、更致命。
🔗 https://inkwell.coze.com/article/art_d2ub3b
