import HR_240325_angryProfessor as ap
#python -m unittest 01_capital_indexes.py
import unittest

def is_class_cancelled(treshold, arrivalsArray):
    return ap.angryProfessor1(treshold, arrivalsArray)

class TestCases(unittest.TestCase):
    def test_run_returns_correct_value1(self):
        actual = is_class_cancelled(3, [-2, -1, 0, 1, 2])
        expected = "NO"
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value2(self):
        actual = is_class_cancelled(3, [-1, -3, 4, 2])
        expected = "YES"
        self.assertEqual(actual, expected)
    
    def test_run_returns_correct_value3(self):
        actual = is_class_cancelled(2, [0, -1, 2, 1])
        expected = "NO"
        self.assertEqual(actual, expected)
