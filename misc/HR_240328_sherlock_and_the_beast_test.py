import HR_240328_sherlock_and_the_beast as mf
#python -m unittest HR_240328_sherlock_and_the_beast.py
import unittest

def run(l:int):
    return mf.decentNumber(l)

class TestCases(unittest.TestCase):
    def test_run_returns_correct_value1(self):
        actual = run(1)
        expected = -1
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value2(self):
        actual = run(2)
        expected = -1
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value_len_6(self):
        actual = mf.sherlockBeastNaive(6)
        expected = "555"+"555"
        self.assertNotEqual(actual, -1)
        self.assertEqual(actual, expected)


    def test_run_returns_correct_value_len_11(self):
        actual = mf.sherlockBeastNaive(11)
        expected = "555"+"555"+"333"+"33"
        self.assertNotEqual(actual, -1)
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value4(self):
        #actual = mf.sherlockBeastNaive(14)
        actual = mf.sherlockBeast(14)
        expected = "555"+"555"+"555"+"333"+"33"
        self.assertNotEqual(actual, -1)
        self.assertEqual(actual, expected)