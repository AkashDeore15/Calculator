import logging
from abc import ABC, abstractmethod

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Command(ABC):
    @abstractmethod
    def execute(self, args=None):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.logger = logging.getLogger(self.__class__.__name__)

    def register_command(self, name, command_obj):
        self.commands[name] = command_obj
        self.logger.info(f"Command '{name}' registered.")

    def execute_command(self, command_name, args=""):
        if command_name in self.commands:
            self.logger.info(f"Executing command: {command_name} with arguments: {args}")
            try:
                self.commands[command_name].execute(args)
            except Exception as e:
                self.logger.error(f"Error executing command '{command_name}': {e}", exc_info=True)
        else:
            self.logger.warning(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
