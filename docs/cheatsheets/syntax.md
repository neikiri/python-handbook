# Python Syntax Cheatsheet

Quick reference for Python syntax fundamentals.

## Comments

```python
# Single-line comment

"""
Multi-line comment (docstring).
Can span multiple lines.
"""

'''
Also valid for multi-line comments.
'''
```

## Indentation

Python uses indentation to define code blocks. Use 4 spaces per level (not tabs).

```python
if x > 5:
    print("x is greater than 5")  # Indented 4 spaces
    if x > 10:
        print("x is greater than 10")  # Indented 8 spaces
```

## Variables and Assignment

```python
x = 10                    # Simple assignment
x, y = 5, 10             # Multiple assignment
x = y = 5                # Chained assignment
x, *rest = [1, 2, 3, 4]  # Unpacking (rest = [2, 3, 4])
```

## Operators

| Operator | Example | Result |
|----------|---------|--------|
| `+` | `5 + 3` | `8` |
| `-` | `5 - 3` | `2` |
| `*` | `5 * 3` | `15` |
| `/` | `5 / 2` | `2.5` |
| `//` | `5 // 2` | `2` |
| `%` | `5 % 2` | `1` |
| `**` | `5 ** 2` | `25` |
| `==` | `5 == 5` | `True` |
| `!=` | `5 != 3` | `True` |
| `<`, `>`, `<=`, `>=` | `5 > 3` | `True` |
| `and`, `or`, `not` | `True and False` | `False` |

## Conditionals

```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code

# Ternary operator
result = value_if_true if condition else value_if_false
```

## Loops

```python
# For loop
for item in iterable:
    print(item)

# While loop
while condition:
    # code

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit loop
```

## Functions

```python
def function_name(param1, param2=default_value):
    """Docstring describing the function."""
    return result

# Calling a function
result = function_name(arg1, arg2)

# Default arguments
def greet(name="World"):
    return f"Hello, {name}!"

# *args and **kwargs
def func(*args, **kwargs):
    print(args)    # Tuple of positional arguments
    print(kwargs)  # Dictionary of keyword arguments
```

## Imports

```python
import module_name
from module_name import function_name
from module_name import function_name as alias
from module_name import *  # Import all (generally avoid)
import module_name as alias
```

## Main Guard

```python
if __name__ == "__main__":
    # Code here runs only when script is executed directly,
    # not when imported as a module
    main()
```

## Common Patterns

### List Comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### Dictionary Comprehension
```python
squares_dict = {x: x**2 for x in range(5)}
```

### Try-Except
```python
try:
    # code that might raise an exception
except SpecificError as e:
    # handle error
except Exception:
    # catch-all
finally:
    # always runs
```

### With Statement
```python
with open("file.txt") as f:
    content = f.read()
# File automatically closed
```

### Lambda Functions
```python
square = lambda x: x**2
result = square(5)  # 25

# Often used with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
```

## String Formatting

```python
# f-strings (preferred, Python 3.6+)
name = "Alice"
age = 30
print(f"{name} is {age} years old")

# .format()
print("{} is {} years old".format(name, age))

# % formatting (older style)
print("%s is %d years old" % (name, age))
```

## Truthiness

Values that evaluate to `False`:
- `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`

All other values evaluate to `True`.