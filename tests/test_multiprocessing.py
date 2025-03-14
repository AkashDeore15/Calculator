"""Tests for the multiprocessing handler."""
from decimal import Decimal
from unittest.mock import patch, MagicMock
import pytest
from calculator.commands import AddCommand, MultiplyCommand
from calculator.multiprocessing_handler import MultiprocessingHandler

def test_multiprocessing_add():
    """Test multiprocessing with add command."""
    command = AddCommand(Decimal('5'), Decimal('3'))
    result = MultiprocessingHandler.run_command_async(command)
    assert result == Decimal('8')

def test_multiprocessing_multiply():
    """Test multiprocessing with multiply command."""
    command = MultiplyCommand(Decimal('4'), Decimal('7'))
    result = MultiprocessingHandler.run_command_async(command)
    assert result == Decimal('28')

def test_multiprocessing_error_handling():
    """Test error handling in multiprocessing."""
    # Create a command that will raise an exception
    class ErrorCommand:
        """A command that raises an exception."""
        def execute(self):
            """Raise an exception."""
            raise ValueError("Test error")
    # Test that the error is properly propagated
    with pytest.raises(ValueError, match="Test error"):
        MultiprocessingHandler.run_command_async(ErrorCommand())

def test_multiprocessing_empty_queue():
    """Test handling of empty queue in multiprocessing."""
    # Create a mock command
    mock_command = MagicMock()
    # Create a mock for Process
    mock_process = MagicMock()
    # Create a mock for Queue that always returns empty
    mock_queue = MagicMock()
    mock_queue.empty.return_value = True
    # Patch multiprocessing.Process and multiprocessing.Queue
    with patch('multiprocessing.Process', return_value=mock_process), \
         patch('multiprocessing.Queue', return_value=mock_queue):
        # Test that an exception is raised for empty queue
        with pytest.raises(RuntimeError, match="Command execution failed"):
            MultiprocessingHandler.run_command_async(mock_command)
        # Verify process was started and joined
        mock_process.start.assert_called_once()
        mock_process.join.assert_called_once()

def test_execute_command_exception():
    """Test exception handling in execute_command."""
    # Create mock command that raises exception when executed
    mock_command = MagicMock()
    mock_command.execute.side_effect = Exception("Test error")
    # Create mock queue
    mock_queue = MagicMock()
    # Execute command with mock queue
    MultiprocessingHandler.execute_command(mock_command, mock_queue)
    # Verify error was put in queue
    mock_queue.put.assert_called_once_with(('error', 'Test error'))

def test_execute_command_success():
    """Test successful execution in execute_command."""
    # Create mock command that returns a value
    mock_command = MagicMock()
    mock_command.execute.return_value = Decimal('10')
    # Create mock queue
    mock_queue = MagicMock()
    # Execute command with mock queue
    MultiprocessingHandler.execute_command(mock_command, mock_queue)
    # Verify result was put in queue
    mock_queue.put.assert_called_once_with(('success', Decimal('10')))
