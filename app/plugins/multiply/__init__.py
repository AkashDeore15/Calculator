import sys
import logging
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, args):
        if not args:
            logging.info("Usage: multiply <number1> <number2>")
            print("Usage: multiply <number1> <number2>")
            return
        try:
            a, b = map(float, args.split())
            logging.info(f"{a} * {b} = {a * b}")
            print(f"{a} * {b} = {a * b}")
        except ValueError:
            logging.info("Invalid input.")
            print("Error: Please provide two numbers separated by a space.")