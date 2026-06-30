# InkWell 完整资讯列表 - 2026-06-30

**采集时间**：2026-06-30 08:00（过去 24 小时）
**总计**：6 篇 / 4 分类
**来源**：inkwell.coze.site

---

## AI & ML（2 篇）

1. **Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding**
   - 作者：Simon Willison
   - 来源：simonwillison.net
   - 原文：https://simonwillison.net/2026/Jun/29/ornith/#atom-everything
   - InkWell：https://inkwell.coze.com/article/art_2v8rl0
   - 发布：2026-06-30 00:17
   - 摘要：DeepReinforce 首发开源权重模型 Ornith-1.0（MIT 许可），含 9B/31B Dense 与 35B/397B MoE 四个变体，基于 Gemma 4 + Qwen 3.5 二次预训练，在同尺寸开源模型编码基准上达 SOTA。Simon 已用 LM Studio 跑 35B Q4_K_M GGUF（20GB），并把它接到自家 Pi harness 上跑 Datasette 代码定位任务，多步工具调用表现优秀；绘制 pelican 输出 103 token/s，初印象非常正面。

2. **Count the number of Safari tabs**
   - 作者：Simon Willison
   - 来源：simonwillison.net
   - 原文：https://simonwillison.net/2026/Jun/29/safari-tab-count/#atom-everything
   - InkWell：https://inkwell.coze.com/article/art_8ghm04
   - 发布：2026-06-30 02:36
   - 摘要：Simon Willison 的"史上最小 TIL"：用一行 AppleScript `osascript -e 'tell application "Safari" to count tabs of every window'` 即可统计 Safari 当前所有窗口的标签页总数。他自己跑出 370 个，配图自嘲"tab-shame"，提醒读者关一关 tab。

---

## Tech Culture（1 篇）

3. **Pluralistic: Gemini is better than search because Google enshittified search (29 Jun 2026)**
   - 作者：Cory Doctorow
   - 来源：pluralistic.net
   - 原文：https://pluralistic.net/2026/06/29/arsonist-firefighters/
   - InkWell：https://inkwell.coze.com/article/art_jio344
   - 发布：2026-06-30 00:34
   - 摘要：Cory Doctorow 抛出"放火的人来当消防员"论：Gemini 之所以比 Google 搜索好用，恰恰是因为 Google 自己把搜索结果"enshittified"（变屎化）——SEO 垃圾、AI 内容农场、广告挤占——逼用户改用大模型问答。文中借此回顾 Microsoft 反垄断翻案、Olympic 盈利谎言、Intuit 截胡儿童税收抵免等案例，把矛头指向"反垄断已成政治反重力"的现实。

---

## Essays（1 篇）

4. **Who you gonna believe: Grok or the docs?**
   - 作者：John D. Cook
   - 来源：johndcook.com
   - 原文：https://www.johndcook.com/blog/2026/06/29/who-you-gonna-believe/
   - InkWell：https://inkwell.coze.com/article/art_tiu6cs
   - 发布：2026-06-29 20:12
   - 摘要：bc 计算器的 Bessel 函数 `j(...)` 参数顺序到底是 `j(n,x)` 还是 `j(x,n)`？Grok 说前者，POSIX man page 说后者。作者用 `j(1,0)=0`、`j(1.2, 3.4)==j(1, 3.4)` 两组实测确认 Grok 正确、man page 错误（第一个参数被 truncate 即为整数阶 n）。结论是别盲信 LLM，也别盲信文档——跑两个测试用例胜过任何权威。

---

## Indie（2 篇）

5. **Unbundling the standard library**
   - 作者：Andrew Nesbitt
   - 来源：nesbitt.io
   - 原文：https://nesbitt.io/2026/06/29/unbundling-the-standard-library.html
   - InkWell：https://inkwell.coze.com/article/art_qdjk0t
   - 发布：2026-06-29 18:00
   - 摘要：GHC 10.2 把内建标识符放进真实模块 `GHC.Essentials`（位于 base 中），导致原本"零依赖"的 Haskell 包 composition 自动隐式依赖 base，"无依赖神话"破灭。作者借此考察各生态系统中"编译器 vs 标准库"的边界划法，并由 Ruby Bug #20516（Ruby 3.3.2 仍捆绑漏洞版 rexml 3.2.6）引出：当标准库被"解绑"后，CVE 与漏洞通告的范围与形态也随之改变。

6. **I turned my prologue into a short video**
   - 作者：Ibrahim Diallo
   - 来源：idiallo.com
   - 原文：https://idiallo.com/byte-size/my-prologue-to-short-video
   - InkWell：https://inkwell.coze.com/article/art_ooj9n
   - 发布：2026-06-29 10:12
   - 摘要：Idiallo 坦言"写完整本书太难"，于是把自己书稿的序章改编成一段短视频先放出来。属于个人创作侧的"先 MVP 再迭代"实验，邀请读者观看反馈。
