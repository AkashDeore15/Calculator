""" Test the logger module """
import os
from calculator.logger import logger

def test_logger():
    """ Test the logger module """
    os.environ["LOG_LEVEL"] = "DEBUG"
    assert logger is not None
