def double_letters1(input:str):
    for i in range(len(input)):
        if i != 0 and input[i-1] == input[i]:
            return True
    return False

# naive solution
def double_letters2(input):
    for i in range(len(input) - 1):
        letter1 = input[i]
        letter2 = input[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters3(input):
    return any([a == b for a, b in zip(input, input[1:])])

def double_letters4(input):
    zipObj = zip(input, input[1:])
    return any([a == b for a, b in zipObj])


def double_letters(p1: str):
    r1 = double_letters4(p1)
    return r1

#python -m unittest 01_capital_indexes.py
import unittest
class TestsFormid(unittest.TestCase):
    def test_returns_true(self):
        actual = double_letters("hello")
        self.assertTrue(actual)

    def test_returns_false2(self):
        actual = double_letters("nono")
        self.assertFalse(actual)

    def test_returns_true2(self):
        actual = double_letters("correlation")
        self.assertTrue(actual)


    def test_cases_all_return_correct_result(self):
        doubleLetterList = ["hello", "123aa321", "abcDDefg"]
        for i in range(len(doubleLetterList)):
            oneInput = doubleLetterList[i]
            with self.subTest(input=oneInput):
                print(f"{oneInput}: {type(oneInput)}")
                actual =  double_letters(input)
                self.assertTrue(actual)
'''
        singleLetterList = ["abc", "abab", "abcabc"]
        for i in range(len(singleLetterList)):
            oneInput = singleLetterList[i]
            with self.subTest(input=oneInput):
                actual =  double_letters(input)
                self.assertFalse(actual)
'''
