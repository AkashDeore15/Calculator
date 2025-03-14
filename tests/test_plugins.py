"""Tests for the plugin system."""
from decimal import Decimal
import pytest
from calculator.command_handler import CommandHandler
from calculator.plugins.power import PowerCommand

def test_plugin_loading():
    """Test that plugins are loaded correctly."""
    handler = CommandHandler()
    # Check if the power command was loaded
    assert 'power' in handler.command_dict
    # Test power command if available
    if 'power' in handler.command_dict:
        power_cmd = handler.get_command('power', ['2', '3'])
        assert power_cmd.execute() == Decimal('8')

def test_invalid_plugin_args():
    """Test invalid arguments for plugin commands."""
    handler = CommandHandler()
    # Test with invalid arguments if power command exists
    if 'power' in handler.command_dict:
        assert handler.get_command('power', ['invalid', '3']) is None

def test_power_non_integer_exponent():
    """Test power command with non-integer exponent."""
    # Create command with decimal exponent
    command = PowerCommand(Decimal('2'), Decimal('3.5'))
    # Test that an exception is raised
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        command.execute()

def test_power_negative_exponent():
    """Test power command with negative exponent."""
    # Create command with negative exponent
    command = PowerCommand(Decimal('2'), Decimal('-3'))
    # Test that negative exponents work correctly
    result = command.execute()
    assert result == Decimal('0.125')
