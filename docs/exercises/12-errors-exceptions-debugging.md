# Chapter 12: Errors, Exceptions, and Debugging — Exercises

## Overview

These exercises help you understand Python's error handling, write robust exception handlers, and debug code effectively. By the end, you will write defensive code that handles errors gracefully.

---

## How to Use These Exercises

- Create a folder called `chapter-12` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Catch and Handle Exceptions

Create a file called `exception_handling.py`:

```python
# Handle ValueError
try:
    number = int("not a number")
except ValueError:
    print("Error: Could not convert to integer")

# Handle KeyError
try:
    d = {"a": 1, "b": 2}
    print(d["c"])
except KeyError:
    print("Error: Key not found")

# Handle IndexError
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("Error: Index out of range")

# Handle multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result: {result}")
except ValueError:
    print("Error: Not a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Handle any exception
try:
    x = 1 / 0
except Exception as e:
    print(f"Error: {e}")
```

Run it and observe exception handling.

---

### Exercise 2: Use try-except-else-finally

Create a file called `try_except_else_finally.py`:

```python
# try-except-else
try:
    number = int("42")
except ValueError:
    print("Error: Invalid number")
else:
    print(f"Success: {number}")

# try-except-finally
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Cleanup: This always runs")

# try-except-else-finally
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Error: Not a valid number")
else:
    print(f"You entered: {value}")
finally:
    print("Done")

# Proper file handling
try:
    with open("test.txt", "w") as f:
        f.write("Hello, World!")
    print("File written successfully")
except IOError as e:
    print(f"Error: {e}")
finally:
    print("File operation complete")
```

Run it and observe the flow of try-except-else-finally.

---

### Exercise 3: Raise Exceptions

Create a file called `raise_exceptions.py`:

```python
# Raise a built-in exception
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

# Raise with a message
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Re-raise an exception
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Caught division by zero")
        raise  # Re-raise the same exception
except ZeroDivisionError:
    print("Exception propagated")

# Chain exceptions
try:
    try:
        int("not a number")
    except ValueError as e:
        raise RuntimeError("Failed to parse input") from e
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")
```

Run it and observe exception raising.

---

### Exercise 4: Debug with Print Statements

Create a file called `debug_print.py`:

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
print(f"Result: {result}")

# Debug with type checking
def process_data(data):
    print(f"Type of data: {type(data)}")
    print(f"Data: {data}")
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sum(data.values())
    else:
        print("Unexpected type")
        return None

print(process_data([1, 2, 3]))
print(process_data({"a": 1, "b": 2}))
```

Run it and observe debugging with print statements.

---

## Practice Exercises

### Exercise 5: Validate User Input

Create a file called `input_validation.py`:

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

# Use the validators
# age = get_positive_integer("Enter your age: ")
# print(f"You are {age} years old")

# options = ["Option A", "Option B", "Option C"]
# choice = get_choice(options)
# print(f"You chose: {options[choice]}")
```

Run it and test the validators.

---

### Exercise 6: Handle File Operations

Create a file called `file_operations.py`:

```python
# Safe file reading
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

# Safe file writing
def write_file_safe(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"File '{filename}' written successfully")
    except IOError as e:
        print(f"Error writing file: {e}")

# Safe JSON operations
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

def save_json_safe(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"JSON saved to '{filename}'")
    except IOError as e:
        print(f"Error writing JSON: {e}")

# Test
write_file_safe("test.txt", "Hello, World!")
content = read_file_safe("test.txt")
print(f"Content: {content}")
```

Run it and observe file handling.

---

### Exercise 7: Create Custom Exceptions

Create a file called `custom_exceptions.py`:

```python
# Define custom exceptions
class InvalidAgeError(Exception):
    """Raised when age is invalid."""
    pass

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass

# Use custom exceptions
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

# Handle custom exceptions
try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"Age error: {e}")

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Funds error: {e}")

# Custom exception with additional info
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

try:
    raise ValidationError("email", "Invalid email format")
except ValidationError as e:
    print(f"Validation error: {e}")
```

Run it and observe custom exceptions.

---

## Challenge Exercises

### Challenge 1: Build a Robust Calculator

Create a file called `robust_calculator.py`:

```python
def safe_divide(a, b):
    """Divide with error handling."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid operand types")
        return None

def safe_calculate(expression):
    """Evaluate expression with error handling."""
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except NameError:
        print("Error: Undefined variable")
        return None
    except SyntaxError:
        print("Error: Invalid expression")
        return None

# Test
print(safe_divide(10, 2))
print(safe_divide(10, 0))

print(safe_calculate("10 + 5"))
print(safe_calculate("10 / 0"))
```

Run it and test the calculator.

---

### Challenge 2: Implement Retry Logic

Create a file called `retry_logic.py`:

```python
def retry(func, max_attempts=3, delay=1):
    """Retry a function with exponential backoff."""
    import time
    
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts:
                print(f"Failed after {max_attempts} attempts")
                raise
            print(f"Attempt {attempt} failed: {e}. Retrying...")
            time.sleep(delay)

def unreliable_function():
    """Simulates an unreliable operation."""
    import random
    if random.random() < 0.7:
        raise RuntimeError("Random failure")
    return "Success!"

# Test
try:
    result = retry(unreliable_function, max_attempts=5)
    print(f"Result: {result}")
except RuntimeError:
    print("Operation failed")
```

Run it and observe retry logic.

---

### Challenge 3: Log Errors to a File

Create a file called `error_logging.py`:

```python
import traceback
from datetime import datetime

def log_error(filename, error):
    """Log an error to a file."""
    try:
        with open(filename, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {error}\n")
            f.write(traceback.format_exc())
            f.write("-" * 50 + "\n")
    except IOError as e:
        print(f"Could not log error: {e}")

def risky_operation():
    """Simulate a risky operation."""
    x = 1 / 0

# Test
try:
    risky_operation()
except Exception as e:
    log_error("errors.log", str(e))
    print("Error logged")

# Read the log
try:
    with open("errors.log", "r") as f:
        print("\nError log:")
        print(f.read())
except FileNotFoundError:
    print("No error log found")
```

Run it and observe error logging.

---

## Hints

**Exception not caught** → Make sure the exception type matches. Use `except Exception` to catch all exceptions.

**Finally block not running** → The `finally` block always runs, even if an exception is raised or caught.

**Bare except is bad** → Avoid `except:` without a type. Use `except Exception:` instead.

**Exception message unclear** → Include context in your exception messages to help with debugging.

---

## What to Review If You Get Stuck

- **Exception types** → Handbook section 2.1
- **try-except blocks** → Handbook section 2.2
- **try-except-else-finally** → Handbook section 2.3
- **Raising exceptions** → Handbook section 2.4
- **Custom exceptions** → Handbook section 2.5
- **Debugging techniques** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Catch and handle exceptions with try-except
- Use try-except-else-finally effectively
- Raise exceptions with meaningful messages
- Create custom exception classes
- Validate user input safely
- Handle file operations robustly
- Debug code with print statements and exception info
- Log errors for later analysis

