"""
This module tests the history-related commands in the application, including
clear, delete, and load commands. It verifies their behavior under various
scenarios such as confirmation handling, input validation, and exception handling.
"""

from unittest.mock import patch
from app.plugins.history.clear import ClearCommand
from app.plugins.history.delete import DeleteCommand
from app.plugins.history.load import LoadCommand

@patch("builtins.input", return_value="yes")
@patch("app.calculation_history.CalculationHistory.clear_history")
@patch("logging.info")
def test_clear_command_confirmed(mock_logging_info, mock_clear_history, mock_input, capsys):
    """Test ClearCommand executes successfully when confirmation is 'yes'."""
    command = ClearCommand()
    command.execute(None)
    captured = capsys.readouterr()
    mock_clear_history.assert_called_once()
    assert "All calculation history has been successfully cleared." in captured.out
    mock_logging_info.assert_any_call("User initiated calculation history clear operation.")
    mock_logging_info.assert_any_call("Attempting to clear the entire calculation history.")
    mock_logging_info.assert_any_call("Calculation history cleared successfully.")

@patch("builtins.input", return_value="no")
@patch("app.calculation_history.CalculationHistory.clear_history")
@patch("logging.info")
def test_clear_command_cancelled(mock_logging_info, mock_clear_history, mock_input, capsys):
    """Test ClearCommand is cancelled correctly when confirmation is 'no'."""
    command = ClearCommand()
    command.execute(None)
    captured = capsys.readouterr()
    mock_clear_history.assert_not_called()
    assert "Clear history operation cancelled." in captured.out
    mock_logging_info.assert_any_call("User initiated calculation history clear operation.")
    mock_logging_info.assert_any_call("Clear history operation was cancelled by the user.")

@patch("builtins.input", return_value="unexpected input")
@patch("app.calculation_history.CalculationHistory.clear_history")
@patch("logging.info")
def test_clear_command_unexpected_input(mock_logging_info, mock_clear_history, mock_input, capsys):
    """Test ClearCommand handles unexpected input correctly."""
    command = ClearCommand()
    command.execute(None)
    captured = capsys.readouterr()
    mock_clear_history.assert_not_called()
    assert "Clear history operation cancelled." in captured.out
    mock_logging_info.assert_any_call("User initiated calculation history clear operation.")
    mock_logging_info.assert_any_call("Clear history operation was cancelled by the user.")

@patch("app.calculation_history.CalculationHistory.delete_history", return_value=True)
@patch("logging.info")
def test_delete_command_success(mock_logging_info, mock_delete_history, capsys):
    """Test DeleteCommand with a valid index leading to successful deletion."""
    command = DeleteCommand()
    command.execute("0")
    captured = capsys.readouterr()
    mock_delete_history.assert_called_once_with(0)
    assert "Record at index 0 successfully deleted." in captured.out
    mock_logging_info.assert_any_call("Attempting to delete calculation history record at index: 0.")
    mock_logging_info.assert_any_call("Successfully deleted calculation history record at index: 0.")

@patch("logging.error")
def test_delete_command_invalid_input(mock_logging_error, capsys):
    """Test DeleteCommand with invalid (non-numeric) input."""
    command = DeleteCommand()
    command.execute("invalid")
    captured = capsys.readouterr()
    assert "Error: Please provide a valid numerical index for the history record you wish to delete." in captured.out
    mock_logging_error.assert_called_once_with("Delete command requires a numerical index as an argument.")

@patch("app.calculation_history.CalculationHistory.delete_history", return_value=False)
@patch("logging.warning")
def test_delete_command_invalid_index(mock_logging_warning, mock_delete_history, capsys):
    """Test DeleteCommand with a numeric input that is an invalid index."""
    command = DeleteCommand()
    command.execute("999")
    captured = capsys.readouterr()
    mock_delete_history.assert_called_once_with(999)
    assert not "Record at index 999 successfully deleted." in captured.out
    mock_logging_warning.assert_called_once_with("Failed to delete calculation history record at index: 999.")

@patch("app.calculation_history.CalculationHistory.load_history", return_value=True)
@patch("logging.info")
def test_load_command_success(mock_logging_info, mock_load_history):
    """Test LoadCommand when history loads successfully."""
    command = LoadCommand()
    command.execute()
    mock_load_history.assert_called_once()
    mock_logging_info.assert_any_call("Attempting to load calculation history.")
    mock_logging_info.assert_any_call("Calculation history loaded and displayed successfully.")

@patch("app.calculation_history.CalculationHistory.load_history", return_value=False)
@patch("logging.info")
def test_load_command_empty_history(mock_logging_info, mock_load_history, capsys):
    """Test LoadCommand with an empty history."""
    command = LoadCommand()
    command.execute()
    captured = capsys.readouterr()
    mock_load_history.assert_called_once()
    assert "No calculation history to display." in captured.out
    mock_logging_info.assert_called_once_with("Attempting to load calculation history.")

@patch("app.calculation_history.CalculationHistory.load_history", side_effect=Exception("Test exception"))
@patch("logging.error")
def test_load_command_exception(mock_logging_error, mock_load_history, capsys):
    """Test LoadCommand when an exception occurs during history loading."""
    command = LoadCommand()
    command.execute()
    captured = capsys.readouterr()
    mock_load_history.assert_called_once()
    assert "An error occurred while trying to load the calculation history." in captured.out
    mock_logging_error.assert_called_once_with("An error occurred while trying to load the calculation history: Test exception")
