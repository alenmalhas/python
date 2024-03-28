import random

def random_number1():
    r = random.randint(0, 100)
    return r
    
def random_number2():
    r = random.randrange(0, 100, 2)
    return r

def random_number3():
    r = random.randrange(0, 100, 5)
    return r

def random_number():
    r1 =  random_number3()
    print(f'Generated random no: {r1}')
    return r1

#python -m unittest 01_capital_indexes.py
import unittest
class TestsFormid(unittest.TestCase):
    def test_random_number_returns_between_1_and_100(self):
        actual = random_number()
        self.assertTrue(actual >= 0 and actual <= 100)

    def test_random_number_returns_between_1_and_100_ten_times(self):
        for i in range(10):
            with self.subTest(input=input):
                actual = random_number()
                self.assertTrue(actual >= 0 and actual <= 100)
