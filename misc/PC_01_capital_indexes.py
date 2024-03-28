#python -m unittest 01_capital_indexes.py
import unittest


def capital_indexes(input):
    return capital_indexes3(input)

def capital_indexes1(input):
    capsArr = []
    for i in range(len(input)):
        if input[i].isupper():
            capsArr.append(i)
    return capsArr

# naive solution
def capital_indexes2(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

# shorter version
def capital_indexes3(input:str):
    uppercase = input.upper()
    return [i for i in range(len(input)) if input[i] in uppercase]

# you can also use the .isupper() string method.


class TestsForcapital_indexes(unittest.TestCase):
    def test_capital_indexes_returns_correct_value(self):
        actual = capital_indexes("HeLlO")
        expected = [0,2,4]
        self.assertEqual(actual, expected)