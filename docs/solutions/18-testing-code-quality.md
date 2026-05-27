# Solutions 18: Testing and Code Quality

## Overview

Chapter 18 exercises cover writing unit tests with pytest and unittest, testing edge cases, using fixtures, measuring code coverage, writing docstring tests, and using code quality tools. This guide explains the reasoning behind each solution and highlights best practices for writing reliable, maintainable tests.

---

## Notes Before Checking Solutions

Tests are not a chore — they are a tool that lets you change code confidently. A good test suite tells you immediately when a change breaks something. Write tests as you write code, not after.

---

## Warm-up Exercise Solutions

### Exercise 1: Write Unit Tests with pytest

`calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

`test_calculator.py`:

```python
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

Run:

```bash
pytest test_calculator.py -v
```

**`pytest.raises(ValueError)`** asserts that the code inside the `with` block raises a `ValueError`. If no exception is raised, the test fails. If a different exception is raised, it propagates and the test errors.

**Multiple assertions per test** are fine when they test the same behavior. `test_add()` tests several inputs for the `add()` function. If you want to know which specific input failed, use `pytest.mark.parametrize` (see below).

**Test function names must start with `test_`.** pytest discovers tests by looking for functions and methods whose names start with `test_`.

---

### Exercise 2: Write Tests with unittest

`string_utils.py`:

```python
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")
```

`test_string_utils.py`:

```python
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

**pytest vs. unittest:** pytest is simpler — plain `assert` statements, no class required. unittest is the built-in framework and is more verbose but familiar to developers from other languages. Both work; pytest is the modern standard for new projects.

---

### Exercise 3: Test Edge Cases

`validation.py`:

```python
def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return len(parts[0]) > 0 and len(parts[1]) > 0

def validate_age(age):
    try:
        age = int(age)
        return 0 <= age <= 150
    except ValueError:
        return False

def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
```

`test_validation.py`:

```python
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
```

**Test edge cases explicitly.** The most common bugs live at boundaries: zero, negative numbers, empty strings, the maximum allowed value. Test these explicitly rather than assuming they work.

**Group related tests in a class.** `TestValidateEmail` groups all email validation tests. This makes the test output easier to read and lets you share setup code with `setUp()` or fixtures.

---

### Exercise 4: Use Code Linters

```bash
pip install flake8 black

# Check style
flake8 messy_code.py

# Auto-format
black messy_code.py
```

**flake8** reports style violations (PEP 8) and potential errors. **black** automatically reformats code to a consistent style. Use both: black fixes formatting, flake8 catches issues black does not fix (like unused imports).

**Configure flake8** with a `.flake8` file to adjust line length or ignore specific rules:

```ini
[flake8]
max-line-length = 88
extend-ignore = E203
```

---

## Practice Exercise Solutions

### Exercise 5: Test with Fixtures

`database.py`:

```python
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

`test_database.py`:

```python
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

def test_multiple_items(db):
    db.add("a", 1)
    db.add("b", 2)
    assert db.get("a") == 1
    assert db.get("b") == 2
```

**Fixtures provide setup and teardown.** The `yield` in the fixture separates setup (before `yield`) from teardown (after `yield`). Each test gets a fresh `Database` instance, so tests do not interfere with each other.

**`conftest.py`** is a special file where you can define fixtures shared across multiple test files. pytest discovers it automatically.

---

### Exercise 6: Measure Code Coverage

```bash
pip install pytest-cov
pytest test_math_utils.py --cov=math_utils --cov-report=term-missing
```

The `--cov-report=term-missing` flag shows which lines are not covered by tests.

**100% coverage does not mean bug-free.** Coverage tells you which lines were executed, not whether the behavior is correct. A test that calls a function but does not assert anything gives 100% coverage with zero value.

**Aim for high coverage on critical code.** Focus on covering edge cases and error paths, not just the happy path.

---

### Exercise 7: Write Docstring Tests

```python
def add(a, b):
    """
    Add two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
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
    """
    return text[::-1]
```

Run:

```bash
python -m doctest doctest_examples.py -v
```

**Doctest is good for simple examples** in documentation. It ensures the examples in your docstrings actually work. For complex tests, use pytest — doctest is not a replacement for a full test suite.

---

## Challenge Exercise Solutions

### Challenge 1: Test a Complex Class

`bank_account.py`:

```python
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

`test_bank_account.py`:

```python
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

**`get_transactions()` returns a copy** of the list. This prevents tests (or callers) from modifying the internal transaction history. Returning a copy is a good defensive practice for mutable internal state.

---

### Challenge 2: Implement Continuous Integration

`.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: pip install pytest pytest-cov flake8
    - name: Lint with flake8
      run: flake8 .
    - name: Run tests with coverage
      run: pytest --cov
```

**CI runs your tests automatically** on every push and pull request. This catches regressions before they reach the main branch. GitHub Actions is free for public repositories.

---

## Common Mistakes

**Testing implementation details instead of behavior.** Tests should verify what a function does, not how it does it. If you test internal state directly, refactoring the implementation breaks the tests even if the behavior is unchanged.

**Not testing error cases.** Many bugs live in error handling code. Always test that your functions raise the right exceptions with the right messages.

**Shared state between tests.** If one test modifies global state or a shared object, it can affect other tests. Use fixtures to create fresh state for each test.

**Ignoring flake8 warnings.** Style warnings often point to real issues. `E711: comparison to None` (use `is None` instead of `== None`) is a common one that can cause subtle bugs.

---

## What to Review Next

- Chapter 12: Errors, Exceptions, and Debugging — testing that exceptions are raised correctly
- Chapter 16: OOP — testing classes with fixtures
- Chapter 22: Practical Projects — adding tests to complete applications
