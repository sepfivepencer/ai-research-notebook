# 文献记录检查工具

从仓库根目录运行：

```bash
python3 tools/check_notebook.py check
python3 tools/check_notebook.py reading-list
python3 tools/check_notebook.py check --file path/to/notebook.json
```

`check` 返回 0 表示记录结构和引用关系通过，返回 1 表示输入或验证失败。错误输出到 stderr。

`reading-list` 先运行相同检查，再把阅读清单写到 stdout；可用终端重定向保存：

```bash
python3 tools/check_notebook.py reading-list > reading-list.md
```

默认数据路径相对工具文件定位，从其他工作目录运行也可使用；显式 `--file` 相对当前工作目录。

## 检查范围

- 顶层结构和版本字段。
- 当前阶段、阶段门禁和候选选择是否一致。
- 文献 ID 唯一性；题名、作者、年份、发表类型、venue、核验日期和范围。
- HTTP(S) URL 与 arXiv 编号的基本格式；arXiv URL 的编号是否与填写编号一致。
- 主张 ID、置信状态和引用来源是否存在。

## 边界

程序不联网，也不判断内容真实性。可解析的 URL 可能已失效，元数据也可能被填错；“已验证”只是填写的状态，必须靠人工与证据支持。请把工具理解为填表与引用关系检查器。

`checked_scope` 记录本次人工核验范围。各条目的范围可能不同；`metadata_and_abstract` 仅表示核验了题录与摘要，其他范围说明所读部分。所有条目都不表示独立复现。


## 结项离线审计

`python3 tools/audit_experiment.py` 检查保存的真实实验记录，不调用 Ollama、不访问网络、不修改原始数据。`--report experiment/audit/verification.json` 可更新派生报告；参数会拒绝原始证据路径，并使用原子替换保护已有数据。

`python3 tools/build_report_pdf.py` 从 `paper/研究报告.md` 重新生成报告 PDF。仅此可选命令需要第三方 `reportlab` 和包含中文的 TrueType 字体；可用 `REPORT_CHINESE_FONT` 指定字体路径。离线审计和 CI 不需要这两项依赖。PDF 使用嵌入字体子集，方便下载阅读。
