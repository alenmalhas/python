
def only_ints1(p1, p2):
    if type(p1) == int and type(p2) == int:
        return True
    return False

def only_ints2(a,b):
    return type(a) == int and type(b) == int

def only_ints(p1, p2):
    r1 =  only_ints1(p1, p2)
    return r1

#python -m unittest 01_capital_indexes.py
import unittest
class TestsFormid(unittest.TestCase):
    def test_only_ints_returns_false(self):
        actual = only_ints("a", 1)
        self.assertFalse(actual)

    def test_only_ints_returns_false2(self):
        actual = only_ints(1, True)
        self.assertFalse(actual)

    def test_only_ints_returns_true(self):
        actual = only_ints(2, 1)
        self.assertTrue(actual)

    # def test_only_ints_returns_between_1_and_100_ten_times(self):
    #     for i in range(10):
    #         with self.subTest(input=input):
    #             actual = only_ints()
    #             self.assertTrue(actual >= 0 and actual <= 100)
