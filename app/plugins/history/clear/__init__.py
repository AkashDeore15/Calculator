import logging
from app.commands import Command
from app.calculation_history import CalculationHistory

class ClearCommand(Command):
    def execute(self, args):
        # Initial log indicating the intention to clear history
        logging.info("User initiated calculation history clear operation.")
        
        # Confirm with the user before proceeding to clear the history
        confirmation = input("Are you sure you want to clear the entire calculation history? (yes/no): ").strip().lower()
        if confirmation != 'yes':
            print("Clear history operation cancelled.")
            logging.info("Clear history operation was cancelled by the user.")
            return

        # Instantiate CalculationHistory
        history = CalculationHistory()

        # Log the attempt to clear history
        logging.info("Attempting to clear the entire calculation history.")
        
        # Perform the clear history action
        history.clear_history()

        # Log and inform the user of successful history clearance
        logging.info("Calculation history cleared successfully.")
        print("All calculation history has been successfully cleared.")
