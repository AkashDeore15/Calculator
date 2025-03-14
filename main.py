"""Main module for the calculator application with REPL."""
import os
from calculator.command_handler import CommandHandler
from calculator.multiprocessing_handler import MultiprocessingHandler
from calculator.logger_config import setup_logging
from calculator.env_config import load_environment

def display_recent_logs(num_lines=20):
    """
    Display the most recent log entries from the log file.
    
    Args:
        num_lines (int): Number of recent log lines to display
    """
    try:
        # Get project root directory (parent of the directory containing this file)
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = os.path.join(project_dir, 'logs', 'app.log')
        
        # For debugging purposes
        print(f"Looking for log file at: {log_path}")
        
        if os.path.exists(log_path):
            print(f"\n--- Last {num_lines} log entries ---")
            
            # Read the last n lines from the log file
            with open(log_path, 'r') as file:
                lines = file.readlines()
                for line in lines[-num_lines:]:
                    print(line.strip())
            
            print("--- End of log entries ---\n")
        else:
            # Try a relative path as fallback
            alt_log_path = os.path.join('logs', 'app.log')
            print(f"Primary path not found, trying: {alt_log_path}")
            
            if os.path.exists(alt_log_path):
                print(f"\n--- Last {num_lines} log entries ---")
                
                with open(alt_log_path, 'r') as file:
                    lines = file.readlines()
                    for line in lines[-num_lines:]:
                        print(line.strip())
                
                print("--- End of log entries ---\n")
            else:
                print(f"Log file not found at either location.")
                print(f"Please check if 'logs/app.log' exists in the project directory.")
    except Exception as e:
        print(f"Error displaying logs: {e}")

def main():
    '''Main function for the calculator application with REPL.'''
    config = load_environment()
    
    # Set up logging
    logger = setup_logging()
    logger.info("Calculator application started")
    if config['DEBUG_MODE']:
        logger.debug(f"Application running with config: {config}")
    print("Welcome to the calculator application!")
    print("Type 'exit' to quit the application.")
    command_handeler = CommandHandler()
    logger.info("Command handler initialized")
    # Display available commands at startup using menu command
    menu_command = command_handeler.get_command('menu', [])    
    if menu_command:
        menu_command.execute()
        logger.info("Menu displayed at startup")
    # REPL loop
    while True:
        try:
            user_input = input("Enter a command: ")
            logger.info(f"User input: {user_input}")
            #check if the user wants to exit
            if user_input.lower() == 'exit':
                print("Exiting the calculator application. Goodbye!")
                logger.info("User exited the application")
                break
            # Check if the user wants to view logs    
            if user_input.lower() == 'log':
                display_recent_logs()
                continue
            # Parse the user input
            parts = user_input.split(' ')
            if not parts:
                print("Invalid input. Please try again.")
                logger.warning("Invalid input received")
                continue
            command_name = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
            logger.info(f"Command: {command_name}, Args: {args}")
            # Special commands that don't need arguments
            if command_name == 'menu':
                menu_command = command_handeler.get_command('menu', [])
                if menu_command:
                    menu_command.execute()
                    logger.info("Menu displayed")
                continue
            #Evaluate the command
            if command_name in command_handeler.command_dict:
                if len(args) != 2:
                    print(f"The {command_name} command requires exactly 2 numeric arguments.Please try again.")
                    logger.warning(f"Invalid number of arguments for {command_name}")
                    continue

                command = command_handeler.get_command(command_name, args)
                if command:
                    try:
                        print("Executing command...")
                        logger.info(f"Executing {command_name} command with args {args}")
                        result = MultiprocessingHandler.run_command_async(command)
                        # print result
                        print(f"The result is: {result}")
                        logger.info(f"Command result: {result}")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        logger.error(f"Error executing command: {str(e)}", exc_info=True)
                else:
                    print("Error executing command. Please try again.")
                    logger.error("Failed to create command object")
            else:
                print(f"Unknown command: {command_name}. Please try again.")
                print("Available operations:",",".join(command_handeler.command_dict.keys()))
                logger.warning(f"Unknown command: {command_name}")
        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting...")
            logger.info("Application interrupted by user")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            logger.error(f"Unexpected error in main loop: {str(e)}", exc_info=True)

if __name__ == '__main__':
    main()
