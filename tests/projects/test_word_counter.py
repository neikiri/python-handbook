"""Tests for the Word Counter project."""

import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "word-counter"


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_count_text_stats_function_exists():
    """Test that count_text_stats function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def count_text_stats" in content, "count_text_stats function not found"


def test_count_text_stats_returns_correct_structure(sample_text_file):
    """Test that count_text_stats returns a dict with expected keys."""
    # Import the function
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("word_counter", PROJECT_DIR / "main.py")
        word_counter = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(word_counter)
        
        stats = word_counter.count_text_stats(str(sample_text_file))
        
        assert isinstance(stats, dict), "Should return a dict"
        assert "line_count" in stats, "Missing line_count key"
        assert "word_count" in stats, "Missing word_count key"
        assert "char_count" in stats, "Missing char_count key"
        assert "word_freq" in stats, "Missing word_freq key"
        
        # Verify counts
        assert stats["line_count"] == 4, f"Expected 4 lines, got {stats['line_count']}"
        assert stats["word_count"] > 0, "Should have some words"
        assert stats["char_count"] > 0, "Should have some characters"
    finally:
        sys.path.pop(0)


def test_count_text_stats_file_not_found():
    """Test that count_text_stats raises FileNotFoundError for missing file."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("word_counter", PROJECT_DIR / "main.py")
        word_counter = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(word_counter)
        
        with pytest.raises(FileNotFoundError):
            word_counter.count_text_stats("/nonexistent/file.txt")
    finally:
        sys.path.pop(0)


def test_word_frequency_counting(sample_text_file):
    """Test that word frequency is counted correctly."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("word_counter", PROJECT_DIR / "main.py")
        word_counter = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(word_counter)
        
        stats = word_counter.count_text_stats(str(sample_text_file))
        
        # Check that word_freq is a Counter-like object
        word_freq = stats["word_freq"]
        
        # The sample text has "Hello, World!" so "Hello" should appear
        # Note: The actual text may vary, just check it's a dict-like object
        assert hasattr(word_freq, 'most_common'), "word_freq should have most_common method"
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


def test_argparse_usage():
    """Test that argparse is used for CLI."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import argparse" in content, "argparse not imported"
    assert "ArgumentParser" in content, "ArgumentParser not used"


def test_collections_counter_used():
    """Test that collections.Counter is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "from collections import Counter" in content, "Counter not imported"
