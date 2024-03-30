# Calculator Application

## Introduction
The Calculator application is a CLI-based Python project designed to perform arithmetic operations and manage their history. It showcases the use of design patterns, environment variables for configuration, structured logging, and demonstrates error handling principles such as "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP).

## Features

- **Calculator Operations:** Supports basic operations such as Addition, Subtraction, Multiplication, and Division. The application's extendibility through the Factory Pattern allows easy addition of more complex operations without altering core logic.

- **History Management:** Efficient management of calculation history by storing, retrieving, and deleting records, leveraging the power of Pandas for data handling.

- **Configuration via Environment Variables:** Offers flexible application configuration, adjusting operational parameters such as application modes and logging levels through environment variables.

- **REPL Interface:** Provides a user-friendly Read-Eval-Print Loop (REPL) interface, enhancing user experience by facilitating interactive input and immediate feedback.

- **Robust Error Handling:** Implements robust error handling strategies, showcasing the principles of Look Before You Leap (LBYL) and Easier to Ask for Forgiveness than Permission (EAFP), to ensure the application's reliability and user-friendly error messages.

- **Plugin Architecture:** Employs a plugin architecture to enhance functionality and facilitate easy integration of new features. Plugins can be dynamically loaded and executed, fostering an ecosystem for extendibility without modifying the application core.

- **Design Patterns Utilized:**
    - **Factory Pattern:** Dynamically creates calculator operation instances based on user input, promoting modularity and flexibility.
    - **Singleton Pattern:** Ensures components like the application logger are instantiated once, providing centralized management.
    - **Command Pattern:** Used in implementing command classes for plugins, encapsulating operations in objects for parameterization and potential undo operations, enhancing application flexibility and scalability.

These features collectively make the Calculator Application a powerful, extendible, and user-friendly tool for performing a variety of mathematical operations, managing calculation history, and easily extending functionality through plugins.


## Installation

### Prerequisites
- Python 3.6 or newer

### Steps
1. Clone this repository or download the ZIP package.
2. Navigate to the project directory.
3. Install the required dependencies: pip install -r requirements.txt

## Usage
To run the Calculator Application, execute the following command from the project root directory: python main.py

To use the calculator, run the script with the desired operation and operands:
python calculator.py add 5 3
python calculator.py subtract 10 4
python calculator.py multiply 6 7
python calculator.py divide 8 2
python calculator.py load
python calculator.py delete (index)
python calculator.py clear

## Configuration
- **Environment Variables**: Customize the application behavior through the `.env` file. This file can be used to set various operational parameters such as debug mode, application port, etc.
- **Logging Configuration**: Adjust the logging settings in `logging.conf` to suit your needs, including log level and file locations.

## Environment Variables
- **CALC_HISTORY_PATH:** Path to the file where calculation history is stored.
- **LOG_LEVEL:** Determines the level of logging output (DEBUG, INFO, WARNING, ERROR, CRITICAL).

## Testing
Run the unit tests to ensure the application is working as expected: pytest
Test files are located in the tests directory, and test results are recorded for analysis.

## Logging
Logging is implemented using Python's logging module, which provides a way to configure logging via environment variables. It is crucial for debugging and understanding the application's flow.

## Architecture and Design Patterns

### Design Patterns

This Calculator Application utilizes several design patterns to ensure code modularity, maintainability, and scalability:

- **Factory Pattern**: Used to create calculator operation instances dynamically based on user input, allowing for easy addition of new operations without modifying the core logic.
- **Singleton Pattern**: Ensures that certain components, such as the application logger, have only one instance throughout the application's lifecycle, providing a centralized point of management for those resources.
- **Command Pattern**: Implemented through command classes for plugins, this pattern encapsulates each operation (command) in an object, allowing for parameterization of clients with queues, requests, or operations. It also supports undoable operations and logging changes, making the application more flexible and extensible.

### REPL (Read-Eval-Print Loop)

The Calculator Application implements a REPL interface, allowing users to interact with the application in a loop of reading input, evaluating expressions, and printing the results. This interactive shell enhances user experience by providing immediate feedback and facilitating iterative testing of calculator functionalities.

### EAFP (Easier to Ask for Forgiveness than Permission)

In line with Python's EAFP philosophy, the application opts for a try-except control flow. This means it attempts operations assuming they will succeed and handles exceptions if they do not. This approach is evident in handling user input and operation execution, prioritizing code readability and performance.

### LBYL (Look Before You Leap)

While EAFP is preferred in many scenarios, the application also employs LBYL in situations where pre-checking conditions can prevent expensive or unsafe operations. For example, validating user input format before attempting to parse or execute calculations ensures that only valid operations proceed to execution, minimizing error handling overhead.

## Plugin Architecture

The Calculator Application employs a plugin architecture to enhance its functionality and allow for easy integration of new features without altering the core system. This approach enables developers to add new operations, functionalities, and integrations by writing separate plugin modules that the application dynamically loads and executes based on user input or predefined conditions.

### How It Works

- **Dynamic Discovery**: The application automatically detects and loads plugins at startup. This is achieved through a dedicated plugin directory where each plugin is stored in its own sub-directory or file.
- **Loose Coupling**: Plugins communicate with the main application through well-defined interfaces or command classes, ensuring that changes to the plugin do not affect the core application logic.
- **Command Classes for Plugins**: Each plugin implements a command class that encapsulates its operation. This class defines the execution logic and any undo functionality, making it easy for the application to execute and, if necessary, revert actions performed by the plugin.
- **Extensibility and Scalability**: Developers can add new features or operations by creating new plugins and placing them in the plugin directory. The application's plugin manager handles the rest, including initialization and execution of plugin commands.

### Benefits

- **Flexibility**: The system can be extended with new features without the need for major modifications to the existing codebase.
- **Modularity**: Features are encapsulated in plugins, making the system easier to understand, develop, and maintain.
- **Customization**: End users or developers can customize the application's functionality by choosing which plugins to include or develop new ones to meet their needs.

### Implementing a New Plugin

To implement a new plugin, developers should:

1. Create a new command class that implements the plugin interface expected by the application.
2. Define the plugin's operation logic within this class.
3. Place the plugin in the designated plugin directory.
4. The application will automatically detect and make the plugin available for use during runtime.

This plugin architecture not only simplifies the process of extending the application but also fosters an ecosystem where developers can share and contribute plugins that add valuable new functionalities to the application.

## Dependencies
Python 3.6 or newer
No external libraries are required, making it easy to set up and run in any environment with Python installed.

## Authors

- **Shweta Shardul** - [shwetashardul](https://github.com/shwetashardul)

## Acknowledgments

- Deeply grateful to Professor Keith Williams from New Jersey Institute of Technology for introducing me to professional coding standards, design patterns, testing, plugin architecture, logging and endless number of things i learnt while developing this project.



