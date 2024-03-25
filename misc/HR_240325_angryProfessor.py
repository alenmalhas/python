import numpy as np

def angryProfessor1(k, a):
    on_time_attendees = [l for l in a if l <= 0]
    ota_count = len(on_time_attendees)
    return "NO" if ota_count >= k else "YES"
    
def angryProfessor2(min_ota, attendees_arrival_times):
    #return "YES" if sum(x <= 0 for x in a) < k else "NO"
    count=0
    for i in range(len(attendees_arrival_times)):
        if(attendees_arrival_times[i]<=0):
            count+=1
    if(count>=min_ota):
        return "NO"
    return "YES"


'''
#python -m unittest 01_capital_indexes.py
import unittest

def run(treshold, arrivalsArray):
    return angryProfessor1(treshold, arrivalsArray)


class TestCases(unittest.TestCase):
    def test_run_returns_correct_value1(self):
        actual = run(3, [-2, -1, 0, 1, 2])
        expected = "YES"
        self.assertEqual(actual, expected)

    def test_run_returns_correct_value2(self):
        actual = run(3, [-1, -3, 4, 2])
        expected = "YES"
        self.assertEqual(actual, expected)
    
    def test_run_returns_correct_value3(self):
        actual = run(2, [0, -1, 2, 1])
        expected = "NO"
        self.assertEqual(actual, expected)
'''