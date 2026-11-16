# AI 研究笔记：从选题到可复现证据

用 M1 MacBook Air、8GB 内存和零新增预算，记录一次本科 AI 研究的完整过程。当前载体是中文技术长文，保留文献、假设、实验与自我审稿的阶段结构。

**2026-11-16 · v1.0.0：探索性研究项目已结项。完整报告、两轮原始记录与离线复核工具已归档；原始“颠覆性、可投稿论文”目标未达成。**

[完整结项入口](PROJECT_CLOSEOUT.md) · [研究报告](paper/研究报告.md) · [下载 PDF](output/pdf/ai-self-test-report.pdf) · [实验与复核](experiment/README.md)

## 从哪里开始

- [第一篇研究日志](articles/001-starting-ai-research-on-m1.md)：起点、候选题和证据边界。
- [第二篇研究日志](articles/002-when-ai-tests-its-own-code.md)：文献比较、当前选择与“假通过”的研究入口。
- [第三篇研究日志：真实本机预实验](articles/003-a-small-experiment-on-ai-tests.md)：两轮结果、代码退化案例和局限。
- [中文研究报告](paper/研究报告.md)：方法、实测结果、失败类型和参考文献。
- [自我审稿与修改记录](paper/自我审稿与修改记录.md)：拒稿理由与尚未解决的问题。
- [实验协议、代码与原始结果](experiment/README.md)：运行与复算方法。
- [第三至六阶段学习包](notes/learning-packages.md)。
- [第二阶段完整文献综述](notes/literature-review.md)：三题代表作、研究缺口及学习包。
- [23 个分方向的机会地图](notes/opportunity-map.md)：AI、系统与交叉前沿的扫描资料和来源。
- [阶段与决策记录](notes/decisions.md)：已经决定的条件，以及仍需确认的分叉。
- [结构化记录](data/notebook.json)：文献元数据、候选题与主张的状态。
- [核心阅读清单](notes/reading-list.md)：从结构化记录导出的代表文献；完整地图的引文另列在地图中。
- [工具使用说明](tools/README.md)：检查记录一致性、导出阅读清单。

博客：[Sepfive 的文章归档](https://www.sepfivepencer.org/writing)。

## 一个可以运行的小工具

需要 **Python 3.9 或更新版本**（本机实测 3.9.6），只使用标准库，无需安装第三方依赖、模型、API key 或 GPU。

```bash
git clone https://github.com/sepfivepencer/ai-research-notebook.git
cd ai-research-notebook
python3 tools/audit_experiment.py
python3 tools/check_notebook.py check
python3 tools/check_notebook.py reading-list
python3 -m unittest discover -s tests -v
```

工具检查必填字段、重复 ID、日期、来源 URL、arXiv 号和引用关系；检查失败返回非零状态，可用于 GitHub Actions。`reading-list` 根据同一份记录生成 Markdown 阅读清单。

**工具通过不代表论文真实、主张正确或文章新颖。** 它不访问网络、不读取论文全文，也不判断研究质量。人工核验范围另有记录。

## 研究状态

| 阶段 | 状态 |
|---|---|
| 1. 全景扫描与三个候选 | 已完成扫描，候选原创性待核查 |
| 2. 文献精读与缺口分析 | 已完成代表作精读与对照；研究缺口仍待验证 |
| 3. 核心论点与证伪设计 | 完成预实验假设与反方核查；新颖性未确立 |
| 4. 方法与真实实验 | 两轮本机探索已运行；存在严重局限 |
| 5. 撰写 | 完整探索性研究报告已定稿，另附 PDF |
| 6. 自我审稿与修改 | 收尾复核与可修正文稿已完成；研究不足作为边界保留 |

三个候选题分别涉及 AI 自生成测试、长期记忆删除、量化后的任务总成本。本人选择了自生成测试中的多轮假通过；两轮探索未观察到预定义假通过。单次实验、玩具任务和受限执行器不支持总体概率或因果结论；完整结果包括无效输出和截断。

## 记录约定

- **已验证**必须写清范围：来源确实存在、原文报告，或本地运行观察。
- **有依据的推断**保留依据和适用范围。
- **待验证**用于研究假设、效果猜想和新颖性判断。
- 研究实验的命令、版本、原始输出与失败记录见 `experiment/`。
- CI 检查资料结构、原始数据完整性、逐轮结果复算及工具回归；不调用模型，也不构成科学同行评审。

## 目录

```text
articles/                 博客文章的 Markdown 源文件
paper/                    最终研究报告、历史初稿入口和审稿修改
output/pdf/               可下载的报告 PDF
experiment/               协议、代码、任务和两轮原始运行记录
notes/                    机会地图与决策记录
data/notebook.json        文献与主张记录
tools/check_notebook.py   零第三方依赖的记录检查工具
tests/                    工具行为测试
.github/workflows/        自动验证
```

## 协作与来源

内容由仓库维护者与 AI 助手协作整理。引用保留一手来源，主会、Findings、workshop 和预印本分开标注。第一阶段扫描记录不等于全文精读；第二阶段对代表论文进行了有重点的精读，但没有独立复现。外部论文与项目的权利归原作者；本仓库保存引用、简要研究笔记及本项目自行生成的代码与实验记录。引用本项目可使用 CITATION.cff；这不代表正式学术发表。
