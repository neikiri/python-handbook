"""Tests for the CSV Sales Report project."""

import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "csv-sales-report"


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_read_sales_data_function_exists():
    """Test that read_sales_data function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def read_sales_data" in content, "read_sales_data function not found"


def test_read_sales_data_returns_list(sample_sales_csv):
    """Test that read_sales_data returns a list of dictionaries."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("sales_report", PROJECT_DIR / "main.py")
        sales_report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sales_report)
        
        sales = sales_report.read_sales_data(str(sample_sales_csv))
        
        assert isinstance(sales, list), "Should return a list"
        assert len(sales) > 0, "Should have sales records"
        assert isinstance(sales[0], dict), "Each record should be a dict"
        
        # Check expected keys
        assert "product" in sales[0], "Missing product key"
        assert "amount" in sales[0], "Missing amount key"
        assert "quantity" in sales[0], "Missing quantity key"
    finally:
        sys.path.pop(0)


def test_read_sales_data_file_not_found():
    """Test that read_sales_data raises FileNotFoundError for missing file."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("sales_report", PROJECT_DIR / "main.py")
        sales_report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sales_report)
        
        with pytest.raises(FileNotFoundError):
            sales_report.read_sales_data("/nonexistent/file.csv")
    finally:
        sys.path.pop(0)


def test_calculate_totals_function_exists():
    """Test that calculate_totals function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def calculate_totals" in content, "calculate_totals function not found"


def test_calculate_totals(sample_sales_csv):
    """Test that calculate_totals computes correct total."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("sales_report", PROJECT_DIR / "main.py")
        sales_report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sales_report)
        
        sales = sales_report.read_sales_data(str(sample_sales_csv))
        total = sales_report.calculate_totals(sales)
        
        # Verify it's a number
        assert isinstance(total, (int, float)), "Total should be a number"
        assert total > 0, "Total should be positive"
    finally:
        sys.path.pop(0)


def test_calculate_by_product(sample_sales_csv):
    """Test that calculate_by_product groups sales by product."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("sales_report", PROJECT_DIR / "main.py")
        sales_report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sales_report)
        
        sales = sales_report.read_sales_data(str(sample_sales_csv))
        by_product = sales_report.calculate_by_product(sales)
        
        assert isinstance(by_product, dict), "Should return a dict"
        assert len(by_product) > 0, "Should have some products"
        
        # Check that values are numbers
        for product, total in by_product.items():
            assert isinstance(total, (int, float)), f"Total for {product} should be a number"
    finally:
        sys.path.pop(0)


def test_calculate_average(sample_sales_csv):
    """Test that calculate_average computes average sale amount."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("sales_report", PROJECT_DIR / "main.py")
        sales_report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sales_report)
        
        sales = sales_report.read_sales_data(str(sample_sales_csv))
        avg = sales_report.calculate_average(sales)
        
        assert isinstance(avg, (int, float)), "Average should be a number"
        assert avg > 0, "Average should be positive"
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


def test_csv_module_used():
    """Test that csv module is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import csv" in content, "csv module not imported"
    assert "DictReader" in content, "DictReader not used"


def test_pathlib_used():
    """Test that pathlib is used."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "from pathlib import Path" in content, "Pathlib not imported"
