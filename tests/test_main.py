"""This file is for testing main.py file"""
from unittest.mock import patch
from io import StringIO
from main import main

# Mock function to simulate user input
def test_command_execution():
    """Test command execution through the REPL."""
    # Test add command
    with patch('builtins.input', side_effect=['add 5 3', 'exit']), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
        assert "The result is: 8" in output
    # Test subtract command
    with patch('builtins.input', side_effect=['subtract 10 4', 'exit']), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
        assert "The result is: 6" in output
    # Test error handling
    with patch('builtins.input', side_effect=['add invalid 3', 'exit']), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
        assert "Error" in output or "Failed" in output

def test_menu_command():
    """Test the menu command in the REPL."""
    with patch('builtins.input', side_effect=['menu', 'exit']), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
        assert "Available commands" in output
        assert "add" in output
        assert "subtract" in output
        assert "menu" in output
        assert "exit" in output

def test_unknown_command():
    """Test handling of unknown commands."""
    with patch('builtins.input', side_effect=['unknown_cmd', 'exit']), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
        assert "Unknown command" in output

# @pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
#     ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
#     ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
#     ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
#     ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
#     ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),\
#             # Adjusted for the actual error message
#     ("9", "3", 'unknown', "Unknown operation: unknown"),\
#             # Test for unknown operation
#     ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),\
#             # Testing invalid number input
#     ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),\
#             # Testing another invalid number input
#     ("", "3", 'add', "Invalid number input:  or 3 is not a valid number."),
#     ("5", "", 'subtract', "Invalid number input: 5 or  is not a valid number."),
#     ("", "", 'multiply', "Invalid number input:  or  is not a valid number."),
#     ("1", "1", "", "Unknown operation: "),
#     ("None", "5", "add", "Invalid number input: None or 5 is not a valid number.")
# ])

# def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
#     '''Test calculate_and_print function'''
#     calculate_and_print(a_string, b_string, operation_string)
#     captured = capsys.readouterr()
#     assert captured.out.strip() == expected_string.strip()
