import sys
import logging
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, args=""):
        logging.info("Displaying the menu of available commands.")
        print("Available commands:")
        
        # Iterating through the commands dictionary to print each command name
        for command_name in self.command_handler.commands.keys():
            print(f"- {command_name}")
