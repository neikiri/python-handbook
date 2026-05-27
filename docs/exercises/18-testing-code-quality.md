# Chapter 18: Testing and Code Quality — Exercises

## Overview

These exercises help you write tests, measure code quality, and follow best practices. By the end, you will write reliable, maintainable code with good test coverage.

---

## How to Use These Exercises

- Create a folder called `chapter-18` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run tests with `pytest` or `python -m unittest`.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Write Unit Tests with pytest

Create a file called `calculator.py`:

```python
"""Simple calculator module."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Create a file called `test_calculator.py`:

```python
"""Tests for calculator module."""

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Run the tests:

```bash
pytest test_calculator.py
```

---

### Exercise 2: Write Tests with unittest

Create a file called `string_utils.py`:

```python
"""String utilities."""

def reverse(text):
    """Reverse a string."""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome."""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def count_vowels(text):
    """Count vowels in a string."""
    return sum(1 for c in text.lower() if c in "aeiou")
```

Create a file called `test_string_utils.py`:

```python
"""Tests for string_utils module."""

import unittest
from string_utils import reverse, is_palindrome, count_vowels

class TestStringUtils(unittest.TestCase):
    
    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
    
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("xyz"), 0)

if __name__ == "__main__":
    unittest.main()
```

Run the tests:

```bash
python test_string_utils.py
```

---

### Exercise 3: Test Edge Cases

Create a file called `validation.py`:

```python
"""Input validation."""

def validate_email(email):
    """Validate email format."""
    if "@" not in email or "." not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return len(parts[0]) > 0 and len(parts[1]) > 0

def validate_age(age):
    """Validate age."""
    try:
        age = int(age)
        return 0 <= age <= 150
    except ValueError:
        return False

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
```

Create a file called `test_validation.py`:

```python
"""Tests for validation module."""

import pytest
from validation import validate_email, validate_age, validate_password

class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com")
    
    def test_missing_at(self):
        assert not validate_email("userexample.com")
    
    def test_missing_dot(self):
        assert not validate_email("user@example")
    
    def test_empty_local(self):
        assert not validate_email("@example.com")
    
    def test_empty_domain(self):
        assert not validate_email("user@")

class TestValidateAge:
    def test_valid_age(self):
        assert validate_age(25)
        assert validate_age(0)
        assert validate_age(150)
    
    def test_negative_age(self):
        assert not validate_age(-1)
    
    def test_too_old(self):
        assert not validate_age(151)
    
    def test_non_numeric(self):
        assert not validate_age("abc")

class TestValidatePassword:
    def test_valid_password(self):
        assert validate_password("MyPassword123")
    
    def test_too_short(self):
        assert not validate_password("Short1")
    
    def test_no_uppercase(self):
        assert not validate_password("mypassword123")
    
    def test_no_lowercase(self):
        assert not validate_password("MYPASSWORD123")
    
    def test_no_digit(self):
        assert not validate_password("MyPassword")
```

Run the tests:

```bash
pytest test_validation.py -v
```

---

### Exercise 4: Use Code Linters

Create a file called `messy_code.py`:

```python
# Bad code with style issues
import os,sys
x=1
y=2
z=x+y
print(z)

def bad_function( ):
    a=1
    b=2
    c=a+b
    return c

class BadClass:
    def __init__(self):
        self.value=1
    def method(self):
        return self.value
```

Run flake8 to check style:

```bash
pip install flake8
flake8 messy_code.py
```

Run black to format code:

```bash
pip install black
black messy_code.py
```

---

## Practice Exercises

### Exercise 5: Test with Fixtures

Create a file called `database.py`:

```python
"""Simple in-memory database."""

class Database:
    def __init__(self):
        self.data = {}
    
    def add(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found")
        return self.data[key]
    
    def delete(self, key):
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found")
        del self.data[key]
    
    def clear(self):
        self.data.clear()
```

Create a file called `test_database.py`:

```python
"""Tests for database module."""

import pytest
from database import Database

@pytest.fixture
def db():
    """Create a fresh database for each test."""
    database = Database()
    yield database
    database.clear()

def test_add_and_get(db):
    db.add("name", "Alice")
    assert db.get("name") == "Alice"

def test_get_nonexistent(db):
    with pytest.raises(KeyError):
        db.get("nonexistent")

def test_delete(db):
    db.add("name", "Alice")
    db.delete("name")
    with pytest.raises(KeyError):
        db.get("name")

def test_delete_nonexistent(db):
    with pytest.raises(KeyError):
        db.delete("nonexistent")

def test_multiple_items(db):
    db.add("a", 1)
    db.add("b", 2)
    db.add("c", 3)
    assert db.get("a") == 1
    assert db.get("b") == 2
    assert db.get("c") == 3
```

Run the tests:

```bash
pytest test_database.py -v
```

---

### Exercise 6: Measure Code Coverage

Create a file called `math_utils.py`:

```python
"""Math utilities."""

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if a number is odd."""
    return n % 2 == 1

def factorial(n):
    """Calculate factorial."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    """Calculate greatest common divisor."""
    while b:
        a, b = b, a % b
    return a
```

Create a file called `test_math_utils.py`:

```python
"""Tests for math_utils module."""

import pytest
from math_utils import is_even, is_odd, factorial, gcd

def test_is_even():
    assert is_even(2)
    assert is_even(0)
    assert not is_even(1)

def test_is_odd():
    assert is_odd(1)
    assert is_odd(3)
    assert not is_odd(2)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(10, 5) == 5
    assert gcd(7, 3) == 1
```

Run with coverage:

```bash
pip install pytest-cov
pytest test_math_utils.py --cov=math_utils
```

---

### Exercise 7: Write Docstring Tests

Create a file called `doctest_examples.py`:

```python
"""Examples with docstring tests."""

def add(a, b):
    """
    Add two numbers.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b

def reverse_string(text):
    """
    Reverse a string.
    
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("")
    ''
    >>> reverse_string("a")
    'a'
    """
    return text[::-1]

def count_vowels(text):
    """
    Count vowels in a string.
    
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    >>> count_vowels("xyz")
    0
    """
    return sum(1 for c in text.lower() if c in "aeiou")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Run docstring tests:

```bash
python doctest_examples.py -v
```

---

## Challenge Exercises

### Challenge 1: Test a Complex Class

Create a file called `bank_account.py`:

```python
"""Bank account class."""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
    
    def get_balance(self):
        return self.balance
    
    def get_transactions(self):
        return self.transactions.copy()
```

Create a file called `test_bank_account.py`:

```python
"""Tests for bank_account module."""

import pytest
from bank_account import BankAccount

@pytest.fixture
def account():
    return BankAccount("Alice", 1000)

def test_initial_balance(account):
    assert account.get_balance() == 1000

def test_deposit(account):
    account.deposit(500)
    assert account.get_balance() == 1500

def test_withdraw(account):
    account.withdraw(300)
    assert account.get_balance() == 700

def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-100)

def test_withdraw_more_than_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)

def test_transactions(account):
    account.deposit(500)
    account.withdraw(200)
    transactions = account.get_transactions()
    assert len(transactions) == 2
    assert transactions[0] == ("deposit", 500)
    assert transactions[1] == ("withdraw", 200)
```

Run the tests:

```bash
pytest test_bank_account.py -v
```

---

### Challenge 2: Implement Continuous Integration

Create a file called `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    - name: Install dependencies
      run: |
        pip install pytest pytest-cov flake8
    - name: Lint with flake8
      run: flake8 .
    - name: Run tests
      run: pytest --cov
```

---

## Hints

**Test not running** → Ensure the test file is named `test_*.py` or `*_test.py` and is in the same directory as the module.

**Fixture not working** → Check that the fixture is defined in the same file or in `conftest.py`.

**Coverage not showing** → Install `pytest-cov` and run with `--cov` flag.

**Linter too strict** → Configure flake8 with a `.flake8` file or use `# noqa` comments to ignore specific lines.

---

## What to Review If You Get Stuck

- **Unit testing** → Handbook section 2.1
- **pytest** → Handbook section 2.2
- **unittest** → Handbook section 2.3
- **Code quality tools** → Handbook section 2.4
- **Code coverage** → Handbook section 2.5
- **Best practices** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Write unit tests with pytest and unittest
- Test edge cases and error conditions
- Use fixtures for test setup
- Measure code coverage
- Use linters to check code quality
- Format code with black
- Write docstring tests
- Implement continuous integration
- Write reliable, maintainable code

