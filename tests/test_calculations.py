"""Tests for the Calculations class."""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculation():
    """Set up the Calculation class."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

@pytest.mark.usefixtures("setup_calculation")
def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('15'), Decimal('28'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc,\
          "Failed to add calculation to history."

@pytest.mark.usefixtures("setup_calculation")
def test_get_history():
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "Failed to get history."

@pytest.mark.usefixtures("setup_calculation")
def test_clear_history():
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "Failed to clear history."

@pytest.mark.usefixtures("setup_calculation")
def test_last_calculation():
    """Test getting the last calculation."""
    latest = Calculations.get_last_calculation()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'),\
          "Did not get the correct latest calculation"

@pytest.mark.usefixtures("setup_calculation")
def test_find_calculations_by_operation():
    """Test finding calculations by operation."""
    add_operation = Calculations.find_calculations_by_operation('add')
    assert len(add_operation) == 1, "Failed to find calculations by add operation."

    subtract_operation = Calculations.find_calculations_by_operation('subtract')
    assert len(subtract_operation) == 1, "Failed to find calculations by subtract operation."

@pytest.mark.usefixtures("setup_calculation")
def test_get_last_with_empty_history():
    """Test getting the last calculation with an empty history."""
    Calculations.clear_history()
    assert Calculations.get_last_calculation() is None,\
          "Failed to get last calculation with empty history."

@pytest.mark.usefixtures("setup_calculation")
def test_get_first_n_calculations():
    """Test getting the first n calculations from history."""
    # Add a third calculation to have more data
    calc = Calculation(Decimal('30'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    # Get more calculations than exist in history
    all_calcs = Calculations.get_first_n_calculations(10)
    assert all_calcs is not None, "Failed to get all calculations"
    assert len(all_calcs) == 3, "Failed to handle n larger than history size"

@pytest.mark.usefixtures("setup_calculation")
def test_empty_get_n_calculations():
    """Test edge cases with empty history for get_n methods."""
    Calculations.clear_history()
    assert Calculations.get_last_n_calculations(1) is None, "Should return None for empty history"
    assert Calculations.get_first_n_calculations(1) is None, "Should return None for empty history"
