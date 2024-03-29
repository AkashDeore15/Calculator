import logging
from app.commands import Command
from app.calculation_history import CalculationHistory

class AddCommand(Command):
    def execute(self, args):
        args_list = args.split()
        
        if not args:
            logging.warning("Add command invoked without arguments.")
            print("Usage: add <number1> <number2>")
            return
        
        if len(args_list) != 2:
            logging.warning("Add command requires exactly two arguments.")
            print("Usage: add <number1> <number2>")
            return

        try:
            a, b = map(float, args_list)
            result = a + b
            print(f"{a} + {b} = {result}")
            # Log the operation before attempting to record it in history
            logging.debug(f"Recording addition to history: {a} + {b} = {result}")
            CalculationHistory().add_record(f"{a} + {b}", result)
            logging.info(f"Addition operation recorded successfully: {a} + {b} = {result}")

        except ValueError:
            logging.error("Add command received invalid arguments.", exc_info=True)
            print("Error: Please provide two numbers separated by a space.")
