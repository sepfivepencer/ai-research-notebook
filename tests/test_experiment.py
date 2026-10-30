import importlib.util
from pathlib import Path
import unittest
spec = importlib.util.spec_from_file_location('pilot', Path(__file__).resolve().parents[1] / 'experiment' / 'runner.py')
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)

class ExperimentTests(unittest.TestCase):
    def test_reference_boundaries(self):
        cases = {
            'abs': {-20:20, 0:0, 3:3}, 'sign': {-1:-1, 0:0, 1:1},
            'clamp': {-1:0, 0:0, 10:10, 11:10}, 'even': {-3:0, -2:1, 0:1},
            'floor_even': {-3:-4, -2:-2, 1:0}, 'three_floor': {-4:-2, -3:-1, 2:0},
            'odd_double': {-3:-6, -2:-1, 3:6}, 'square_cap': {-11:100, -9:81, 0:0},
            'distance_five': {-6:1, -3:2, 0:0, 3:2, 6:1}, 'digits': {-20:2, -9:1, 0:1, 10:2}}
        for task, examples in cases.items():
            for x,y in examples.items():
                with self.subTest(task=task,x=x): self.assertEqual(pilot.ref(task,x),y)
    def test_expression_safety_and_results(self):
        self.assertEqual(pilot.evaluate('x if x >= 0 else -x', -3), 3)
        self.assertEqual(pilot.evaluate('min(x*x, 100)', 11),100)
        for text in ['__import__("os").system("id")', 'x.__class__', '2**100', '[x for x in range(9)]', 'x == 2']:
            with self.subTest(text=text), self.assertRaises(ValueError): pilot.evaluate(text,2)
    def test_test_filter(self):
        tests,rejected=pilot.checked_tests({'tests':[{'input':3,'expected':5},{'input':True,'expected':1},{'input':21,'expected':0}]})
        self.assertEqual(tests,[{'input':3,'expected':5}]); self.assertEqual(len(rejected),2)

if __name__=='__main__': unittest.main()
