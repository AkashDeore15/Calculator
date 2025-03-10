import os
from src.logger import logger

def test_logger():
    os.environ["LOG_LEVEL"] = "DEBUG"
    assert logger is not None
