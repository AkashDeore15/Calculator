# Calculator Application

## Introduction
The Calculator application is a CLI-based Python project designed to perform arithmetic operations and manage their history. It showcases the use of design patterns, environment variables for configuration, structured logging, and demonstrates error handling principles such as "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP).

## Features

- **Calculator Operations:** The Calculator Application supports a range of basic to complex mathematical operations. Utilizing the Factory Pattern for its extendibility, the application allows for the seamless addition of new operations without the need to modify the core logic. Supported operations include:
    - **Addition:** Combines two or more numbers into a single sum.
    - **Subtraction:** Calculates the difference between numbers.
    - **Multiplication:** Computes the product of two or more numbers.
    - **Division:** Divides one number by another, returning the quotient.

- **History Management:** Manages calculation history with advanced features:
    - **Loading History**: Users can load previous calculations to review or reuse results.
    - **Deleting History by Index**: Offers the capability to delete specific calculations from history, enhancing data management.
    - **Clearing History**: Provides the option to clear the entire history, useful for starting a new session or maintaining privacy.
    - **Saving in CSV**: Utilizes Pandas DataFrames to store and manage history efficiently in a CSV file, ensuring data persistence and easy access.

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

-python calculator.py add 5 3

-python calculator.py subtract 10 4

-python calculator.py multiply 6 7

-python calculator.py divide 8 2

-python calculator.py load

-python calculator.py delete (index)

-python calculator.py clear

## Configuration
- **Environment Variables**: Customize the application behavior through the `.env` file. This file can be used to set various operational parameters such as debug mode, application port, etc.
- **Logging Configuration**: Adjust the logging settings in `logging.conf` to suit your needs, including log level and file locations.

## Environment Variables in the Calculator Application
- **CALC_HISTORY_PATH:** Path to the file where calculation history is stored.
- **LOG_LEVEL:** Determines the level of logging output (DEBUG, INFO, WARNING, ERROR, CRITICAL).

In the Calculator Application, environment variables play a pivotal role in configuring operational behavior, enhancing security, and ensuring the smooth execution of automated workflows, such as GitHub Actions. Their usage is critical in several specific areas:

### Operational Configuration
Environment variables like `CALC_HISTORY_PATH` and `LOG_LEVEL` allow you to dynamically set the path for storing calculation history and adjust the verbosity of logging. This capability is essential for adapting the application to various environments (development, testing, production) without altering the source code.

### Security
The application uses environment variables to manage sensitive information securely. This approach prevents hard-coded credentials or paths from being stored in the source code, reducing the risk of exposing sensitive data through version control systems. It's particularly important for API keys or database connections that your application might use in the future.

### Portability Across Environments
Whether running locally, in a CI/CD pipeline, or in a production environment, environment variables ensure that your application can easily be configured to suit the specific context. This simplifies deployment and operational management across different platforms.

### Seamless GitHub Actions Integration
The use of an absolute path configured via environment variables (e.g., `CALC_HISTORY_PATH`) is a strategic choice for facilitating GitHub Actions. It ensures that the application correctly locates and accesses necessary resources—like the history file—regardless of the environment in which the GitHub Action runs. This configuration eliminates the common problem of path discrepancies between local development environments and the GitHub Actions runner environment.

### Automated Workflows Efficiency
By configuring an absolute path and other settings through environment variables, your project ensures that automated tasks such as testing, building, and deploying within GitHub Actions are executed smoothly. This setup minimizes errors related to resource access or configuration mismatches, making the CI/CD process more reliable and efficient.

### Best Practices for Development and Deployment
Adopting environment variables for configuration aligns with industry best practices for application development and deployment. It ensures a high degree of flexibility, security, and maintainability of the application, making it easier for developers to work collaboratively and for operations teams to manage deployments.


## Testing

In developing the Calculator Application, I've prioritized ensuring that each piece of functionality not only works in isolation but also integrates seamlessly with other parts of the application. To achieve this, I've implemented a comprehensive testing strategy, encompassing both unit and integration testing.

### Unit Testing

For unit testing, I focus on the smallest parts of the application:

- **Mathematical Operations**: I've written tests for each mathematical operation (add, subtract, multiply, divide) to cover a range of inputs, including edge cases. This ensures each operation performs correctly under any given scenario.
- **Input Parsing**: Considering the diverse inputs the application can handle, I've created unit tests to verify that the parsing logic accurately interprets user commands and expressions. These tests help me quickly identify and fix any parsing issues.
- **Utility Functions**: I also test utility functions, such as those for managing calculation history or reading environment variables. These tests confirm that these utilities behave as expected across different conditions.

I run these unit tests using `pytest`, which allows me to get immediate feedback on the code I write or modify.

### Integration Testing

Integration testing allows me to examine how different parts of the application work together:

- **End-to-End Calculation Workflow**: I simulate user interactions from input to output, ensuring the entire calculation process, including history management, functions as a cohesive unit.
- **Environment and Configuration**: I test the application's response to various environment settings, like different logging levels or history file paths set through environment variables, to guarantee it adapts correctly to different operating conditions.
- **Error Handling and Edge Cases**: I've crafted tests to see how the application manages invalid inputs or commands, focusing on maintaining stability and providing clear feedback to the user without crashing.

To streamline my development process, I integrate these tests into a Continuous Integration (CI) pipeline, automatically running them against every commit. This not only helps in maintaining high code quality but also ensures that the application is robust and user-friendly.

By employing both unit and integration tests, I ensure that every component of my Calculator Application not only performs its intended function accurately but also interacts perfectly with other components. This dual approach to testing forms the backbone of my quality assurance process, allowing me to build a reliable and effective application.


## Architecture and Design Patterns

### Factory Pattern

The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. In the context of the Calculator Application, this pattern plays a critical role in handling calculator operations.

#### Implementation Detail
When a user inputs a command to perform a calculation (like addition, subtraction, multiplication, or division), the application doesn't directly instantiate the operation classes. Instead, it uses a factory class that decides which operation class to instantiate based on the user input. This means adding new operations doesn't require changes to the core application logic, only additions to the factory's logic and the creation of new operation classes.

#### Benefits
This approach significantly enhances modularity by decoupling the client code in the application (that requests an operation to be performed) from the concrete classes that implement those operations. It simplifies maintenance and the integration of new operations, adhering to the Open/Closed Principle of software design.

### Singleton Pattern

The Singleton Pattern is another creational pattern designed to ensure that a class has only one instance while providing a global point of access to that instance. It's particularly useful for managing resources that are naturally singular, like configuration managers or logging.

#### Implementation Detail
In the Calculator Application, the logging component is implemented as a singleton. This ensures that all parts of your application use the same logging instance, facilitating consistent logging behavior and centralized log management. The first time the logging component is needed, the singleton instance is created, and subsequent requests return the already instantiated logger, preserving system resources.

#### Benefits
Using the Singleton Pattern for the logger ensures consistency across the application and makes it easier to manage the logging output. It also helps in controlling access to shared resources, such as log files, preventing potential conflicts or resource leaks.

### Command Pattern

The Command Pattern is a behavioral design pattern that turns a request or simple operation into an object. This pattern allows for parameterizing objects with operations, queueing or logging operations, and supports undoable operations.

#### Implementation Detail
In the context of plugin architecture, the Command Pattern is employed to encapsulate each plugin's operation within command classes. Each command object has a method that defines the execution logic for the operation it represents. When the application needs to execute an operation, it does so by invoking the command object's execution method, not by directly calling the operation. This design supports the addition of operations such as undoing an action or logging changes without altering the core plugin logic.

#### Benefits
The Command Pattern offers several advantages, including the ability to add new commands without changing existing code, thereby following the Open/Closed Principle. It also simplifies the extension of the application's functionality by allowing for the dynamic addition of new operations and the easy implementation of additional features like undo mechanisms or operation logging.

By leveraging these design patterns, the Calculator Application achieves a high degree of code modularity, maintainability, and scalability. Each pattern addresses a specific aspect of application design, from creating flexible operation handling with the Factory Pattern to ensuring consistent and centralized management of logging with the Singleton Pattern, and enhancing the flexibility and extensibility of plugins through the Command Pattern.


## REPL (Read-Eval-Print Loop)

The Read-Eval-Print Loop (REPL) is an interactive programming environment that takes single user inputs (reads), executes them (evaluates), and returns the result to the user (prints). This cycle repeats indefinitely until the user decides to exit the program.

In the Calculator Application, the REPL is a core feature that significantly enhances user interaction. Here's how it works in more detail:

- **Read**: The application prompts the user for input, which could be a mathematical expression or a command (like viewing history, clearing history, etc.).
- **Eval**: Upon receiving input, the application parses and evaluates the expression or executes the command. This step involves dynamically identifying the operation requested, using the Factory Pattern to instantiate the appropriate operation class, and executing the operation.
- **Print**: The result of the evaluation or the outcome of the command is then displayed back to the user.
- **Loop**: This process repeats, with the application ready to read the next input, creating a seamless interactive experience.

This interface makes the application intuitive and user-friendly, allowing for quick calculations and immediate feedback, which is especially useful for testing and educational purposes.

## EAFP (Easier to Ask for Forgiveness than Permission)

The EAFP principle is a Pythonic approach that encourages the execution of commands under the assumption that they will succeed and dealing with problems if they arise instead of checking for potential problems beforehand. In the Calculator Application, this philosophy is adopted in several ways:

- When performing calculations, the application doesn't extensively check the validity of every operation before attempting it. Instead, it tries to execute the operation directly.
- If an operation fails (e.g., division by zero, invalid input format), the application catches the resulting exceptions and handles them gracefully, such as by displaying an error message to the user without crashing.

This approach streamlines the code and enhances performance by avoiding unnecessary checks. It also aligns with Python's dynamic nature and its comprehensive exception handling capabilities.

## LBYL (Look Before You Leap)

The LBYL approach is more cautious, involving explicit checks before performing operations to prevent exceptions and errors. While the Calculator Application generally follows the EAFP philosophy, it employs LBYL in scenarios where pre-validation is more efficient or necessary:

- **Input Validation**: Before parsing user inputs, the application checks the format of the input to ensure it matches expected patterns. This prevents attempting to parse and evaluate inputs that are clearly invalid, which would unnecessarily raise exceptions.
- **Safety Checks**: In operations that could lead to unsafe conditions (such as file operations that could overwrite critical data), the application checks the state and conditions before proceeding.

By combining EAFP and LBYL approaches, the Calculator Application achieves a balance between efficient code execution and safety, ensuring that operations are performed smoothly and only when conditions are favorable, thereby minimizing potential errors and ensuring a better user experience.

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

## Logging
Logging is implemented using Python's logging module, which provides a way to configure logging via environment variables. It is crucial for debugging and understanding the application's flow. The Calculator Application adopts professional logging practices to ensure thorough monitoring, debugging, and operational transparency. A comprehensive logging system is in place, serving as a cornerstone for maintaining high standards of reliability and maintainability.

### Features of the Logging System:

- **Detailed Recording:** Logs detailed information regarding application operations, data manipulations, errors, and informational messages. This ensures that every significant action and event within the application is recorded, facilitating easier debugging and historical analysis.

- **Severity Differentiation:** Log messages are differentiated by severity levels—INFO, WARNING, ERROR—allowing for efficient monitoring and troubleshooting. This categorization helps in filtering logs based on urgency and severity, enabling quick responses to errors while also capturing routine operations and warnings for future reference.

- **Dynamic Configuration:** Logging behavior, including severity levels and output destinations, can be dynamically configured through environment variables. This flexibility allows for on-the-fly adjustments to logging verbosity and targeting without needing to modify the application code. It supports different operational modes, such as more detailed logging during development and focused error logging in production environments.

### How It Works:

- **Initialization:** At the application's start, the logging system initializes based on configurations specified in `logging.conf` and environment variables. This initialization process sets up the log formats, handlers, and level thresholds.

- **Operation:** During operation, the application code uses logging calls to record messages of various severities. The logging system handles these messages according to the predefined rules, directing them to appropriate outputs (e.g., console, file) and formatting them for readability.

- **Adjustment:** Administrators or developers can adjust the logging settings by changing environment variables, such as `LOG_LEVEL` for the general verbosity or specifying different log files for different types of logs. This makes it easy to tailor the logging system to the needs of different environments or to focus on specific issues.

### Best Practices:

- **Consistent Usage:** Across the application, logging is used consistently, with clear conventions for message severity and content, ensuring that logs provide a reliable and coherent view of the application's behavior.

- **Security and Privacy:** Care is taken to avoid logging sensitive information, protecting user privacy and application security.

- **Performance Considerations:** The logging system is designed to minimize performance impacts, ensuring that detailed logging does not significantly affect the application's responsiveness or resource usage.

This structured approach to logging not only aids in monitoring and debugging but also contributes to the application's overall robustness. By providing clear insights into the application's workings and issues, it supports continuous improvement and aids in maintaining high quality and reliability.


## Dependencies
Python 3.6 or newer
No external libraries are required, making it easy to set up and run in any environment with Python installed.

## Authors

- **Akash Deore** - [akashdeore](https://github.com/AkashDeore15)
Link to explanatory video:  [Video]()

## Acknowledgments

- Deeply grateful to Professor Keith Williams from New Jersey Institute of Technology for introducing me to professional coding standards, design patterns, testing, plugin architecture, logging and endless number of things I learnt while developing this project.



