# Inkwell 完整文章列表
**更新时间**: 2026-06-16 | **来源**: inkwell.coze.site

---

## AI & ML

**Quoting Julia Evans**
▸ Simon Willison 引用 Julia Evans 的写作心得："Instead, I picture a specific person and I just write for them. Often this person is 'me, but 3 years ago' or a good friend." —— 关于写作对象感的经典洞见
🔗 https://simonwillison.net/2026/Jun/15/julia-evans/

**"They screwed us": Personality clashes sent Anthropic's models offline**
▸ Axios 深度报道：Anthropic Fable/Mythos 被美国政府以国家安全为由禁止出口的幕后故事。Logan Graham（Anthropic 前沿红队负责人）、Dave Orr（安全负责人）及 Nicholas Carlini 正与商务部谈判。根本问题：完美防越狱可能根本不存在
🔗 https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/

**Why AI hasn't replaced software engineers, and won't**
▸ Arvind Narayanan 和 Sayash Kapoor 论文：AI 替代软件工程师的叙事被数据证伪。真正瓶颈在于：(1)决定做什么 (2)验证和问责 (3)对代码库/业务/环境的深度人类理解。纽约 WARN 法案首年 AI 相关裁员申报为 0
🔗 https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/

---

## Essays

**Writing Prolog with ChatGPT**
▸ John Cook 尝试用 ChatGPT 编写 SWI Prolog 解决 4x4 棋盘摆棋问题。ChatGPT 一次性生成完整代码，找到全部 16 种解法。Prolog 语法老旧但 LLM 掌握良好，逻辑编程 + AI 帮助可能是个舒适的工作流
🔗 https://www.johndcook.com/blog/2026/06/15/writing-prolog-with-chatgpt/

**Quaternion Rotations, Claude, and Lean**
▸ John Cook 用 Claude Sonnet 4.6 验证四元数与旋转矩阵的数学定理。Claude 检测到博客 Python 代码与 LaTeX 公式中的下标错误（实际是 alt 文本的笔误），选择相信 Python 为权威实现。Lean 4 证明代码经过 4 轮迭代最终通过
🔗 https://www.johndcook.com/blog/2026/06/15/quaternions-claude-lean/

**Pluralistic: AI and amateurism (15 Jun 2026)**
▸ Cory Doctorow 论 AI 与业余主义：Vibe coding 是 Hypercard/Scratch 系谱的延伸，让非程序员能直接控制工具。真正危险是" vibe coded 原型替代生产代码"的叙事——AI 泡沫已烧掉 1.4 万亿美元，年收入仅数百亿。真正重要的是个人/本地工具的异质性
🔗 https://pluralistic.net/2026/06/15/vernacular/

---

## Tech Culture

**AI's Brokenomics**
▸ （内容获取失败）
🔗 https://www.wheresyoured.at/brokenomics/

**[RSS Club] What happens to old posts?**
▸ （内容获取失败）
🔗 https://shkspr.mobi/blog/2026/06/rss-club-what-happens-to-old-posts/

---

## Systems

**EU & Civil Society need to progress on Digital Autonomy**
▸ Bert Hubert 论欧洲数字主权的困境：公民社会与智库讨论流于空谈，真正需要的是采购部门、IT 部门、供应商和议会议员的实际参与。核心障碍：政府外包 IT 导致执行力缺失、四大会计师事务所和集成商完全绑定美国平台、员工25年微软习惯难以改变
🔗 https://berthub.eu/articles/posts/eu-civil-society-need-progress-digital-autonomy/

---

## Indie

**JAX: commitment issues**
▸ Giles Thomas 揭示 JAX 默认 device 上下文管理器的陷阱：用 default_device 创建数组不会"提交"到设备，JAX 会自由移动数据。使用 device_put 显式提交后，数组查找从 5.4s 降至 0.95s，后续查找从 1.2s 降至 0.0002s。教训：如果你想确保数组在特定设备上，用 device_put 钉死它
🔗 https://www.gilesthomas.com/2026/06/jax-commitment-issues

**AI GPUs probably live longer than three years**
▸ Sean Goedecke 质疑"GPU 只活三年"的流行说法。来源是匿名消息源的匿名采访，而 Google 公开称其 8 年旧 TPU 100% 利用率运行，AWS CEO 称从未退役 A100 服务器。泰坦超级计算机数据显示 3 年后 95% GPU 存活，6 年后底部节点仍超 90%
🔗 https://seangoedecke.com/ai-gpus-live-longer-than-three-years/

**Things that made me think: Open Source trust relationships, knowledge without provenance, and theory building**
▸ AI Agent 可在数小时建立可信 GitHub Profile，导致开源信任系统崩塌；引用不等于溯源，训练集上下文才是理解答案的关键；Peter Naur 的"编程即理论构建"——代码是理论的表现形式而非理论本身，组织变更会摧毁正在构建的理论
🔗 https://tomrenner.com/posts/ttmmt-4/

**A brief history of KV cache compression developments**
▸ 自 2017 年来 KV cache 内存效率提升约 100 倍（同期 GPU 内存仅增 18 倍）。关键里程碑：MQA(2019)→GQA(2023)→MLA(2024,DeepSeek)→线性注意力混合(2025)。4K→128K→1M 上下文窗口主要靠数学而非硬件。意义：效率提升被用于更长上下文而非更便宜
🔗 https://martinalderson.com/posts/a-brief-history-of-kv-cache-compression-developments/

**Meetups in July and August 2026: call for organizers**
▸ Henrik Karlsson 发起 Escaping Flatland 读者线下聚会招募。哥本哈根和 NYC 已举办首场。需要更多城市组织者，deadline 6月23日，地点建议公园（人多）或咖啡馆。最低要求：能定时间地点并出现
🔗 https://www.henrikkarlsson.xyz/p/meetups-in-july-and-august-2026-call

---

## Security

**Weekly Update 508**
▸ Troy Hunt 周报：澳大利亚寻找合适轻触开关的困难——必须是无状态的（上下拨动式而非按钮）、外观要好看，但澳洲标准和美国不同难以进口
🔗 https://www.troyhunt.com/weekly-update-508/

---

## 📊 统计概览
- 本期总数: 15 条
- 覆盖分类: 6 个
- 原文链接完整率: 93%
