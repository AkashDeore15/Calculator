"""This module contains the MultiprocessingHandler class."""
import multiprocessing
import logging
from decimal import Decimal
from calculator.commands import Command

logger = logging.getLogger('calculator.multiprocessing')
class MultiprocessingHandler:
    @staticmethod
    def execute_command(command: Command, result_queue):
        """Execute a command and put the result in a queue."""
        logger.debug(f"Executing command in subprocess: {command.__class__.__name__}")
        try:
            result = command.execute()
            logger.debug(f"Command execution successful, result: {result}")
            result_queue.put(('success', result))
        except Exception as e:
            logger.error(f"Error executing command: {str(e)}")
            result_queue.put(('error', str(e)))
    
    @staticmethod
    def run_command_async(command: Command):
        """Run a command in a separate process."""
        # Create a multiprocessing queue to get the result
        logger.info(f"Running command asynchronously: {command.__class__.__name__}")
        result_queue = multiprocessing.Queue()
        # Create and start a process
        process = multiprocessing.Process(
            target=MultiprocessingHandler.execute_command,
            args=(command, result_queue)
        )
        process.start()
        logger.debug("Process started")
        # Wait for the process to complete and get the result
        process.join()
        logger.debug("Process completed")
        # Get the result from the queue
        if not result_queue.empty():
            status, result = result_queue.get()
            if status == 'success':
                logger.info(f"Command completed successfully with result: {result}")
                return result
            else:
                logger.error(f"Command failed with error: {result}")
                raise ValueError(result)
        else:
            logger.error("Command execution failed: Empty result queue")
            raise RuntimeError("Command execution failed")
