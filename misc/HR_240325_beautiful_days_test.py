import HR_240325_beautiful_days as bd
#python -m unittest 01_capital_indexes.py
import unittest

def run(start, end, divisor):
    return bd.beautifulDays(start, end, divisor)

class TestCases(unittest.TestCase):
    def test_run_returns_correct_value1(self):
        actual = run(20, 23, 6)
        expected = 2
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value2(self):
        actual = run(13, 45, 3)
        expected = 33
        self.assertEqual(actual, expected)