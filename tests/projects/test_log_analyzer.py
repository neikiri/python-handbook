"""Tests for the Log Analyzer project."""

import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "log-analyzer"


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_parse_log_file_function_exists():
    """Test that parse_log_file function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def parse_log_file" in content, "parse_log_file function not found"


def test_parse_log_file_returns_correct_structure(sample_log_file):
    """Test that parse_log_file returns a dict with expected keys."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("log_analyzer", PROJECT_DIR / "main.py")
        log_analyzer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(log_analyzer)
        
        stats = log_analyzer.parse_log_file(str(sample_log_file))
        
        assert isinstance(stats, dict), "Should return a dict"
        assert "total_lines" in stats, "Missing total_lines key"
        assert "level_counts" in stats, "Missing level_counts key"
        assert "error_lines" in stats, "Missing error_lines key"
        
        # Verify counts
        assert stats["total_lines"] == 6, f"Expected 6 lines, got {stats['total_lines']}"
    finally:
        sys.path.pop(0)


def test_parse_log_file_file_not_found():
    """Test that parse_log_file raises FileNotFoundError for missing file."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("log_analyzer", PROJECT_DIR / "main.py")
        log_analyzer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(log_analyzer)
        
        with pytest.raises(FileNotFoundError):
            log_analyzer.parse_log_file("/nonexistent/file.log")
    finally:
        sys.path.pop(0)


def test_log_level_counts(sample_log_file):
    """Test that log levels are counted correctly."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("log_analyzer", PROJECT_DIR / "main.py")
        log_analyzer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(log_analyzer)
        
        stats = log_analyzer.parse_log_file(str(sample_log_file))
        
        level_counts = stats["level_counts"]
        
        # Check that we have some level counts
        assert len(level_counts) > 0, "Should have some log levels"
        
        # Check for expected levels
        assert "INFO" in level_counts, "INFO level not found"
        assert "ERROR" in level_counts, "ERROR level not found"
    finally:
        sys.path.pop(0)


def test_error_line_extraction(sample_log_file):
    """Test that error lines are extracted correctly."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("log_analyzer", PROJECT_DIR / "main.py")
        log_analyzer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(log_analyzer)
        
        stats = log_analyzer.parse_log_file(str(sample_log_file))
        
        error_lines = stats["error_lines"]
        
        # Should have some error lines
        assert isinstance(error_lines, list), "error_lines should be a list"
        
        # Each error line should be a string
        for line in error_lines:
            assert isinstance(line, str), "Each error line should be a string"
    finally:
        sys.path.pop(0)


def test_error_lines_contain_errors(sample_log_file):
    """Test that error lines actually contain error messages."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("log_analyzer", PROJECT_DIR / "main.py")
        log_analyzer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(log_analyzer)
        
        stats = log_analyzer.parse_log_file(str(sample_log_file))
        
        error_lines = stats["error_lines"]
        
        # Check that error lines contain ERROR or CRITICAL
        for line in error_lines:
            assert "ERROR" in line or "CRITICAL" in line, "Error line should contain ERROR or CRITICAL"
    finally:
        sys.path.pop(0)


def test_main_module_compiles():
    """Test that main.py compiles without errors."""
    main_file = PROJECT_DIR / "main.py"
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(main_file)],
        capture_output=True,
        text=True,
        timeout=30
    )
    assert result.returncode == 0, f"Compilation failed: {result.stderr}"


def test_re_module_used():
    """Test that re module is used for pattern matching."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import re" in content, "re module not imported"


def test_collections_counter_used():
    """Test that collections.Counter is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "from collections import Counter" in content, "Counter not imported"


def test_pathlib_used():
    """Test that pathlib is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "from pathlib import Path" in content, "Pathlib not imported"
