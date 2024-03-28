"""Module for testing command functionalities in the application."""
#from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_add_command(capfd):
    """Test that the REPL correctly handles the 'add' command."""
    command = AddCommand()
    command.execute("3 4")
    out, _ = capfd.readouterr()
    assert out.strip() == "3.0 + 4.0 = 7.0", "The AddCommand should correctly add two numbers"

def test_subtract_command(capfd):
    """Test that the REPL correctly handles the 'subtract' command."""
    command = SubtractCommand()
    command.execute("10 4")
    out, _ = capfd.readouterr()
    assert out.strip() == "10.0 - 4.0 = 6.0", "The SubtractCommand should correctly subtract two numbers"

def test_multiply_command(capfd):
    """Test that the REPL correctly handles the 'multiply' command."""
    command = MultiplyCommand()
    command.execute("2 5")
    out, _ = capfd.readouterr()
    assert out.strip() == "2.0 * 5.0 = 10.0", "The MultiplyCommand should correctly multiply two numbers"

def test_divide_command(capfd):
    """Test that the REPL correctly handles the 'divide' command."""
    command = DivideCommand()
    command.execute("8 2")
    out, _ = capfd.readouterr()
    assert out.strip() == "8.0 / 2.0 = 4.0", "The DivideCommand should correctly divide two numbers"

def test_divide_by_zero_command(capfd):
    """Test that the REPL correctly handles the 'divide by zero' command."""
    command = DivideCommand()
    command.execute("8 0")
    out, _ = capfd.readouterr()
    assert "Error" in out, "The DivideCommand should handle division by zero with an error message"
