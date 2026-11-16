# 收尾文献核查记录

核查日期：2026-11-16。核查对象为中文初稿的全部 5 篇引用，以及第二阶段综述、第一阶段机会地图中的书目与部分具体主张。方法是重新访问 arXiv、会议论文集、出版方页面和作者所在机构提供的论文；另从 arXiv 页面提取题名、作者、首发及修订日期进行交叉检查。

**结论：初稿 5 篇引用均真实可查，题名、作者、年份及 arXiv 编号相符，相关工作中的简要概括获得原文支持。【已验证：文献核查】未发现这些引用是虚构论文，也未发现把预印本冒称顶会主会的情况。**这不代表论文所有结论均正确，更不代表本项目复现了它们的实验；全文细节、附录、代码、原始数据和全部后续文献没有穷尽核查。

## 初稿全部引用

| 编号 | 核实的题录与版本 | 支持的主张及限制 |
| --- | --- | --- |
| [1] | Xiancai Chen 等，2025，*Revisit Self-Debugging with Self-Generated Tests for Code Generation*；[ACL 2025 正式长文](https://aclanthology.org/2025.acl-long.881/)，DOI 10.18653/v1/2025.acl-long.881；[arXiv:2501.12793v1](https://arxiv.org/abs/2501.12793v1)。 | 摘要明确讨论自生成测试偏差及执行后、执行中两种调试反馈。正式版作者含 Xinyu Zhang，预印本名单没有该作者；应以所引用版本为准。初稿已经说明名单差异。【已验证】 |
| [2] | Michael Konstantinou、Florian Tambon、Mike Papadakis，2026，*On the risk of coding before testing: An empirical study on LLM-based test generation workflow*；[arXiv:2607.05139v1](https://arxiv.org/abs/2607.05139v1)，2026-07-06。未独立核实正式会议身份。 | 原文报告代码可见时后续测试可能复制错误，并在作者筛选设置下报告约 14% 与 25% 的检出率。不能当成所有模型的一般故障率。【已验证：作者报告；未复现】 |
| [3] | Zhangyi Hu、Chenhui Liu、Tian Huang、Jindong Li、Yang Yang、Jiemin Wu、Zining Zhong、Menglin Yang、Yutao Yue，2026，*CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test*；[arXiv:2605.23491v2](https://arxiv.org/html/2605.23491v2)，2026-05-25。未独立核实正式会议身份。 | 第 4.3 节直接报告其设置下通过数与真实正确性正相关；附录提供按数据集、轮次的分析。它支持“不能预设自测随轮次必定恶化”，不保证任何任务上自测都可靠。【已验证：原文对应段落；未复现】 |
| [4] | Jingjing Liu、Dishu Yang、Hongbo Qin、Hansong Zhang，2026，*Passing Tests, Missing Semantics: Evidence of Interpretive Lock-In in Plan-Based DataFrame Code Generation*；[arXiv:2610.15797v2](https://arxiv.org/html/2610.15797v2)，2026-10-19。 | 摘要与结果报告测试通过增加但参考输出不匹配；同时明确流程的反馈、预算与编辑权限不同，诊断不是因果结论。[arXiv 题录](https://arxiv.org/abs/2610.15797v2)中的 ICECER 2026 接收属作者备注，本次未取得正式出版记录，不能进一步确认会议出版身份。【已验证：作者报告；出版待核实；未复现】 |
| [5] | Srijan Bansal、Jiao Fangkai、Yilun Zhou、Austin Xu、Shafiq Joty、Semih Yavuz，2026，*VIBEPASS: Can Vibe Coders Really Pass the Vibe Check?*；[arXiv:2603.15921v1](https://arxiv.org/html/2603.15921v1)，2026-03-16。未独立核实正式会议身份。 | 原文分别定义触发缺陷的测试生成和针对缺陷的修复，并比较不同诊断条件；测试有效与真正触发缺陷不能混为一谈。它不是本项目小模型实验的复现依据。【已验证：问题定义和作者报告；未复现】 |

## 综述的其他核心来源

下表补查第二阶段的其他来源；上表 [1]、[2]、[3]、[5] 不重复列出。短名称仅用于对应原综述，完整题名与全部作者以链接原页为准。

| 来源 | 作者、年份、身份与一手链接 | 本次核查支持什么 |
| --- | --- | --- |
| AfterDeleteBench | Ehsan Saleh、Roozbeh Nahavandi、Sama Salarian、Raef Bassily、Andrew Perrault，2026；[2610.31366v1](https://arxiv.org/html/2610.31366v1)，预印本。 | 匹配的“曾暴露后删除 / 从未暴露”对照及衍生状态残留；正文主设置的 0.68 和来源闭包处理有原文依据。并非真实产品一般泄露率。【已验证；未复现】 |
| MEME | Seokwon Jung、Alexander Rubinstein、Arnas Uselis、Sangdoo Yun、Seong Joon Oh，2026；历史阅读应使用 [2605.12477v1](https://arxiv.org/html/2605.12477v1)。[现题录](https://arxiv.org/abs/2605.12477)已更新至 2026-11-11 的 v2；未独立核实正式会议。 | v1 明确两个知识图谱、100 个 episode、约 35K-token 上下文及六个记忆系统；依赖更新、删除和不确定性是不同任务。综述相应概括有依据。【已验证；未复现】 |
| Forgetting Without Restarting | Chao Yao 等，2026；完整题名为 *Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents*；[2609.04875v1](https://arxiv.org/abs/2609.04875v1)，预印本。 | 摘要明确 prompt、摘要、明文状态、工具计划、KV cache 与来源追踪重放；保证依赖确定性转移等假设。【已验证：题录及摘要；未复现】 |
| Auditing Forgetting in Limited Memory Language Models | Arya Raeesi、Hanna Roed，2026；[2607.00605v1](https://arxiv.org/abs/2607.00605v1)，预印本。 | 固定模型、改变数据库/检索状态以区分参数残留与检索通路，摘要支持近邻恢复的概括。【已验证：题录及摘要；未复现】 |
| Agentic Unlearning | Bin Wang 等，2026；*Agentic Unlearning: When LLM Agent Meets Machine Unlearning*；[2602.17692v2](https://arxiv.org/abs/2602.17692v2)，预印本。 | 参数与持久记忆双通路、依赖闭包及医疗问答设置有原文依据。没有核实该方案能在本机复现。【已验证：题录及摘要；未复现】 |
| SWE-Mutation | Yuxuan Sun 等，2026；*SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software Engineering?*；[Findings of ACL 2026 正式页](https://aclanthology.org/2026.findings-acl.1976/)，arXiv:2605.22175。 | 正式页核实 Findings 身份、作者及使用变异程序评估生成测试的研究范围；不能把变异测试当作本项目新方法。【已验证：正式元数据及摘要；未复现】 |
| Agent-CoEvo | Kefan Li 等，2026；*Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints*；[2604.04580v1](https://arxiv.org/abs/2604.04580v1)，预印本。 | 摘要明确候选代码、测试共同演化，使用 SWE-bench Lite / SWT-bench Lite；“多轮共同演化”已不是未被探索的总思路。【已验证：题录及摘要；未复现】 |
| 量化任务能耗 | Stephen Abkin 等，2026；*Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents*；综述所读 [2610.32417v2](https://arxiv.org/html/2610.32417v2)；[现题录](https://arxiv.org/abs/2610.32417)为 2026-10-30 的 v3；预印本。 | v2 方法及结果支持 29 个任务、两个模型、A100、4/8-bit 和任务级成本排名可能不同；主测量不计加载，但论文另有模型加载敏感性分析，不能写成全篇从未考虑加载。【已验证：题录及相关段落；未复现】 |
| Apple Silicon 优化 | Kyrylo Yemets 等，2026；*Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon*；[2610.31479v1](https://arxiv.org/abs/2610.31479v1)。 | 摘要支持四类优化效果依赖硬件、运行时和负载。作者备注称 NeurIPS 2026 ODI 与 SLM-Agents workshop 接收；本次打开两条 OpenReview 均遇浏览器验证，未独立确认，不写成 NeurIPS 主会。【已验证：题录及作者备注；会议待核实；未复现】 |

## 第一阶段机会地图的书目抽查与扩展核对

机会地图中所有 21 个不同 arXiv 链接编号均已重新取回题名、作者及日期，未发现编号指向无关论文。结合综述共核对了 32 个不同 arXiv 链接编号。下列正式身份通过会议/出版方记录或作者机构的论文核实；这是元数据与摘要核查，并非对 23 个研究方向重新做完整综述。

| 原编号 | 一手记录、作者和身份 | 核查支持的范围 |
| --- | --- | --- |
| AI1 | [Setlur 等，ICML 2025 / PMLR 267](https://proceedings.mlr.press/v267/setlur25a.html)；arXiv:2502.12118。 | 验证与测试时计算的理论比较有分布条件。 |
| AI2 | [Yao 等，ICLR 2025 正式 PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf)；arXiv:2406.12045。 | τ-bench 的交互任务、重复可靠性研究身份。 |
| AI3 | [Wu 等，ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html)；arXiv:2410.10813。 | LongMemEval 的长期记忆、更新、拒答任务。 |
| AI4 | [Yue 等，ACL 2025 长文](https://aclanthology.org/2025.acl-long.736/)；arXiv:2409.02813。 | MMMU-Pro 的纯文本捷径及多模态评估范围。 |
| AI5 | [Yang 等，NeurIPS 2024 主会](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)；arXiv:2405.15793。 | SWE-agent 研究 Agent 与工具接口的影响。 |
| AI6 | [Ye 等，MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)；arXiv:2501.01005。 | FlashInfer 的注意力内核、缓存格式及调度。 |
| AI7 | [Xing 等，MLSys 2026](https://proceedings.mlsys.org/paper_files/paper/2026/hash/37e44c4b5321605735be9761f9b758fc-Abstract-Conference.html)；arXiv:2601.00227。 | FlashInfer-Bench 的生成、评估、部署闭环。 |
| AI8 | [Lin 等，OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/lin-jinkun)，pp.483–498；arXiv 未核实。 | 拖慢节点并非总由硬件故障造成；what-if 分析。 |
| AI9 | [Wu 等，2026，LongMemEval-V2](https://arxiv.org/abs/2605.12493v1)；预印本，正式会议未核实。 | 题录、日期及记忆任务范围。 |
| AI10 | [Jung 等，MEME 2605.12477v1](https://arxiv.org/abs/2605.12477v1)，2026；预印本。 | 见上表，历史扫描宜固定 v1。 |
| AI11 | [Hu、Wang、McAuley，ICLR 2026 正式论文集](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fd1eff9dd295df50a41f2521942fa31d-Abstract.html)；arXiv:2507.05257。 | **本次补核了原先待核实的正式会议身份**；MemoryAgentBench 包含四种记忆能力。 |
| AI12 / R1 | [Black 等，RSS 2025](https://roboticsproceedings.org/rss21/p010.html)；arXiv:2410.24164，DOI 10.15607/RSS.2025.XXI.010。 | π₀ 的 VLA、flow matching 与机器人泛化设置；两处为同一研究。 |
| AI13 | [Debenedetti 等，NeurIPS 2024 Datasets and Benchmarks](https://proceedings.nips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)；arXiv:2406.13352。 | AgentDojo 同时关心任务完成与注入攻击。 |
| AI14 | [Debenedetti 等，Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)，2025；预印本，正式会议未核实。 | CaMeL 的控制流、数据流与权限隔离总思路已有工作。 |
| AI15 | [Zarif 等，Ignored, Not Refused](https://arxiv.org/abs/2610.23254v1)，2026；预印本。 | 题录与小模型低攻击成功率混淆的摘要范围。 |
| AI16 | [Wang 等，Safety, or Just Capability?](https://arxiv.org/abs/2607.28685v1)，2026；历史版 v1；现题录 v2 为 2026-11-04 修订。 | 安全分数受指标和模型能力影响的研究范围；未复核全部统计。 |
| AI17 | [Pakhomov、Nijkamp，Bookkeeping, Composition, or Unreachable Gold?](https://arxiv.org/abs/2610.09193v1)，2026。 | 题录和摘要；NeurIPS 2026 IAB non-archival workshop 接收为作者备注，未独立确认，不能写成主会。 |
| S1 | [Ziegler、Lubin、Chasins，作者机构 PDF](https://jlubin.net/assets/pldi25b.pdf)，PACMPL 9 / PLDI 2025 Article 175，DOI 10.1145/3729278；arXiv 未核实。 | Patch-reconciliation 是直接操纵编程研究，不能称为新前端框架。 |
| S2 | [Zhu、Sun、Madhyastha，NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/zhu-jingyuan)，pp.669–684；arXiv 未核实。 | 归档页面执行保真度及 FidEx 问题范围。 |
| S3 | [Xing 等，NSDI 2025](https://www.usenix.org/conference/nsdi25/presentation/xing)，pp.21–36；arXiv 未核实。 | Rajomon 的调用图协同过载控制。 |
| S4 | [Chai 等，OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/chai-xiaohu)，pp.199–218；arXiv 未核实。 | 生产 Serverless 冷启动的端到端、并发瓶颈。 |
| S5 | [Cao、Arpaci-Dusseau、Arpaci-Dusseau、Caraza-Harter，NSDI 2025](https://www.usenix.org/conference/nsdi25/presentation/cao)，pp.189–204；arXiv 未核实。 | Leopard 对计费与真实资源消耗不一致的研究。原总议程本次超时，直接论文页可访问。 |
| S6 | [Kuiper、Groß、Boncz、Mühleisen，官方 PDF](https://www.vldb.org/pvldb/vol18/p2748-kuiper.pdf)，PVLDB 18(8):2748–2760，2025，DOI 10.14778/3742728.3742762；arXiv 未核实。 | Saving Private Hash Join 的超内存断崖及 DuckDB 已有实现。 |
| S7 | [Cornacchia、Benson、Bilal、Canini，NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/cornacchia)，pp.153–174；arXiv 未核实。 | μView 的细粒度监控与 IPU 方案。 |
| S8 | [Li 等，OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/li)，pp.575–593；arXiv 未核实。 | Tintin 的硬件计数器测量误差与归因。 |
| S9 | [Zhang、Kim，NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/zhang-xiao)，pp.1759–1776；arXiv 未核实。 | SMEC 的 SLO、无线接入与边缘资源竞争。 |
| S10 | [Tian 等，USENIX ATC 2025](https://www.usenix.org/conference/atc25/presentation/tian)，pp.563–585；arXiv 未核实。 | CLONE 的软硬件协同边缘推理，不能推定 M1 等价复现。 |
| S11 | [Hosseini 等，NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/hosseini)，pp.493–507；arXiv 未核实。 | CacheCatalyst 的提前验证与网络往返代价。 |
| S12 | [Liu 等，USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/liu-zhengyu)，pp.8293–8312；arXiv 未核实。 | DOMino / Hulk 研究无脚本 HTML 经现有 JS gadget 产生危害。 |
| S13 | [Hantke、Snyder、Haddadi、Stock，USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/hantke)，pp.8235–8253；arXiv:2501.15911。 | WebREC 的执行记录与可复现 Web 测量范围。 |
| Q1 | [Google Quantum AI and Collaborators，Nature 638:920–926 (2025)](https://www.nature.com/articles/s41586-024-08449-y)；arXiv:2408.13687。 | 正式在线日期 2024-12-09；表面码阈值、实时解码与相关错误均在摘要讨论。出版方另有 2026-04-28 作者更正，本次没有逐项审读更正。 |
| H1 | [Gabrielle O’Brien，CHI 2025](https://doi.org/10.1145/3706598.3713668)；arXiv:2502.17348。 | 科学家使用及核验代码 LLM 的研究；正式 DOI 与机构存档匹配。 |
| H2 | [Xiao 等，作者机构正式 PDF](https://www.terpconnect.umd.edu/~gegao/paper/Xiao%20et%20al_CHI%202025_Sustaining%20Human%20Agency%2C%20Attending%20to%20Its%20Cost.pdf)，CHI 2025，DOI 10.1145/3706598.3713626；arXiv:2503.07970。 | 用户参与翻译与沟通绩效代价；Berkeley 记录本次 403，作者 PDF 与 arXiv 可核实。 |
| O1 | [Spracklen 等，USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)，pp.3687–3706；arXiv:2406.10279。 | 包幻觉的研究及 Distinguished Paper Award 身份。 |
| D1 | [Hu 等，NSDI 2025](https://www.usenix.org/conference/nsdi25/presentation/hu)，pp.779–794；arXiv 未核实。 | Ladder 的 DAG 并行排序、确认及攻击韧性问题。 |
| C1 | [Khwa、Wen、Hsu 等，Nature 639:617–623 (2025)](https://www.nature.com/articles/s41586-025-08639-2)，DOI 10.1038/s41586-025-08639-2；arXiv 未核实。 | 混合精度 memristor/SRAM 芯片；原页面打开遇身份重定向，但出版方检索记录可取得题录、摘要及代码不公开声明。没有复现器件或代码。 |

上述表格中的范围性事实来自对应一手记录。【已验证：题录、摘要和注明的正文段落】机会地图提出的“可被挑战的假设”仍是研究建议，不能因参考论文真实存在而升级为已发现的新颖缺口。

## 本次发现的文档一致性问题与未完成的核查

1. **历史快照要标明时间。** 第二阶段综述的“尚未下载模型、未运行实验、方法待确认”描述属于当时状态。收尾时需要保留历史意义，并指向后来的两轮探索及最终结论，不能让读者误认成最新状态。
2. **结构化书目数量要准确。** 机会地图曾称 `data/notebook.json` 仅六篇；本次读取实际为 15 篇。结构化书目仍不覆盖机会地图全部文献，也不代表自动检查验证过每段研究概括。
3. **固定阅读版本。** MEME v1、任务能耗 v2、Safety Audit v1 是历史扫描对应版本；无版本链接现在可能指向更新稿。尤其 MEME v2 为 11 月新版本，不能默认为 10 月已经读过。
4. **正式身份存在证据层级。** MemoryAgentBench 的 ICLR 2026 身份已通过正式论文集补核；ICECER 2026、两个 Apple Silicon workshop 及 IAB workshop 仍按作者备注或未独立核实处理。不用 arXiv 接收备注替代主会出版证据。
5. **没有全量复核。** 本次没有逐项检查全部附录、开源代码、数据、统计显著性或作者论文的重复运行；没有穷尽查找 2026-10-30 之后所有相关新作；未核实的 arXiv 号保持留空，不猜填。初稿五篇以外的详细方法概括，只有本记录明确注明的部分经过正文补核。

本记录属于来源审计；本项目自己的实验是否真实、结果能否复算、评估器是否正确，应另看实验协议、原始记录和运行检查，不能由文献存在性代替。【已验证：本次核查的工作边界】
