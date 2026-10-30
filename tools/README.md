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
