import logging
from app.commands import Command
from app.calculation_history import CalculationHistory  # Maintain the import for CalculationHistory

class DeleteCommand(Command):
    def execute(self, args):
        # Strip whitespace and check if the argument is a digit
        if not args.strip().isdigit():
            logging.error("Delete command requires a numerical index as an argument.")
            print("Error: Please provide a valid numerical index for the history record you wish to delete.")
            return

        # Convert the argument to an integer
        index = int(args.strip())
        
        # Instantiate CalculationHistory
        history = CalculationHistory()

        # Informing about the attempt to delete a specific record
        logging.info(f"Attempting to delete calculation history record at index: {index}.")
        
        # Attempt to delete the history record and provide feedback
        if history.delete_history(index):
            logging.info(f"Successfully deleted calculation history record at index: {index}.")
            print(f"Record at index {index} successfully deleted.")
        else:
            # In case of failure, log a warning. Assuming delete_history() handles its error messages internally
            logging.warning(f"Failed to delete calculation history record at index: {index}.")
