
import pkgutil
import os
import importlib
import sys
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)
    
    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                            logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
                    except TypeError:
                        #logging.error(f"Error importing plugin {plugin_name}")
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        print("Type 'menu' to display available commands. \nType 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            input_command = input(">>> ").strip()  # Read the command input
            command_parts = input_command.split(maxsplit=1)  # Split into command and arguments
            command_name = command_parts[0]  # The command itself
            args = command_parts[1] if len(command_parts) > 1 else ""  # Arguments, if any

            # Execute the command with the provided arguments
            if command_name in self.command_handler.commands:
                self.command_handler.execute_command(command_name, args)
            else:
                print(f"No such command: {command_name}")
            
