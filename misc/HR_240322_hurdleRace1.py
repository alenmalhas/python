def hurdleRace1(maxJumpAbility, height):
    maxHudleHeight = max(height)
    diff = maxHudleHeight - maxJumpAbility
    return diff if diff > 0 else 0



#python -m unittest 01_capital_indexes.py
import unittest

def run(maxJumpAbility, heightArr):
    return hurdleRace1(maxJumpAbility, heightArr)


class TestsFormid(unittest.TestCase):
    def test_run_returns_correct_value1(self):
        actual = run(1, [1, 2, 3, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value2(self):
        actual = run(4, [1, 6, 3, 5, 2])
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_run_returns_correct_value3(self):
        actual = run(7, [2, 5, 4, 5, 2])
        expected = 0
        self.assertEqual(actual, expected)