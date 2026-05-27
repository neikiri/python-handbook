# Chapter 18: Testing and Code Quality

## 1. Overview

Writing code that works once is not enough. You need to know it still works
after you change something, after a teammate edits it, or after you come back
to it six months later. Tests give you that confidence.

This chapter introduces automated testing with pytest — the standard testing
tool in the Python ecosystem — and covers the habits that make code easier to
test and maintain. You will also get a brief look at two tools, ruff and mypy,
that catch problems before your tests even run.

---

## 2. What You Will Learn

- Why testing matters and what makes code easy to test
- How to write simple, testable functions
- Installing and running pytest
- Writing test files and test functions
- Using `assert` statements to check results
- Running tests from the command line
- Using fixtures for test setup and teardown
- Organizing tests in a `tests/` directory
- Code quality habits: small functions, meaningful names, no magic numbers
- What ruff does and how to run it
- What mypy does and why type checking helps

---

## 3. Core Concepts

### 3.1 Why Testing Matters

Every program has bugs. The question is whether you find them before your
users do. Automated tests let you:

- Catch regressions — changes that break something that used to work
- Document expected behavior in a concrete, runnable form
- Refactor with confidence, knowing the tests will catch mistakes
- Collaborate more safely, because tests verify that new code does not break
  existing behavior

A test is just a function that calls your code and checks the result. If the
check fails, the test fails and you know something is wrong.

---

### 3.2 Writing Testable Code

Not all code is equally easy to test. The easiest code to test is a **pure
function**: a function that takes inputs, returns an output, and has no side
effects.

A side effect is anything a function does beyond returning a value: writing to
a file, printing to the screen, modifying a global variable, making a network
request. Side effects are not bad — programs need them — but they make testing
harder because you have to set up and clean up the external state.

**Hard to test — side effects mixed in:**

```python
def process_order(order_id: int) -> None:
    # reads from a database, writes to a file, sends an email
    order = db.get_order(order_id)
    total = order["qty"] * order["price"]
    with open("receipts.txt", "a") as f:
        f.write(f"Order {order_id}: ${total:.2f}\n")
    send_email(order["email"], total)
```

**Easy to test — pure calculation separated out:**

```python
def calculate_total(qty: int, price: float) -> float:
    return qty * price
```

Now `calculate_total` can be tested with a simple call and an `assert`. The
parts that touch the database, filesystem, and email can be tested separately
or mocked.

**Rules of thumb for testable code:**

- Keep functions small and focused on one thing
- Separate calculation from I/O
- Avoid global state
- Accept inputs as parameters rather than reading them from the environment

---

### 3.3 Installing pytest

pytest is not part of the standard library, but it is the de facto standard
for Python testing. Install it into your virtual environment:

```bash
pip install pytest
```

Verify the installation:

```bash
pytest --version
# pytest 8.x.x
```

If you are using a `pyproject.toml`, you can add pytest as a development
dependency:

```toml
[project.optional-dependencies]
dev = ["pytest"]
```

Then install with:

```bash
pip install -e ".[dev]"
```

---

### 3.4 Writing Your First Test

pytest discovers tests automatically. You just need to follow two naming rules:

1. Test files must be named `test_*.py` or `*_test.py`
2. Test functions must start with `test_`

Here is a simple module and its test file.

**`math_utils.py`** — the code being tested:

```python
def add(a: float, b: float) -> float:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


def clamp(value: float, low: float, high: float) -> float:
    """Return value clamped to the range [low, high]."""
    return max(low, min(value, high))
```

**`test_math_utils.py`** — the tests:

```python
from math_utils import add, clamp, is_even


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(7) is False


def test_is_even_with_zero():
    assert is_even(0) is True


def test_clamp_within_range():
    assert clamp(5.0, 0.0, 10.0) == 5.0


def test_clamp_below_low():
    assert clamp(-3.0, 0.0, 10.0) == 0.0


def test_clamp_above_high():
    assert clamp(15.0, 0.0, 10.0) == 10.0
```

Notice that `test_add_floats` uses `pytest.approx`. Floating-point arithmetic
is not exact, so `0.1 + 0.2` is not exactly `0.3`. `pytest.approx` checks
that two values are close enough (within a small tolerance).

```python
import pytest

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

---

### 3.5 The `assert` Statement

`assert` is Python's built-in way to check a condition. If the condition is
`False`, it raises `AssertionError`.

```python
assert 1 + 1 == 2          # passes silently
assert 1 + 1 == 3          # raises AssertionError
assert "hello".upper() == "HELLO"
assert len([1, 2, 3]) == 3
```

pytest intercepts `AssertionError` and produces a detailed failure message
showing the actual and expected values. You do not need a special assertion
library — plain `assert` is all you need.

You can add an optional message after a comma:

```python
result = add(2, 3)
assert result == 5, f"Expected 5, got {result}"
```

**Common assertion patterns:**

```python
# Equality
assert result == expected

# Inequality
assert result != unexpected

# Membership
assert "error" in log_output

# Type check
assert isinstance(result, list)

# Boolean
assert is_valid(data)
assert not is_empty(collection)

# Approximate equality for floats
import pytest
assert result == pytest.approx(3.14, rel=1e-3)

# Exception is raised
import pytest
with pytest.raises(ValueError):
    parse_date("not-a-date")
```

---

### 3.6 Running Tests

Run all tests in the current directory and subdirectories:

```bash
pytest
```

Run with verbose output (shows each test name and pass/fail):

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_math_utils.py
```

Run a specific test function:

```bash
pytest tests/test_math_utils.py::test_add_positive_numbers
```

Run tests whose names match a keyword:

```bash
pytest -k "clamp"
```

Stop after the first failure:

```bash
pytest -x
```

**Reading pytest output:**

A passing run looks like this:

```text
========================= test session starts ==========================
collected 9 items

tests/test_math_utils.py .........                               [100%]

========================== 9 passed in 0.12s ===========================
```

Each `.` is a passing test. An `F` means a failure. An `E` means an error
(an exception was raised outside of a `pytest.raises` block).

A failing run shows the assertion that failed and the actual values:

```text
FAILED tests/test_math_utils.py::test_add_positive_numbers
AssertionError: assert 4 == 5
 +  where 4 = add(2, 2)
```

---

### 3.7 Fixtures: Setup and Teardown

A **fixture** is a function that prepares something your tests need — a
temporary file, a sample dataset, a configured object — and optionally cleans
it up afterward. Fixtures are decorated with `@pytest.fixture`.

```python
import pytest


@pytest.fixture
def sample_scores() -> list[int]:
    return [72, 85, 90, 88, 76, 92, 85, 68, 95, 80]


def test_average(sample_scores):
    total = sum(sample_scores)
    avg = total / len(sample_scores)
    assert avg == pytest.approx(83.1)


def test_max_score(sample_scores):
    assert max(sample_scores) == 95


def test_min_score(sample_scores):
    assert min(sample_scores) == 68
```

pytest sees that `test_average` has a parameter named `sample_scores`, finds
the fixture with that name, calls it, and passes the result in. Each test gets
a fresh call to the fixture.

#### Fixtures with cleanup using `yield`

Use `yield` instead of `return` when you need to clean up after the test.
Everything before `yield` is setup; everything after is teardown.

```python
import pytest
from pathlib import Path


@pytest.fixture
def temp_file(tmp_path: Path):
    """Create a temporary file with some content."""
    path = tmp_path / "data.txt"
    path.write_text("line1\nline2\nline3\n", encoding="utf-8")
    yield path
    # teardown: pytest's tmp_path fixture handles cleanup automatically,
    # but you could delete files or close connections here


def test_line_count(temp_file: Path):
    lines = temp_file.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 3


def test_first_line(temp_file: Path):
    lines = temp_file.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "line1"
```

`tmp_path` is a built-in pytest fixture that provides a temporary directory
unique to each test. You do not need to define it yourself.

#### Other useful built-in fixtures

| Fixture | What it provides |
|---|---|
| `tmp_path` | A `Path` to a temporary directory, cleaned up after the test |
| `capsys` | Capture `stdout` and `stderr` output |
| `monkeypatch` | Temporarily replace attributes, environment variables, or functions |
| `caplog` | Capture log records |

---

### 3.8 Organizing Tests

For small scripts, a single `test_*.py` file next to your code is fine. For
larger projects, put all tests in a `tests/` directory at the project root.

```text
my_project/
    my_module.py
    utils.py
    tests/
        __init__.py        ← optional, but helps with imports
        test_my_module.py
        test_utils.py
        conftest.py        ← shared fixtures live here
```

**`conftest.py`** is a special file that pytest loads automatically. Put
fixtures that are shared across multiple test files in `conftest.py` — you do
not need to import them; pytest finds them by name.

```python
# tests/conftest.py
import pytest


@pytest.fixture
def admin_user() -> dict:
    return {"name": "Admin", "role": "admin", "active": True}


@pytest.fixture
def regular_user() -> dict:
    return {"name": "Alice", "role": "user", "active": True}
```

Any test file in the `tests/` directory can use `admin_user` or `regular_user`
as a parameter without importing anything.

---

### 3.9 Code Quality Habits

Tests catch bugs at runtime. Good code habits prevent bugs from being written
in the first place and make code easier to read, test, and maintain.

#### Keep functions small

A function that does one thing is easier to name, easier to test, and easier
to understand. If a function is getting long, look for a natural split.

```python
# Hard to test — does too many things at once
def process(filepath: str) -> None:
    with open(filepath) as f:
        lines = f.readlines()
    cleaned = [line.strip().lower() for line in lines if line.strip()]
    counts = {}
    for word in " ".join(cleaned).split():
        counts[word] = counts.get(word, 0) + 1
    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, n in top:
        print(f"{word}: {n}")


# Easier to test — each step is a separate function
def read_lines(filepath: str) -> list[str]:
    with open(filepath, encoding="utf-8") as f:
        return f.readlines()


def clean_lines(lines: list[str]) -> list[str]:
    return [line.strip().lower() for line in lines if line.strip()]


def count_words(lines: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in " ".join(lines).split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n(counts: dict[str, int], n: int = 10) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]
```

Now each function can be tested independently with simple inputs.

#### Use meaningful names

Names should say what something is or does. Avoid single-letter variables
outside of short loops or mathematical formulas.

```python
# Unclear
def calc(x, y, z):
    return x * y * (1 - z)

# Clear
def calculate_discounted_price(
    quantity: int, unit_price: float, discount_rate: float
) -> float:
    return quantity * unit_price * (1 - discount_rate)
```

#### Avoid magic numbers

A magic number is a numeric literal with no explanation. Replace them with
named constants.

```python
# Magic numbers — what do 0.15 and 100 mean?
def apply_tax(amount: float) -> float:
    return amount * 1.15 if amount > 100 else amount

# Named constants — intent is clear
TAX_RATE = 0.15
TAX_THRESHOLD = 100.0

def apply_tax(amount: float) -> float:
    if amount > TAX_THRESHOLD:
        return amount * (1 + TAX_RATE)
    return amount
```

Named constants also make tests easier to write, because you can reference
the constant rather than repeating the literal.

---

### 3.10 ruff — Fast Linting

A **linter** reads your code without running it and reports style problems,
potential bugs, and violations of best practices. `ruff` is a fast Python
linter written in Rust. It replaces several older tools (flake8, isort,
pyupgrade) with a single command.

Install it:

```bash
pip install ruff
```

Run it on your project:

```bash
ruff check .
```

Fix auto-fixable issues:

```bash
ruff check --fix .
```

Example output when there are issues:

```text
math_utils.py:3:1: F401 `os` imported but unused
math_utils.py:12:5: E711 comparison to `None` (use `is` or `is not`)
Found 2 errors.
```

ruff checks things like:

- Unused imports
- Undefined names
- Comparison style (`== None` vs `is None`)
- Unreachable code
- Import ordering

You do not need to memorize the rules. Run `ruff check .` and fix what it
reports. Over time the habits become automatic.

---

### 3.11 mypy — Static Type Checking

**mypy** reads your type hints and checks that you are using values
consistently. It catches type errors before you run the code.

Install it:

```bash
pip install mypy
```

Run it:

```bash
mypy my_module.py
```

Example — a function with a type error:

```python
def greet(name: str) -> str:
    return "Hello, " + name


result: int = greet("Alice")   # type error: str assigned to int variable
print(result.upper())
```

mypy output:

```text
error: Incompatible types in assignment (expression has type "str",
       variable has type "int")
```

mypy does not run your code. It only reads it. This means it can catch
mistakes in code paths that your tests might not exercise.

You do not need to add type hints everywhere to benefit from mypy. Start by
annotating function signatures and let mypy tell you where the types do not
add up.

---

## 4. Practical Examples

### 4.1 Testing a String Utility Module

**`string_utils.py`:**

```python
def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug.

    Example: "Hello World!" -> "hello-world"
    """
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length characters, appending suffix if cut."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def count_vowels(text: str) -> int:
    """Return the number of vowels in text (case-insensitive)."""
    return sum(1 for ch in text.lower() if ch in "aeiou")
```

**`tests/test_string_utils.py`:**

```python
import pytest
from string_utils import count_vowels, slugify, truncate


class TestSlugify:
    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self):
        assert slugify("Hello, World!") == "hello-world"

    def test_multiple_spaces(self):
        assert slugify("too   many   spaces") == "too-many-spaces"

    def test_already_lowercase(self):
        assert slugify("already-fine") == "already-fine"

    def test_empty_string(self):
        assert slugify("") == ""


class TestTruncate:
    def test_short_string_unchanged(self):
        assert truncate("hello", 10) == "hello"

    def test_exact_length_unchanged(self):
        assert truncate("hello", 5) == "hello"

    def test_long_string_truncated(self):
        result = truncate("hello world", 8)
        assert result == "hello..."
        assert len(result) == 8

    def test_custom_suffix(self):
        result = truncate("hello world", 7, suffix="…")
        assert result.endswith("…")

    def test_empty_string(self):
        assert truncate("", 5) == ""


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_case_insensitive(self):
        assert count_vowels("HELLO") == 2

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_empty_string(self):
        assert count_vowels("") == 0
```

Grouping related tests into classes keeps the file organized. The class name
describes the function being tested; each method tests one specific behavior.

---

### 4.2 Testing Exception Behavior

Use `pytest.raises` as a context manager to assert that a function raises a
specific exception.

**`validators.py`:**

```python
def parse_age(value: str) -> int:
    """Parse a string as a non-negative integer age."""
    try:
        age = int(value)
    except ValueError:
        raise ValueError(f"Age must be a number, got: {value!r}")
    if age < 0:
        raise ValueError(f"Age cannot be negative, got: {age}")
    if age > 150:
        raise ValueError(f"Age {age} is unrealistically large")
    return age
```

**`tests/test_validators.py`:**

```python
import pytest
from validators import parse_age


def test_valid_age():
    assert parse_age("25") == 25


def test_zero_age():
    assert parse_age("0") == 0


def test_non_numeric_raises():
    with pytest.raises(ValueError, match="must be a number"):
        parse_age("abc")


def test_negative_age_raises():
    with pytest.raises(ValueError, match="cannot be negative"):
        parse_age("-5")


def test_unrealistic_age_raises():
    with pytest.raises(ValueError, match="unrealistically large"):
        parse_age("200")
```

The `match` argument to `pytest.raises` checks that the exception message
contains the given substring (as a regex pattern). This makes the test more
specific — it verifies not just that an exception was raised, but that it was
the right one.

---

### 4.3 Using Fixtures for Shared Setup

**`inventory.py`:**

```python
class Inventory:
    def __init__(self) -> None:
        self._items: dict[str, int] = {}

    def add(self, item: str, qty: int) -> None:
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        self._items[item] = self._items.get(item, 0) + qty

    def remove(self, item: str, qty: int) -> None:
        if item not in self._items:
            raise KeyError(f"Item not found: {item}")
        if self._items[item] < qty:
            raise ValueError("Not enough stock")
        self._items[item] -= qty
        if self._items[item] == 0:
            del self._items[item]

    def stock(self, item: str) -> int:
        return self._items.get(item, 0)

    def total_items(self) -> int:
        return sum(self._items.values())
```

**`tests/test_inventory.py`:**

```python
import pytest
from inventory import Inventory


@pytest.fixture
def stocked_inventory() -> Inventory:
    inv = Inventory()
    inv.add("apple", 10)
    inv.add("banana", 5)
    inv.add("cherry", 20)
    return inv


def test_initial_stock(stocked_inventory: Inventory):
    assert stocked_inventory.stock("apple") == 10
    assert stocked_inventory.stock("banana") == 5


def test_total_items(stocked_inventory: Inventory):
    assert stocked_inventory.total_items() == 35


def test_remove_reduces_stock(stocked_inventory: Inventory):
    stocked_inventory.remove("apple", 3)
    assert stocked_inventory.stock("apple") == 7


def test_remove_all_deletes_item(stocked_inventory: Inventory):
    stocked_inventory.remove("banana", 5)
    assert stocked_inventory.stock("banana") == 0


def test_remove_nonexistent_raises(stocked_inventory: Inventory):
    with pytest.raises(KeyError):
        stocked_inventory.remove("mango", 1)


def test_remove_too_many_raises(stocked_inventory: Inventory):
    with pytest.raises(ValueError, match="Not enough stock"):
        stocked_inventory.remove("cherry", 100)


def test_add_invalid_qty_raises():
    inv = Inventory()
    with pytest.raises(ValueError, match="must be positive"):
        inv.add("apple", 0)
```

Each test gets a fresh `stocked_inventory` because the fixture is called
once per test. Tests do not share state, so they cannot interfere with each
other.

---

### 4.4 Testing File I/O with `tmp_path`

`tmp_path` is a built-in pytest fixture that provides a temporary directory
unique to each test. Use it whenever your code reads or writes files.

```python
# file_tools.py
from pathlib import Path


def count_lines(path: Path) -> int:
    """Return the number of non-empty lines in a file."""
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
```

```python
# tests/test_file_tools.py
from pathlib import Path
from file_tools import count_lines


def test_count_lines(tmp_path: Path):
    p = tmp_path / "sample.txt"
    p.write_text("line one\nline two\n\nline four\n", encoding="utf-8")
    assert count_lines(p) == 3   # blank line not counted


def test_count_lines_empty_file(tmp_path: Path):
    p = tmp_path / "empty.txt"
    p.write_text("", encoding="utf-8")
    assert count_lines(p) == 0
```

Each test gets its own temporary directory, so tests do not interfere with
each other's files. pytest cleans up the directory after the test run.

---

## 5. Common Mistakes

### 5.1 Testing Implementation Instead of Behavior

Tests should check what a function does, not how it does it. If you test
internal details, the tests break every time you refactor, even when the
behavior is unchanged.

```python
# Wrong — tests internal variable name
def test_word_count_internal():
    wc = WordCounter("hello world hello")
    assert wc._word_dict == {"hello": 2, "world": 1}   # fragile

# Correct — tests observable behavior
def test_word_count_behavior():
    wc = WordCounter("hello world hello")
    assert wc.count("hello") == 2
    assert wc.count("world") == 1
    assert wc.count("missing") == 0
```

---

### 5.2 Writing Tests That Always Pass

A test that never fails is not a test — it is noise. This often happens when
the assertion is too weak.

```python
# Wrong — always passes, proves nothing
def test_process():
    result = process_data([1, 2, 3])
    assert result is not None

# Correct — checks the actual result
def test_process():
    result = process_data([1, 2, 3])
    assert result == [2, 4, 6]
```

---

### 5.3 One Giant Test Function

Putting many unrelated checks in one test makes it hard to tell what failed
and why. Write one test per behavior.

```python
# Hard to diagnose — which assertion failed?
def test_everything():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert is_even(4) is True
    assert is_even(3) is False
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0

# Better — each test has a clear name and single purpose
def test_add_positive():
    assert add(1, 2) == 3

def test_add_to_zero():
    assert add(-1, 1) == 0

def test_is_even_true():
    assert is_even(4) is True
```

---

### 5.4 Not Testing Edge Cases

Most bugs live at the edges: empty inputs, zero, negative numbers, the
maximum value, a single-element list. Always ask "what happens at the
boundary?"

```python
def test_average_normal():
    assert average([10, 20, 30]) == 20.0

# Edge cases worth testing:
def test_average_single_element():
    assert average([42]) == 42.0

def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])

def test_average_negative_numbers():
    assert average([-10, -20, -30]) == -20.0
```

---

### 5.5 Forgetting to Import pytest for `pytest.approx` and `pytest.raises`

`pytest.approx` and `pytest.raises` require `import pytest`. Forgetting this
gives a `NameError` that looks confusing.

```python
# Wrong — NameError: name 'pytest' is not defined
def test_area():
    assert circle_area(1.0) == pytest.approx(3.14159, rel=1e-4)

# Correct
import pytest

def test_area():
    assert circle_area(1.0) == pytest.approx(3.14159, rel=1e-4)
```

---

### 5.6 Naming Test Files or Functions Without the `test_` Prefix

pytest silently skips any file or function that does not follow the naming
convention. This is a common source of confusion when tests appear to pass but
were never actually run.

```text
# These are NOT discovered by pytest:
check_math.py
tests/math_checks.py

def verify_add():   ...
def should_add():   ...

# These ARE discovered:
test_math.py
tests/test_math.py

def test_add():   ...
```

If you run `pytest -v` and see `0 items collected`, check your file and
function names.
---

## 6. Practice Tasks

1. Write a function `celsius_to_fahrenheit(c: float) -> float` that converts
   Celsius to Fahrenheit using the formula `F = C * 9/5 + 32`. Then write at
   least five tests covering normal values, zero, negative temperatures, and
   the boiling point (100°C = 212°F).

2. Write a function `is_palindrome(text: str) -> bool` that returns `True` if
   the string reads the same forwards and backwards, ignoring case and
   non-alphanumeric characters. Write tests for: a plain palindrome, a
   palindrome with punctuation (`"A man, a plan, a canal: Panama"`), a
   non-palindrome, an empty string, and a single character.

3. Write a function `find_duplicates(items: list) -> list` that returns a
   sorted list of items that appear more than once. Write tests for: a list
   with duplicates, a list with no duplicates, an empty list, and a list
   where all items are the same.

4. Create a `tests/conftest.py` with a fixture called `word_list` that
   returns `["apple", "banana", "cherry", "apple", "date", "banana", "apple"]`.
   Write a test file that uses this fixture to test a `most_common(words, n)`
   function that returns the `n` most frequent words.

5. Write a function `safe_divide(a: float, b: float) -> float` that raises
   `ZeroDivisionError` with the message `"Cannot divide by zero"` when `b`
   is zero. Write tests that verify: normal division, division by a negative
   number, and that the correct exception and message are raised for `b = 0`.

6. Write a function `read_csv_column(path: Path, column: int) -> list[str]`
   that reads a CSV-like text file (comma-separated, one row per line) and
   returns all values from the given column index. Use `tmp_path` in your
   tests to create temporary CSV files with known content.

7. Install `ruff` in your virtual environment and run `ruff check .` on a
   Python file you have written. Fix any issues it reports. Then run it again
   to confirm the issues are resolved.

8. Add type hints to the functions you wrote in tasks 1–3. Run `mypy` on
   those files and fix any type errors it reports.

---

## 7. Key Takeaways

- Tests are functions that call your code and use `assert` to check the
  result. If the assertion fails, the test fails.
- Pure functions — no side effects, same output for the same input — are the
  easiest to test. Separate calculation from I/O to make both parts testable.
- pytest discovers tests automatically: files named `test_*.py` and functions
  named `test_*`. Run `pytest -v` to see each test by name.
- Use `pytest.approx` for floating-point comparisons. Use `pytest.raises` to
  assert that a function raises a specific exception.
- Fixtures (`@pytest.fixture`) set up shared test data and clean up afterward.
  Put shared fixtures in `tests/conftest.py` so all test files can use them.
- `tmp_path` is a built-in fixture that gives each test its own temporary
  directory — use it whenever your code reads or writes files.
- Keep functions small, use meaningful names, and replace magic numbers with
  named constants. These habits make code easier to read and easier to test.
- `ruff check .` catches style issues and common bugs without running your
  code. Run it regularly and fix what it reports.
- `mypy` checks that your type hints are consistent. It catches type errors
  before runtime, especially in code paths that tests might not cover.

---

### What's Next

Chapter 19 covers **type hints** — how to annotate function parameters and
return types, use collection types like `list[str]` and `dict[str, int]`,
express optional values with `str | None`, and run mypy to catch type errors
before your code runs.

---

*See also:*
- [Exercises for Chapter 18](../exercises/18-testing-code-quality.md)
- [Solutions for Chapter 18](../solutions/18-testing-code-quality.md)
- [Cheatsheet: Syntax](../cheatsheets/syntax.md)
