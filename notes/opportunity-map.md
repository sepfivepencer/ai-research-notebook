# 机会地图：第一轮扫描

检索截至 2026-10-29，覆盖 23 个分方向。以下是选择性机会扫描，资料核验范围为元数据、摘要和公开项目；未开展全文精读或独立复现。每个切口均待确认，不代表已发现新颖学术空白。

结构化记录 `data/notebook.json` 目前只收录六篇核心文献，不覆盖本页全部引文；工具检查也不验证本页的文字或链接。

# 附录 A：AI（9 个分方向）

检索截止：2026-10-29。优先窗口：2024-10-29—2026-10-29，按正式会议年份纳入代表作，同时明确首次预印本日期。已真实检索会议论文集、arXiv 和作者项目；这里只完成元数据与摘要层面的扫描，不是第二阶段精读。没有运行实验，没有验证候选题的新颖性或效果。

已知用户条件更新：M1 Air **8GB**、零新增预算、每周可投入 **10 小时以上**、技术基础入门，目标中文技术长文并体验完整科研。可行性指“值得在后续阶段试运行”，不是已经在该设备跑通。应优先考虑量化的小模型、有限上下文和小批次；模型参数及上下文上限由真实内存测量决定。

标签含义：【已验证】只表示链接、题名、作者、会议等已从一手页面核验，或原文确实报告该事实；作者实验结论不等于我们独立复现。【有依据的推断】表示据已有工作判断痛点或资源可行性。【待验证】表示拟检验的机会，绝不表示已经发现新颖缺口。

## 机会地图

| 方向 | 现状与痛点 | 近两年正式会议代表作（完整书目见后） | 可检验的“颠覆点” | M1 Air、零预算可行性 |
|---|---|---|---|---|
| 大模型推理 | 研究已从一次输出扩展到测试时搜索、验证与额外计算；额外 token 如何有效换取正确率受任务与验证器影响。【有依据的推断；AI1】 | AI1，ICML 2025 | “多想更好”是否在固定真实运行时间和正确性目标下成立？将可验证的小任务中长推理与短推理加工具比较。【待验证】 | 可选小模型与程序判分；不复现 32B 训练。具体模型与上下文上限须在已知 8 GB 内存条件下通过试运行确定。【有依据的推断】 |
| Agent | 工具、领域规则、用户交互和状态改变共同决定可靠性；一次成功率不足以说明重复运行可靠性。【有依据的推断；AI2】 | AI2，ICLR 2025 | “任务结果正确”是否足以代表过程正确？可在沙盒中测成功结果之外的额外状态修改，并研究确定性执行检查。【待验证】 | 自建小型文件/SQLite 沙盒，不用真实账号和付费 API；完整 τ-bench 的用户模拟与强模型成本不适合零预算直接全跑。【有依据的推断】 |
| 长上下文与记忆 | 记忆评估已覆盖更新、时序、拒答，2026 年进一步覆盖环境经验、依赖更新、删除；简单“长上下文不等于记忆”已不是空白。【已验证；AI3、AI9、AI10】 | AI3，ICLR 2025；AI11 的 ICLR 2026 身份尚需会议页面最终核验，暂不计正式代表作 | 可比较原文、摘要、BM25、显式事件表在同一证据预算下的性能；“用数据库做更新/删除”已有相邻工作，必须进一步找窄缺口。【待验证】 | 文本生成器、SQLite、BM25 可本地；长至百万 token 或强模型判分不可作为默认方案。【有依据的推断】 |
| 多模态 | 视觉语言测试可能被纯文本线索、选项猜测和 OCR 绕开；MMMU-Pro 已针对这些捷径改进评测。【已验证；AI4】 | AI4，ACL 2025 | 某类“视觉理解”成功究竟依赖图像关系，还是依赖题面线索？使用成对反事实图表和可程序验证答案测失效条件。【待验证；新颖性需二阶段查重】 | 自生成简单图表和少量小型 VLM 推理可能可行，须核实内存；全面重测前沿 VLM 不适合。【有依据的推断】 |
| AI 编程助手 | Agent 的文件浏览、编辑、运行接口能改变完成情况；单看模型参数忽略了接口作用。【已验证；AI5】 | AI5，NeurIPS 2024（首次预印本 2024-05，正式会议在窗口内） | 在同一模型和预算下，测试通过是否掩盖未覆盖的回归？可用独立性质检查、变形测试与变异程序检验“测试绿灯”的证据强度。【待验证；测试不足是已知问题，不能直接自称新发现】 | 小 Python 项目和合成可验证任务适合本机；不要从完整 SWE-bench 容器集群起步。【有依据的推断】 |
| AI Infra：推理优化 | 高性能注意力内核需兼顾 KV cache 布局与动态请求；2026 年已出现 Agent 生成内核到验证部署的闭环。【已验证；AI6、AI7】 | AI6，MLSys 2025；AI7，MLSys 2026 | GPU token/s 排名不能自动外推到 M1：统一内存、长输入和持续运行条件下，模型/量化配置的“每个正确答案所需时间”排名是否改变？【待验证】 | 可做本机测量，但 CUDA 内核本体和数据中心吞吐论文无法在 M1 上等价复现；不能以单台 M1 外推整个硬件市场。【有依据的推断】 |
| AI Infra：分布式训练 | 千卡同步训练中的拖慢节点可源于多类因素，what-if 追踪可分析影响。【已验证；AI8】 | AI8，OSDI 2025 | 把训练停顿归因于硬件故障是否过度简化？可研究公开 trace 或小型仿真中的归因偏差，但仿真结果需要外部验证。【待验证】 | 无集群与真实 trace 授权，不优先；本地模拟只能验证模型内结论。【有依据的推断】 |
| 具身智能 | VLA 把视觉语言预训练与动作学习连接起来；跨任务泛化和真实环境稳健性仍需大量数据与实体验证。【有依据的推断；AI12】 | AI12，RSS 2025 | 语言遵循与真实控制是否可解耦测量？在可控模拟中区分感知、规划和执行失效。【待验证】 | 无机器人，VLA 训练与真实控制不优先；只能做轻量模拟或公开轨迹分析，结论范围受限。【有依据的推断】 |
| AI 安全与对齐 | AgentDojo 同时测试任务效用和攻击；2026 年已有人审计“小模型低攻击成功率其实只是忽略/不会执行”的混淆。【已验证；AI13、AI15、AI16】 | AI13，NeurIPS 2024；AI14 为 2025 预印本，不冒充顶会论文 | “攻击未成功”是否意味着完成了安全任务？这一大问题已有直接工作，应在授权边界、状态可审计性或更窄失效上找可复现实验。【待验证】 | 在合成沙盒做安全与效用联合评价可行；强模型全量攻击成本不适合。【有依据的推断】 |

## 核验后的书目

- **AI1** Amrith Setlur, Nived Rajaraman, Sergey Levine, Aviral Kumar. **Scaling Test-Time Compute Without Verification or RL is Suboptimal.** ICML 2025，PMLR 267:54058–54094；arXiv:**2502.12118**。正式论文集核验：[PMLR](https://proceedings.mlr.press/v267/setlur25a.html)；[arXiv](https://arxiv.org/abs/2502.12118)。理论结论有特定分布条件，不能泛化成“所有任务验证都更优”。【已验证元数据】
- **AI2** Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan. **τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.** ICLR 2025；arXiv:**2406.12045**（首发 2024-06-17）。[ICLR 正式论文](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf)；[arXiv](https://arxiv.org/abs/2406.12045)。已核对首页“Published as a conference paper at ICLR 2025”；论文提出 pass^k 衡量重复可靠性。【已验证元数据】
- **AI3** Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu. **LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.** ICLR 2025；arXiv:**2410.10813**（首发 2024-10-14，正式会议在窗口内）。[正式论文集](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html)；[arXiv](https://arxiv.org/abs/2410.10813)；[作者代码](https://github.com/xiaowu0162/LongMemEval)。【已验证元数据】
- **AI4** Xiang Yue et al. **MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark.** ACL 2025 长文，15134–15186；arXiv:**2409.02813**（首发 2024-09，会议在窗口内）。[ACL Anthology](https://aclanthology.org/2025.acl-long.736/)；[arXiv](https://arxiv.org/abs/2409.02813)。注意是 ACL 2025，不是 CVPR 2025。【已验证元数据】
- **AI5** John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press. **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering.** NeurIPS 2024 Main Conference；arXiv:**2405.15793**。首次预印本早于窗口，正式会议在 2024-12。[正式论文集](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)；[arXiv](https://arxiv.org/abs/2405.15793)。【已验证元数据】
- **AI6** Zihao Ye et al. **FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving.** MLSys 2025；arXiv:**2501.01005**。[正式论文集](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)；[arXiv](https://arxiv.org/abs/2501.01005)。【已验证元数据】
- **AI7** Shanli Xing et al. **FlashInfer-Bench: Building the Virtuous Cycle for AI-driven LLM Systems.** MLSys 2026；arXiv:**2601.00227**。[正式论文集](https://proceedings.mlsys.org/paper_files/paper/2026/hash/37e44c4b5321605735be9761f9b758fc-Abstract-Conference.html)；[arXiv](https://arxiv.org/abs/2601.00227)。【已验证元数据】
- **AI8** Jinkun Lin et al. **Understanding Stragglers in Large Model Training Using What-if Analysis.** OSDI 2025，483–498；arXiv 号【未核实，非必要，不猜填】。[USENIX 正式页面及 BibTeX](https://www.usenix.org/conference/osdi25/presentation/lin-jinkun)。【已验证元数据】
- **AI9** Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang. **LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues.** arXiv:**2605.12493**，2026-05-12；页面标 Work in Progress，未核验正式会议。[arXiv](https://arxiv.org/abs/2605.12493)。【已验证预印本身份】
- **AI10** Seokwon Jung, Alexander Rubinstein, Arnas Uselis, Sangdoo Yun, Seong Joon Oh. **MEME: Multi-entity & Evolving Memory Evaluation.** arXiv:**2605.12477**，2026-05-12；会议身份【待核实】，不能按网页转述当 NeurIPS 主会已发表。[arXiv](https://arxiv.org/abs/2605.12477)；[作者项目](https://seokwonjung-jay.github.io/meme-eval/)。【已验证预印本与任务范围】
- **AI11** Yuanzhe Hu, Yu Wang, Julian McAuley. **Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions.** arXiv:**2507.05257**，2025 首发、2026 修订；项目及作者评论材料称 ICLR 2026，但本扫描未取得正式会议论文集页面，故会议字段【待核实】。[arXiv](https://arxiv.org/abs/2507.05257)；[作者代码](https://github.com/HUST-AI-HYZ/MemoryAgentBench)。【已验证预印本元数据】
- **AI12** Kevin Black et al. **π₀: A Vision-Language-Action Flow Model for General Robot Control.** RSS 2025；arXiv:**2410.24164**（2024-10-31 首发）。[RSS 正式论文](https://www.roboticsproceedings.org/rss21/p010.pdf)；[arXiv](https://arxiv.org/abs/2410.24164)；[作者开源公告](https://www.pi.website/blog/openpi)。【已验证元数据】
- **AI13** Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramèr. **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.** NeurIPS 2024 Datasets and Benchmarks；arXiv:**2406.13352**。[正式论文集](https://proceedings.nips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)；[arXiv](https://arxiv.org/abs/2406.13352)。【已验证元数据】
- **AI14** Edoardo Debenedetti et al. **Defeating Prompt Injections by Design.** arXiv:**2503.18813**，2025-03 首发、2025-06 修订；会议身份未核验。[arXiv](https://arxiv.org/abs/2503.18813)。CaMeL 已研究控制流/数据流分离与权限检查，不能把这套总思路声称为我们的新发明。【已验证预印本与摘要所述方法】
- **AI15** Farhan Zarif et al. **Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents.** arXiv:**2610.23254**，2026-10-16；未核验正式会议。[arXiv](https://arxiv.org/abs/2610.23254)。【已验证预印本；结论未独立复现】
- **AI16** Youting Wang, Xiao Han, Dingyan Shang, Yuan Tang, Bowen Liu. **Safety, or Just Capability? A Validity Audit of Agent-Safety Benchmarks.** arXiv:**2607.28685**，2026-07-30；未核验正式会议。[arXiv](https://arxiv.org/abs/2607.28685)。【已验证预印本；结论未独立复现】
- **AI17** Egor Pakhomov, Erik Nijkamp. **Bookkeeping, Composition, or Unreachable Gold? Reading MemoryAgentBench's Conflict-Resolution Scores Against a Frozen Last-Write Resolver.** arXiv:**2610.09193**，2026-10-06；arXiv 作者备注称 NeurIPS 2026 IAB Workshop（non-archival），这不是 NeurIPS 主会。[arXiv](https://arxiv.org/abs/2610.09193)。【已验证预印本；workshop 接收为作者声明】



---

# 附录 B：全栈与系统（8 个分方向）

检索日：2026-10-29；优先窗口：2024-10-29—2026-10-29。以下是选择性机会扫描，依据会议官方摘要、官方 BibTeX、作者论文和项目一手资料；不等同于第二阶段精读，也没有验证任何新选题的新颖性或实际收益。

置信标签中，【已验证】表示论文存在、元数据和所引作者报告已核对，不表示我们复现了作者实验；【有依据的推断】是据文献提炼的方向判断；【待验证】是拟检验假设。arXiv 标“未核实”表示尚未确认对应条目，不等于证明不存在。

| 方向 | 现状与痛点 | 窗口内顶会代表作 | 可被挑战的假设 / 低成本切口 | 对入门者与 M1 Air 的判断 |
|---|---|---|---|---|
| 前端框架与渲染 | 增量更新、状态同步、浏览器加载是不同层次的问题；交互系统中重新完整执行会拖慢反馈，历史页面保存齐全也可能回放失真。【有依据的推断】 | Ziegler et al., PLDI 2025 [S1]；Zhu et al., NSDI 2026 [S2]。两篇分别是直接操纵编程与 Web 归档的相邻证据，并非 React/Vue 框架排行榜研究。 | “截图相同 / DOM 相似即可证明页面行为等价”可被检验。【待验证】用本地网页的事件、状态变更、缓存和异步回调建立行为轨迹，检验 UI 测试是否漏掉语义差异；与 Web Agent 评测可交叉。 | 浏览器与本地页面容易获得；做 Chromium 内核改造则难。建议优先现成浏览器的可控测试，不能据此宣称已超越 FidEx。 |
| 后端架构 | 微服务的依赖和共享资源使单服务过载控制难以保证整个请求图的尾延迟。【已验证：S3 的研究问题】 | Xing et al., NSDI 2025, Rajomon [S3]。 | “每个服务各自限流就能保障端到端 SLO”是可检验假设。【待验证】本机多进程模拟扇出、重试、请求类型混合，比较独立限流和沿调用链传播的预算。 | 可做机制演示和请求回放；原文大规模多核环境不能在 M1 上等规模复现。新颖性门槛高，作为学习副题更适合。 |
| 云原生与 Serverless | 冷启动不仅是加载镜像或进程初始化，控制路径、并发竞争和用户代码初始化也影响端到端体验；计费与实际资源消耗之间亦有缺口。【已验证：S4/S5】 | Chai et al., OSDI 2025 [S4]；Cao et al., NSDI 2025, Leopard [S5]。 | “缩短单个组件启动时间就能稳定缩短应用冷启动”可能在并发下不成立。【待验证】优先使用公开请求轨迹做排队与缓存回放，而不是支付云平台费用。 | 公开数据与模拟适合零预算，但模拟结论必须明确依赖模型，不能冒充真实云部署结果；不列为首选。 |
| 数据库 | 面向内存的连接算法在数据或中间结果超内存后可能出现性能陡降；已有研究通过自适应外存哈希连接、压缩与动态内存分配缓解。【已验证：S6】 | Kuiper et al., PVLDB 18(8) / VLDB 2025 [S6]。 | “平均查询延迟足以衡量小内存数据库表现”可挑战。【待验证】固定内存限额，在并发、数据偏斜和字符串键下寻找延迟断崖，再评价调度 / 自适应策略。 | DuckDB 可本地开展，实验成本低；已有外存内存管理研究很成熟，单纯展示溢写变慢不足以构成新贡献。 |
| DevOps 与可观测性 | 收集更多指标会争抢计算、网络和存储资源，粗粒度采样又可能遗漏瞬时故障；硬件计数器也存在测量和归因不确定性。【已验证：S7/S8】 | Cornacchia et al., NSDI 2026, μView [S7]；Li et al., OSDI 2025, Tintin [S8]。 | “记录得更全就一定诊断得更准”需同时检查观测干扰与故障覆盖率。【待验证】在本地小服务或 Agent 任务中逐步增加日志 / tracing，比较吞吐、P95/P99 和漏诊率。 | 用户态日志 / 指标实验可行；μView 的 IPU、Tintin 的特定硬件计数器机制不能直接迁移到 macOS。可研究软件层问题。 |
| 边缘计算 | 算力离用户更近仍可能有尾延迟和资源竞争；端侧推理还要平衡延迟、功耗与准确率。【已验证：S9/S10】 | Zhang & Kim, NSDI 2026, SMEC [S9]；Tian et al., USENIX ATC 2025, CLONE [S10]。 | “本地运行天然保证低延迟”是可检验的有限命题。【待验证】单机同时运行轻量模型与浏览器负载，观察统一内存压力、后台任务对延迟与质量的影响。 | M1 本身是合适的端侧测量对象；结论只能针对测过的设备与设置。手机、5G、专用加速器和跨硬件普遍性不适合当前资源。 |
| Web 性能 | 高带宽情境下，资源缓存再验证的往返时延仍可能限制页面加载；缓存命中率不能完整反映用户等待。【已验证：S11】 | Hosseini et al., NSDI 2026, CacheCatalyst [S11]。 | “带宽提高 / 缓存命中提高就一定带来等比例页面提速”可检验。【待验证】本地服务器、受控延迟和固定页面资源，分解 revalidation 与 JS/渲染等待。 | 可做轻量实证，指标和因果控制清晰；已有新缓存方案，不宜重复“提前验证”思路并宣称新颖。 |
| Web 安全 | DOM 和 JavaScript 的兼容语义会令无脚本 HTML 通过既有代码产生危险行为；Web 测量工具本身也可能遗漏或误归因事件。【已验证：S12/S13】 | Liu et al., USENIX Security 2025, The DOMino Effect [S12]；Hantke et al., USENIX Security 2025, Web Execution Bundles [S13]。 | “输入不含脚本就安全”“抓到资源即可准确复现执行”都需精确限定。【待验证】只用本地玩具应用和公开样例，测试防护或测量工具在状态 / 事件边界上的遗漏。 | 可本地开展防护与测量实验。对初学者，先建立清晰威胁模型；不能用几个案例声称修复整个 Web 安全问题。 |

## 核对过的一手文献

- **[S1]** Parker Ziegler, Justin Lubin, Sarah E. Chasins. **Fast Direct Manipulation Programming with Patch-Reconciliation Correspondence**. *Proceedings of the ACM on Programming Languages*, 9 (PLDI), Article 175, June 2025. DOI: 10.1145/3729278。arXiv：【未核实】。[作者 PDF](https://jlubin.net/assets/pldi25b.pdf)。作者研究通过对应的程序修改与结果协调避免每次完整求值，属于与 UI 增量更新相关的编程语言研究；不能写成“新的前端框架”。
- **[S2]** Jingyuan Zhu, Huanchen Sun, Harsha V. Madhyastha. **Detecting and Diagnosing Errors in Serving Archived Web Pages**. *NSDI 2026*, pp. 669–684. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/nsdi26/presentation/zhu-jingyuan)。FidEx 比较脚本执行以发现归档改写造成的保真度错误，研究支持“视觉 / 报错比较存在盲区”的切口。
- **[S3]** Jiali Xing et al. **Rajomon: Decentralized and Coordinated Overload Control for Latency-Sensitive Microservices**. *NSDI 2025*, pp. 21–36. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/nsdi25/presentation/xing)。分布式令牌与价格沿调用图传播以协调过载控制。
- **[S4]** Xiaohu Chai et al. **Fork in the Road: Reflections and Optimizations for Cold Start Latency in Production Serverless Systems**. *OSDI 2025*, pp. 199–218. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/osdi25/presentation/chai-xiaohu)。作者基于生产系统讨论端到端冷启动瓶颈；我们的扫描未运行 AFaaS。
- **[S5]** Tingjia Cao, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau, Tyler Caraza-Harter. **Making Serverless Pay-For-Use a Reality with Leopard**. *NSDI 2025*. arXiv：【未核实】。[会议官方议程含作者与摘要](https://www.usenix.org/conference/nsdi25/technical-sessions)。该研究质疑静态线性、只计交互式资源的计费假设；无必要向用户承诺本机可以验证云账单收益。
- **[S6]** Laurens Kuiper, Paul Groß, Peter Boncz, Hannes Mühleisen. **Saving Private Hash Join**. *PVLDB*, 18(8), pp. 2748–2760, 2025（VLDB 2025）。arXiv：【未核实】。[官方 PDF](https://www.vldb.org/pvldb/vol18/p2748-kuiper.pdf)；[DuckDB 项目页](https://duckdb.org/library/saving-private-hash-join-vldb/)。项目页明确这些技术已整合到 DuckDB v1.2.0；研究基线需考虑已实现的机制。
- **[S7]** Alessandro Cornacchia, Theophilus A. Benson, Muhammad Bilal, Marco Canini. **Observability Is Eating Your Cores: Fine-Grained Analysis of Microservice Metrics with IPU-Hosted Sketches**. *NSDI 2026*, pp. 153–174. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/nsdi26/presentation/cornacchia)。μView 在 IPU 上以流式摘要处理细粒度指标；M1 上的软件实验不构成其硬件实现的复现。
- **[S8]** Ao Li, Marion Sudvarg, Zihan Li, Sanjoy Baruah, Chris Gill, Ning Zhang. **Tintin: A Unified Hardware Performance Profiling Infrastructure to Uncover and Manage Uncertainty**. *OSDI 2025*, pp. 575–593. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/osdi25/presentation/li)。其研究明确考虑硬件事件复用误差与事件归因，说明“测量值天然可信”需要检查。
- **[S9]** Xiao Zhang, Daehyeok Kim. **Enabling SLO-Aware 5G Multi-Access Edge Computing with SMEC**. *NSDI 2026*, pp. 1759–1776. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/nsdi26/presentation/zhang-xiao)。论文报告无线接入网和边缘服务器上的争用导致尾延迟；本文未对其百分比或倍数作独立复现。
- **[S10]** Chunlin Tian et al. **CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge**. *USENIX ATC 2025*, pp. 563–585. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/atc25/presentation/tian)。软硬件协同设计，当前设备和预算下不建议以复现全部硬件为主任务。
- **[S11]** Mohammad Hosseini, Sina Darabi, Hannaneh B. Pasandi, Patrick Eugster, Mahmood Choopani. **CacheCatalyst: Enhancing Web Caching for the Latency-Constrained Internet**. *NSDI 2026*, pp. 493–507. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/nsdi26/presentation/hosseini)。研究通过较早的缓存验证减少再验证往返；它已占据“提前验证”的直接方法位置。
- **[S12]** Zhengyu Liu, Theo Lee, Jianjia Yu, Zifeng Kang, Yinzhi Cao. **The DOMino Effect: Detecting and Exploiting DOM Clobbering Gadgets via Concolic Execution with Symbolic DOM**. *USENIX Security 2025*, pp. 8293–8312. arXiv：【未核实】。[会议原页](https://www.usenix.org/conference/usenixsecurity25/presentation/liu-zhengyu)。扫描只引用其 DOM 命名碰撞与约束求解问题，不开展外部目标攻击。
- **[S13]** Florian Hantke, Peter Snyder, Hamed Haddadi, Ben Stock. **Web Execution Bundles: Reproducible, Accurate, and Archivable Web Measurements**. *USENIX Security 2025*, pp. 8235–8253. arXiv:**2501.15911**（2025-01-27 提交，2025-06-04 修订）。[会议原页](https://www.usenix.org/conference/usenixsecurity25/presentation/hantke)；[arXiv 原页](https://arxiv.org/abs/2501.15911)。WebREC 和 .web 格式关注执行行为的准确记录与复用；可作为低成本 Web / Agent 测量方向的相关工作警戒线。



---

# 附录 C：前沿交叉（6 个分方向）
检索日：2026-10-29。目标窗口为 2024-10-29—2026-10-29，以正式发表年份判断会议/期刊覆盖；若预印本首发更早，单独注明。面向入门本科生、M1 MacBook Air（8 GB 内存）、零新增预算、中文技术长文。以下只做机会筛选，未进入精读、复现或新颖性判定。

标签含义：【已验证】指已查到出版方、会议或 arXiv 的对应记录/摘要，并非我们复现了论文结果；【有依据的推断】是基于公开证据的研究判断；【待验证】是候选假设或资源可行性估计。

| 方向 | 现状与痛点 | 可挑战假设/机会 | 对本机的适配 |
|---|---|---|---|
| 量子计算 | 【已验证】Willow 的表面码工作报告了低于阈值的纠错存储，实时解码仍是系统组成部分。它是 Nature 2025 正式论文（预印本首发 2024-08，在滚动窗口外）。[Q1] | 【待验证】“平均逻辑错误率足以描述可用性”是否会掩盖突发相关错误、解码延迟和资源开销？机会在噪声模型和指标审计；这不是声称纠错无效。 | 【有依据的推断】小规模经典噪声模拟可能可做；真实量子硬件贡献和成熟纠错算法研究的前置知识成本高，当前不优先。 |
| 机器人 | 【已验证】π₀ 将预训练视觉语言模型与动作生成结合，发表于 RSS 2025；数据、泛化、鲁棒性被其摘要明确列为障碍。[R1] | 【待验证】“语义指令理解改善会同步改善动作可靠性”是否成立？可区分视觉/语言理解错误、规划错误、控制失败。 | 【有依据的推断】小型模拟环境或公开视频/轨迹分析可能可做；无机器人、无 GPU，不能据纯软件结果宣称真实机械控制泛化。当前优先级低。 |
| 人机交互 HCI | 【已验证】CHI 2025 研究观察科学家如何用 LLM 编程及其验证行为；另一项 CHI 2025 翻译辅助研究报告，保留用户参与可能伴随沟通绩效成本。[H1][H2] | 【待验证】“让用户审核一次即可有效控制 AI 错误”可能忽视审核者知识、任务反馈和认知成本。可研究结构化可检验产物是否比单纯解释更有助于发现错误。 | 【有依据的推断】界面原型、公开交互日志分析适合本机。一个人的自我体验只能做案例研究；涉及其他参与者的结论需另行选择研究设计与合规路径。 |
| 开源生态 | 【已验证】USENIX Security 2025 已系统研究代码 LLM 生成不存在依赖包的现象，因而“发现包幻觉”本身不具新颖性。[O1] | 【待验证】把“包存在”视作“依赖建议正确”可能漏掉真实包的错误版本、错误 API、同名导入与生态迁移。可研究依赖建议的可执行证据，避免仅统计幻觉数量。 | 【有依据的推断】静态分析、隔离环境中验证公开代码样例、包元数据和 API 签名检查都适合本机；无需购买模型 API。最适合转向 AI 编程可靠性。 |
| 去中心化系统 | 【已验证】NSDI 2025 的 Ladder 探索结构化 DAG 区块链；公开摘要指出并行块排序、确认复杂度和攻击韧性相互牵制。[D1] | 【待验证】“单一吞吐/平均延迟即可代表协议优势”可能忽视负载偏斜、故障模式、公平性和尾部延迟。可研究指标结论对工作负载的敏感性。 | 【有依据的推断】小型事件模拟可做，M1 单机不能重现真实广域网规模。对于当前 AI 主兴趣，学习成本较高，暂不作为首选。 |
| 芯片与存算一体 | 【已验证】Nature 2025 的异构存算芯片结合 memristor/SRAM/数字单元与混合精度，反映精度、存储、能耗及唤醒延迟的联合权衡。[C1] | 【待验证】“算子峰值能效提升能直接推导应用端收益”是否在模型加载、精度修正、数据搬运等成本加入后仍成立？可做公开系统数据的成本建模。 | 【有依据的推断】模型计算量和存储成本估计适合本机；芯片能耗、流片和器件噪声实测需要硬件。公开模拟无法冒充芯片实验。 |

## 已核实的代表作

- **[Q1] Google Quantum AI and Collaborators.** *Quantum error correction below the surface code threshold.* **Nature 638, 920–926 (2025)**，在线发表 2024-12-09；arXiv:**2408.13687**（2024-08-24 首发，首发早于滚动窗口）。[出版方](https://www.nature.com/articles/s41586-024-08449-y)；[arXiv](https://arxiv.org/abs/2408.13687)。作者署名为合作组，应保留该署名，不杜撰“第一作者”。
- **[R1] Kevin Black et al.** *π₀: A Vision-Language-Action Flow Model for General Robot Control.* **Robotics: Science and Systems, 2025**，DOI **10.15607/RSS.2025.XXI.010**；arXiv:**2410.24164**（2024-10-31 首发，落在窗口内）。[会议正式页](https://roboticsproceedings.org/rss21/p010.html)；[arXiv](https://arxiv.org/abs/2410.24164)。
- **[H1] Gabrielle O’Brien.** *How Scientists Use Large Language Models to Program.* **CHI 2025**；arXiv:**2502.17348**。[arXiv](https://arxiv.org/abs/2502.17348)。
- **[H2] Yimin Xiao et al.** *Sustaining Human Agency, Attending to Its Cost: An Investigation into Generative AI Design for Non-Native Speakers’ Language Use.* **CHI 2025**；arXiv:**2503.07970**。[作者所在大学正式研究记录](https://www.ischool.berkeley.edu/research/publications/2025/sustaining-human-agency-attending-its-cost-investigation-generative-ai)；[作者版 PDF](https://www.terpconnect.umd.edu/~gegao/paper/Xiao%20et%20al_CHI%202025_Sustaining%20Human%20Agency%2C%20Attending%20to%20Its%20Cost.pdf)；[arXiv](https://arxiv.org/abs/2503.07970)。
- **[O1] Joseph Spracklen et al.** *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs.* **34th USENIX Security Symposium, 2025, pp. 3687–3706**；arXiv:**2406.10279**（2024-06-12 首发，首发早于滚动窗口）。[USENIX 正式页](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)；[arXiv](https://arxiv.org/abs/2406.10279)。正式会议页标注 Distinguished Paper Award。
- **[D1] Dengcheng Hu et al.** *Ladder: A Convergence-based Structured DAG Blockchain for High Throughput and Low Latency.* **22nd USENIX Symposium on Networked Systems Design and Implementation (NSDI 25), 2025, pp. 779–794**。arXiv：本轮未核实，留空。[USENIX 正式页](https://www.usenix.org/conference/nsdi25/presentation/hu)。
- **[C1] Win-San Khwa et al.** *A mixed-precision memristor and SRAM compute-in-memory AI processor.* **Nature 639, 617–623 (2025)**，在线发表 2025-03-05，DOI **10.1038/s41586-025-08639-2**。arXiv：本轮未核实，留空。[出版方](https://www.nature.com/articles/s41586-025-08639-2)。第一组三位作者为共同第一作者；该页注明代码不公开，非商业使用例外须经申请批准。这直接限制了“完全复现”的可行性。

说明：量子与芯片代表作使用高水平期刊，未将其冒称为计算机顶会论文；上表优先展示正式发表于滚动窗口内的研究，不把检索结果数量视为覆盖全部文献的证明。
