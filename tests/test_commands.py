"""
The test_commands.py file contains tests for the command classes in the calculator.commands module.
The tests cover the AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, and\
      MenuCommand classes.
"""
from decimal import Decimal
from unittest.mock import patch
import pytest
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.command_handler import CommandHandler

def test_add_command():
    """Test the AddCommand."""
    command = AddCommand(Decimal('5'), Decimal('3'))
    assert command.execute() == Decimal('8')

def test_subtract_command():
    """Test the SubtractCommand."""
    command = SubtractCommand(Decimal('10'), Decimal('4'))
    assert command.execute() == Decimal('6')

def test_multiply_command():
    """Test the MultiplyCommand."""
    command = MultiplyCommand(Decimal('6'), Decimal('7'))
    assert command.execute() == Decimal('42')

def test_divide_command():
    """Test the DivideCommand."""
    command = DivideCommand(Decimal('10'), Decimal('2'))
    assert command.execute() == Decimal('5')

def test_divide_by_zero_command():
    """Test the DivideCommand with division by zero."""
    command = DivideCommand(Decimal('10'), Decimal('0'))
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        command.execute()

def test_command_handler():
    """Test the CommandHandler."""
    handler = CommandHandler()
    # Test add command
    add_cmd = handler.get_command('add', ['5', '3'])
    assert add_cmd.execute() == Decimal('8')
    # Test invalid command
    assert handler.get_command('invalid', []) is None
    # Test invalid arguments
    assert handler.get_command('add', ['invalid', '3']) is None

def test_menu_command(capsys):
    """Test the MenuCommand."""
    handler = CommandHandler()
    menu_cmd = handler.get_command('menu', [])
    result = menu_cmd.execute()
    # Check that output contains expected commands
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "menu" in captured.out
    # Check that the result is as expected
    assert result == "Menu displayed"

def test_nonexistent_plugins_dir():
    """Test behavior when plugins directory does not exist."""
    # When plugins dir doesn't exist, the power command won't be loaded
    with patch('os.path.exists') as mock_exists:
        # Return False only for the plugins directory check
        mock_exists.side_effect = lambda path: 'plugins' not in path
        handler = CommandHandler()
        # No exception should be raised
        assert 'power' not in handler.command_dict
