# Chapter 14: Modules, Packages, and Imports — Exercises

## Overview

These exercises help you organize code into modules and packages, use imports effectively, and understand Python's module system. By the end, you will write well-organized, reusable code.

---

## How to Use These Exercises

- Create a folder called `chapter-14` in your `python-learning` directory.
- Write each program in a separate `.py` file or create subdirectories for packages.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Create and Import a Module

Create a file called `math_utils.py`:

```python
"""Simple math utilities."""

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

PI = 3.14159
```

Create a file called `use_math_utils.py`:

```python
import math_utils

print(f"Add: {math_utils.add(10, 5)}")
print(f"Subtract: {math_utils.subtract(10, 5)}")
print(f"Multiply: {math_utils.multiply(10, 5)}")
print(f"Divide: {math_utils.divide(10, 5)}")
print(f"PI: {math_utils.PI}")
```

Run `use_math_utils.py` and observe the imports.

---

### Exercise 2: Use Different Import Styles

Create a file called `import_styles.py`:

```python
# Import entire module
import math_utils
result1 = math_utils.add(10, 5)
print(f"Style 1: {result1}")

# Import specific items
from math_utils import add, subtract
result2 = add(10, 5)
result3 = subtract(10, 5)
print(f"Style 2: add={result2}, subtract={result3}")

# Import with alias
from math_utils import multiply as mul
result4 = mul(10, 5)
print(f"Style 3: {result4}")

# Import all (not recommended)
from math_utils import *
result5 = divide(10, 5)
print(f"Style 4: {result5}")

# Import module with alias
import math_utils as mu
result6 = mu.add(10, 5)
print(f"Style 5: {result6}")
```

Run it and observe different import styles.

---

### Exercise 3: Use Built-in Modules

Create a file called `builtin_modules.py`:

```python
import math
import random
import datetime
import os

# Math module
print(f"sqrt(16): {math.sqrt(16)}")
print(f"ceil(3.2): {math.ceil(3.2)}")
print(f"floor(3.8): {math.floor(3.8)}")
print(f"pi: {math.pi}")

# Random module
print(f"\nRandom int: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['a', 'b', 'c'])}")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled: {numbers}")

# Datetime module
now = datetime.datetime.now()
print(f"\nNow: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")

# OS module
print(f"\nCurrent directory: {os.getcwd()}")
print(f"Path separator: {os.sep}")
```

Run it and observe built-in modules.

---

### Exercise 4: Understand Module Scope

Create a file called `module_scope.py`:

```python
# Define module-level variables
module_var = "I'm a module variable"

def function1():
    """Function with local scope."""
    local_var = "I'm local"
    print(f"Inside function1: {local_var}")
    print(f"Inside function1: {module_var}")

def function2():
    """Function accessing module variable."""
    print(f"Inside function2: {module_var}")

# Module-level code
print(f"Module level: {module_var}")
function1()
function2()

# Check what's in the module
print(f"\nModule contents: {dir()}")
```

Create a file called `use_module_scope.py`:

```python
import module_scope

print(f"Accessing module_var: {module_scope.module_var}")
module_scope.function1()
module_scope.function2()
```

Run both files and observe scope.

---

## Practice Exercises

### Exercise 5: Create a Package

Create a directory structure:

```
mypackage/
  __init__.py
  math_ops.py
  string_ops.py
```

Create `mypackage/__init__.py`:

```python
"""My package of utilities."""

from .math_ops import add, subtract
from .string_ops import uppercase, lowercase

__all__ = ["add", "subtract", "uppercase", "lowercase"]
```

Create `mypackage/math_ops.py`:

```python
"""Math operations."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Create `mypackage/string_ops.py`:

```python
"""String operations."""

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()
```

Create `use_package.py`:

```python
# Import from package
from mypackage import add, subtract, uppercase, lowercase

print(f"Add: {add(10, 5)}")
print(f"Subtract: {subtract(10, 5)}")
print(f"Uppercase: {uppercase('hello')}")
print(f"Lowercase: {lowercase('HELLO')}")
```

Run it and observe package imports.

---

### Exercise 6: Use Standard Library Modules

Create a file called `stdlib_examples.py`:

```python
import json
import csv
from pathlib import Path
from collections import Counter
from itertools import combinations

# JSON
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(f"JSON: {json_str}")

# CSV
rows = [["Name", "Age"], ["Alice", "30"], ["Bob", "25"]]
csv_file = Path("temp.csv")
with open(csv_file, "w", newline="") as f:
    csv.writer(f).writerows(rows)
print(f"CSV written to {csv_file}")

# Collections
items = ["a", "b", "a", "c", "b", "a"]
counts = Counter(items)
print(f"Counts: {counts}")

# Itertools
items = [1, 2, 3]
pairs = list(combinations(items, 2))
print(f"Combinations: {pairs}")

# Clean up
csv_file.unlink()
```

Run it and observe standard library modules.

---

### Exercise 7: Organize Code into Modules

Create a file called `calculator.py`:

```python
"""Calculator module."""

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

Create a file called `validator.py`:

```python
"""Input validation module."""

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_positive(value):
    return float(value) > 0
```

Create a file called `app.py`:

```python
"""Main application."""

import calculator
import validator

def main():
    print("Simple Calculator")
    
    while True:
        try:
            a = input("Enter first number: ")
            if not validator.is_number(a):
                print("Invalid number")
                continue
            
            op = input("Enter operation (+, -, *, /): ")
            
            b = input("Enter second number: ")
            if not validator.is_number(b):
                print("Invalid number")
                continue
            
            a, b = float(a), float(b)
            
            if op == "+":
                result = calculator.add(a, b)
            elif op == "-":
                result = calculator.subtract(a, b)
            elif op == "*":
                result = calculator.multiply(a, b)
            elif op == "/":
                result = calculator.divide(a, b)
            else:
                print("Invalid operation")
                continue
            
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
```

Run `app.py` and test the calculator.

---

## Challenge Exercises

### Challenge 1: Create a Utility Library

Create a directory structure:

```
utils/
  __init__.py
  text.py
  numbers.py
  files.py
```

Create `utils/__init__.py`:

```python
"""Utility library."""

from .text import reverse, count_words
from .numbers import is_prime, factorial
from .files import read_file, write_file

__all__ = ["reverse", "count_words", "is_prime", "factorial", "read_file", "write_file"]
```

Create `utils/text.py`:

```python
def reverse(text):
    return text[::-1]

def count_words(text):
    return len(text.split())
```

Create `utils/numbers.py`:

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Create `utils/files.py`:

```python
from pathlib import Path

def read_file(filename):
    return Path(filename).read_text()

def write_file(filename, content):
    Path(filename).write_text(content)
```

Create `test_utils.py`:

```python
from utils import reverse, count_words, is_prime, factorial

print(f"Reverse: {reverse('hello')}")
print(f"Word count: {count_words('hello world python')}")
print(f"Is 7 prime: {is_prime(7)}")
print(f"Factorial of 5: {factorial(5)}")
```

Run it and observe the utility library.

---

### Challenge 2: Implement Module Reloading

Create a file called `config.py`:

```python
"""Configuration module."""

DEBUG = True
MAX_RETRIES = 3
TIMEOUT = 30
```

Create a file called `reload_example.py`:

```python
import config
import importlib

print(f"Initial DEBUG: {config.DEBUG}")
print(f"Initial MAX_RETRIES: {config.MAX_RETRIES}")

# Simulate changing the config
config.DEBUG = False
config.MAX_RETRIES = 5

print(f"\nAfter change:")
print(f"DEBUG: {config.DEBUG}")
print(f"MAX_RETRIES: {config.MAX_RETRIES}")

# Reload the module
importlib.reload(config)

print(f"\nAfter reload:")
print(f"DEBUG: {config.DEBUG}")
print(f"MAX_RETRIES: {config.MAX_RETRIES}")
```

Run it and observe module reloading.

---

## Hints

**ImportError** → Check that the module file exists in the same directory or in the Python path.

**Circular imports** → Avoid importing A in B and B in A. Restructure your code or use late imports.

**`__name__ == "__main__"`** → Use this to write code that runs only when the module is executed directly, not when imported.

**Module not found** → Ensure `__init__.py` exists in package directories.

---

## What to Review If You Get Stuck

- **Modules** → Handbook section 2.1
- **Imports** → Handbook section 2.2
- **Packages** → Handbook section 2.3
- **Standard library** → Handbook section 2.4
- **Module scope** → Handbook section 2.5
- **Organizing code** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Create and import modules
- Use different import styles
- Organize code into packages
- Use standard library modules
- Understand module scope and namespaces
- Avoid circular imports
- Write reusable, well-organized code
- Use `__name__ == "__main__"` effectively

