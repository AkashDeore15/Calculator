import sys
import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self, args):
        if not args:
            logging.info("Usage: divide <number1> <number2>")
            print("Usage: divide <number1> <number2>")
            return
        try:
            a, b = map(float, args.split())
            if b == 0:
                logging.info("Error: Division by zero.")
                print("Error: Division by zero.")
            else:
                logging.info(f"{a} / {b} = {a / b}")
                print(f"{a} / {b} = {a / b}")
        except ValueError:
            logging.info("Error: Please provide two numbers separated by a space.")
            print("Error: Please provide two numbers separated by a space.")