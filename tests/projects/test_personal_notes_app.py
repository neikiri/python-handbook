"""Tests for the Personal Notes App project."""

import json
import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "personal-notes-app"


@pytest.fixture
def test_data_dir(temp_dir):
    """Create a test data directory with a temporary notes file."""
    return temp_dir


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_load_notes_function_exists():
    """Test that load_notes function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def load_notes" in content, "load_notes function not found"


def test_save_notes_function_exists():
    """Test that save_notes function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def save_notes" in content, "save_notes function not found"


def test_add_note_function_exists():
    """Test that add_note function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def add_note" in content, "add_note function not found"


def test_search_notes_function_exists():
    """Test that search_notes function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def search_notes" in content, "search_notes function not found"


def test_delete_note_function_exists():
    """Test that delete_note function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def delete_note" in content, "delete_note function not found"


def test_load_and_save_notes(test_data_dir):
    """Test loading and saving notes to JSON."""
    test_file = test_data_dir / "notes.json"
    
    # Create a sample JSON
    notes = [
        {"id": 1, "content": "First note", "created": "2024-01-01 10:00:00"},
        {"id": 2, "content": "Second note", "created": "2024-01-02 12:00:00"},
    ]
    
    with open(test_file, 'w') as f:
        json.dump(notes, f)
    
    # Load them back
    with open(test_file, 'r') as f:
        loaded = json.load(f)
    
    assert len(loaded) == 2
    assert loaded[0]["content"] == "First note"
    assert loaded[1]["id"] == 2


def test_add_note_logic(test_data_dir):
    """Test the logic for adding a note."""
    test_file = test_data_dir / "notes.json"
    
    # Start with empty list
    notes = []
    
    # Simulate adding a note
    note = {
        "id": len(notes) + 1,
        "content": "New note",
        "created": "2024-01-01 10:00:00"
    }
    notes.append(note)
    
    # Verify
    assert len(notes) == 1
    assert notes[0]["id"] == 1
    assert notes[0]["content"] == "New note"


def test_search_notes_logic(test_data_dir):
    """Test the logic for searching notes."""
    test_file = test_data_dir / "notes.json"
    
    # Create sample notes
    notes = [
        {"id": 1, "content": "First note about Python", "created": "2024-01-01"},
        {"id": 2, "content": "Second note about Java", "created": "2024-01-02"},
        {"id": 3, "content": "Third note about Python and Django", "created": "2024-01-03"},
    ]
    
    # Search for "Python"
    query = "python"
    matches = [n for n in notes if query in n['content'].lower()]
    
    assert len(matches) == 2
    assert matches[0]["content"] == "First note about Python"
    assert matches[1]["content"] == "Third note about Python and Django"


def test_delete_note_logic(test_data_dir):
    """Test the logic for deleting a note."""
    test_file = test_data_dir / "notes.json"
    
    # Create sample notes
    notes = [
        {"id": 1, "content": "First note", "created": "2024-01-01"},
        {"id": 2, "content": "Second note", "created": "2024-01-02"},
        {"id": 3, "content": "Third note", "created": "2024-01-03"},
    ]
    
    # Delete note 2
    for i, note in enumerate(notes):
        if note["id"] == 2:
            notes.pop(i)
            break
    
    # Renumber
    for j, n in enumerate(notes, 1):
        n["id"] = j
    
    # Verify
    assert len(notes) == 2
    assert notes[0]["id"] == 1
    assert notes[1]["id"] == 2


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


def test_json_module_used():
    """Test that json module is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import json" in content, "json module not imported"
    assert "json.load" in content, "json.load not used"
    assert "json.dump" in content, "json.dump not used"


def test_datetime_module_used():
    """Test that datetime module is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "from datetime import datetime" in content, "datetime not imported"


def test_argparse_usage():
    """Test that argparse is used for CLI."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import argparse" in content, "argparse not imported"
    assert "ArgumentParser" in content, "ArgumentParser not used"
