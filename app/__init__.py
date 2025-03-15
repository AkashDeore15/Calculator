import importlib
import logging
import logging.config
import os
import pkgutil
import sys
from dotenv import load_dotenv

# Importing  command classes
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand


class App:
    """Main application class responsible for initializing and running the command interface."""

    def __init__(self):
        """Initializes the application by configuring logging, loading environment variables, and setting up command handling."""
        self.ensure_log_directory()
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def ensure_log_directory(self):
        """Ensure that the log directory exists."""
        os.makedirs('logs', exist_ok=True)

    def configure_logging(self):
        """Configures logging for the application."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Loads and returns environment variables as a dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugin_commands(self, path, package):
        """Dynamically loads and registers command plugins from a specified directory."""
        if not os.path.exists(path):
            logging.warning(f"Directory '{path}' not found.")
            return

        for _, plugin_name, _ in pkgutil.iter_modules([path]):
            self.try_load_plugin(plugin_name, package)

    def try_load_plugin(self, plugin_name, package):
        """Attempts to load a single plugin, handling errors gracefully."""
        try:
            plugin_module = importlib.import_module(f'{package}.{plugin_name}')
            self.instantiate_and_register_command(plugin_module, plugin_name)
        except ImportError as e:
            logging.error(f"Error importing plugin {plugin_name}: {e}")

    def instantiate_and_register_command(self, plugin_module, plugin_name):
        """Instantiates and registers a command with the command handler."""
        try:
            command_instance = self.create_command_instance(plugin_module, plugin_name)
            if command_instance:
                self.command_handler.register_command(plugin_name, command_instance)
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
        except TypeError:
            logging.error(f"Failed to instantiate command '{plugin_name.capitalize()}Command' due to missing arguments.")

    def create_command_instance(self, plugin_module, plugin_name):
        """Creates an instance of a command, handling special cases as necessary."""
        command_class_name = f'{plugin_name.capitalize()}Command'
        if plugin_name.lower() == 'menu':
            return getattr(plugin_module, command_class_name)(self.command_handler)
        return getattr(plugin_module, command_class_name)()

    def load_plugins(self):
        """Loads all plugins from the plugins directory."""
        plugins_package = 'app.plugins'
        self.load_plugin_commands(os.path.join(plugins_package.replace('.', '/'), 'history'), f'{plugins_package}.history')
        self.load_plugin_commands(plugins_package.replace('.', '/'), f'{plugins_package}')

    def start(self):
        """Starts the application, handling user input and executing commands."""
        self.load_plugins()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        print("Type 'menu' to display available commands.\nType 'exit' to exit.")
        self.run_command_loop()

    def run_command_loop(self):
        """Runs the main command loop, processing user input."""
        try:
            while True:
                input_command = input(">>> ").strip()
                if input_command.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)
                self.process_input_command(input_command)
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")

    def process_input_command(self, input_command):
        """Processes a single input command."""
        command_parts = input_command.split(maxsplit=1)
        command_name = command_parts[0].lower()
        args = command_parts[1] if len(command_parts) > 1 else ""
        try:
            self.command_handler.execute_command(command_name, args)
        except KeyError:
            logging.error("Unknown command")
            print(f"No such command: {command_name}")
            sys.exit(1)

