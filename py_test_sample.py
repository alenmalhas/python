# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_method1():
    assert inc(1) == 2

def test_method2():
    assert inc(2) == 3
