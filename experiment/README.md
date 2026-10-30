# 本地 AI 自测预实验

这是小规模、探索性的研究练习，不是顶会论文的充分证据。两次方案分开保存：第一轮 `protocol.md` / `runner.py`，后续探索 `protocol-v2.md` / `runner_v2.py`。查看相应 `runs/*-summary.json` 与原始 `runs/*.json`；原始记录包含任务、提示、模型回答、修复反馈、每轮自测与独立检查，方便审计失败而非只展示成功。

## 复核已保存结果

需要 Python 3.10 及以上，无第三方包。复算会修改指定原始 JSON 的分析字段及对应汇总，建议先复制原始文件后执行：

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
