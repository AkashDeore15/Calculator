'''My Calculator Test'''
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

# pylint: disable=unnecessary-dunder-call, invalid-name
def test_addition():
    '''Test that addition function works '''
    calc = add(Decimal('1'), Decimal('1'))
    assert calc == Decimal ('2')

def test_subtraction():
    '''Test that subtraction function works '''    
    calc = subtract(Decimal('2'), Decimal('1'))
    assert calc == Decimal('1')

def test_multiply():
    '''Test that multiplication function works '''
    calc = multiply(Decimal('4'),  Decimal('3'))
    assert calc == Decimal('12')

def test_divide():
    '''Test that division function works '''
    calc = divide(Decimal('10.5'), Decimal('10'))
    assert calc == Decimal('1.05')
