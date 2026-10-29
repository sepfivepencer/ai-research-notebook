import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools' / 'check_notebook.py'
spec = importlib.util.spec_from_file_location('check_notebook', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class NotebookTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'data' / 'notebook.json').read_text(encoding='utf-8'))

    def test_repository_record_is_valid(self):
        self.assertEqual(checker.validate(self.data), [])

    def test_duplicate_source_id_is_rejected(self):
        self.data['sources'].append(copy.deepcopy(self.data['sources'][0]))
        self.assertTrue(any('重复 ID' in e for e in checker.validate(self.data)))

    def test_unknown_claim_source_is_rejected(self):
        self.data['claims'][0]['source_ids'] = ['missing-paper']
        self.assertTrue(any('未知来源' in e for e in checker.validate(self.data)))

    def test_unsupported_confidence_is_rejected(self):
        self.data['claims'][0]['status'] = 'probably'
        self.assertTrue(any('status' in e for e in checker.validate(self.data)))

    def test_arxiv_link_and_identifier_must_agree(self):
        self.data['sources'][1]['arxiv'] = '2501.12345'
        self.assertTrue(any('不一致' in e for e in checker.validate(self.data)))

    def test_unverified_arxiv_can_be_null_for_conference_url(self):
        self.data['sources'][0]['arxiv'] = None
        self.assertEqual(checker.validate(self.data), [])

    def test_invalid_date_is_rejected(self):
        self.data['sources'][0]['checked_at'] = '2026-02-30'
        self.assertTrue(any('有效 ISO 日期' in e for e in checker.validate(self.data)))

    def test_credentials_and_non_http_urls_are_rejected(self):
        credentials_example = 'https://' + 'example-user:example-pass@example.org'
        for url in ['file:///etc/passwd', credentials_example, 'https://bad host.org']:
            with self.subTest(url=url):
                self.data['sources'][0]['url'] = url
                self.assertTrue(any('.url' in e for e in checker.validate(self.data)))

    def test_wrong_nested_shapes_report_errors_without_crashing(self):
        for path, bad in [('sources', [None]), ('candidates', [False]), ('claims', [0])]:
            with self.subTest(path=path):
                data = copy.deepcopy(self.data)
                data[path] = bad
                self.assertTrue(checker.validate(data))
        self.assertTrue(checker.validate([]))

    def test_non_string_enum_values_are_reported(self):
        self.data['sources'][0]['kind'] = []
        self.data['claims'][0]['status'] = {}
        self.assertTrue(checker.validate(self.data))

    def test_stage_cannot_skip_or_select_nonexistent_topic(self):
        self.data['research']['next_stage'] = 4
        self.data['research']['selected_topic'] = 'not-a-candidate'
        errors = checker.validate(self.data)
        self.assertTrue(any('next_stage' in e for e in errors))
        self.assertTrue(any('selected_topic' in e for e in errors))

    def test_boolean_is_not_a_publication_year(self):
        self.data['sources'][0]['year'] = True
        self.assertTrue(any('.year' in e for e in checker.validate(self.data)))

    def test_cli_works_from_another_directory(self):
        with tempfile.TemporaryDirectory() as cwd:
            result = subprocess.run([sys.executable, str(SCRIPT), 'check'], cwd=cwd,
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('不证明', result.stdout)

    def test_cli_invalid_json_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as cwd:
            path = Path(cwd) / 'broken.json'
            path.write_text('{broken', encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), 'check', '--file', str(path)],
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn('Traceback', result.stderr)

    def test_reading_list_lists_all_source_ids(self):
        text = checker.reading_list(self.data)
        for source in self.data['sources']:
            self.assertIn(source['id'], text)
            self.assertIn(source['url'], text)


if __name__ == '__main__':
    unittest.main()
