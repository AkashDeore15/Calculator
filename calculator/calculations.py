from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Return the calculation history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the calculation history."""
        cls.history.clear()
    
    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Return the last calculation."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_last_n_calculations(cls, n: int) -> List[Calculation]:
        """Return the last n calculations."""
        return cls.history[-n:] if cls.history else None

    @classmethod
    def get_first_n_calculations(cls, n: int) -> List[Calculation]:
        """Return the first n calculations."""
        return cls.history[:n] if cls.history else None
    
    @classmethod
    def find_calculations_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Return a list of calculations that match the operation."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
