from decimal import Decimal
from src.commands import Command

class PowerCommand(Command):
    def __init__(self, base: Decimal, exponent: Decimal):
        self.base = base
        self.exponent = exponent
    
    def execute(self):
        # Convert exponent to int for power operation
        exponent_int = int(self.exponent)
        if Decimal(exponent_int) != self.exponent:
            raise ValueError("Exponent must be an integer")
        
        return self.base ** exponent_int
