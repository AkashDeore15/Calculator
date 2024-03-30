import logging
from app.commands import Command
from app.calculation_history import CalculationHistory

class DivideCommand(Command):
    def execute(self, args):
        args_list = args.split()
        
        if not args:
            logging.warning("Divide command invoked without arguments.")
            print("Usage: divide <number1> <number2>")
            return
        
        if len(args_list) != 2:
            logging.warning("Divide command requires exactly two arguments.")
            print("Usage: divide <number1> <number2>")
            return

        try:
            a, b = map(float, args_list)
            if b == 0:
                logging.warning("Attempted division by zero.")
                print("Error: Division by zero is not allowed.")
                return

            result = a / b
            print(f"{a} / {b} = {result}")
            logging.debug(f"Recording division to history: {a} / {b} = {result}")
            CalculationHistory().add_record(f"{a} / {b}", result)
            logging.info(f"Division operation recorded successfully: {a} / {b} = {result}")

        except ValueError:
            logging.error("Divide command received invalid arguments.")
            print("Error: Please provide two numbers separated by a space.")
