import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_experiment', ROOT / 'tools' / 'audit_experiment.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class EvidenceAuditTests(unittest.TestCase):
    def test_frozen_evidence_reproduces(self):
        data = audit.audit()
        self.assertEqual([r['summary']['final_false_pass'] for r in data['runs']], [0, 0])
        self.assertEqual([r['length_limited_calls'] for r in data['runs']], [1, 1])

    def test_corrupted_summary_is_rejected(self):
        path = ROOT / 'experiment' / 'runs' / 'pilot-summary.json'
        original = Path.read_text
        def tampered(target, *args, **kwargs):
            text = original(target, *args, **kwargs)
            if target == path:
                obj = json.loads(text)
                obj['final_false_pass'] = 99
                return json.dumps(obj)
            return text
        with patch.object(Path, 'read_text', tampered):
            with self.assertRaisesRegex(ValueError, 'summary mismatch'):
                audit.audit_run(ROOT, 'pilot.json', 'runner.py')

    def test_hash_change_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'experiment').mkdir()
            (root / 'evidence').write_text('changed')
            (root / 'experiment' / 'SHA256SUMS').write_text('0' * 64 + '  evidence\n')
            with self.assertRaisesRegex(ValueError, 'Hash mismatch'):
                audit.check_manifest(root)

    def test_report_cannot_overwrite_evidence(self):
        for name in ['experiment/runs/pilot.json', 'experiment/tasks.json', 'experiment/SHA256SUMS', 'tools/audit_experiment.py']:
            with self.subTest(path=name), self.assertRaisesRegex(ValueError, 'evidence paths are forbidden'):
                audit.report_destination(ROOT / name)
        self.assertEqual(audit.report_destination(ROOT / 'experiment/audit/fresh.json'), ROOT / 'experiment/audit/fresh.json')

    def test_python_boolean_semantics_and_short_circuit(self):
        for version in ['runner.py', 'runner_v2.py']:
            runner = audit.load_runner(version)
            for expression, x, expected in [('x and 7', 2, 7), ('x and 7', 0, 0), ('x or 7', 2, 2), ('x or 7', 0, 7), ('0 and (1 // 0)', 2, 0), ('1 or (1 // 0)', 2, 1)]:
                with self.subTest(version=version, expression=expression, x=x):
                    self.assertEqual(runner.evaluate(expression, x), expected)

if __name__ == '__main__':
    unittest.main()
