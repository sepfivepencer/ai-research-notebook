# 第三阶段：多轮自生成测试的前作核查（进行中）

核查日期：2026-10-30。用户最初选择先查前作；随后授权助手连续推进，已另外开展本地预实验。本文是检索与论文内容核验，不是对所引论文的实验复现。标注【已验证】表示核实了对应论文中的内容，**不表示其结论已由我们复现**。

## 已有工作和反方证据

| 论文 | 如何生成或使用反馈 | 作者使用的检验及结论 | 对我们意味着什么 |
|---|---|---|---|
| Chen 等，ACL 2025 | 比较自生成测试的执行后反馈和运行过程反馈，进行自我调试 | 作者指出执行后自测存在偏差；报告过程信息有助于其设置中的调试。【已验证：论文摘要】 | 单纯提出“自生成测试可能误导修复”已不新。【有依据的推断】 |
| Konstantinou 等，2026 预印本 | 比较代码先生成、测试后生成与测试独立生成等信息条件 | 作者在其选定设置中报告错误实现可影响后续测试，降低检错效果；实验有任务、筛选和模型范围。【已验证：论文摘要及方法】 | 共同错误及上下文信息泄漏本身已有研究；多轮条件下是否有不同现象，仍需逐项对照。【待验证】 |
| Li 等，Agent-CoEvo，2026 预印本 | 仓库级代码补丁和测试补丁分别生成，执行矩阵交叉评估并多轮更新 | 作者使用 SWE-bench Lite 和 SWT-bench Lite，分别考察修复与测试质量，并分析迭代和成本。【已验证：论文方法及实验】 | “代码和测试多轮共同演化”不是新意；仓库级工作和简单函数任务不能不加区分地比较。【有依据的推断】 |
| Hu 等，CoSPlay，2026 预印本 | 候选代码与单元测试池按执行矩阵多轮更新，并以共识选取候选 | 作者在四组代码挑战基准、7B 和 14B 设置中报告通过数与参考正确性呈正相关；其多数分析采用每组 200 个问题的采样设置。【已验证：论文第 3.1、4.3 节；未复现】 | 这是对“自测总会恶化”的直接反例；相关关系并不证明每个任务或每一轮均改善。【有依据的推断】 |
| Bansal 等，VibePass，2026 预印本 | 拆分出触发缺陷的测试生成与修复，在无测试、外部触发测试、自生成测试条件下比较 | 测试须满足输入有效等条件，并以参考实现及官方测试评估；作者分析测试是否真正触发缺陷。【已验证：论文第 2 节】 | “测试能否触发错误”与“修复是否正确”应分开讨论；这里已有成熟对照，不能直接当作原创方法。【有依据的推断】 |
| Liu 等，2026 预印本 | 比较一次生成、测试指导修订和计划审计指导修订 | 作者报告，在其 DataFrame 任务中，测试通过增加但参考结果仍不匹配；作者明确说不同流程的比较不是因果推断。【已验证：摘要；未复现】 | 与“自测通过但语义未对齐”的研究入口高度重合，不能声称该现象首次被我们发现。【有依据的推断】 |
| Kiecker 等，2026 预印本 | 研究不同修复循环预算和反馈流程 | 作者报告所测流程中后续轮次存在收益递减。【已验证：摘要，未复现】 | 单独比较修复轮数也不是新问题。【有依据的推断】 |

## 正反观点及尚需核实的边界

- 假说：某些设置中，代码与测试共享错误或遗漏，导致自测表面改善而独立检查未改善甚至变差。【待验证】
- 反方：如果生成测试足够有效、反馈与选择机制合适，自测信号可能反映正确性，迭代也可能改善结果；CoSPlay 报告的正相关支持这一方向，但不构成跨任务的普遍保证。【已验证：作者报告；有依据的推断】
- 创新性尚未确立：已检索论文不等于完整查重，也不能以更换模型、设备或数据集宣称创新。仍需明确可观察的失败条件、前作是否已经覆盖以及独立检查的可信来源。【待验证】
- CoSPlay 使用的 7B/14B 模型及候选池并不自动适配 8 GB M1；能否在现有资源下复现或设计有意义的小规模对照，尚未测试。【待验证】

## 核查边界与待决事项

研究比较中的“自测变好”应考虑测试集是否变化：若每轮测试不同，通过率不能直接比较；独立检查本身也可能不完整或错误。【有依据的推断】后续预实验的选择、执行与局限以 `experiment/` 中方案和运行记录为准；它不构成对上述文献的复现。负结果与运行失败均保留。

## 可查文献

1. Xiancai Chen 等，2025，ACL 2025 主会，*Revisit Self-Debugging with Self-Generated Tests for Code Generation*，arXiv:2501.12793（预印本作者名单与正式版本略有差异）。[正式论文](https://aclanthology.org/2025.acl-long.881/)。
2. Michael Konstantinou、Florian Tambon、Mike Papadakis，2026，预印本，*On the risk of coding before testing: An empirical study on LLM-based test generation workflow*，arXiv:2607.05139；会议身份【待核实】。[原文](https://arxiv.org/html/2607.05139)。
3. Kefan Li 等，2026，预印本，*Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints*，arXiv:2604.04580；会议身份【待核实】。[原文](https://arxiv.org/html/2604.04580)。
4. Zhangyi Hu 等，2026，预印本，*CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test*，arXiv:2605.23491v2；会议身份【待核实】。[原文](https://arxiv.org/html/2605.23491)。
5. Srijan Bansal、Jiao Fangkai、Yilun Zhou、Austin Xu、Shafiq Joty、Semih Yavuz，2026，预印本，*VibePass: Can Vibe Coders Really Pass the Vibe Check?*，arXiv:2603.15921；会议身份【待核实】。[原文](https://arxiv.org/html/2603.15921)。
6. Tobias Kiecker、Eik Reichmann、Hosung Kang、Gabin An、Lars Grunske，2026，预印本，*Is Three the Magic Number? An Empirical Evaluation of LLM-Based Repair Loops*，arXiv:2607.05197；会议身份【待核实】。[摘要](https://arxiv.org/abs/2607.05197)。
7. Jingjing Liu、Dishu Yang、Hongbo Qin、Hansong Zhang，2026，*Passing Tests, Missing Semantics: Evidence of Interpretive Lock-In in Plan-Based DataFrame Code Generation*，arXiv:2610.15797v2；arXiv 页面称已被 ICECER 2026 接收，正式出版信息【待核实】。[摘要](https://arxiv.org/abs/2610.15797)。
