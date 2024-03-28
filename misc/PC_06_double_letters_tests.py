import PC_06_double_letters as dl

#python -m unittest 01_capital_indexes.py
import unittest
class TestsFormid(unittest.TestCase):
    def test_returns_true(self):
        actual = dl.double_letters("hello")
        self.assertTrue(actual)

    def test_returns_false2(self):
        actual = dl.double_letters("nono")
        self.assertFalse(actual)

    def test_returns_true2(self):
        actual = dl.double_letters("correlation")
        self.assertTrue(actual)


    def test_cases_all_return_correct_result(self):
        doubleLetterList = ["hello", "123aa321", "abcDDefg"]
        for i in range(len(doubleLetterList)):
            oneInput = doubleLetterList[i]
            with self.subTest("Message for this subtest", oneInput=oneInput):
                print(f"{oneInput}: {type(oneInput)}")
                actual =  dl.double_letters(oneInput)
                self.assertTrue(actual)
'''
        singleLetterList = ["abc", "abab", "abcabc"]
        for i in range(len(singleLetterList)):
            oneInput = singleLetterList[i]
            with self.subTest(input=oneInput):
                actual =  double_letters(input)
                self.assertFalse(actual)
'''
