# Chapter 12: Errors, Exceptions, and Debugging

## 1. Overview

Every program encounters unexpected situations: a file that does not exist, a
user who types letters where a number was expected, a network request that
times out. Python's exception system gives you a structured way to detect
these situations, respond to them, and keep your program from crashing
unexpectedly.

This chapter also covers debugging — the practical skill of figuring out why
your code does not behave the way you expect. Reading tracebacks, using
`print()` strategically, and working with the built-in debugger are all tools
you will use throughout your Python career.

---

## 2. What You Will Learn

- The difference between syntax errors and runtime exceptions
- How to read a Python traceback
- Common built-in exception types and when they occur
- Handling exceptions with `try`, `except`, `else`, and `finally`
- Catching multiple exception types
- Accessing exception details with `as`
- Raising exceptions with `raise`
- Creating custom exception classes
- The `assert` statement for internal checks
- Practical debugging techniques: `print()`, `breakpoint()`, and the `pdb`
  debugger

---

## 3. Core Concepts

### 3.1 Syntax Errors vs. Exceptions

Python reports two broad categories of problems.

**Syntax errors** are detected before the program runs. Python cannot even
parse the code.

```python
# SyntaxError — missing colon
def greet(name)
    print(f"Hello, {name}!")
```

```text
  File "example.py", line 1
    def greet(name)
                   ^
SyntaxError: expected ':'
```

Fix syntax errors first — nothing else will run until they are gone.

**Exceptions** (also called runtime errors) occur while the program is
running. The code is syntactically valid, but something goes wrong during
execution.

```python
numbers = [1, 2, 3]
print(numbers[10])   # IndexError: list index out of range
```

---

### 3.2 Reading a Traceback

When an unhandled exception occurs, Python prints a **traceback** — a record
of the call stack at the moment of the error. Learning to read tracebacks
quickly is one of the most valuable debugging skills.

```python
def divide(a, b):
    return a / b

def calculate(x):
    return divide(x, 0)

calculate(10)
```

```text
Traceback (most recent call last):
  File "example.py", line 7, in <module>
    calculate(10)
  File "example.py", line 5, in calculate
    return divide(x, 0)
  File "example.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

Read a traceback from **bottom to top**:

1. The last line names the exception type and gives a short message.
   `ZeroDivisionError: division by zero`
2. The line just above it shows the exact line of code that raised the error.
3. Working upward, each frame shows the call that led to the next one.
4. The top frame is where execution started (usually the module level or the
   entry point).

The most useful information is almost always at the bottom. Start there.

---

### 3.3 Common Built-in Exceptions

| Exception | When it occurs |
|---|---|
| `ValueError` | Right type, wrong value — e.g., `int("abc")` |
| `TypeError` | Wrong type — e.g., `"hello" + 5` |
| `IndexError` | Sequence index out of range — e.g., `lst[99]` on a short list |
| `KeyError` | Dict key not found — e.g., `d["missing"]` |
| `AttributeError` | Object has no such attribute — e.g., `42.upper()` |
| `NameError` | Name not defined — e.g., using a variable before assigning it |
| `ZeroDivisionError` | Division or modulo by zero |
| `FileNotFoundError` | File or directory does not exist |
| `PermissionError` | Not allowed to read/write a file |
| `ImportError` | Module cannot be imported |
| `StopIteration` | Iterator has no more items |
| `RecursionError` | Maximum recursion depth exceeded |
| `OverflowError` | Arithmetic result too large for a float |
| `MemoryError` | Not enough memory |
| `OSError` | General OS-level failure (parent of many file errors) |

You do not need to memorize all of these. When you see an unfamiliar
exception, read the message — it usually tells you exactly what went wrong.

---

### 3.4 Handling Exceptions with `try` and `except`

Wrap code that might raise an exception in a `try` block. If an exception
occurs, Python jumps to the matching `except` block.

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That is not a valid number.")
```

If the user types `"hello"`, `int("hello")` raises a `ValueError`, and the
`except` block runs. If the user types `"42"`, the `except` block is skipped.

#### Catching multiple exception types

List multiple exception types in a tuple to handle them the same way:

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print(f"100 / {value} = {result}")
except (ValueError, ZeroDivisionError):
    print("Please enter a non-zero number.")
```

Or use separate `except` clauses to handle them differently:

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That is not a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Python checks `except` clauses in order and runs the first one that matches.

#### Catching any exception

Use `except Exception` to catch any non-system-exiting exception. This is
useful at the top level of a program, but avoid it deep inside your code —
it hides bugs.

```python
try:
    risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
```

Never use a bare `except:` without a type. It catches everything, including
`KeyboardInterrupt` and `SystemExit`, which you almost never want to suppress.

---

### 3.5 The `else` Clause

The `else` block runs only if the `try` block completed without raising an
exception. Use it for code that should run on success but that you do not want
inside the `try` block.

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    # Only runs if no exception was raised
    print(f"You entered {value}. Its square is {value ** 2}.")
```

Keeping the success path in `else` makes it clear which code is "protected"
by the `try` and which code runs only on success.

---

### 3.6 The `finally` Clause

The `finally` block always runs — whether an exception occurred or not, and
whether it was handled or not. Use it for cleanup that must happen regardless
of outcome: closing files, releasing locks, disconnecting from a database.

```python
def read_file(path: str) -> str:
    f = open(path, encoding="utf-8")
    try:
        return f.read()
    finally:
        f.close()   # always runs, even if read() raises an exception
```

In practice, the `with` statement (covered in Chapter 13) handles this pattern
more cleanly. But `finally` is still useful when you need explicit cleanup
logic.

```python
try:
    result = risky_operation()
except SomeError:
    handle_error()
else:
    use_result(result)
finally:
    cleanup()   # always runs
```

---

### 3.7 Accessing Exception Details with `as`

Use `as` to bind the exception object to a name. The exception object has a
`args` attribute and can be converted to a string for a human-readable message.

```python
try:
    with open("missing.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Could not open file: {e}")
    # Could not open file: [Errno 2] No such file or directory: 'missing.txt'
```

You can also inspect the exception type:

```python
try:
    result = int("abc")
except ValueError as e:
    print(type(e).__name__)   # ValueError
    print(e.args)             # ("invalid literal for int() with base 10: 'abc'",)
```

---

### 3.8 Raising Exceptions

Use `raise` to signal that something has gone wrong. Raise the most specific
exception type that fits the situation.

```python
def set_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}.")
    if age < 0 or age > 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}.")
    print(f"Age set to {age}.")


set_age(25)      # Age set to 25.
set_age(-1)      # ValueError: Age must be between 0 and 150, got -1.
set_age("old")   # TypeError: Age must be an integer, got str.
```

#### Re-raising an exception

Inside an `except` block, a bare `raise` re-raises the current exception
without modifying it. This is useful when you want to log the error but still
let it propagate.

```python
import logging

try:
    result = risky_operation()
except Exception as e:
    logging.error(f"Operation failed: {e}")
    raise   # re-raise the original exception
```

#### Exception chaining

Use `raise NewException(...) from original` to chain exceptions. This
preserves the original cause in the traceback.

```python
def load_config(path: str) -> dict:
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file not found: {path}") from e
```

---

### 3.9 Custom Exceptions

Define your own exception classes by inheriting from `Exception` (or a more
specific built-in exception). Custom exceptions make your code's error
conditions explicit and allow callers to catch them specifically.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""

    def __init__(self, amount: float, balance: float) -> None:
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw {amount:.2f}: balance is only {balance:.2f}."
        )


class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}.")


account = BankAccount(100.0)
account.withdraw(30.0)    # Withdrew 30.00. New balance: 70.00.

try:
    account.withdraw(200.0)
except InsufficientFundsError as e:
    print(e)
    print(f"You tried to withdraw: {e.amount}")
    print(f"Available balance:     {e.balance}")
```

For a hierarchy of related errors, create a base exception class and inherit
from it:

```python
class AppError(Exception):
    """Base class for all application errors."""

class DatabaseError(AppError):
    """Raised for database-related failures."""

class NetworkError(AppError):
    """Raised for network-related failures."""
```

Callers can then catch `AppError` to handle all application errors, or catch
`DatabaseError` specifically.

---

### 3.10 The `assert` Statement

`assert` checks that a condition is true. If it is false, it raises an
`AssertionError`. Use it to catch programming mistakes — incorrect assumptions
in your own code — not to validate user input.

```python
def average(numbers: list[float]) -> float:
    assert len(numbers) > 0, "Cannot average an empty list."
    return sum(numbers) / len(numbers)
```

Assertions can be disabled globally with the `-O` (optimize) flag when running
Python. Never use `assert` for security checks or input validation that must
always run.

```python
# Wrong — assertions can be disabled
assert user.is_admin(), "Access denied."

# Correct — use a proper check
if not user.is_admin():
    raise PermissionError("Access denied.")
```

---

### 3.11 Debugging Techniques

#### Print debugging

The simplest technique: add `print()` calls to inspect values at key points.

```python
def process(data: list[int]) -> list[int]:
    print(f"Input: {data}")          # debug
    result = [x * 2 for x in data if x > 0]
    print(f"After filter: {result}") # debug
    return result
```

Remove or comment out debug prints before committing code.

#### `breakpoint()`

Python 3.7+ includes `breakpoint()`, which drops you into the interactive
debugger (`pdb`) at that line.

```python
def calculate(items: list[int]) -> int:
    total = 0
    for item in items:
        breakpoint()   # execution pauses here
        total += item
    return total
```

At the `(Pdb)` prompt, useful commands are:

| Command | What it does |
|---|---|
| `n` | Execute the next line (step over) |
| `s` | Step into a function call |
| `c` | Continue until the next breakpoint |
| `p expr` | Print the value of an expression |
| `pp expr` | Pretty-print the value |
| `l` | List the surrounding source code |
| `q` | Quit the debugger |
| `h` | Show help |

#### Inspecting objects

```python
x = [1, 2, 3]
print(type(x))       # <class 'list'>
print(dir(x))        # list of attributes and methods
print(vars(x))       # __dict__ of an object (not for built-ins)
help(x.append)       # documentation for a method
```

#### Checking types at runtime

```python
def process(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}.")
    return value * 2
```

#### Logging instead of printing

For larger programs, use the `logging` module instead of `print()`. It lets
you control verbosity without removing statements from the code.

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a: float, b: float) -> float:
    logging.debug(f"divide called with a={a}, b={b}")
    if b == 0:
        logging.error("Division by zero attempted.")
        raise ZeroDivisionError("Cannot divide by zero.")
    result = a / b
    logging.debug(f"Result: {result}")
    return result
```

Log levels in order of severity: `DEBUG`, `INFO`, `WARNING`, `ERROR`,
`CRITICAL`. Set the level to `WARNING` in production to suppress debug output.

---

## 4. Practical Examples

### 4.1 Robust Input Loop

Keep asking for input until the user provides a valid value.

```python
def get_positive_int(prompt: str) -> int:
    """Ask for a positive integer, retrying on invalid input."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid integer. Try again.")
            continue
        if value <= 0:
            print(f"  Please enter a positive number. Got {value}.")
            continue
        return value


# Usage (interactive — uncomment to run):
# count = get_positive_int("How many items? ")
# print(f"You want {count} items.")
```

---

### 4.2 Safe Dictionary Lookup

```python
def get_config_value(config: dict, key: str, default=None):
    """Return a config value, or default if the key is missing."""
    try:
        return config[key]
    except KeyError:
        return default


# Equivalent and more idiomatic:
def get_config_value(config: dict, key: str, default=None):
    return config.get(key, default)
```

The `dict.get()` method is usually cleaner than `try/except` for this pattern.
Use `try/except` when the operation is more complex than a single lookup.

---

### 4.3 File Reading with Error Handling

```python
from pathlib import Path


def read_text_file(path: str | Path) -> str | None:
    """Read a text file and return its contents, or None on failure."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"Permission denied: {path}")
        return None
    except OSError as e:
        print(f"Could not read {path}: {e}")
        return None


content = read_text_file("notes.txt")
if content is not None:
    print(content)
```

---

### 4.4 Validating Function Arguments

```python
def create_user(name: str, age: int, email: str) -> dict:
    """Create a user record after validating inputs."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    if not isinstance(age, int) or not (0 <= age <= 150):
        raise ValueError(f"Age must be an integer between 0 and 150, got {age!r}.")
    if not isinstance(email, str) or "@" not in email:
        raise ValueError(f"Invalid email address: {email!r}.")

    return {
        "name": name.strip(),
        "age": age,
        "email": email.lower(),
    }


try:
    user = create_user("Alice", 30, "alice@example.com")
    print(user)
except ValueError as e:
    print(f"Validation error: {e}")
```

---

### 4.5 Context Manager for Timing

```python
import time
from contextlib import contextmanager


@contextmanager
def timer(label: str = ""):
    """Context manager that prints elapsed time."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        tag = f"[{label}] " if label else ""
        print(f"{tag}Elapsed: {elapsed:.4f}s")


with timer("sorting"):
    data = sorted(range(1_000_000), reverse=True)

# [sorting] Elapsed: 0.0821s  (time will vary)
```

---

### 4.6 Exception Hierarchy in a Library

```python
class StorageError(Exception):
    """Base class for storage-related errors."""


class ReadError(StorageError):
    """Raised when a read operation fails."""


class WriteError(StorageError):
    """Raised when a write operation fails."""


class StorageFullError(WriteError):
    """Raised when there is no space left."""

    def __init__(self, needed: int, available: int) -> None:
        self.needed = needed
        self.available = available
        super().__init__(
            f"Need {needed} bytes but only {available} bytes available."
        )


def save_data(data: bytes, available_space: int) -> None:
    needed = len(data)
    if needed > available_space:
        raise StorageFullError(needed, available_space)
    print(f"Saved {needed} bytes.")


try:
    save_data(b"hello world", available_space=5)
except StorageFullError as e:
    print(f"Storage full: {e}")
    print(f"  Needed:    {e.needed} bytes")
    print(f"  Available: {e.available} bytes")
except WriteError as e:
    print(f"Write failed: {e}")
except StorageError as e:
    print(f"Storage error: {e}")
```

---

### 4.7 Retry Logic

```python
import time


def retry(func, attempts: int = 3, delay: float = 1.0, exceptions=(Exception,)):
    """Call func up to `attempts` times, waiting `delay` seconds between tries."""
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except exceptions as e:
            last_error = e
            print(f"Attempt {attempt}/{attempts} failed: {e}")
            if attempt < attempts:
                time.sleep(delay)
    raise RuntimeError(f"All {attempts} attempts failed.") from last_error


# Example usage with a simulated flaky operation:
import random

call_count = 0

def flaky_operation():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Simulated network failure.")
    return "success"


result = retry(flaky_operation, attempts=5, delay=0.0, exceptions=(ConnectionError,))
print(f"Result: {result}")
# Attempt 1/5 failed: Simulated network failure.
# Attempt 2/5 failed: Simulated network failure.
# Result: success
```

---

## 5. Common Mistakes

### 5.1 Catching Too Broadly

Catching `Exception` (or worse, bare `except`) hides bugs and makes debugging
harder.

```python
# Bad — catches everything, including bugs in your own code
try:
    result = complex_operation(data)
except Exception:
    print("Something went wrong.")

# Better — catch only what you expect
try:
    result = complex_operation(data)
except ValueError as e:
    print(f"Invalid data: {e}")
except IOError as e:
    print(f"I/O error: {e}")
```

---

### 5.2 Silently Swallowing Exceptions

An empty `except` block hides errors completely. At minimum, log the error.

```python
# Bad — error disappears silently
try:
    process(item)
except Exception:
    pass

# Better — at least log it
try:
    process(item)
except Exception as e:
    print(f"Warning: could not process item: {e}")
```

---

### 5.3 Using Exceptions for Normal Control Flow

Exceptions are for exceptional situations. Using them for expected conditions
makes code harder to read and slower.

```python
# Awkward — using exceptions for a normal check
try:
    index = items.index(target)
except ValueError:
    index = -1

# Clearer
index = items.index(target) if target in items else -1
```

That said, Python's "easier to ask forgiveness than permission" (EAFP) style
does use `try/except` for things like dict lookups and attribute access, where
it is idiomatic and efficient.

---

### 5.4 Forgetting `finally` for Cleanup

If you open a resource manually, always close it — even if an exception
occurs.

```python
# Risky — f.close() is skipped if an exception occurs
f = open("data.txt")
data = f.read()   # what if this raises?
f.close()

# Safe — finally always runs
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()

# Best — use a context manager (with statement)
with open("data.txt") as f:
    data = f.read()
```

---

### 5.5 Raising the Wrong Exception Type

Raise the exception type that best describes the problem. Callers use the type
to decide how to respond.

```python
# Wrong — ValueError is for bad values, not missing files
def load(path: str):
    if not Path(path).exists():
        raise ValueError(f"File not found: {path}")

# Correct
def load(path: str):
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")
```

---

### 5.6 Modifying the Exception Message Accidentally

When re-raising, use bare `raise` to preserve the original traceback. Using
`raise e` creates a new traceback that starts at the `except` line.

```python
try:
    risky()
except SomeError as e:
    raise e    # traceback starts here — loses original context

try:
    risky()
except SomeError:
    raise      # re-raises with original traceback intact
```

---

## 6. Practice Tasks

1. Write a function `safe_divide(a: float, b: float) -> float | None` that
   returns `a / b`, or `None` if `b` is zero, without raising an exception to
   the caller.

2. Write a function `parse_int(s: str) -> int` that converts a string to an
   integer and raises a `ValueError` with a helpful message if the string is
   not a valid integer.

3. Write a function `read_lines(path: str) -> list[str]` that reads a file and
   returns its lines as a list. Handle `FileNotFoundError` and
   `PermissionError` separately, printing a descriptive message for each.

4. Create a custom exception `NegativeValueError(ValueError)` that stores the
   offending value. Write a function `sqrt(x: float) -> float` that raises
   `NegativeValueError` if `x` is negative.

5. Write a function `load_json(path: str) -> dict` that reads a JSON file and
   returns its contents as a dict. Handle missing files and invalid JSON
   separately.

6. Write a function `get_element(lst: list, index: int, default=None)` that
   returns `lst[index]` or `default` if the index is out of range.

7. Add `try/except/else/finally` to a function that opens a file, reads it,
   and prints a success or failure message. The `finally` block should always
   print "Done."

8. Use `breakpoint()` to step through a short function and inspect its local
   variables at each step.

---

## 7. Key Takeaways

- Syntax errors are caught before the program runs. Exceptions occur at
  runtime.
- Read tracebacks from the bottom up: the last line names the exception; the
  frames above show the call chain.
- Use `try/except` to handle exceptions you expect and can recover from.
- Catch specific exception types — avoid bare `except` and overly broad
  `except Exception`.
- The `else` clause runs only when no exception occurred. Use it for success
  logic that should not be inside the `try` block.
- The `finally` clause always runs. Use it for cleanup.
- Use `as` to bind the exception object and access its message and attributes.
- `raise` signals an error. Use the most specific exception type that fits.
- Bare `raise` inside an `except` block re-raises the original exception with
  its original traceback.
- Custom exceptions inherit from `Exception` and make your error conditions
  explicit and catchable.
- `assert` is for catching programming mistakes, not for validating user input.
- `breakpoint()` drops you into `pdb` for interactive debugging. `print()`
  and `logging` are useful for tracing values.

---

### What's Next

Chapter 13 covers **files, paths, JSON, and CSV** — reading and writing files,
navigating the filesystem with `pathlib`, and working with the two most common
data formats you will encounter in real programs.

---

*See also:*
- [Exercises for Chapter 12](../exercises/12-errors-exceptions-debugging.md)
- [Solutions for Chapter 12](../solutions/12-errors-exceptions-debugging.md)
- [Reference: Built-in Exceptions](../references/builtin-exceptions.md)
