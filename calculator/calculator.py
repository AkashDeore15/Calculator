"""A simple calculator to perform basic arithmetic operations."""
class Calculator:
    """A simple calculator to perform basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the division of two numbers. Handles division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
