"""
This file contains the tests for the calculator module.
"""
import pytest
from src.calculator import Calculator

def test_add():
    """Test the add method"""
    assert Calculator.add(3, 2) == 5
    assert Calculator.add(-1, -1) == -2
    assert Calculator.add(0, 0) == 0

def test_subtract():
    """Test the subtract method"""
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(-3, -7) == 4

def test_multiply():
    """Test the multiply method"""
    assert Calculator.multiply(3, 2) == 6
    assert Calculator.multiply(-1, 5) == -5
    assert Calculator.multiply(0, 10) == 0

def test_divide():
    """Test the divide method"""
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(-10, 2) == -5

    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(5, 0)
