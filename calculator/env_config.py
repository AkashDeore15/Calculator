"""
Module for loading environment variables for the calculator application.
"""
import os
from dotenv import load_dotenv

def load_environment():
    """
    Load environment variables from .env file.
    
    Returns:
        dict: Dictionary containing environment variables
    """
    # Load .env file if it exists
    load_dotenv()
    
    # Get LOG_LEVEL with default
    log_level = os.getenv('LOG_LEVEL')
    if log_level is None:
        log_level = 'INFO'
    
    # Get PLUGINS_PATH with default
    plugins_path = os.getenv('PLUGINS_PATH')
    if plugins_path is None:
        plugins_path = 'calculator/plugins'
    
    # Get DEBUG_MODE with default
    debug_mode = os.getenv('DEBUG_MODE')
    if debug_mode is None:
        debug_mode = 'False'
    
    config = {
        'LOG_LEVEL': log_level,
        'PLUGINS_PATH': plugins_path,
        'DEBUG_MODE': debug_mode.lower() == 'true'
    }
    
    return config
