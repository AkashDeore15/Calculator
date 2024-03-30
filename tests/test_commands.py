"""Module for testing command functionalities in the application."""

from unittest.mock import patch, MagicMock
from app.calculation_history import CalculationHistory
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_add_command_no_arguments(capsys):
    """Test that the add command shows usage instructions when no arguments are provided."""
    command = AddCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: add <number1> <number2>" in captured.out

def test_add_command_incorrect_arguments(capsys):
    """Test that the add command shows usage instructions when incorrect arguments are provided."""
    command = AddCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: add <number1> <number2>" in captured.out

def test_add_command_non_numeric_arguments(capsys):
    """Test that the add command shows an error message for non-numeric arguments."""
    command = AddCommand()
    command.execute("a b")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out

@patch.object(CalculationHistory, 'add_record')
def test_add_command_success(mock_add_record, capsys):
    """Test successful execution of the add command."""
    command = AddCommand()
    command.execute("1 2")
    captured = capsys.readouterr()
    assert "1.0 + 2.0 = 3.0" in captured.out
    mock_add_record.assert_called_with("1.0 + 2.0", 3.0)

def test_subtract_command_no_arguments(capsys):
    """Test SubtractCommand with no arguments."""
    command = SubtractCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: subtract <number1> <number2>" in captured.out

def test_subtract_command_incorrect_arguments_count(capsys):
    """Test SubtractCommand with incorrect number of arguments."""
    command = SubtractCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: subtract <number1> <number2>" in captured.out

@patch("logging.error")
def test_subtract_command_invalid_arguments(mock_logging_error, capsys):
    """Test SubtractCommand with non-numeric arguments."""
    command = SubtractCommand()
    command.execute("one two")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out
    mock_logging_error.assert_called_once()

@patch("app.calculation_history.CalculationHistory.add_record", MagicMock())
@patch("logging.info")
def test_subtract_command_valid_subtraction(mock_logging_info, capsys):
    """Test SubtractCommand with valid arguments for subtraction."""
    command = SubtractCommand()
    command.execute("10 2")
    captured = capsys.readouterr()
    assert "10.0 - 2.0 = 8.0" in captured.out
    mock_logging_info.assert_called_with("Subtraction operation recorded successfully: 10.0 - 2.0 = 8.0")

def test_divide_command_no_arguments(capsys):
    """Test DivideCommand with no arguments."""
    command = DivideCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: divide <number1> <number2>" in captured.out

def test_divide_command_incorrect_arguments_count(capsys):
    """Test DivideCommand with incorrect number of arguments."""
    command = DivideCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: divide <number1> <number2>" in captured.out

def test_divide_command_division_by_zero(capsys):
    """Test DivideCommand with division by zero."""
    command = DivideCommand()
    command.execute("1 0")
    captured = capsys.readouterr()
    assert "Error: Division by zero is not allowed." in captured.out

@patch("logging.error")
def test_divide_command_invalid_arguments(mock_logging_error, capsys):
    """Test DivideCommand with non-numeric arguments."""
    command = DivideCommand()
    command.execute("one two")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out
    mock_logging_error.assert_called_once()

@patch("app.calculation_history.CalculationHistory.add_record", MagicMock())
@patch("logging.info")
def test_divide_command_valid_division(mock_logging_info, capsys):
    """Test DivideCommand with valid arguments for division."""
    command = DivideCommand()
    command.execute("10 2")
    captured = capsys.readouterr()
    assert "10.0 / 2.0 = 5.0" in captured.out
    mock_logging_info.assert_called_with("Division operation recorded successfully: 10.0 / 2.0 = 5.0")

def test_multiply_command_no_arguments(capsys):
    """Test MultiplyCommand with no arguments."""
    command = MultiplyCommand()
    command.execute("")
    captured = capsys.readouterr()
    assert "Usage: multiply <number1> <number2>" in captured.out

def test_multiply_command_incorrect_arguments_count(capsys):
    """Test MultiplyCommand with incorrect number of arguments."""
    command = MultiplyCommand()
    command.execute("1")
    captured = capsys.readouterr()
    assert "Usage: multiply <number1> <number2>" in captured.out

@patch("logging.error")
def test_multiply_command_invalid_arguments(mock_logging_error, capsys):
    """Test MultiplyCommand with non-numeric arguments."""
    command = MultiplyCommand()
    command.execute("one two")
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers separated by a space." in captured.out
    mock_logging_error.assert_called_once_with("Multiply command received invalid arguments.", exc_info=True)

@patch("app.calculation_history.CalculationHistory.add_record", MagicMock())
@patch("logging.info")
def test_multiply_command_valid_multiplication(mock_logging_info, capsys):
    """Test MultiplyCommand with valid arguments for multiplication."""
    command = MultiplyCommand()
    command.execute("10 2")
    captured = capsys.readouterr()
    assert "10.0 * 2.0 = 20.0" in captured.out
    mock_logging_info.assert_called_with("Multiplication operation recorded successfully: 10.0 * 2.0 = 20.0")


