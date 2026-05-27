# Solutions 14: Modules, Packages, and Imports

## Overview

Chapter 14 exercises cover creating and importing modules, using different import styles, organizing code into packages, and using standard library modules. This guide explains the reasoning behind each solution and highlights best practices for code organization.

---

## Notes Before Checking Solutions

Modules are the primary unit of code organization in Python. A module is just a `.py` file. A package is a directory containing an `__init__.py` file. The goal is to group related code together and keep each module focused on one responsibility.

---

## Warm-up Exercise Solutions

### Exercise 1: Create and Import a Module

`math_utils.py`:

```python
"""Simple math utilities."""

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

PI = 3.14159
```

`use_math_utils.py`:

```python
import math_utils

print(math_utils.add(10, 5))       # 15
print(math_utils.subtract(10, 5))  # 5
print(math_utils.multiply(10, 5))  # 50
print(math_utils.divide(10, 5))    # 2.0
print(math_utils.PI)               # 3.14159
```

**Why use `import math_utils` instead of `from math_utils import *`?** The `import module` style makes it clear where each name comes from. When you read `math_utils.add(...)`, you know immediately that `add` comes from `math_utils`. With `from math_utils import *`, names appear without context and can silently overwrite existing names.

---

### Exercise 2: Use Different Import Styles

```python
# Style 1: import entire module
import math_utils
result = math_utils.add(10, 5)

# Style 2: import specific names
from math_utils import add, subtract
result = add(10, 5)

# Style 3: import with alias
from math_utils import multiply as mul
result = mul(10, 5)

# Style 4: module alias
import math_utils as mu
result = mu.add(10, 5)
```

**When to use each style:**
- `import module` — preferred for most cases; keeps namespace clean
- `from module import name` — useful when you use a name frequently and the source is obvious
- `import module as alias` — useful for long module names (`import numpy as np`)
- `from module import *` — avoid in production code; use only in interactive sessions

---

### Exercise 3: Use Built-in Modules

```python
import math
import random
import datetime
import os

print(math.sqrt(16))    # 4.0
print(math.ceil(3.2))   # 4
print(math.floor(3.8))  # 3
print(math.pi)          # 3.141592653589793

print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))

now = datetime.datetime.now()
print(now.year, now.month, now.day)

print(os.getcwd())
```

**The standard library is large.** Before installing a third-party package, check whether the standard library already has what you need. `math`, `random`, `datetime`, `os`, `pathlib`, `json`, `csv`, `collections`, `itertools`, and `functools` cover a huge range of common tasks.

---

### Exercise 4: Understand Module Scope

`module_scope.py`:

```python
module_var = "I'm a module variable"

def function1():
    local_var = "I'm local"
    print(local_var)
    print(module_var)  # can read module-level variable

def function2():
    print(module_var)

print(module_var)
function1()
function2()
```

`use_module_scope.py`:

```python
import module_scope

print(module_scope.module_var)
module_scope.function1()
```

**Module-level code runs on import.** When you `import module_scope`, Python executes the module file from top to bottom. The `print(module_var)` at the bottom of `module_scope.py` runs immediately. Use `if __name__ == "__main__":` to prevent this.

---

## Practice Exercise Solutions

### Exercise 5: Create a Package

Directory structure:

```
mypackage/
  __init__.py
  math_ops.py
  string_ops.py
```

`mypackage/__init__.py`:

```python
"""My package of utilities."""

from .math_ops import add, subtract
from .string_ops import uppercase, lowercase

__all__ = ["add", "subtract", "uppercase", "lowercase"]
```

`mypackage/math_ops.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

`mypackage/string_ops.py`:

```python
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()
```

`use_package.py`:

```python
from mypackage import add, subtract, uppercase, lowercase

print(add(10, 5))          # 15
print(uppercase("hello"))  # HELLO
```

**`__init__.py`** marks a directory as a Python package. It can be empty, or it can import names from submodules to create a cleaner public API. The `from .math_ops import add` syntax uses a relative import (the `.` means "from this package").

**`__all__`** defines what is exported when someone does `from mypackage import *`. It is also a useful documentation tool — it explicitly lists the public API.

---

### Exercise 6: Use Standard Library Modules

```python
import json
import csv
from pathlib import Path
from collections import Counter
from itertools import combinations

data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)  # {"name": "Alice", "age": 30}

items = ["a", "b", "a", "c", "b", "a"]
counts = Counter(items)
print(counts)  # Counter({'a': 3, 'b': 2, 'c': 1})

items = [1, 2, 3]
pairs = list(combinations(items, 2))
print(pairs)  # [(1, 2), (1, 3), (2, 3)]
```

---

### Exercise 7: Organize Code into Modules

`calculator.py`:

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

`validator.py`:

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

`app.py`:

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

**`if __name__ == "__main__":`** prevents `main()` from running when `app.py` is imported by another module. It only runs when the file is executed directly. This is a standard Python idiom — always use it in scripts.

---

## Challenge Exercise Solutions

### Challenge 1: Create a Utility Library

`utils/__init__.py`:

```python
"""Utility library."""

from .text import reverse, count_words
from .numbers import is_prime, factorial
from .files import read_file, write_file

__all__ = ["reverse", "count_words", "is_prime", "factorial", "read_file", "write_file"]
```

`utils/text.py`:

```python
def reverse(text):
    return text[::-1]

def count_words(text):
    return len(text.split())
```

`utils/numbers.py`:

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

`utils/files.py`:

```python
from pathlib import Path

def read_file(filename):
    return Path(filename).read_text()

def write_file(filename, content):
    Path(filename).write_text(content)
```

`test_utils.py`:

```python
from utils import reverse, count_words, is_prime, factorial

print(reverse("hello"))           # olleh
print(count_words("hello world")) # 2
print(is_prime(7))                # True
print(factorial(5))               # 120
```

---

### Challenge 2: Implement Module Reloading

```python
import config
import importlib

print(config.DEBUG)       # True
config.DEBUG = False      # modify in memory

importlib.reload(config)  # re-execute the module file

print(config.DEBUG)       # True — reset to original value
```

**`importlib.reload()`** re-executes the module file, resetting all module-level variables to their original values. This is useful during development but rarely needed in production code.

---

## Common Mistakes

**`ImportError: No module named X`** — Check that the module file exists in the same directory or in the Python path. For packages, ensure `__init__.py` exists.

**Circular imports.** If module A imports from module B, and module B imports from module A, Python gets stuck in a loop. Restructure the code to break the cycle, or use a late import (import inside a function).

**Forgetting `if __name__ == "__main__":`** — Without this guard, module-level code runs when the module is imported, which can cause unexpected side effects.

**Using `from module import *` in production.** This pollutes the namespace and makes it hard to trace where names come from. Use explicit imports.

---

## What to Review Next

- Chapter 15: Virtual Environments and pip — managing dependencies for your modules
- Chapter 17: Standard Library — exploring the built-in modules available to you
- Chapter 18: Testing and Code Quality — testing your modules with pytest
