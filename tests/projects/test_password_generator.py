"""Tests for the Password Generator project."""

import subprocess
import sys
from pathlib import Path
import pytest

PROJECT_DIR = Path(__file__).parent.parent.parent / "projects" / "password-generator"


def test_import_main_module():
    """Test that the main module can be imported."""
    main_file = PROJECT_DIR / "main.py"
    assert main_file.exists(), "main.py not found"
    
    import py_compile
    py_compile.compile(main_file, doraise=True)


def test_generate_password_function_exists():
    """Test that generate_password function exists."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "def generate_password" in content, "generate_password function not found"


def test_generate_password_returns_string():
    """Test that generate_password returns a string."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        password = password_gen.generate_password(length=12)
        
        assert isinstance(password, str), "Should return a string"
    finally:
        sys.path.pop(0)


def test_generate_password_length():
    """Test that generate_password creates passwords of correct length."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        # Test different lengths
        for length in [8, 12, 16, 20]:
            password = password_gen.generate_password(length=length)
            assert len(password) == length, f"Expected length {length}, got {len(password)}"
    finally:
        sys.path.pop(0)


def test_generate_password_minimum_length():
    """Test that generate_password enforces minimum length of 4."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        # Even with length < 4, should get at least 4 characters
        password = password_gen.generate_password(length=2)
        assert len(password) >= 4, "Minimum length should be 4"
    finally:
        sys.path.pop(0)


def test_generate_password_with_symbols():
    """Test that generate_password includes symbols when requested."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        # Generate with symbols
        password_with_symbols = password_gen.generate_password(length=20, include_symbols=True)
        
        # Check if it contains any symbols
        import string
        has_symbol = any(c in string.punctuation for c in password_with_symbols)
        
        # With 20 chars, it's extremely likely to have at least one symbol
        # If not, we can't be certain, but it's very improbable
        assert has_symbol or len(password_with_symbols) < 4, "Password with symbols should contain symbols"
    finally:
        sys.path.pop(0)


def test_generate_password_without_symbols():
    """Test that generate_password excludes symbols when not requested."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        # Generate without symbols
        password_without_symbols = password_gen.generate_password(length=20, include_symbols=False)
        
        # Check that it doesn't contain symbols
        import string
        has_symbol = any(c in string.punctuation for c in password_without_symbols)
        
        assert not has_symbol, "Password without symbols should not contain symbols"
    finally:
        sys.path.pop(0)


def test_generate_password_has_lowercase():
    """Test that generate_password includes lowercase letters."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        password = password_gen.generate_password(length=20)
        
        assert any(c.islower() for c in password), "Password should contain lowercase letters"
    finally:
        sys.path.pop(0)


def test_generate_password_has_uppercase():
    """Test that generate_password includes uppercase letters."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        password = password_gen.generate_password(length=20)
        
        assert any(c.isupper() for c in password), "Password should contain uppercase letters"
    finally:
        sys.path.pop(0)


def test_generate_password_has_digits():
    """Test that generate_password includes digits."""
    sys.path.insert(0, str(PROJECT_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("password_gen", PROJECT_DIR / "main.py")
        password_gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_gen)
        
        password = password_gen.generate_password(length=20)
        
        assert any(c.isdigit() for c in password), "Password should contain digits"
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


def test_secrets_module_used():
    """Test that secrets module is used for secure random generation."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import secrets" in content, "secrets module not imported"


def test_string_module_used():
    """Test that string module is used for character sets."""
    main_file = PROJECT_DIR / "main.py"
    content = main_file.read_text()
    
    assert "import string" in content, "string module not imported"
