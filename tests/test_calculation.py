"""
This module contains the tests for the calculator operations and calculation class.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.operations import add, divide
from calculator.calculation import Calculation

def test_calculation(a, b, operation, expected):
    """Test the Calculation class with various operations."""
    calc = Calculation(a, b, operation)
    assert calc.get_result() == expected,\
          f"Failed to calculate {a} {operation.__name__} {b} = {expected}"

def test_calculation_repr():
    """Test the Calculation class __repr__ method."""
    calc = Calculation(Decimal('1'), Decimal('2'), add)
    assert calc.__repr__() == "Calculation(1, 2, add)",\
          "The __repr__ method failed to get the correct representation of the calculation."

def test_divide_by_zero():
    """Test divide by zero."""
    calc = Calculation(Decimal('101'), Decimal('0'), divide)
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        calc.get_result()
