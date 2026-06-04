# InkWell 完整归档
**日期**: 2026年6月5日
**文章总数**: 31

---

## AI & ML

**🔬Scaling Past Informal AI - Carina Hong, Axiom Math**
▸ Axiom通过"验证AI"方法在Putnam数学竞赛取得12/12满分(超DeepSeek 103/120)，核心观点是形式化验证对AGI的重要性。99% ProofGen benchmark准确率(187/189)，提出"Verified AI"概念——用Lean证明系统验证数学推理，实现"复合智能"而非仅"修复缺陷"。
🔗 https://www.latent.space/p/scaling-past-informal-ai

**⚡️Satya Nadella: No Priors x Latent Space Crossover Special at Microsoft Build**
▸ Satya阐述Microsoft定位为"前沿智能平台"，MAI模型采用"从零攀登"策略而非蒸馏。强调企业需要"私有评估"和"Token IP"作为护城河。AI ROI面临挑战：部分企业开始限制AI编码工具支出(如Uber限制$1500/月/人)。
🔗 https://www.latent.space/p/satya-nadella-no-priors

**[AINews] Reve 2 and Ideogram 4: Layouts in Imagegen**
▸ GPT-Image-2在图像合成领域保持领先，Reve和Ideogram 4.0同天发布并强调布局标签和代码生成。Gemma 4 12B采用无编码器设计(图像直接投影到文本token空间)，可在16GB VRAM设备运行。开源模型加速本地AI部署。
🔗 https://www.latent.space/p/ainews-reve-2-ideogram-4

**Microsoft Copilot Cowork Exfiltrates Files**
▸ Microsoft Copilot Cowork存在严重安全漏洞：AI代理发送的邮件中的外部图片可触发网络请求，导致数据泄露。攻击者可通过钓鱼邮件利用OneDrive预认证下载链接窃取文件。prompt注入攻击是主要威胁向量。
🔗 https://simonwillison.net/2026/May/26/microsoft-copilot-cowork/

**The mysterious Hy3 LLM is topping OpenRouter Model Rankings**
▸ 神秘Hy3 LLM在OpenRouter模型排行榜上大幅领先，引发社区热议。模型身份和来源尚不明确，但其性能表现引起广泛关注。
🔗 https://openrouter.ai/models/hy3

**The pressure**
▸ AI领域竞争加剧，文章探讨当前AI发展面临的压力和挑战。
🔗 https://simonwillison.net/2026/May/27/the-pressure/

**Hackers Simply Asked Meta AI to Give Them Access to High-Profile Instagram Accounts. It Worked**
▸ 黑客通过简单prompt成功绕过Meta AI安全限制，获取高知名度Instagram账户访问权限。暴露了AI系统在认证和访问控制方面的严重缺陷。
🔗 https://simonwillison.net/2026/May/23/meta-ai-instagram/

**Why Video Agent models are next — Ethan He, xAI Grok Imagine**
▸ 视频Agent模型将成为下一重点方向。xAI的Grok Imagine团队认为视频理解和生成能力是通向更通用AI的关键一步。
🔗 https://www.latent.space/p/video-agent-models

**How we contain Claude across products**
▸ Anthropic发布详细文档，阐述如何在多个产品中沙箱化Claude模型。文档透明度受到社区好评，详细介绍了安全隔离机制的实现细节。
🔗 https://simonwillison.net/2026/May/30/how-we-contain-claude/

**Quoting Natalie Lung**
▸ Anthropic定义"运行率收入"两部分：最近28天消费销售额×13 + 月订阅×12。这一指标衡量方式引发讨论。
🔗 https://simonwillison.net/2026/Jun/2/quoting-natalie-lung/

**Uber Caps Usage of AI Tools Like Claude Code to Manage Costs**
▸ Uber开始限制员工使用AI编码工具(如Claude Code)的支出上限，约为$1500/月/人。这反映了企业AI部署面临成本控制挑战。
🔗 https://simonwillison.net/2026/Jun/3/uber-caps-usage/

---

## Programming

**IPv6 zones in URLs are a mistake**
▸ RFC 9884试图解决IPv6地址中zone ID的URL表示问题。URL中的百分号编码导致与标准URL编码冲突，Go的net/url库无法正确处理"[fe80::4%eth0]"格式。现有解决方案需要双重编码"%25"，但兼容性仍存在问题。
🔗 https://xeiaso.net/blog/ipv6-zones-urls

**Using Safetensors with Flax**
▸ 探索在Flax中使用Safetensors格式的方法，Safetensors是Hugging Face推出的安全张量序列化格式。
🔗 https://flax.readthedocs.io/

**Reality: The Final Eval — Lukas Petersson and Axel Backlund of Andon Labs**
▸ Andon Labs关于AI评估的深度讨论，探索如何定义和衡量AI系统的"现实"能力边界。
🔗 https://www.andorl.com/

**The Latin of Linux**
▸ 探讨Linux系统内部原理和技术细节，类比拉丁语在现代语言中的角色。
🔗 https://www.kernel.org/

**Integrating smooth periodic functions**
▸ 数学研究：如何积分平滑周期函数，探讨傅里叶分析和相关数学技术。
🔗 https://johndcook.com/

**Quoting Emanuel Maiberg, 404 Media**
▸ 404 Media关于AI和数据隐私的报道，探讨科技公司如何处理用户数据。
🔗 https://www.404media.co/

**How Long Does It Take to Plan a Bridge?**
▸ 探讨桥梁规划的时间跨度和复杂性，从工程角度分析基础设施建设。
🔗 https://en.wikipedia.org/wiki/Bridge_engineering

**Partitions over permutations**
▸ 算法研究：分割与排列的数学关系，探讨组合数学在计算机科学中的应用。
🔗 https://en.wikipedia.org/wiki/Combinatorics

**Book Review: Accessible Communications by Lisa Riemers and Matisse Hamel-Nelis**
▸ 关于无障碍传播的书籍评论，探讨如何让信息传达更具包容性。
🔗 https://www.elsevier.com/

**A survey of inlining heuristics**
▸ 编译器优化研究：内联启发式算法的综述，探讨代码内联优化策略。
🔗 https://bernsteinbear.com/blog/inlining-survey/

**Logic for Programmers extra credits**
▸ 为程序员提供的逻辑学补充材料，探讨形式逻辑在编程中的应用。
🔗 https://www.buttondown.com/hillelwayne/

---

## Systems

**Rotation revisited: A shocking discovery about gcc's unidirectional rotation algorithm**
▸ gcc libstdc++的旋转算法与前向迭代器算法惊人相似。Raymond Chen揭示了两种算法实现在深层逻辑上的等价性，仅在操作方向上有所区别。这一发现展示了编译器优化背后的数学美感。
🔗 https://devblogs.microsoft.com/oldnewthing/

---

## Tech Culture

**Pluralistic: Delusion as a service (04 Jun 2026)**
▸ Cory Doctorow探讨"服务型妄想"现象，批判科技平台如何利用用户心理弱点。
🔗 https://pluralistic.net/2026/06/04/storytelling/

**Anti-AI nostalgia and the cult of the past**
▸ 反思对AI的怀旧情结和"过去崇拜"现象，探讨技术进步的辩证关系。
🔗 https://www.eff.org/

**London Data Store Relaunch**
▸ 伦敦数据存储服务重新上线，探讨城市数据基础设施。
🔗 https://data.london.gov.uk/

**How To Read More**
▸ 实用指南：如何在信息爆炸时代培养阅读习惯。
🔗 https://www.goodreads.com/

**The web is changing, and we are not going back**
▸ 探讨Web技术演进和去中心化趋势。
🔗 https://www.w3.org/

---

## Indie

**Is datacentre sovereignty really that important?**
▸ 英国数据中心主权辩论：作者认为延迟、税收、就业等优势被夸大。数据中心价值主要来自运行其上的模型，而非物理位置。即使在英国建有数据中心，也无法强迫私人运营商给予优先访问权。真正的杠杆是合同锁定算力，而非地理位置。
🔗 https://martinalderson.com/posts/is-datacentre-sovereignty-really-that-important/

**Now that your newsletter is AI-generated, I've Unsubscribed**
▸ 作者订阅了20年的Newsletter转为AI生成后选择退订。核心观点：人类声音背后的真实经历无可替代，AI生成内容缺乏"呼吸感"和"漫游感"。订阅者珍视的是作者本人的思考和观点，而非模板化的技术内容。
🔗 https://idiallo.com/blog/ai-newsletter-unsubscribe

**gittuf - a signed log for git refs**
▸ gittuf项目解决git refs未被签名的问题。传统branch protection由代码托管平台管理，攻击者可利用漏洞修改refs。gittuf通过哈希链记录每个ref更新，使用TUF委托模型实现多人签名验证，可检测恶意服务器回滚ref。
🔗 https://nesbitt.io/2026/06/04/skills-registry-threat-models.html

**Skills Registry Threat Models**
▸ 探讨技能注册表的威胁模型和安全考量。
🔗 https://nesbitt.io/

**People are too big to fit inside our heads**
▸ 知识管理：人类认知局限与外部知识系统的关系。
🔗 https://henrikkarlsson.substack.com/

---

## Essays

**Naively summing an alternating series**
▸ 数学科普：直观理解交错级数求和，探讨(-1)^n级数的收敛性问题。
🔗 https://johndcook.com/blog/2026/Jun/01/naive-alternating-series/

**An Ode to the Exacting Pedantry of Computers**
▸ 颂扬计算机的精确性和"吹毛求疵"，探讨人类与机器思维的差异。
🔗 https://blog.jim-nielsen.com/

---

## Hardware

**Microcode inside the Intel 8087 floating-point chip: register exchange**
▸ Intel 8087协处理器内部微码分析，揭示1980年代浮点芯片设计细节。
🔗 https://www.righto.com/2026/05/microcode-inside-intel-8087-floating.html
