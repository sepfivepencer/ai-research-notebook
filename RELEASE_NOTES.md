# v1.0.0 · 本科 AI 研究探索报告结项

本版本收齐了从全景扫描、文献核查、两轮真实本机预实验到报告、自我审稿和证据复核的公开材料。结项类型为研究过程练习与探索性技术报告；原始“颠覆性、可投稿研究论文”目标未达成。

## 阅读入口

- [结项说明](https://github.com/sepfivepencer/ai-research-notebook/blob/v1.0.0/PROJECT_CLOSEOUT.md)
- [完整中文报告](https://github.com/sepfivepencer/ai-research-notebook/blob/v1.0.0/paper/%E7%A0%94%E7%A9%B6%E6%8A%A5%E5%91%8A.md)
- [协议、代码与原始证据](https://github.com/sepfivepencer/ai-research-notebook/tree/v1.0.0/experiment)
- [自我审稿与修改记录](https://github.com/sepfivepencer/ai-research-notebook/blob/v1.0.0/paper/%E8%87%AA%E6%88%91%E5%AE%A1%E7%A8%BF%E4%B8%8E%E4%BF%AE%E6%94%B9%E8%AE%B0%E5%BD%95.md)
- [正式博客](https://www.sepfivepencer.org/writing/a-small-experiment-on-ai-tests)

附件包含可下载的 5 页中文 PDF、机器可读审计报告与数据 SHA-256 清单；GitHub 自动生成的 Source code 压缩包包含本版本全部仓库材料，不包含模型权重。

## 保存的结果

两轮各 10 题，最终全部自测通过 1/10、3/10，预定义假通过均为 0。两轮各有一次生成截断；API 错误均为 0。第二轮一题从全部 41 点正确变为 20 点失败，自测通过数也下降，因此不能作为“自测改善但独立结果变差”的证据，更不能推断因果或普遍故障率。

本版本修正文稿中的 Python 版本为日志记录的 3.9.6，披露无效输出类型，修复执行器 and/or 的短路与操作数返回语义。全部历史候选均不含 BoolOp，修正后汇总不变；原始 JSON 和摘要保持原样。

## 离线复核

```bash
python3 tools/audit_experiment.py
python3 tools/check_notebook.py check
python3 -m unittest discover -s tests -v
```

本机 23 项自动测试通过。CI 配置覆盖 Python 3.9 / 3.10 / 3.12；远端状态以该版本对应的 Actions 结果为准。复核不调用模型、无需网络或第三方库；这些检查不等于人类同行评审。
