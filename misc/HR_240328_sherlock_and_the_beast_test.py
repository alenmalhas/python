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

    def test_cases_all_return_correct_result(self):
        dictInputExpectedOutput = { 
            1:"-1", 
            3:"555",
            5:"33333",
            11:"55555533333",
            13:"5553333333333",
            15:"555555555555555"
        }
        for input in dictInputExpectedOutput.keys():
            expected = dictInputExpectedOutput[input]
            with self.subTest("dictInputExpectedOutput tests return True", input=input):
                actual =  mf.sherlockBeastNaive(input)
                self.assertEqual(actual, expected)
