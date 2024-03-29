import sys
import logging
from app.commands import Command

class ExitCommand(Command):
    def execute(self, args=None):
        # Log the exit intention before executing the exit command
        logging.info("Exiting the application on user command.")

        # Exiting the application
        print("Exiting...")
        sys.exit(0)  # Using a standard exit code for successful termination
