"""Tests for the env_config module."""
from unittest.mock import patch
from calculator.env_config import load_environment

# def test_load_environment():
#     """Test load_environment function."""
#     # Test with environment variables set
#     with patch('os.getenv') as mock_getenv, \
#          patch('dotenv.load_dotenv'):
#         # Mock environment variable values
#         def getenv_side_effect(key, default):
#             '''mocking the environment variables'''
#             values = {
#                 'LOG_LEVEL': 'INFO',
#                 'PLUGINS_PATH': '/calculator/plugins',
#                 'DEBUG_MODE': 'false'
#             }
#             return values.get(key, default)
#         mock_getenv.side_effect = getenv_side_effect
#         config = load_environment()
#         # Verify environment was loaded correctly
#         # Note: We don't check if load_dotenv was called since that's not essential
#         assert config['LOG_LEVEL'] == 'INFO'
#         assert config['PLUGINS_PATH'] == '/calculator/plugins'
#         assert config['DEBUG_MODE'] is False

def test_load_environment_defaults():
    """Test load_environment function with default values."""
    # Test with no environment variables set
    with patch('os.getenv', return_value=None), \
         patch('dotenv.load_dotenv'):
        config = load_environment()
        # Verify default values are used
        assert config['LOG_LEVEL'] == 'INFO'
        assert config['PLUGINS_PATH'] == 'calculator/plugins'
        assert config['DEBUG_MODE'] is False
