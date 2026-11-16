# 本地 AI 自测预实验

这是小规模、探索性的研究练习，不是顶会论文的充分证据。两次方案分开保存：第一轮 `protocol.md` / `runner.py`，后续探索 `protocol-v2.md` / `runner_v2.py`。查看相应 `runs/*-summary.json` 与原始 `runs/*.json`；原始记录包含任务、提示、模型回答、修复反馈、每轮自测与独立检查，方便审计失败而非只展示成功。

## 推荐：只读离线复核

```bash
python3 tools/audit_experiment.py
```

无需模型、网络或第三方包，不会改动原始记录。检查 SHA-256、任务及生成衔接、固定测试、停止规则、逐轮失败输入与汇总，并用不同写法核对参考。机器报告见 [audit/verification.json](audit/verification.json)，解释见[最终报告](../paper/研究报告.md)。校验清单用于检测意外变化，不是第三方签名。

2026-11-16 修正了执行器 and/or 的短路与操作数返回语义。历史候选没有使用 BoolOp，复算结果不变；原始源码分别保留于实验前提交 e557835 和 88a3dbb。两轮原始 JSON 均保持不变。

## 传统复算（写入副本）

需要 Python 3.9 及以上（原始日志记录 3.9.6），无第三方包。复算会修改指定原始 JSON 的分析字段及对应汇总，建议先复制原始文件后执行：

```bash
cp experiment/runs/pilot.json /tmp/pilot-recheck.json
python3 experiment/runner.py --analyze-only --output /tmp/pilot-recheck.json
cp experiment/runs/pilot-v2.json /tmp/pilot-v2-recheck.json
python3 experiment/runner_v2.py --analyze-only --output /tmp/pilot-v2-recheck.json
python3 -m unittest discover -s tests -v
```

每个版本只用对应评估器复算；两个版本支持的表达式不同。参考实现由研究者手写，经过边界测试但未经独立人类同行审查。

## 重新生成

安装 Ollama 并启动本机服务，再获取对应模型，运行对应 Python 脚本：

```bash
ollama pull qwen2.5-coder:0.5b
ollama pull qwen2.5-coder:1.5b
python3 experiment/runner.py --output /tmp/pilot-new.json
python3 experiment/runner_v2.py --output /tmp/pilot-v2-new.json
```

生成结果可能因操作系统、Ollama、模型版本、推理后端及环境变化而不同；请记录模型摘要，勿覆盖已发布原始结果。模型生成的是受限表达式，解释器拒绝不在白名单内的语法；不能把所有拒绝都当作模型语义错误。即便测试不通过，也不是一个可靠的生产代码执行沙箱：不要直接执行任何模型生成的任意代码。
