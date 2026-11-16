#!/usr/bin/env python3
"""Read-only offline audit of preserved runs; never calls a model or rewrites evidence."""
import argparse
import ast
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import os

ROOT = Path(__file__).resolve().parents[1]


def load_runner(name, root=ROOT):
    spec = importlib.util.spec_from_file_location(name, root / 'experiment' / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def independent_reference(task, x):
    """Alternate finite-domain definitions, separate from the historical ref implementation."""
    refs = {
        'abs': lambda n: max(n, -n),
        'sign': lambda n: (n > 0) - (n < 0),
        'clamp': lambda n: sorted((0, n, 10))[1],
        'even': lambda n: int(n in range(-20, 21, 2)),
        'floor_even': lambda n: max(v for v in range(-22, 23, 2) if v <= n),
        'three_floor': lambda n: max(v for v in range(-10, 11) if 3 * v <= n),
        'odd_double': lambda n: n + n if n % 2 else sum(1 for _ in range(abs(n))) // 2 * (-1 if n < 0 else 1),
        'square_cap': lambda n: 100 if abs(n) >= 10 else n * n,
        'distance_five': lambda n: min(abs(n-v) for v in range(-25, 26, 5)),
        'digits': lambda n: 2 if n <= -10 or n >= 10 else 1,
    }
    return refs[task](x)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_manifest(root):
    path = root / 'experiment' / 'SHA256SUMS'
    for line in path.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        require(hashlib.sha256((root / rel).read_bytes()).hexdigest() == digest, 'Hash mismatch: ' + rel)


def audit_run(root, filename, runner_name):
    mod = load_runner(runner_name, root)
    path = root / 'experiment' / 'runs' / filename
    data = json.loads(path.read_text())
    tasks = json.loads((root / 'experiment' / 'tasks.json').read_text())
    require(data.get('complete') is True, filename + ': incomplete run')
    require([r['task'] for r in data['tasks']] == tasks, filename + ': task order/spec mismatch')
    categories = Counter()
    calls = []
    rows = []
    boolop_candidates = 0
    for rec in data['tasks']:
        task = rec['task']['id']
        tests, rejected = mod.checked_tests(rec['test_call'].get('parsed'))
        require(tests == rec['tests'] and rejected == rec['rejected_tests'], task + ': test filtering mismatch')
        require(1 <= len(rec['rounds']) <= 3, task + ': invalid round count')
        calls.extend([rec['initial_call'], rec['test_call']])
        bad_tests = [t for t in tests if t['expected'] != independent_reference(task, t['input'])]
        require(bad_tests == rec['test_oracle_disagreements'], task + ': oracle mismatch')
        expression = (rec['initial_call'].get('parsed') or {}).get('expression', '')
        for i, rnd in enumerate(rec['rounds']):
            require(rnd['round'] == i and rnd['expression'] == expression, task + ': generation/round link mismatch')
            checks = mod.selfcheck(expression, tests)
            fingerprint = lambda seq: [(c['input'], c['expected'], c['pass'], c['actual'].get('value'), 'error' in c['actual']) for c in seq]
            require(fingerprint(checks) == fingerprint(rnd['self_checks']), task + ': self-check mismatch')
            failures = []
            errors = []
            try:
                boolop_candidates += int(any(isinstance(n, ast.BoolOp) for n in ast.walk(ast.parse(expression, mode='eval'))))
            except SyntaxError:
                pass
            for x in range(-20, 21):
                expected = independent_reference(task, x)
                require(expected == mod.ref(task, x), task + ': reference cross-check mismatch')
                actual = mod.result(expression, x)
                if 'error' in actual:
                    errors.append(actual['error'])
                if 'error' in actual or actual.get('value') != expected:
                    failures.append({'x': x, 'expected': expected, 'actual': actual})
            # Error messages can differ across Python versions; compare failing inputs, expected values, values/error presence.
            saved = rnd['independent_failures']
            normalize = lambda seq: [(f['x'], f['expected'], f['actual'].get('value'), 'error' in f['actual']) for f in seq]
            require(normalize(failures) == normalize(saved), task + ': independent failure list mismatch')
            self_pass = bool(tests) and all(c['pass'] for c in checks)
            external_pass = not failures
            require(rnd['independent_failure_count'] == len(failures), task + ': failure count mismatch')
            require((rnd['self_all_pass'], rnd['independent_all_pass'], rnd['false_pass']) == (self_pass, external_pass, self_pass and not external_pass), task + ': flags mismatch')
            if i == len(rec['rounds']) - 1:
                require('repair_call' not in rnd and (i == 2 or not tests or self_pass), task + ': final stopping rule mismatch')
            if i < len(rec['rounds']) - 1:

                require(tests and not self_pass and 'repair_call' in rnd, task + ': stopping rule mismatch')
                calls.append(rnd['repair_call'])
                expression = (rnd['repair_call'].get('parsed') or {}).get('expression', '')
        if not errors:
            category = 'correct' if external_pass else 'semantic_wrong'
        else:
            try:
                ast.parse(rec['rounds'][-1]['expression'], mode='eval')
                category = 'output_type_reject' if all(e == 'result_not_integer' for e in errors) else 'unsupported_or_runtime_error'
            except SyntaxError:
                category = 'syntax_reject'
        categories[category] += 1
        rows.append({'task': task, 'final_category': category, 'self_tests': len(tests), 'wrong_test_expectations': len(bad_tests), 'initial_independent_failures': rec['rounds'][0]['independent_failure_count'], 'final_independent_failures': len(failures)})
    first = [t['rounds'][0] for t in data['tasks']]
    last = [t['rounds'][-1] for t in data['tasks']]
    summary = {'tasks': len(rows), 'completed': True, 'with_usable_tests': sum(bool(t['tests']) for t in data['tasks']),
        'initial_self_pass': sum(r['self_all_pass'] for r in first), 'final_self_pass': sum(r['self_all_pass'] for r in last),
        'initial_independent_pass': sum(r['independent_all_pass'] for r in first), 'final_independent_pass': sum(r['independent_all_pass'] for r in last),
        'initial_false_pass': sum(r['false_pass'] for r in first), 'final_false_pass': sum(r['false_pass'] for r in last),
        'tasks_with_bad_test_oracles': sum(bool(t['test_oracle_disagreements']) for t in data['tasks']), 'repairs': sum(len(t['rounds'])-1 for t in data['tasks'])}
    require(summary == json.loads(path.with_name(path.stem + '-summary.json').read_text()), filename + ': summary mismatch')
    for call in calls:
        try:
            reparsed = json.loads(call['raw'])
        except (ValueError, TypeError):
            require(call.get('parsed') is None, filename + ': invalid JSON has a parsed value')
        else:
            require(reparsed == call.get('parsed'), filename + ': raw/parsed mismatch')
    return {'file': filename, 'recorded_python': data['python'], 'model': data['model'], 'summary': summary,
        'final_categories': dict(sorted(categories.items())), 'calls': len(calls), 'api_errors': sum('error' in c for c in calls),
        'length_limited_calls': sum(c.get('done_reason') == 'length' for c in calls),
        'bad_json_calls': sum(c.get('parsed') is None for c in calls), 'historical_boolop_candidates': boolop_candidates,
        'accepted_test_assertions': sum(len(t['tests']) for t in data['tasks']), 'wrong_test_assertions': sum(len(t['test_oracle_disagreements']) for t in data['tasks']),
        'tasks': rows}


def audit(root=ROOT):
    check_manifest(root)
    return {'evidence_date': '2026-10-30', 'audit_date': '2026-11-16', 'audit_python': sys.version.split()[0],
        'scope': 'Offline recomputation and alternate reference implementation; no model regeneration or human peer review.',
        'original_research_goal_achieved': False,
        'runs': [audit_run(root, 'pilot.json', 'runner.py'), audit_run(root, 'pilot-v2.json', 'runner_v2.py')]}


def report_destination(path, root=ROOT):
    target = path.resolve()
    allowed = (root / 'experiment' / 'audit').resolve()
    require(target.parent == allowed and target.suffix == '.json', '--report must be a JSON file directly inside experiment/audit; evidence paths are forbidden')
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, help='Write derived JSON directly inside experiment/audit; evidence paths are rejected.')
    args = parser.parse_args()
    try:
        destination = report_destination(args.report) if args.report else None
        result = audit()
    except (ValueError, KeyError, OSError, TypeError) as exc:
        print('AUDIT FAILED: ' + str(exc), file=sys.stderr)
        return 1
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=destination.parent, delete=False) as temporary:
            temporary.write(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
            temp_path = Path(temporary.name)
        os.replace(temp_path, destination)
    for r in result['runs']:
        print(r['file'] + ': PASS; calls=' + str(r['calls']) + '; length_limited=' + str(r['length_limited_calls']) + '; categories=' + json.dumps(r['final_categories']))
    print('Evidence hashes, historical summaries, traces, and 410 task-input reference combinations per runner verified. No model called.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
