"""Tests for the CommandHandler class."""
from unittest.mock import patch, MagicMock
from decimal import Decimal
from calculator.command_handler import CommandHandler
from calculator.commands import Command, AddCommand

class TestPluginCommand(Command):
    """A test plugin command for testing."""
    def __init__(self, value_a: Decimal, value_b: Decimal):
        '''initilizing funtion'''# Fixed parameter naming
        self.a = value_a
        self.b = value_b
    def execute(self):
        """Execute the test command."""
        return self.a * self.b + 1  # Different from standard commands

def test_command_handler_initialization():
    """Test CommandHandler initialization."""
    handler = CommandHandler()
    assert 'add' in handler.command_dict
    assert 'subtract' in handler.command_dict
    assert 'multiply' in handler.command_dict
    assert 'divide' in handler.command_dict
    assert 'menu' in handler.command_dict

def test_create_commands_invalid_args():
    """Test command creation with invalid arguments."""
    handler = CommandHandler()
    # Test each command create method with invalid arguments
    assert handler.create_add_command(['invalid', '3']) is None
    assert handler.create_subtract_command(['5', 'invalid']) is None
    assert handler.create_multiply_command(['invalid', 'invalid']) is None
    assert handler.create_divide_command(['10', 'abc']) is None

def test_load_plugins_nonexistent_dir():
    """Test plugin loading when directory doesn't exist."""
    with patch('os.path.exists', return_value=False):
        handler = CommandHandler()
        # No exception should be raised, and no plugins should be loaded
        assert 'power' not in handler.command_dict

def test_load_plugins_import_error():
    """Test plugin loading with import error."""
    with patch('os.path.exists', return_value=True), \
         patch('os.listdir', return_value=['test_plugin.py']), \
         patch('importlib.import_module', side_effect=ImportError("Test import error")):
        handler = CommandHandler()
        # No exception should be raised, and no plugins should be loaded
        assert 'test_plugin' not in handler.command_dict

# Using public methods instead of accessing protected members
def test_internal_command_creation():
    """Test command creation directly using public methods."""
    handler = CommandHandler()
    # Test with valid arguments
    command = handler.create_add_command(['5', '3'])
    assert isinstance(command, AddCommand)
    assert command.a == Decimal('5')
    assert command.b == Decimal('3')
    # Test with invalid arguments
    command = handler.create_add_command(['invalid', '3'])
    assert command is None

def test_load_plugins_non_command_class():
    """Test plugin loading with a module that doesn't contain Command subclasses."""
    with patch('os.path.exists', return_value=True), \
         patch('os.listdir', return_value=['test_plugin.py']), \
         patch('importlib.import_module') as mock_import:
        # Create a mock module with no Command subclasses
        mock_module = MagicMock()
        mock_module.__name__ = 'calculator.plugins.test_plugin'
        mock_import.return_value = mock_module
        handler = CommandHandler()
        # No exception should be raised, and no plugins should be loaded
        assert 'test_plugin' not in handler.command_dict

# def test_load_plugins_command_class():
#     """Test plugin loading with a module that contains Command subclasses."""
#     with patch('calculator.command_handler.CommandHandler._create_command') as mock_create, \
#         patch('os.path.exists', return_value=True), \
#         patch('os.listdir', return_value=['test_plugin.py']), \
#         patch('importlib.import_module') as mock_import, \
#         patch('inspect.getmembers') as mock_getmembers, \
#         patch('inspect.isclass') as mock_isclass:
#         # Return a test command when _create_command is called
#         mock_create.return_value = "MOCKED_COMMAND"
#         # Set up TestPluginCommand correctly
#         TestPluginCommand.__module__ = 'calculator.plugins.test_plugin'
#         # Properly mock isclass to return True for our test command
#         mock_isclass.side_effect = lambda obj: obj is TestPluginCommand
#         # Define a proper mock for issubclass
#         original_issubclass = issubclass
#         def mock_issubclass(cls, class_or_tuple):
#             if cls is TestPluginCommand and Command in \
#                 (class_or_tuple if isinstance(class_or_tuple, tuple) else (class_or_tuple,)):
#                 return True
#             return original_issubclass(cls, class_or_tuple)
#         # Apply our issubclass mock
#         with patch('builtins.issubclass', side_effect=mock_issubclass):
#             # Mock the module
#             mock_module = MagicMock()
#             mock_module.__name__ = 'calculator.plugins.test_plugin'
#             # Setup the return value for getmembers
#             mock_getmembers.return_value = [('TestPluginCommand', TestPluginCommand)]
#             mock_import.return_value = mock_module
#             # Create handler which will load plugins
#             handler = CommandHandler()
#             # The command name should be derived from TestPluginCommand
#             command_name = TestPluginCommand.__name__.lower()
#             if command_name.endswith('command'):
#                 command_name = command_name[:-7]
#             # Check if the command was registered
#             assert command_name in handler.command_dict
#             # Test the command works
#             result = handler.command_dict[command_name](['2', '3'])
#             assert result == "MOCKED_COMMAND"  # Should use our mocked return value
