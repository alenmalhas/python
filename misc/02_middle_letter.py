def mid1(input):
    if (len(input) % 2 == 0):
        return ""
    else:
        indexMidChar = (len(input) // 2) 
        return input[indexMidChar]

# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid2(input):
    if len(input) % 2 == 0:
        return ""
    return input[len(input)//2]

#python -m unittest 01_capital_indexes.py
import unittest

def mid(input):
    return mid1(input)


class TestsFormid(unittest.TestCase):
    def test_mid_returns_correct_value1(self):
        actual = mid("HeLlO")
        expected = "L"
        self.assertEqual(actual, expected)

    def test_mid_returns_correct_value2(self):
        actual = mid("abc")
        expected = "b"
        self.assertEqual(actual, expected)