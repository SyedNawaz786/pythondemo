# test_factorial.py

from your_script_name import factorial

def test_factorial_positive_number():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_large_number():
    assert factorial(10) == 3628800
