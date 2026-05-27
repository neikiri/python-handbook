# Built-in Exceptions Reference

Comprehensive reference for Python's built-in exceptions.

## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    ├── SyntaxError
    │   └── IndentationError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    └── Warning
```

## Common Exceptions

### SyntaxError

Raised when Python encounters invalid syntax.

```python
# Invalid syntax
if x = 5:  # SyntaxError: invalid syntax
    pass

# Caught at parse time, before execution
```

### IndentationError

Raised when indentation is incorrect.

```python
if x > 5:
print("x is greater than 5")  # IndentationError: expected an indented block
```

### NameError

Raised when a variable or function name is not found.

```python
print(undefined_variable)  # NameError: name 'undefined_variable' is not defined
```

### TypeError

Raised when an operation is applied to an object of inappropriate type.

```python
"hello" + 5  # TypeError: can only concatenate str (not "int") to str
len(5)  # TypeError: object of type 'int' has no len()
```

### ValueError

Raised when an operation receives an argument of correct type but inappropriate value.

```python
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
int("10.5")  # ValueError: invalid literal for int() with base 10: '10.5'
```

### IndexError

Raised when a sequence index is out of range.

```python
lst = [1, 2, 3]
lst[10]  # IndexError: list index out of range
```

### KeyError

Raised when a dictionary key is not found.

```python
d = {"a": 1}
d["b"]  # KeyError: 'b'
```

### AttributeError

Raised when an attribute reference or assignment fails.

```python
x = 5
x.append(1)  # AttributeError: 'int' object has no attribute 'append'
```

### FileNotFoundError

Raised when a file or directory is requested but doesn't exist.

```python
open("nonexistent.txt")  # FileNotFoundError: [Errno 2] No such file or directory
```

### ZeroDivisionError

Raised when division by zero is attempted.

```python
10 / 0  # ZeroDivisionError: division by zero
```

### ImportError / ModuleNotFoundError

Raised when an import fails.

```python
import nonexistent_module  # ModuleNotFoundError: No module named 'nonexistent_module'
from os import nonexistent  # ImportError: cannot import name 'nonexistent'
```

### RuntimeError

Raised when an error is detected that doesn't fall into any other category.

```python
# Rarely raised directly; usually indicates a problem in the Python runtime
```

### AssertionError

Raised when an assert statement fails.

```python
assert 1 == 2  # AssertionError
assert False, "This is false"  # AssertionError: This is false
```

### StopIteration

Raised by an iterator to signal that there are no more items.

```python
# Usually handled automatically by for loops
it = iter([1, 2, 3])
next(it)  # 1
next(it)  # 2
next(it)  # 3
next(it)  # StopIteration
```

## How to Read Exception Names

Exception names follow a pattern:

- **Error suffix**: Indicates something went wrong (e.g., `ValueError`, `TypeError`)
- **Exception suffix**: More general (e.g., `ImportError`)
- **Name structure**: Usually describes what went wrong
  - `NameError`: A name (variable/function) was not found
  - `TypeError`: Wrong type for an operation
  - `ValueError`: Wrong value for an operation
  - `IndexError`: Index out of range
  - `KeyError`: Dictionary key not found

## When to Catch Exceptions

### Catch Specific Exceptions

```python
try:
    x = int(user_input)
except ValueError:
    print("Please enter a valid number")
```

### Catch Multiple Exceptions

```python
try:
    result = 10 / x
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```

### Catch and Inspect

```python
try:
    open("file.txt")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

### Catch All (Use Sparingly)

```python
try:
    # code
except Exception as e:
    print(f"An error occurred: {e}")
```

### Finally Block

```python
try:
    f = open("file.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    f.close()  # Always runs
```

## Best Practices

- **Catch specific exceptions**: Avoid bare `except:` or `except Exception:`
- **Use context managers**: `with` statements handle cleanup automatically
- **Don't catch and ignore**: At least log or print the error
- **Raise with context**: Include the original exception when re-raising
- **Use custom exceptions**: For application-specific errors, create custom exception classes

```python
class InvalidAgeError(ValueError):
    """Raised when age is invalid."""
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age
```