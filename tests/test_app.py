
"""Tests for the app module."""
import pytest
from app import App

def test_app_get_environment_variable():
    """Test whether the environment variables are fetched """
    app = App()
    #Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test app starts and exits correctly."""
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit
    out, _ = capfd.readouterr()
    assert "Type 'exit' to exit." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    #abc
    with pytest.raises(SystemExit) as excinfo:
        app.start()
        # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_menu_command_listing(capfd, monkeypatch):
    """Test that the 'menu' command correctly lists available commands."""
    # Assuming your test environment has a fixed set of plugins, or you've mocked the plugin loading.
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    # Catch the SystemExit exception raised by the 'exit' command
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    #app.start()
    # Now you can make assertions even after the 'exit' command was processed
    assert excinfo.type == SystemExit, "App should exit using sys.exit"

    out, _ = capfd.readouterr()
    # Verify that expected commands are listed. Adjust according to your actual plugins/commands.
    expected_commands = ["menu", "exit"]  # Extend this list based on your test setup
    for command in expected_commands:
        assert command in out, f"Expected '{command}' to be listed in the menu."
        
