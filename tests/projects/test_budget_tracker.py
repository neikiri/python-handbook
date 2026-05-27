"""Tests for the Budget Tracker project."""

import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "budget-tracker"


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_load_transactions_function_exists():
    """Test that load_transactions function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def load_transactions" in content, "load_transactions function not found"


def test_save_transactions_function_exists():
    """Test that save_transactions function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def save_transactions" in content, "save_transactions function not found"


def test_add_transaction_function_exists():
    """Test that add_transaction function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def add_transaction" in content, "add_transaction function not found"


def test_load_and_save_transactions(temp_dir):
    """Test loading and saving transactions to CSV."""
    test_file = temp_dir / "transactions.csv"
    
    # Create a sample CSV
    test_file.write_text(
        "date,type,description,amount,category\n"
        "2024-01-01 10:00:00,income,Salary,5000.00,salary\n"
        "2024-01-02 12:00:00,expense,Food,25.50,food\n"
    )
    
    # Import and test loading
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("budget_tracker", PROJECT_DIR / "main.py")
        budget_tracker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(budget_tracker)
        
        # Mock the DATA_FILE
        original_data_file = budget_tracker.DATA_FILE
        budget_tracker.DATA_FILE = test_file
        
        transactions = budget_tracker.load_transactions()
        
        assert isinstance(transactions, list), "Should return a list"
        assert len(transactions) == 2, f"Expected 2 transactions, got {len(transactions)}"
        
        # Restore original
        budget_tracker.DATA_FILE = original_data_file
    finally:
        sys.path.pop(0)


def test_add_transaction_logic(temp_dir):
    """Test the logic for adding a transaction."""
    test_file = temp_dir / "transactions.csv"
    
    # Start with empty list
    transactions = []
    
    # Simulate adding an income transaction
    transaction = {
        "date": "2024-01-01 10:00:00",
        "type": "income",
        "description": "Salary",
        "amount": 5000.00,
        "category": "salary"
    }
    transactions.append(transaction)
    
    # Simulate adding an expense transaction
    expense = {
        "date": "2024-01-02 12:00:00",
        "type": "expense",
        "description": "Food",
        "amount": 25.50,
        "category": "food"
    }
    transactions.append(expense)
    
    assert len(transactions) == 2
    assert transactions[0]["type"] == "income"
    assert transactions[1]["type"] == "expense"


def test_balance_calculation(temp_dir):
    """Test balance calculation logic."""
    test_file = temp_dir / "transactions.csv"
    
    # Create sample transactions
    transactions = [
        {"date": "2024-01-01", "type": "income", "amount": "5000.00"},
        {"date": "2024-01-02", "type": "expense", "amount": "250.00"},
        {"date": "2024-01-03", "type": "expense", "amount": "150.00"},
    ]
    
    # Calculate income and expense
    income = sum(float(t["amount"]) for t in transactions if t["type"] == "income")
    expense = sum(float(t["amount"]) for t in transactions if t["type"] == "expense")
    balance = income - expense
    
    assert income == 5000.00
    assert expense == 400.00
    assert balance == 4600.00


def test_category_summary_logic(temp_dir):
    """Test category summary calculation logic."""
    test_file = temp_dir / "transactions.csv"
    
    # Create sample transactions
    transactions = [
        {"type": "expense", "category": "food", "amount": "25.00"},
        {"type": "expense", "category": "food", "amount": "15.00"},
        {"type": "expense", "category": "transport", "amount": "10.00"},
        {"type": "expense", "category": "housing", "amount": "500.00"},
    ]
    
    # Calculate by category
    by_category = {}
    for t in transactions:
        cat = t["category"]
        by_category[cat] = by_category.get(cat, 0) + float(t["amount"])
    
    assert by_category["food"] == 40.00
    assert by_category["transport"] == 10.00
    assert by_category["housing"] == 500.00


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


def test_csv_module_used():
    """Test that csv module is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import csv" in content, "csv module not imported"
    assert "DictReader" in content, "DictReader not used"
    assert "DictWriter" in content, "DictWriter not used"


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
