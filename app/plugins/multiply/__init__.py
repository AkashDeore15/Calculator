import sys
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, args):
        if not args:
            print("Usage: multiply <number1> <number2>")
            return
        try:
            a, b = map(float, args.split())
            print(f"{a} * {b} = {a * b}")
        except ValueError:
            print("Error: Please provide two numbers separated by a space.")