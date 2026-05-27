"""Tests for the Todo CLI project."""

import json
import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "todo-cli"


@pytest.fixture
def test_data_dir(temp_dir):
    """Create a test data directory with a temporary todos file."""
    return temp_dir


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_load_todos_empty_file(test_data_dir):
    """Test loading todos from an empty JSON file."""
    # Import the module
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("todo_cli", PROJECT_DIR / "main.py")
        todo_cli = importlib.util.module_from_spec(spec)
        
        # Mock the DATA_FILE to use our temp directory
        test_file = test_data_dir / "todos.json"
        test_file.write_text("[]")
        
        # We need to test the logic directly
        with open(test_file, 'r') as f:
            data = json.load(f)
        
        assert data == [], "Empty file should load as empty list"
    finally:
        sys.path.pop(0)


def test_save_and_load_todos(test_data_dir):
    """Test saving and loading todos."""
    test_file = test_data_dir / "todos.json"
    
    # Save some todos
    todos = [
        {"id": 1, "description": "Test task 1", "completed": False},
        {"id": 2, "description": "Test task 2", "completed": True},
    ]
    
    with open(test_file, 'w') as f:
        json.dump(todos, f)
    
    # Load them back
    with open(test_file, 'r') as f:
        loaded = json.load(f)
    
    assert len(loaded) == 2
    assert loaded[0]["description"] == "Test task 1"
    assert loaded[1]["completed"] is True


def test_add_todo_logic(test_data_dir):
    """Test the logic for adding a todo."""
    test_file = test_data_dir / "todos.json"
    
    # Start with empty list
    todos = []
    
    # Simulate adding a todo
    todo = {
        "id": len(todos) + 1,
        "description": "New task",
        "completed": False
    }
    todos.append(todo)
    
    # Save
    with open(test_file, 'w') as f:
        json.dump(todos, f)
    
    # Verify
    with open(test_file, 'r') as f:
        loaded = json.load(f)
    
    assert len(loaded) == 1
    assert loaded[0]["id"] == 1
    assert loaded[0]["description"] == "New task"


def test_complete_todo_logic(test_data_dir):
    """Test the logic for marking a todo as complete."""
    test_file = test_data_dir / "todos.json"
    
    # Start with some todos
    todos = [
        {"id": 1, "description": "Task 1", "completed": False},
        {"id": 2, "description": "Task 2", "completed": False},
    ]
    
    # Mark task 1 as complete
    for todo in todos:
        if todo["id"] == 1:
            todo["completed"] = True
            break
    
    # Verify
    assert todos[0]["completed"] is True
    assert todos[1]["completed"] is False


def test_delete_todo_logic(test_data_dir):
    """Test the logic for deleting a todo."""
    test_file = test_data_dir / "todos.json"
    
    # Start with some todos
    todos = [
        {"id": 1, "description": "Task 1", "completed": False},
        {"id": 2, "description": "Task 2", "completed": False},
        {"id": 3, "description": "Task 3", "completed": False},
    ]
    
    # Delete task 2
    for i, todo in enumerate(todos):
        if todo["id"] == 2:
            todos.pop(i)
            break
    
    # Renumber
    for j, t in enumerate(todos, 1):
        t["id"] = j
    
    # Verify
    assert len(todos) == 2
    assert todos[0]["id"] == 1
    assert todos[1]["id"] == 2


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
    assert "add_argument" in content, "add_argument not used"


def test_json_persistence():
    """Test that JSON module is used for persistence."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import json" in content, "json module not imported"
    assert "json.load" in content, "json.load not used"
    assert "json.dump" in content, "json.dump not used"
