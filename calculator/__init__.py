from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    
    @staticmethod
    def _get_calculations(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and Perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    
    @staticmethod
    def add(a:Decimal, b:Decimal) -> Decimal:
        return Calculator._get_calculations(a, b, add)
    
    @staticmethod
    def subtract(a:Decimal, b:Decimal) -> Decimal:
        return Calculator._get_calculations(a, b, subtract)
    
    @staticmethod
    def multiply(a:Decimal, b:Decimal) -> Decimal:
        return Calculator._get_calculations(a, b, multiply)

    @staticmethod
    def divide(a:Decimal, b:Decimal) -> Decimal:
        return Calculator._get_calculations(a, b, divide)
