import os
import pandas as pd
from dotenv import load_dotenv

class CalculationHistory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        load_dotenv()
        self.history_file = os.getenv('HISTORY_FILE_PATH')
        self.history_file = os.path.abspath(self.history_file)
        self.history_df = self.load_or_initialize_history()

    def load_or_initialize_history(self):
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        else:
            return pd.DataFrame(columns=['Operation', 'Result'])

    '''def add_record(self, operation, result):
        self.history_df = self.history_df.append({'Operation': operation, 'Result': result}, ignore_index=True)
        self.save_history()'''
    def add_record(self, operation, result):
    # Create a new DataFrame for the record to add
        new_record_df = pd.DataFrame([{'Operation': operation, 'Result': result}])
    # Exclude columns in new_record_df that are entirely NA
        cleaned_new_record_df = new_record_df.dropna(axis=1, how='all')
    
    # Concatenate the new record DataFrame with the existing history DataFrame
        self.history_df = pd.concat([self.history_df, cleaned_new_record_df], ignore_index=True)
    
    # Save the updated history
        self.save_history()

    def save_history(self):
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        self.history_df.to_csv(self.history_file, index=False)

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
            print(self.history_df.to_string(index=False))
        else:
            print("History file does not exist.")

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Result'])
        self.save_history()
        print("History cleared.")

    def delete_history(self, index):
        if not os.path.exists(self.history_file) or self.history_df.empty:
            print("History file does not exist or is empty.")
            return False
        try:
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            self.save_history()
            print(f"Record at index {index} deleted.")
            return True
        except KeyError:
            print(f"Invalid index: {index}. No record deleted.")
            return False

# Example usage:
'''if __name__ == "__main__":
    history_manager = CalculationHistory()
    history_manager.add_record("3 + 4", 7)
    history_manager.add_record("10 / 2", 5)
    history_manager.load_history()
    history_manager.delete_history(0)  # Attempt to delete the first record
    history_manager.load_history()
    history_manager.clear_history()'''
