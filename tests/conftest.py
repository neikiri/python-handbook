"""Shared fixtures for pytest tests."""

import tempfile
import shutil
import subprocess
import sys
from pathlib import Path
import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    temp = tempfile.mkdtemp()
    yield Path(temp)
    shutil.rmtree(temp)


@pytest.fixture
def sample_csv_file(temp_dir):
    """Create a sample CSV file for testing."""
    csv_path = temp_dir / "sales.csv"
    csv_path.write_text(
        "product,quantity,price\n"
        "Widget,10,9.99\n"
        "Gadget,5,19.99\n"
        "Gizmo,20,4.99\n"
    )
    return csv_path


@pytest.fixture
def sample_log_file(temp_dir):
    """Create a sample log file for testing."""
    log_path = temp_dir / "app.log"
    log_path.write_text(
        "2024-01-01 10:00:00 INFO Application started\n"
        "2024-01-01 10:01:00 INFO Processing request\n"
        "2024-01-01 10:02:00 ERROR Database connection failed\n"
        "2024-01-01 10:03:00 INFO Retrying connection\n"
        "2024-01-01 10:04:00 ERROR Timeout occurred\n"
        "2024-01-01 10:05:00 INFO Connection restored\n"
    )
    return log_path


@pytest.fixture
def sample_text_file(temp_dir):
    """Create a sample text file for testing."""
    text_path = temp_dir / "sample.txt"
    text_path.write_text(
        "Hello, World!\n"
        "This is a test file.\n"
        "It has multiple lines.\n"
        "And some words.\n"
    )
    return text_path


@pytest.fixture
def run_python_script():
    """Helper to run a Python script with subprocess."""
    def _run(script_path, args=None, input_text=None, cwd=None):
        cmd = [sys.executable, str(script_path)]
        if args:
            cmd.extend(args)
        
        result = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            input=input_text,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result
    
    return _run


@pytest.fixture
def sample_sales_csv(temp_dir):
    """Create a sample sales CSV file."""
    csv_path = temp_dir / "sales.csv"
    csv_path.write_text(
        "product,amount,quantity\n"
        "Widget,9.99,10\n"
        "Gadget,19.99,5\n"
        "Gizmo,4.99,20\n"
        "Widget,9.99,3\n"
    )
    return csv_path


@pytest.fixture
def sample_log_content():
    """Return sample log content as a string."""
    return (
        "2024-01-01 10:00:00 INFO Application started\n"
        "2024-01-01 10:01:00 INFO Processing request\n"
        "2024-01-01 10:02:00 ERROR Database connection failed\n"
        "2024-01-01 10:03:00 WARNING High memory usage\n"
        "2024-01-01 10:04:00 ERROR Timeout occurred\n"
        "2024-01-01 10:05:00 CRITICAL System failure\n"
        "2024-01-01 10:06:00 INFO Recovery started\n"
    )