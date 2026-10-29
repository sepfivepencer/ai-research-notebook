#!/usr/bin/env python3
"""Check local notebook structure and references; never verify scientific truth."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

DEFAULT_FILE = Path(__file__).resolve().parents[1] / 'data' / 'notebook.json'
STATUSES = {'已验证', '有依据的推断', '待验证'}
KINDS = {'conference', 'findings', 'journal', 'workshop', 'preprint'}
ARXIV = re.compile(r'\d{4}\.\d{4,5}(?:v[1-9]\d*)?\Z')


def validate(document):
    """Return actionable errors for JSON data, including malformed input shapes."""
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    def records(key):
        value = document.get(key)
        if not isinstance(value, list) or not value:
            errors.append(f'{key}: 必须是非空数组')
            return []
        return value

    def unique_id(record, seen, label):
        identifier = record.get('id')
        if not nonempty(identifier):
            errors.append(f'{label}.id: 必须是非空字符串')
        elif identifier in seen:
            errors.append(f'{label}.id: 重复 ID {identifier}')
        else:
            seen.add(identifier)

    if not isinstance(document, dict):
        return ['顶层必须是 JSON 对象']
    require(type(document.get('schema_version')) is int and document['schema_version'] == 1,
            'schema_version: 必须是整数 1')

    source_ids = set()
    for index, source in enumerate(records('sources')):
        label = f'sources[{index}]'
        if not isinstance(source, dict):
            errors.append(f'{label}: 必须是对象')
            continue
        unique_id(source, source_ids, label)
        for key in ('title', 'venue', 'checked_scope'):
            require(nonempty(source.get(key)), f'{label}.{key}: 必须是非空字符串')
        authors = source.get('authors')
        require(isinstance(authors, list) and bool(authors) and all(nonempty(a) for a in authors),
                f'{label}.authors: 必须是非空作者字符串数组')
        year = source.get('year')
        require(type(year) is int and 1900 <= year <= date.today().year,
                f'{label}.year: 必须是 1900 到当前年份之间的整数')
        require(isinstance(source.get('kind'), str) and source['kind'] in KINDS,
                f'{label}.kind: 不支持的发表类型')
        try:
            checked = date.fromisoformat(source.get('checked_at', ''))
            require(checked <= date.today(), f'{label}.checked_at: 核验日期不能在未来')
        except (TypeError, ValueError):
            errors.append(f'{label}.checked_at: 必须是有效 ISO 日期')
        raw_url = source.get('url')
        parsed = None
        try:
            parsed = urlparse(raw_url if isinstance(raw_url, str) else '')
            valid = (parsed.scheme in {'http', 'https'} and bool(parsed.hostname)
                     and not parsed.username and not parsed.password
                     and isinstance(raw_url, str) and not any(c.isspace() for c in raw_url))
        except ValueError:
            valid = False
        require(valid, f'{label}.url: 必须是无凭据的 HTTP(S) URL')
        arxiv = source.get('arxiv')
        if arxiv is not None:
            require(isinstance(arxiv, str) and bool(ARXIV.fullmatch(arxiv)),
                    f'{label}.arxiv: 编号格式无效；未核实时填写 null')
        if valid and parsed.hostname == 'arxiv.org' and parsed.path.startswith('/abs/'):
            require(parsed.path.removeprefix('/abs/').removesuffix('/') == arxiv,
                    f'{label}.arxiv: 与 arXiv URL 中的编号不一致')

    candidate_ids = set()
    for index, candidate in enumerate(records('candidates')):
        label = f'candidates[{index}]'
        if not isinstance(candidate, dict):
            errors.append(f'{label}: 必须是对象')
            continue
        unique_id(candidate, candidate_ids, label)
        require(nonempty(candidate.get('label')), f'{label}.label: 必须是非空字符串')
        require(isinstance(candidate.get('novelty_status'), str)
                and candidate['novelty_status'] in STATUSES,
                f'{label}.novelty_status: 不支持的状态')

    research = document.get('research')
    if not isinstance(research, dict):
        errors.append('research: 必须是对象')
    else:
        completed = research.get('completed_stage')
        require(type(completed) is int and 0 <= completed <= 6,
                'research.completed_stage: 必须是 0 到 6 之间的整数')
        if type(completed) is int and 0 <= completed <= 6:
            expected_next = completed + 1 if completed < 6 else None
            require(research.get('next_stage') == expected_next
                    and type(research.get('next_stage')) is type(expected_next),
                    'research.next_stage: 必须与已完成阶段衔接')
        require(type(research.get('next_stage_confirmed')) is bool,
                'research.next_stage_confirmed: 必须是布尔值')
        selected = research.get('selected_topic')
        require(selected is None or (isinstance(selected, str) and selected in candidate_ids),
                'research.selected_topic: 必须为空或引用现有候选 ID')

    claim_ids = set()
    for index, claim in enumerate(records('claims')):
        label = f'claims[{index}]'
        if not isinstance(claim, dict):
            errors.append(f'{label}: 必须是对象')
            continue
        unique_id(claim, claim_ids, label)
        for key in ('text', 'scope'):
            require(nonempty(claim.get(key)), f'{label}.{key}: 必须是非空字符串')
        require(isinstance(claim.get('status'), str) and claim['status'] in STATUSES,
                f'{label}.status: 必须是三个置信状态之一')
        references = claim.get('source_ids')
        if not isinstance(references, list):
            errors.append(f'{label}.source_ids: 必须是数组')
            continue
        for reference in references:
            require(isinstance(reference, str) and reference in source_ids,
                    f'{label}.source_ids: 未知来源 {reference!r}')
    return errors


def reading_list(document):
    lines = ['# 阅读清单', '', '核验范围为记录所填范围；不代表独立复现。', '']
    for source in document['sources']:
        authors = '、'.join(source['authors'])
        identifier = f"arXiv:{source['arxiv']}" if source['arxiv'] else 'arXiv 号未核实'
        lines += [f"## {source['id']} · {source['title']}", '',
                  f"{authors}，{source['year']}，{source['venue']}（{source['kind']}）。{identifier}。",
                  f"核验：{source['checked_at']}，范围：{source['checked_scope']}。", '',
                  f"[一手来源]({source['url']})", '']
    return '\n'.join(lines).rstrip()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('check', 'reading-list'))
    parser.add_argument('--file', type=Path, default=DEFAULT_FILE)
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.file.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f'无法读取记录：{exc}', file=sys.stderr)
        return 1
    errors = validate(document)
    if errors:
        for error in errors:
            print(f'错误：{error}', file=sys.stderr)
        return 1
    if args.command == 'reading-list':
        print(reading_list(document))
    else:
        print(f"通过：{len(document['sources'])} 篇来源、{len(document['claims'])} 条主张。")
        print('仅检查记录结构与引用关系；不证明论文真实性、主张正确性或研究新颖性。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
