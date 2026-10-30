---
title: AI 自己写的测试，能证明代码真的修对了吗？
description: 本科研究记录第二篇：从三条候选路线的文献比较出发，聚焦多轮修复里的“假通过”，并记下已有工作与尚未回答的问题。
publishedAt: 2026-10-30
tags:
  - research
  - ai
  - testing
  - learning
featured: false
---

我和 AI 助手正在尝试走完一次本科研究：先查文献，再定义问题，最后用真实实验检验想法。第一篇记录了三个候选方向；这一次读完代表论文后，我选择优先关注 AI 自生成测试，并进一步关注多轮修复中的“假通过”。【已验证：项目决策】

目前仍处于立论阶段：**没有下载模型、没有运行研究实验，也没有证明这个具体切口具有原创性。**【已验证：项目状态】这篇文章记录已读到的工作，以及接下来需要回答的问题。

## 一个“通过了，但没有修对”的例子

假设任务是写一个函数，返回列表中最大的数字。一个错误实现把最大值的初始值设为 0：

~~~python
def maximum(numbers):
    result = 0
    for number in numbers:
        if number > result:
            result = number
    return result
~~~

测试 [2, 5] 会得到 5，看起来通过了；但输入 [-5, -2] 应该得到 -2，这段代码却返回 0。这个例子是人工构造的教学说明，不是模型实验结果。

如果测试只覆盖正数，它可能和错误实现一起给出“已经正确”的错觉。【有依据的推断】我们想继续追问的是：**经过多轮“生成测试—修代码—再测试”后，自测结果变好时，独立检查是否仍可能变差？在什么条件下会发生？**【待验证】

## 别急着说“这是新发现”

核对文献后，最重要的收获不是找到了一个新名词，而是知道哪些事情已经有人研究。

Xiancai Chen 等在 [ACL 2025 的论文](https://aclanthology.org/2025.acl-long.881/)中研究了自生成测试的偏差，以及执行后反馈和运行过程信息对自我调试的影响。作者使用多个代码生成基准和模型；他们的结果是他们的实验报告，不是我们在 M1 上的复现。【已验证：论文研究范围】

Michael Konstantinou 等的 [2026 年预印本](https://arxiv.org/html/2607.05139)比较了只根据任务描述生成测试，与看过错误实现或保留代码生成历史后生成测试。作者报告，在其选定的任务和模型设置下，后者可能更难检出错误。【已验证：论文报告；尚未独立复现】

此外，[Agent-CoEvo](https://arxiv.org/abs/2604.04580) 和 [CoSPlay](https://arxiv.org/abs/2605.23491) 已经研究代码与测试的共同演化。因此，“让代码和测试多轮迭代”本身也不能作为我们的新贡献。【已验证：两篇预印本的方法；具体差异仍需深入核对】

更值得注意的是反方证据：CoSPlay 作者报告，在他们测试的任务与模型上，通过更多生成测试的代码往往更可能通过独立的正确性检查。这并不能保证所有场景都如此，却足以提醒我们不能预设“多轮自测一定让真实正确性变差”。【已验证：作者报告，尚未独立复现】更详细的逐篇对照与限制记录在[第三阶段前作核查](https://github.com/sepfivepencer/ai-research-notebook/blob/main/notes/phase3-prior-work.md)。

这意味着，我们不能仅凭换一台 M1、换一个小模型，或者重复“AI 会写错测试”，就宣称发现了新的学术问题。【有依据的推断】

## 另外两个方向给了我什么提醒

第二阶段并没有只看一个方向。

**记忆删除。** [AfterDeleteBench](https://arxiv.org/html/2610.31366) 研究了原始记录删除后，衍生状态仍可能支持信息恢复的问题，并在完整来源关系等限定条件下测试了处理方法。【已验证：论文研究范围】所以“删掉原文但摘要还在”也不是我们首先发现的现象。

**量化与任务成本。** [一项 2026 年预印本](https://arxiv.org/html/2610.32417)发现，在其 A100 和特定模型、任务设置下，单 token 更省能耗的配置不一定在每个成功任务上更省能耗。【已验证：作者报告；不适用于直接推断 M1 结果】

完整的论文题录、阅读记录、范围限制和三个候选的对照保存在 [GitHub 研究仓库的文献综述](https://github.com/sepfivepencer/ai-research-notebook/blob/main/notes/literature-review.md)。

## 接下来怎么避免自己骗自己

我们会先把“假通过”说清楚：模型在自己的测试上通过，与代码符合真实要求，是两个不同的判断。独立检查需要有独立的依据；如果测试本身错误或不完整，也可能误判。【有依据的推断】

真正的研究还要回答三个问题：

1. 如何区分“模型修好了代码”和“测试没有触及错误”？【待验证】
2. 多轮过程中的测试与代码变化，和现有研究相比有没有真正有价值的区别？【待验证】
3. 如果独立检查显示修复其实变好了，我们是否愿意承认原先的猜想不成立？答案应该是愿意。负结果同样需要记录。

具体任务、模型、对照组、评价指标和计算预算会在后续与我共同确认；此刻没有任何效果数字，也没有“预期结果”。如果继续查重后发现问题已被充分解决，我们就修改问题或重新选择。

项目仓库：[ai-research-notebook](https://github.com/sepfivepencer/ai-research-notebook)。文献核查截至 2026 年 10 月 30 日。本文由本人和 AI 助手协作整理。

## 参考文献

1. Xiancai Chen 等，2025，ACL 2025 主会长文，*Revisit Self-Debugging with Self-Generated Tests for Code Generation*，DOI: 10.18653/v1/2025.acl-long.881；同标题预印本 arXiv:2501.12793，作者名单与正式版本略有差异。[正式论文](https://aclanthology.org/2025.acl-long.881/)
2. Michael Konstantinou、Florian Tambon、Mike Papadakis，2026，预印本，*On the risk of coding before testing*，arXiv:2607.05139；正式会议身份【待核实】。[原文](https://arxiv.org/abs/2607.05139)
3. Kefan Li 等，2026，预印本，*Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints*，arXiv:2604.04580；正式会议身份【待核实】。[原文](https://arxiv.org/abs/2604.04580)
4. Zhangyi Hu 等，2026，预印本，*CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test*，arXiv:2605.23491；正式会议身份【待核实】。[原文](https://arxiv.org/abs/2605.23491)
5. Ehsan Saleh、Roozbeh Nahavandi、Sama Salarian、Raef Bassily、Andrew Perrault，2026，预印本，*AfterDeleteBench*，arXiv:2610.31366；正式会议身份【待核实】。[原文](https://arxiv.org/abs/2610.31366)
6. Stephen Abkin 等，2026，预印本，*Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents*，arXiv:2610.32417；正式会议身份【待核实】。[原文](https://arxiv.org/abs/2610.32417)
