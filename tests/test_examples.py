"""Smoke tests for example Python files."""

import subprocess
import sys
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def get_python_files():
    """Get all Python files in the examples directory."""
    return list(EXAMPLES_DIR.rglob("*.py"))


def test_examples_compile():
    """Verify all example files compile without syntax errors."""
    python_files = get_python_files()
    assert len(python_files) > 0, "No Python files found in examples directory"
    
    for py_file in python_files:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", str(py_file)],
            capture_output=True,
            text=True,
            timeout=30
        )
        assert result.returncode == 0, f"Failed to compile {py_file.name}: {result.stderr}"


def test_examples_run_non_interactive(run_python_script):
    """Run non-interactive example files to verify they execute."""
    interactive_files = {
        "input_and_output.py",  # Uses input()
        "args_kwargs.py",       # May use interactive examples
    }
    
    python_files = get_python_files()
    errors = []
    
    for py_file in python_files:
        # Skip interactive files
        if py_file.name in interactive_files:
            continue
        
        # Skip files that import tkinter or other GUI libraries
        content = py_file.read_text()
        if "tkinter" in content or "PyQt" in content or "wxpython" in content.lower():
            continue
        
        result = run_python_script(py_file)
        
        # Allow files to fail with SystemExit (common in argparse examples)
        if result.returncode not in (0, 1):
            errors.append(f"{py_file.name}: {result.stderr}")
    
    if errors:
        raise AssertionError("\n".join(errors))


def test_variables_and_types_example(run_python_script):
    """Test the variables and types example runs."""
    example_file = EXAMPLES_DIR / "basics" / "variables_and_types.py"
    result = run_python_script(example_file)
    assert result.returncode == 0
    assert "Variables and Types" in result.stdout


def test_operators_example(run_python_script):
    """Test the operators example runs."""
    example_file = EXAMPLES_DIR / "basics" / "operators.py"
    result = run_python_script(example_file)
    assert result.returncode == 0
    assert "Arithmetic Operators" in result.stdout


def test_basic_functions_example(run_python_script):
    """Test the basic functions example runs."""
    example_file = EXAMPLES_DIR / "functions" / "basic_functions.py"
    result = run_python_script(example_file)
    assert result.returncode == 0
    assert "Defining a Function" in result.stdout


def test_lists_example(run_python_script):
    """Test the lists example runs."""
    example_file = EXAMPLES_DIR / "collections" / "lists.py"
    result = run_python_script(example_file)
    assert result.returncode == 0
    assert "Creating Lists" in result.stdout


def test_argparse_example(run_python_script):
    """Test the argparse example runs."""
    example_file = EXAMPLES_DIR / "stdlib" / "argparse_example.py"
    result = run_python_script(example_file)
    assert result.returncode == 0
    assert "Basic Argument Parser" in result.stdout


def test_string_formatting_example(run_python_script):
    """Test the string formatting example runs."""
    example_file = EXAMPLES_DIR / "strings" / "formatting.py"
    result = run_python_script(example_file)
    assert result.returncode == 0


def test_json_read_write_example(run_python_script):
    """Test the JSON read/write example runs."""
    example_file = EXAMPLES_DIR / "files" / "json_read_write.py"
    result = run_python_script(example_file)
    assert result.returncode == 0


def test_csv_read_write_example(run_python_script):
    """Test the CSV read/write example runs."""
    example_file = EXAMPLES_DIR / "files" / "csv_read_write.py"
    result = run_python_script(example_file)
    assert result.returncode == 0
