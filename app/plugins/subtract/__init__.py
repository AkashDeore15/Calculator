import sys
import logging
from app.commands import Command

class SubtractCommand(Command):
    def execute(self, args):
        if not args:
            logging.info("Usage: subtract <number1> <number2>")
            print("Usage: subtract <number1> <number2>")
            return
        try:
            a, b = map(float, args.split())
            logging.info(f"{a} - {b} = {a - b}")
            print(f"{a} - {b} = {a - b}")
        except ValueError:
            logging.info("Invalid input.")
            print("Error: Please provide two numbers separated by a space.")