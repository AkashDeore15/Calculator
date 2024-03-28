import sys
import logging
from app.commands import Command

class AddCommand(Command):
    def execute(self, args):
        if not args:
            logging.info("Usage: add <number1> <number2>")
            print("Usage: add <number1> <number2>")
            return
        try:
            a, b = map(float, args.split())
            logging.info(f"Addition: {a} + {b} = {a + b}")
            print(f"{a} + {b} = {a + b}")
        except ValueError:
            print("Error: Please provide two numbers separated by a space.")