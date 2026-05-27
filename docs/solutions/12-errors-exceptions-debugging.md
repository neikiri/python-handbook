# Solutions 12: Errors, Exceptions, and Debugging

## Overview

Chapter 12 exercises cover catching and handling exceptions, using `try-except-else-finally`, raising exceptions, creating custom exception classes, validating input, and debugging techniques. This guide explains the reasoning behind each solution and highlights best practices for writing robust, defensive code.

---

## Notes Before Checking Solutions

Exception handling is not about hiding errors — it is about responding to them appropriately. The goal is to catch exceptions you can handle, let the ones you cannot handle propagate, and always leave the program in a consistent state.

---

## Warm-up Exercise Solutions

### Exercise 1: Catch and Handle Exceptions

```python
try:
    number = int("not a number")
except ValueError:
    print("Error: Could not convert to integer")

try:
    d = {"a": 1, "b": 2}
    print(d["c"])
except KeyError:
    print("Error: Key not found")

try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("Error: Index out of range")

try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result: {result}")
except ValueError:
    print("Error: Not a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

try:
    x = 1 / 0
except Exception as e:
    print(f"Error: {e}")
```

**Catch specific exceptions, not `Exception`.** Using `except Exception` catches almost everything, which can hide bugs. Catch the most specific exception type you expect. If you genuinely need to catch anything, use `except Exception as e` and log or re-raise it.

**Multiple `except` clauses** are checked in order. Python uses the first one that matches. Put more specific exceptions before more general ones.

---

### Exercise 2: Use try-except-else-finally

```python
# try-except-else: else runs only if no exception was raised
try:
    number = int("42")
except ValueError:
    print("Error: Invalid number")
else:
    print(f"Success: {number}")  # runs because no exception

# try-except-finally: finally always runs
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Cleanup: This always runs")

# Proper file handling with context manager
try:
    with open("test.txt", "w") as f:
        f.write("Hello, World!")
    print("File written successfully")
except IOError as e:
    print(f"Error: {e}")
finally:
    print("File operation complete")
```

**`else` vs. putting code after `try`:** Code in the `else` block only runs if no exception was raised in the `try` block. Code placed after the entire `try-except` block runs regardless (unless an exception propagated). Use `else` to make the "success path" explicit.

**`finally` is for cleanup.** It runs whether or not an exception occurred, and even if a `return` statement is hit. Use it to release resources, close connections, or restore state. In practice, `with` statements handle most cleanup automatically.

---

### Exercise 3: Raise Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Re-raise
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Caught division by zero")
        raise  # re-raises the same exception
except ZeroDivisionError:
    print("Exception propagated")

# Exception chaining
try:
    try:
        int("not a number")
    except ValueError as e:
        raise RuntimeError("Failed to parse input") from e
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")
```

**`raise` without arguments** re-raises the current exception. Use this when you want to log or partially handle an exception but still let it propagate.

**`raise X from Y`** chains exceptions. The `__cause__` attribute on the new exception points to the original. This preserves the full error context and is more informative than swallowing the original exception.

**Include context in error messages.** `raise ValueError("Age cannot be negative")` is more useful than `raise ValueError("Invalid input")`. The caller needs to know what went wrong.

---

### Exercise 4: Debug with Print Statements

```python
def calculate_average(numbers):
    print(f"Input: {numbers}")
    total = sum(numbers)
    print(f"Total: {total}")
    count = len(numbers)
    print(f"Count: {count}")
    average = total / count
    print(f"Average: {average}")
    return average

result = calculate_average([10, 20, 30, 40])
# Input: [10, 20, 30, 40]
# Total: 100
# Count: 4
# Average: 25.0
```

**Print debugging is effective for quick investigations.** For more complex debugging, use Python's built-in `pdb` debugger (`import pdb; pdb.set_trace()`) or your IDE's debugger. Remove debug prints before committing code.

---

## Practice Exercise Solutions

### Exercise 5: Validate User Input

```python
def get_positive_integer(prompt):
    """Get a positive integer from user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Must be positive")
                continue
            return value
        except ValueError:
            print("Error: Not a valid integer")

def get_choice(options):
    """Get a choice from a list of options."""
    while True:
        try:
            choice = int(input(f"Choose (1-{len(options)}): "))
            if choice < 1 or choice > len(options):
                print(f"Error: Choose between 1 and {len(options)}")
                continue
            return choice - 1
        except ValueError:
            print("Error: Not a valid number")
```

**The validation loop pattern:** `while True` with `continue` on invalid input and `return` on valid input is the standard Python pattern for input validation. It keeps retrying until the user provides valid input.

**Separate validation from business logic.** `get_positive_integer()` only handles the input loop. The caller decides what to do with the value. This makes the validator reusable.

---

### Exercise 6: Handle File Operations

```python
def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def write_file_safe(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"File '{filename}' written successfully")
    except IOError as e:
        print(f"Error writing file: {e}")

import json

def load_json_safe(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'")
        return None
```

**Always use `with` for file operations.** It guarantees the file is closed even if an exception occurs. Never rely on the garbage collector to close files.

**Return `None` on failure** when the caller needs to check whether the operation succeeded. Alternatively, let the exception propagate if the caller should handle it. Avoid returning error strings — they are easy to ignore.

---

### Exercise 7: Create Custom Exceptions

```python
class InvalidAgeError(Exception):
    """Raised when age is invalid."""
    pass

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass

def validate_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Age {age} is invalid")
    return age

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount} from balance {balance}"
        )
    return balance - amount

# Custom exception with additional attributes
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

try:
    raise ValidationError("email", "Invalid email format")
except ValidationError as e:
    print(f"Validation error on field '{e.field}': {e.message}")
```

**Why create custom exceptions?** They let callers catch specific error types without catching everything. `except InvalidAgeError` is more precise than `except ValueError`. They also carry domain-specific information (like `field` in `ValidationError`).

**Always call `super().__init__(message)`** so the exception message is set correctly and shows up in tracebacks.

**Inherit from `Exception`, not `BaseException`.** `BaseException` is the root of all exceptions including `KeyboardInterrupt` and `SystemExit`. Inheriting from `Exception` keeps your custom exceptions in the normal exception hierarchy.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Robust Calculator

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid operand types")
        return None

safe_divide(10, 2)   # 5.0
safe_divide(10, 0)   # None, prints error
```

**Avoid `eval()` in production code.** The exercise uses `eval()` for demonstration, but it executes arbitrary Python code and is a security risk. In real applications, parse expressions explicitly or use a safe math library.

---

### Challenge 2: Implement Retry Logic

```python
import time

def retry(func, max_attempts=3, delay=1):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts:
                print(f"Failed after {max_attempts} attempts")
                raise
            print(f"Attempt {attempt} failed: {e}. Retrying...")
            time.sleep(delay)
```

**Re-raise on the final attempt** so the caller knows the operation failed. Swallowing the exception would hide the failure.

**Exponential backoff** (doubling the delay each attempt) is common in production retry logic. The simple version here uses a fixed delay, which is fine for learning.

---

### Challenge 3: Log Errors to a File

```python
import traceback
from datetime import datetime

def log_error(filename, error):
    try:
        with open(filename, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {error}\n")
            f.write(traceback.format_exc())
            f.write("-" * 50 + "\n")
    except IOError as e:
        print(f"Could not log error: {e}")

try:
    x = 1 / 0
except Exception as e:
    log_error("errors.log", str(e))
    print("Error logged")
```

**`traceback.format_exc()`** returns the full traceback as a string, including the exception type, message, and the call stack. This is much more useful than just the error message when debugging.

**Open in append mode (`"a"`)** so each error is added to the log rather than overwriting it.

In production, use Python's `logging` module instead of manual file writing — it handles log levels, rotation, and formatting automatically.

---

## Common Mistakes

**Bare `except:` clause.** `except:` catches everything, including `KeyboardInterrupt` and `SystemExit`. This can make your program impossible to stop with Ctrl+C. Always specify at least `except Exception:`.

**Swallowing exceptions silently.** An empty `except` block hides errors and makes debugging very difficult. At minimum, log the error or print it.

```python
# Bad
try:
    risky_operation()
except Exception:
    pass  # silently ignores all errors

# Better
try:
    risky_operation()
except Exception as e:
    print(f"Warning: {e}")
```

**Catching too broadly.** Catching `Exception` when you only expect `ValueError` means you will also catch unexpected errors like `AttributeError` or `TypeError`, hiding bugs.

**Not cleaning up resources.** If you open a file or acquire a lock in a `try` block, always release it in `finally` or use a `with` statement.

---

## What to Review Next

- Chapter 13: Files, Paths, JSON, and CSV — applying exception handling to file operations
- Chapter 18: Testing and Code Quality — testing that exceptions are raised correctly
- Chapter 22: Practical Projects — building applications with robust error handling
