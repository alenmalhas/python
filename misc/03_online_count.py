def online_count1(statuses):
    onlineArr = [k for k in statuses.keys() if statuses[k] == "online"]
    return len(onlineArr)
    
#python -m unittest 01_capital_indexes.py
import unittest

def online_count(input):
    return online_count1(input)


class TestsFormid(unittest.TestCase):
    def test_mid_returns_correct_value1(self):
        statuses = {
            "Alice": "online",
            "Bob": "offline",
            "Eve": "online",
        }
        actual = online_count(statuses)
        expected = 2
        self.assertEqual(actual, expected)

    def test_mid_returns_correct_value2(self):
        statuses = {
            "Alice": "online",
            "Bob": "online",
            "Eve": "online",
        }
        actual = online_count(statuses)
        expected = 3
        self.assertEqual(actual, expected)

    def test_online_count_with_multiple_test_cases_returns_correct(self):
        tests = [
            (2, {
                    "Alice": "online",
                    "Bob": "offline",
                    "Eve": "online",
                }),
            (3, {
                    "Alice": "online",
                    "Bob": "online",
                    "Eve": "online",
                }),
        ]
        for expected, input in tests:
            with self.subTest(input=input):
                self.assertEqual(online_count(input), expected)