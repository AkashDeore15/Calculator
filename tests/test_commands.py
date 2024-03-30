"""Module for testing command functionalities in the application."""
from unittest.mock import patch, MagicMock
import pytest

from app.calculation_history import CalculationHistory
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand

def test_add_command_no_arguments(capsys):
    """Test displaying usage instructions when no arguments are provided for the add command."""
    command = AddCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: add <number1> <number2>" in captured.out

def test_add_command_incorrect_arguments(capsys):
    """Test displaying usage instructions for incorrect argument count in add command."""
    command = AddCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: add <number1> <number2>" in captured.out

def test_add_command_non_numeric_arguments(capsys):
    """Test error message for non-numeric arguments in add command."""
    command = AddCommand()
    command.execute("a b")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out

@patch.object(CalculationHistory, 'add_record')
def test_add_command_success(mock_add_record, capsys):
    """Test successful addition and history recording."""
    command = AddCommand()
    command.execute("1 2")
    captured = capsys.readouterr()
    assert "1.0 + 2.0 = 3.0" in captured.out
    mock_add_record.assert_called_with("1.0 + 2.0", 3.0)

def test_subtract_command_no_arguments(capsys):
    """Test displaying usage instructions when no arguments are provided for the subtract command."""
    command = SubtractCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: subtract <number1> <number2>" in captured.out

def test_subtract_command_incorrect_arguments_count(capsys):
    """Test displaying usage instructions for incorrect argument count in subtract command."""
    command = SubtractCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: subtract <number1> <number2>" in captured.out

@patch("logging.error")
def test_subtract_command_invalid_arguments(mock_logging_error, capsys):
    """Test error message for non-numeric arguments in subtract command."""
    command = SubtractCommand()
    command.execute("one two")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out
    mock_logging_error.assert_called_once()

@patch("app.calculation_history.CalculationHistory.add_record", MagicMock())
@patch("logging.info")
def test_subtract_command_valid_subtraction(mock_logging_info, capsys):
    """Test successful subtraction and history recording."""
    command = SubtractCommand()
    command.execute("10 2")
    captured = capsys.readouterr()
    assert "10.0 - 2.0 = 8.0" in captured.out
    mock_logging_info.assert_called_with("Subtraction operation recorded successfully: 10.0 - 2.0 = 8.0")

@pytest.fixture
def divide_command():
    """Fixture for DivideCommand."""
    return DivideCommand()

@patch("logging.warning")
def test_divide_command_no_arguments(mock_logging, divide_command, capsys):
    """Test displaying usage instructions when no arguments are provided for the divide command."""
    divide_command.execute("")
    captured = capsys.readouterr()
    assert "Usage: divide <number1> <number2>" in captured.out
    mock_logging.assert_called_with("Divide command invoked without arguments.")

@patch("logging.warning")
def test_divide_command_incorrect_arguments_count(mock_logging, divide_command, capsys):
    """Test displaying usage instructions for incorrect argument count in divide command."""
    divide_command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: divide <number1> <number2>" in captured.out
    mock_logging.assert_called_with("Divide command requires exactly two arguments.")

@patch("logging.warning")
def test_divide_command_division_by_zero(mock_logging, divide_command, capsys):
    """Test error message for division by zero in divide command."""
    divide_command.execute("1 0")
    captured = capsys.readouterr()
    assert "Error: Division by zero is not allowed." in captured.out
    mock_logging.assert_called_with("Attempted division by zero.")

@patch("logging.error")
def test_divide_command_invalid_arguments(mock_logging, divide_command, capsys):
    """Test error message for non-numeric arguments in divide command."""
    divide_command.execute("one two")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out
    mock_logging.assert_called_with("Divide command received invalid arguments.")

@patch("app.calculation_history.CalculationHistory.add_record")
@patch("logging.info")
def test_divide_command_valid_division(mock_logging_info, mock_add_record, divide_command, capsys):
    """Test successful division and history recording."""
    divide_command.execute("10 2")
    captured = capsys.readouterr()
    assert "10.0 / 2.0 = 5.0" in captured.out
    mock_logging_info.assert_called_with("Division operation recorded successfully: 10.0 / 2.0 = 5.0")
    mock_add_record.assert_called_with("10.0 / 2.0", 5.0)

def test_multiply_command_no_arguments(capsys):
    """Test displaying usage instructions when no arguments are provided for the multiply command."""
    command = MultiplyCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: multiply <number1> <number2>" in captured.out

def test_multiply_command_incorrect_arguments_count(capsys):
    """Test displaying usage instructions for incorrect argument count in multiply command."""
    command = MultiplyCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: multiply <number1> <number2>" in captured.out

@patch("logging.error")
def test_multiply_command_invalid_arguments(mock_logging_error, capsys):
    """Test error message for non-numeric arguments in multiply command."""
    command = MultiplyCommand()
    command.execute("one two")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out
    mock_logging_error.assert_called_once_with("Multiply command received invalid arguments.", exc_info=True)

@patch("app.calculation_history.CalculationHistory.add_record", MagicMock())
@patch("logging.info")
def test_multiply_command_valid_multiplication(mock_logging_info, capsys):
    """Test successful multiplication and history recording."""
    command = MultiplyCommand()
    command.execute("10 2")
    captured = capsys.readouterr()
    assert "10.0 * 2.0 = 20.0" in captured.out
    mock_logging_info.assert_called_with("Multiplication operation recorded successfully: 10.0 * 2.0 = 20.0")

@patch("logging.info")
@patch("sys.exit")
def test_exit_command(mock_exit, mock_logging_info, capsys):
    """Test that ExitCommand logs an exit message and exits the application."""
    command = ExitCommand()
    command.execute()
    captured = capsys.readouterr()

    # Verify the log message was recorded
    mock_logging_info.assert_called_once_with("Exiting the application on user command.")

    # Verify that sys.exit(0) was called
    mock_exit.assert_called_once_with(0)

    # Check the printed exit message
    assert "Exiting..." in captured.out
