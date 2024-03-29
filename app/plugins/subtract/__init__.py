import sys
import logging
from app.commands import Command
from app.calculation_history import CalculationHistory

class SubtractCommand(Command):
    def execute(self, args):
        args_list = args.split()

        # Check if any arguments were provided
        if not args:
            logging.warning("Subtract command invoked without arguments.")
            print("Usage: subtract <number1> <number2>")
            return
        
        # Ensure exactly two arguments are provided
        if len(args_list) != 2:
            logging.warning("Subtract command requires exactly two arguments.")
            print("Usage: subtract <number1> <number2>")
            return

        try:
            # Convert arguments to float and attempt subtraction
            a, b = map(float, args_list)
            result = a - b
            print(f"{a} - {b} = {result}")
            
            # Log the operation before attempting to record it in history
            logging.debug(f"Recording subtraction to history: {a} - {b} = {result}")
            CalculationHistory().add_record(f"{a} - {b}", result)
            logging.info(f"Subtraction operation recorded successfully: {a} - {b} = {result}")

        except ValueError:
            logging.error("Subtract command received invalid arguments.", exc_info=True)
            print("Error: Please provide two numbers separated by a space.")
