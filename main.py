#!/usr/bin/env python3
"""
Advanced Calculator Application with REPL, logging, and plugin support.
This is the main entry point for the application.
"""
import cmd
from src.calculator import Calculator
from src.logger import logger

class CalculatorREPL(cmd.Cmd):
    """Command-line interface for the calculator application."""
    
    intro = "Welcome to Advanced Calculator. Type 'help' for available commands."
    prompt = "calc> "
    
    def do_add(self, arg):
        """Add two numbers: add 5 3"""
        try:
            args = self._parse_args(arg, 2)
            if args:
                result = Calculator.add(args[0], args[1])
                self._log_and_print_result("add", args, result)
        except Exception as e:
            logger.error(f"Error in add operation: {e}")
            print(f"Error: {e}")
    
    def do_subtract(self, arg):
        """Subtract second number from first: subtract 8 3"""
        try:
            args = self._parse_args(arg, 2)
            if args:
                result = Calculator.subtract(args[0], args[1])
                self._log_and_print_result("subtract", args, result)
        except Exception as e:
            logger.error(f"Error in subtract operation: {e}")
            print(f"Error: {e}")
    
    def do_multiply(self, arg):
        """Multiply two numbers: multiply 5 3"""
        try:
            args = self._parse_args(arg, 2)
            if args:
                result = Calculator.multiply(args[0], args[1])
                self._log_and_print_result("multiply", args, result)
        except Exception as e:
            logger.error(f"Error in multiply operation: {e}")
            print(f"Error: {e}")
    
    def do_divide(self, arg):
        """Divide first number by second: divide 15 3"""
        try:
            args = self._parse_args(arg, 2)
            if args:
                result = Calculator.divide(args[0], args[1])
                self._log_and_print_result("divide", args, result)
        except Exception as e:
            logger.error(f"Error in divide operation: {e}")
            print(f"Error: {e}")
    
    def do_exit(self, arg):
        """Exit the calculator"""
        logger.info("Exiting calculator")
        print("Goodbye!")
        return True
    
    def do_quit(self, arg):
        """Exit the calculator"""
        return self.do_exit(arg)
    
    def do_EOF(self, arg):
        """Support for Ctrl+D to exit"""
        print()  # Add a newline for cleaner exit
        return self.do_exit(arg)
    
    def _parse_args(self, arg, expected_count):
        """Parse and validate command arguments."""
        try:
            args = list(map(float, arg.split()))
            if len(args) != expected_count:
                print(f"Error: Expected {expected_count} arguments, got {len(args)}")
                return None
            return args
        except ValueError:
            print("Error: Arguments must be numbers")
            return None
    
    def _log_and_print_result(self, operation, args, result):
        """Log the operation and print the result."""
        arg_str = ' '.join(map(str, args))
        logger.info(f"Operation: {operation} {arg_str} = {result}")
        print(f"Result: {result}")

def main():
    """Main entry point for the calculator application."""
    logger.info("Starting calculator application")
    try:
        CalculatorREPL().cmdloop()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        logger.info("Application terminated via keyboard interrupt")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"An error occurred: {e}")
    finally:
        logger.info("Shutting down calculator application")

if __name__ == "__main__":
    main()
