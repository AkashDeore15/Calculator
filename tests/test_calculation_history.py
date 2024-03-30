"""
Test module for the CalculationHistory class in the 'app' package. These tests
ensure that the CalculationHistory class correctly initializes, loads, adds,
saves, and deletes calculation records, with a focus on functionality for
managing calculation history in a DataFrame.
"""
from unittest.mock import patch, MagicMock
import pytest
import pandas as pd


from app.calculation_history import CalculationHistory

# Fixture to reset the CalculationHistory singleton for isolation between tests
@pytest.fixture(autouse=True)
def reset_calculation_history_singleton():
    """Reset the CalculationHistory singleton before and after each test for isolation."""
    CalculationHistory._instance = None
    yield
    CalculationHistory._instance = None

@patch("dotenv.load_dotenv", MagicMock())
@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv", return_value=pd.DataFrame([{'Operation': '3 + 4', 'Result': 7}]))
@patch("os.getenv", return_value="test_history.csv")
@patch("os.path.abspath", return_value="/fakepath/test_history.csv")
def test_load_or_initialize_history_with_existing_file(mock_abspath, mock_getenv, mock_read_csv, mock_exists):
    """Test that history is loaded correctly from an existing file."""
    history = CalculationHistory()
    assert not history.history_df.empty
    assert history.history_df.iloc[0]['Operation'] == '3 + 4'
    assert history.history_df.iloc[0]['Result'] == 7

@patch("dotenv.load_dotenv", MagicMock())
@patch("os.makedirs", MagicMock())
@patch("pandas.DataFrame.to_csv", MagicMock())
def test_save_history():
    """Test saving the current history to a file."""
    history = CalculationHistory()
    history.history_df = MagicMock()
    history.save_history()
    history.history_df.to_csv.assert_called_with(history.history_file, index=False)

@patch("dotenv.load_dotenv", MagicMock())
@patch("os.makedirs", MagicMock())
@patch("pandas.DataFrame.to_csv", MagicMock())
def test_add_record():
    """Test adding a record to the calculation history."""
    history = CalculationHistory()
    history.add_record("3 * 3", 9)
    assert not history.history_df.empty
    assert history.history_df.iloc[-1]['Operation'] == "3 * 3"
    assert history.history_df.iloc[-1]['Result'] == 9

@patch("dotenv.load_dotenv", MagicMock())
@patch("os.makedirs", MagicMock())
@patch("pandas.DataFrame.to_csv", MagicMock())
def test_clear_history():
    """Test clearing all records from the calculation history."""
    history = CalculationHistory()
    history.clear_history()
    assert history.history_df.empty

@patch("dotenv.load_dotenv", MagicMock())
@patch("os.makedirs", MagicMock())
@patch("pandas.DataFrame.to_csv", MagicMock())
@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv", return_value=pd.DataFrame([{'Operation': '3 + 4', 'Result': 7}]))
def test_delete_history_valid_index(mock_read_csv, mock_exists):
    """Test deleting a history record by a valid index."""
    history = CalculationHistory()
    result = history.delete_history(0)
    assert result is True
    assert history.history_df.empty

@patch("dotenv.load_dotenv", MagicMock())
@patch("os.makedirs", MagicMock())
@patch("pandas.DataFrame.to_csv", MagicMock())
@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv", return_value=pd.DataFrame([{'Operation': '3 + 4', 'Result': 7}]))
def test_delete_history_invalid_index(mock_read_csv, mock_exists):
    """Test attempting to delete a history record by an invalid index."""
    history = CalculationHistory()
    result = history.delete_history(999)  # Assuming an index that doesn't exist
    assert result is False
    assert not history.history_df.empty  # The DataFrame should remain unchanged
