"""Tests for the Number Guessing Game project."""

import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "number-guessing-game"


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    # Verify the file compiles
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_game_functions_exist():
    """Test that expected functions exist in the game."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    # Check for key functions
    assert "def get_user_guess()" in content, "get_user_guess function not found"
    assert "def play_round()" in content, "play_round function not found"
    assert "def main()" in content, "main function not found"


def test_game_compiles():
    """Test that the game compiles without errors."""
    main_file = PROJECT_DIR / "main.py"
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(main_file)],
        capture_output=True,
        text=True,
        timeout=30
    )
    assert result.returncode == 0, f"Compilation failed: {result.stderr}"


def test_game_runs(run_python_script):
    """Test that the game can be started (non-interactive smoke test)."""
    main_file = PROJECT_DIR / "main.py"
    
    # Just verify it starts without immediate error
    # We can't fully test interactive input in a non-interactive test
    result = subprocess.run(
        [sys.executable, str(main_file)],
        capture_output=True,
        text=True,
        timeout=30,
        cwd=str(PROJECT_DIR)
    )
    
    # The game will fail on input() but should at least start
    # and print the welcome message
    assert "Number Guessing Game" in result.stdout, "Game should print welcome message"


def test_random_module_used():
    """Test that the random module is imported."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import random" in content, "random module not imported"


def test_input_validation_logic():
    """Test that input validation is present."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "try:" in content, "No try/except for input validation"
    assert "except ValueError" in content, "No ValueError handling"
    assert "1 <= guess <= 100" in content, "Range validation not found"
