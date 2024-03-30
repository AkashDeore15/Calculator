# Calculator Application

## Introduction
The Calculator application is a CLI-based Python project designed to perform arithmetic operations. It showcases the use of design patterns, environment variables for configuration, structured logging, and demonstrates error handling principles such as "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP).

## Features
- **Perform basic arithmetic operations: 
- **Implement design patterns like Command and Singleton for managing commands and calculation history.
- **Configure application behavior through environment variables.
- **Detailed logging for operation tracking and debugging.
- **Robust error handling showcasing LBYL and EAFP principles.
- **Calculator Operations:** Addition, Subtraction, Multiplication, and Division.
- **History Management:** Effective History management by storing, retreiving and deleting records using Pandas.
- **Configuration via Environment Variables:** Flexible application configuration.
- **REPL Interface:** ser-friendly command-line interface.
### Configuration Examples
To configure the application, set the environment variables in your shell or within a .env file:
export CALC_HISTORY_PATH="./calc_history.csv"
export LOG_LEVEL="INFO"

## Design Patterns
### Command Pattern
This application uses the Command pattern to encapsulate all information needed to perform an action or trigger an event at a later time. This includes the AddCommand, SubtractCommand, MultiplyCommand, and DivideCommand classes.

### Singleton Pattern
The CalculationHistory class uses the Singleton pattern to ensure that only one instance of the calculation history is created and accessible throughout the application's lifecycle.

## Environment Variables
### CALC_HISTORY_PATH: Path to the file where calculation history is stored.
### LOG_LEVEL: Determines the level of logging output (DEBUG, INFO, WARNING, ERROR, CRITICAL).

## Logging
Logging is implemented using Python's logging module, which provides a way to configure logging via environment variables. It is crucial for debugging and understanding the application's flow.

## Error Handling

### Look Before You Leap (LBYL)
This approach involves checking for potential issues before attempting an operation. For example, verifying input types or checking for the existence of files before trying to read them.

### Easier to Ask for Forgiveness than Permission (EAFP)
This idiomatic approach tries to perform the operation and catches exceptions if something goes wrong, which is more aligned with Python's style and can lead to cleaner code.

## Usage
To use the calculator, run the script with the desired operation and operands:

python calculator.py add 5 3
python calculator.py subtract 10 4
python calculator.py multiply 6 7
python calculator.py divide 8 2

## Dependencies
Python 3.6 or newer
No external libraries are required, making it easy to set up and run in any environment with Python installed.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

