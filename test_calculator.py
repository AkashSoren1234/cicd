# test_calculator.py
# pytest looks for files named test_*.py and runs functions named test_*

import pytest
from calculator import add, subtract, multiply, divide
# ↑ imports our 4 functions from calculator.py (must be in the same folder)

def test_add():
    assert add(2, 3) == 5          # 2 + 3 must equal 5; if not, test FAILS

def test_subtract():
    assert subtract(10, 4) == 6    # 10 - 4 must equal 6

def test_multiply():
    assert multiply(3, 4) == 12    # 3 × 4 must equal 12

def test_divide():
    assert divide(10, 2) == 5.0    # 10 ÷ 2 must equal 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):  # this block MUST raise a ValueError
        divide(5, 0)                 # if it doesn't raise, the test FAILS
