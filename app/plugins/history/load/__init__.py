import sys
import logging
from app.commands import Command
from app.calculation_history import CalculationHistory  # Ensure the import is maintained

class LoadCommand(Command):
    def execute(self, args=None):
        logging.info("Attempting to load calculation history.")
    
        history = CalculationHistory()
    
        try:
            result = history.load_history()
            if result is True:  # Assuming True indicates history was found and displayed
                logging.info("Calculation history loaded and displayed successfully.")
            elif result is False:  # False indicates the history is empty but was successfully accessed
                print("No calculation history to display.")
        except Exception as e:  # Consider catching more specific exceptions
            logging.error(f"An error occurred while trying to load the calculation history: {e}")
            print("An error occurred while trying to load the calculation history.")

