# AI 研究笔记：从选题到可复现证据

用 M1 MacBook Air、8GB 内存和零新增预算，记录一次本科 AI 研究的完整过程。当前载体是中文技术长文，保留文献、假设、实验与自我审稿的阶段结构。

**当前状态：第一阶段全景扫描已完成；等待确认后进入文献精读。最终题目未定，研究实验尚未开始。**

## 从哪里开始

- [第一篇研究日志](articles/001-starting-ai-research-on-m1.md)：起点、候选题和证据边界。
- [23 个分方向的机会地图](notes/opportunity-map.md)：AI、系统与交叉前沿的扫描资料和来源。
- [阶段与决策记录](notes/decisions.md)：已经决定的条件，以及仍需确认的分叉。
- [结构化记录](data/notebook.json)：文献元数据、候选题与主张的状态。
- [核心阅读清单](notes/reading-list.md)：从结构化记录导出的六篇文献；完整地图的引文另列在地图中。
- [工具使用说明](tools/README.md)：检查记录一致性、导出阅读清单。

博客：[Sepfive 的文章归档](https://www.sepfivepencer.org/writing)。

## 一个可以运行的小工具

需要 **Python 3.10 或更新版本**，只使用标准库，无需安装第三方依赖、模型、API key 或 GPU。

```bash
git clone https://github.com/sepfivepencer/ai-research-notebook.git
cd ai-research-notebook
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
| 2. 文献精读与缺口分析 | 等待确认 |
| 3. 核心论点与证伪设计 | 尚未进入 |
| 4. 方法与真实实验 | 尚未进入 |
| 5. 完整初稿 | 尚未进入 |
| 6. 自我审稿与修改 | 尚未进入 |

候选题分别涉及 AI 自生成测试、长期记忆删除、量化后的任务总成本。它们都有直接相关前作，当前不宣称发现了新的学术空白。

## 记录约定

- **已验证**必须写清范围：来源确实存在、原文报告，或本地运行观察。
- **有依据的推断**保留依据和适用范围。
- **待验证**用于研究假设、效果猜想和新颖性判断。
- 研究实验的命令、版本、原始输出与失败记录，在进入第四阶段后再逐项加入。
- 这个仓库的 CI 是资料工具与数据结构检查，不是模型实验。

## 目录

```text
articles/                 博客文章的 Markdown 源文件
notes/                    机会地图与决策记录
data/notebook.json        文献与主张记录
tools/check_notebook.py   零第三方依赖的记录检查工具
tests/                    工具行为测试
.github/workflows/        自动验证
```

## 协作与来源

内容由仓库维护者与 AI 助手协作整理。引用保留一手来源，主会、Findings、workshop 和预印本分开标注。扫描记录不等于全文精读或独立复现。外部论文与项目的权利归原作者；本仓库只整理引用和简要研究笔记。
