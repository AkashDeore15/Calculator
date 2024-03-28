import sys
import logging
from app.commands import Command


class ExitCommand(Command):
    def execute(self, args=None):
        logging.info("Exit!")
        sys.exit("Exiting...")