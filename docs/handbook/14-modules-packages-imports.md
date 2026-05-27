# Chapter 14: Modules and Packages

## 1. Overview

As programs grow, keeping all the code in a single file becomes unmanageable.
Python's module system lets you split code across multiple files, reuse it
across projects, and take advantage of the vast standard library and
third-party ecosystem.

A **module** is any Python file. A **package** is a directory of modules. The
`import` statement is how you bring code from one module into another.
Understanding how imports work — and how to structure your own code — is
essential for writing maintainable Python programs.

---

## 2. What You Will Learn

- What a module is and how to import one
- Different import styles and when to use each
- How Python finds modules (the module search path)
- Writing your own modules
- The `if __name__ == "__main__"` pattern
- What a package is and how to create one
- Relative imports within a package
- The `__init__.py` file
- Common import mistakes and how to avoid them
- A tour of useful standard library modules

---

## 3. Core Concepts

### 3.1 What Is a Module?

A module is a Python file. Any `.py` file is a module. When you write:

```python
# greetings.py
def hello(name: str) -> str:
    return f"Hello, {name}!"

def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

GREETING = "Hello"
```

You have created a module named `greetings`. Other files can import it and
use its functions and variables.

---

### 3.2 Importing a Module

#### `import module`

The most basic form. Imports the module and makes it available under its name.

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
print(math.floor(3.7))  # 3
```

You access names from the module using dot notation: `module.name`. This keeps
the module's names in their own namespace, avoiding conflicts with your own
names.

#### `from module import name`

Import specific names directly into the current namespace.

```python
from math import pi, sqrt

print(pi)       # 3.141592653589793
print(sqrt(25)) # 5.0
```

Now you can use `pi` and `sqrt` directly without the `math.` prefix. The
downside is that it is less obvious where these names came from when reading
the code.

#### `from module import *`

Import all public names from a module. Avoid this in most cases — it pollutes
your namespace and makes it hard to tell where names come from.

```python
from math import *   # imports sin, cos, pi, sqrt, floor, ceil, ...
```

The only common exception is interactive sessions or very small scripts where
convenience matters more than clarity.

#### `import module as alias`

Import a module under a different name. Useful for long module names or to
avoid conflicts.

```python
import collections as col
import pathlib as pl

d = col.defaultdict(list)
p = pl.Path("data")
```

#### `from module import name as alias`

Import a specific name under a different name.

```python
from datetime import datetime as dt

now = dt.now()
print(now)
```

---

### 3.3 How Python Finds Modules

When you write `import something`, Python searches for it in this order:

1. **`sys.modules`** — the cache of already-imported modules. If it is there,
   Python reuses it without re-executing the file.
2. **Built-in modules** — modules compiled into the Python interpreter (like
   `sys`, `builtins`).
3. **`sys.path`** — a list of directories Python searches. It includes:
   - The directory containing the script being run (or the current directory
     in interactive mode).
   - Directories from the `PYTHONPATH` environment variable.
   - Standard library directories.
   - Site-packages (where `pip` installs third-party packages).

```python
import sys
print(sys.path)   # list of directories Python searches
```

If Python cannot find the module in any of these locations, it raises an
`ImportError` (or `ModuleNotFoundError`, which is a subclass).

---

### 3.4 Writing Your Own Module

Any `.py` file is a module. Create a file, put functions and variables in it,
and import it from another file in the same directory.

```python
# math_utils.py

def clamp(value: float, low: float, high: float) -> float:
    """Return value constrained to [low, high]."""
    return max(low, min(high, value))


def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolation between a and b by factor t."""
    return a + (b - a) * t


PI = 3.141592653589793
```

```python
# main.py (in the same directory as math_utils.py)

import math_utils

print(math_utils.clamp(15, 0, 10))   # 10
print(math_utils.lerp(0, 100, 0.25)) # 25.0
print(math_utils.PI)                 # 3.141592653589793
```

Or import specific names:

```python
from math_utils import clamp, lerp

print(clamp(-5, 0, 10))   # 0
print(lerp(10, 20, 0.5))  # 15.0
```

---

### 3.5 The `if __name__ == "__main__"` Pattern

When Python runs a file directly (e.g., `python script.py`), it sets the
module's `__name__` attribute to `"__main__"`. When the same file is imported
as a module, `__name__` is set to the module's name instead.

This lets you write code that runs only when the file is executed directly,
not when it is imported.

```python
# greetings.py

def hello(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = input("Enter your name: ")
    print(hello(name))


if __name__ == "__main__":
    main()
```

When you run `python greetings.py`, `main()` is called. When another file
does `import greetings`, `main()` is not called — only the function
definitions are loaded.

This pattern is the standard way to make a module both importable and
runnable. Always put runnable code inside `if __name__ == "__main__":` rather
than at the module's top level.

---

### 3.6 Packages

A **package** is a directory that contains Python modules and a special file
called `__init__.py`. The `__init__.py` file marks the directory as a package
and can be empty or contain initialization code.

```text
mypackage/
    __init__.py
    utils.py
    parser.py
    formatter.py
```

Import from a package using dot notation:

```python
import mypackage.utils
from mypackage import parser
from mypackage.formatter import format_output
```

#### The `__init__.py` file

`__init__.py` runs when the package is first imported. You can use it to:

- Leave it empty (just marks the directory as a package).
- Import names from submodules to make them available at the package level.
- Define package-level variables or run initialization code.

```python
# mypackage/__init__.py

from .utils import helper_function
from .parser import parse

VERSION = "1.0.0"
```

After this, users can write:

```python
from mypackage import helper_function, parse
```

instead of:

```python
from mypackage.utils import helper_function
from mypackage.parser import parse
```

#### Nested packages

Packages can contain sub-packages:

```text
myapp/
    __init__.py
    core/
        __init__.py
        models.py
        views.py
    utils/
        __init__.py
        text.py
        numbers.py
```

```python
from myapp.core import models
from myapp.utils.text import slugify
```

---

### 3.7 Relative Imports

Inside a package, you can use **relative imports** to import from sibling
modules without specifying the full package path. This makes the package more
portable — renaming the package does not break internal imports.

```python
# mypackage/formatter.py

from .utils import helper_function      # import from sibling module
from .parser import parse               # import from sibling module
from ..other_package import something   # import from parent package
```

A single dot `.` means the current package. Two dots `..` mean the parent
package.

Relative imports only work inside packages. You cannot use them in a script
run directly (where `__name__ == "__main__"`).

---

### 3.8 Standard Library Highlights

Python's standard library is large. Here are modules you will use regularly:

| Module | What it provides |
|---|---|
| `os` | OS interface: environment variables, process info, low-level file ops |
| `sys` | Interpreter info: `sys.argv`, `sys.path`, `sys.exit()` |
| `pathlib` | Object-oriented filesystem paths (covered in Chapter 13) |
| `math` | Mathematical functions: `sqrt`, `floor`, `ceil`, `log`, trig |
| `random` | Random numbers and choices |
| `datetime` | Dates, times, and durations |
| `collections` | Specialized containers: `Counter`, `defaultdict`, `deque`, `namedtuple` |
| `itertools` | Iterator building blocks: `chain`, `islice`, `product`, `groupby` |
| `functools` | Higher-order functions: `lru_cache`, `partial`, `reduce` |
| `re` | Regular expressions |
| `json` | JSON encoding and decoding (covered in Chapter 13) |
| `csv` | CSV reading and writing (covered in Chapter 13) |
| `io` | In-memory streams: `StringIO`, `BytesIO` |
| `copy` | Shallow and deep copying |
| `time` | Time measurement and sleep |
| `logging` | Flexible logging (covered in Chapter 12) |
| `unittest` | Built-in testing framework |
| `argparse` | Command-line argument parsing (covered in Chapter 20) |
| `dataclasses` | Data classes with auto-generated methods |
| `typing` | Type hint utilities |
| `contextlib` | Utilities for context managers |
| `hashlib` | Cryptographic hash functions |
| `uuid` | UUID generation |
| `textwrap` | Text wrapping and filling |
| `pprint` | Pretty-printing data structures |

You do not need to memorize all of these. When you need a common task, check
the standard library before reaching for a third-party package.

---

### 3.9 Useful Standard Library Examples

#### `collections.Counter`

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts)                    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts.most_common(2))     # [('apple', 3), ('banana', 2)]
```

#### `collections.defaultdict`

```python
from collections import defaultdict

# Group words by first letter
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
by_letter: defaultdict[str, list[str]] = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)

print(dict(by_letter))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

#### `itertools.chain` and `itertools.islice`

```python
from itertools import chain, islice

# Combine multiple iterables
combined = list(chain([1, 2], [3, 4], [5]))
print(combined)   # [1, 2, 3, 4, 5]

# Take the first n items from any iterable
first_five = list(islice(range(1_000_000), 5))
print(first_five)   # [0, 1, 2, 3, 4]
```

#### `functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### `datetime`

```python
from datetime import date, datetime, timedelta

today = date.today()
print(today)                          # 2024-03-15
print(today.strftime("%B %d, %Y"))    # March 15, 2024

now = datetime.now()
print(now.isoformat())                # 2024-03-15T09:30:00.123456

deadline = today + timedelta(days=30)
print(deadline)                       # 2024-04-14
```

#### `random`

```python
import random

print(random.randint(1, 6))           # random integer 1–6
print(random.choice(["a", "b", "c"])) # random element
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)                          # shuffled in place
print(random.sample(items, 3))        # 3 unique random elements
```

---

## 4. Practical Examples

### 4.1 A Simple Utility Module

```python
# text_utils.py

"""Utility functions for text processing."""


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Example: "Hello, World!" -> "hello-world"
    """
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length characters, appending suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split())


if __name__ == "__main__":
    samples = [
        "Hello, World!",
        "  Python is great  ",
        "This is a longer sentence for testing truncation.",
    ]
    for s in samples:
        print(f"Original:  {s!r}")
        print(f"Slug:      {slugify(s)!r}")
        print(f"Truncated: {truncate(s, 20)!r}")
        print(f"Words:     {word_count(s)}")
        print()
```

---

### 4.2 A Package with Multiple Modules

```text
calculator/
    __init__.py
    basic.py
    advanced.py
```

```python
# calculator/basic.py

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```

```python
# calculator/advanced.py

import math
from .basic import multiply   # relative import from sibling module


def power(base: float, exp: float) -> float:
    return base ** exp


def square_root(x: float) -> float:
    if x < 0:
        raise ValueError(f"Cannot take square root of {x}.")
    return math.sqrt(x)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative numbers.")
    return math.factorial(n)
```

```python
# calculator/__init__.py

from .basic import add, subtract, multiply, divide
from .advanced import power, square_root, factorial

__version__ = "1.0.0"
__all__ = ["add", "subtract", "multiply", "divide",
           "power", "square_root", "factorial"]
```

```python
# main.py

import calculator

print(calculator.add(3, 4))          # 7
print(calculator.square_root(16))    # 4.0
print(calculator.factorial(5))       # 120
print(calculator.__version__)        # 1.0.0

# Or import specific functions
from calculator import power, divide
print(power(2, 10))   # 1024.0
print(divide(10, 3))  # 3.3333333333333335
```

---

### 4.3 Using `sys.argv` for Simple Scripts

```python
# greet.py

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python greet.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    greeting = sys.argv[2] if len(sys.argv) > 2 else "Hello"
    print(f"{greeting}, {name}!")


if __name__ == "__main__":
    main()
```

```bash
python greet.py Alice
# Hello, Alice!

python greet.py Bob "Good morning"
# Good morning, Bob!
```

---

### 4.4 Lazy Imports for Optional Dependencies

If a module is only needed in certain code paths, import it inside the
function rather than at the top of the file. This avoids an `ImportError` if
the module is not installed, and speeds up startup if the function is rarely
called.

```python
def export_to_excel(data: list[dict], path: str) -> None:
    """Export data to an Excel file. Requires openpyxl."""
    try:
        import openpyxl
    except ImportError:
        raise ImportError(
            "openpyxl is required for Excel export. "
            "Install it with: pip install openpyxl"
        ) from None

    wb = openpyxl.Workbook()
    ws = wb.active
    # ... write data ...
    wb.save(path)
```

---

### 4.5 Inspecting a Module

```python
import math
import pprint

# List all public names in a module
print(dir(math))

# Get documentation
help(math.sqrt)

# Check where a module is located
print(math.__file__)

# Check the module's version (if it has one)
import json
print(json.__version__ if hasattr(json, "__version__") else "no version")
```

---

### 4.6 Reloading a Module During Development

In an interactive session, if you edit a module file, Python will not
automatically pick up the changes because it caches imported modules. Use
`importlib.reload()` to force a reload.

```python
import importlib
import my_module

# After editing my_module.py:
importlib.reload(my_module)
```

This is mainly useful in interactive sessions. In normal scripts, just restart
the interpreter.

---

## 5. Common Mistakes

### 5.1 Naming Your File the Same as a Standard Library Module

If you create a file named `math.py`, `random.py`, or `json.py`, it will
shadow the standard library module. Any `import math` in your project will
import your file instead of the standard library.

```text
# Bad — shadows the standard library
math.py
random.py
json.py

# Good — use descriptive names
math_utils.py
random_helpers.py
json_config.py
```

---

### 5.2 Circular Imports

A circular import occurs when module A imports module B, and module B imports
module A. Python can handle some circular imports, but they often cause
`ImportError` or `AttributeError` because one module is not fully loaded when
the other tries to use it.

```python
# a.py
from b import func_b   # imports b

# b.py
from a import func_a   # imports a — circular!
```

Fix by restructuring: move shared code to a third module that both A and B
import, or move the import inside the function that needs it.

---

### 5.3 Importing at the Wrong Level

Putting imports inside loops or frequently-called functions is wasteful.
Python caches modules after the first import, but the lookup still has a cost.
Put imports at the top of the file.

```python
# Slow — re-evaluates the import statement on every call
def process(data):
    import json   # fine for lazy/optional imports, but not for regular use
    return json.dumps(data)

# Better — import once at the top
import json

def process(data):
    return json.dumps(data)
```

The exception is lazy imports for optional or rarely-used dependencies, as
shown in section 4.4.

---

### 5.4 Using `from module import *` in Production Code

Wildcard imports make it impossible to tell where a name came from. They also
risk overwriting names you defined yourself.

```python
# Bad — where does 'sqrt' come from?
from math import *
from cmath import *   # also has sqrt — which one wins?

result = sqrt(4)

# Good — explicit
from math import sqrt
result = sqrt(4)
```

---

### 5.5 Forgetting `if __name__ == "__main__"`

Code at the module's top level runs when the module is imported. If you put
runnable code there without the guard, it runs every time someone imports your
module.

```python
# Bad — runs on import
print("Starting program...")
result = expensive_computation()

# Good — only runs when executed directly
if __name__ == "__main__":
    print("Starting program...")
    result = expensive_computation()
```

---

### 5.6 Relative Imports Outside a Package

Relative imports only work inside packages. If you try to use them in a
script run directly, you get an `ImportError`.

```python
# script.py (run directly as: python script.py)
from .utils import helper   # ImportError: attempted relative import with no known parent package
```

Use absolute imports in scripts. Use relative imports inside packages.

---

### 5.7 Modifying `sys.path` Unnecessarily

Adding directories to `sys.path` at runtime is a code smell. It makes the
import structure implicit and fragile. Prefer proper package structure and
running scripts from the right directory.

```python
# Fragile — avoid
import sys
sys.path.append("/some/absolute/path")
import my_module

# Better — structure your project as a package and install it,
# or run scripts from the project root
```

---

## 6. Practice Tasks

1. Create a module `string_utils.py` with three functions: `is_palindrome`,
   `count_vowels`, and `reverse_words`. Add a `if __name__ == "__main__":`
   block that demonstrates each function.

2. Create a package `geometry/` with an `__init__.py` and two modules:
   `shapes.py` (with functions for area and perimeter of circles and
   rectangles) and `conversions.py` (with functions to convert between units).
   Import from both in a `main.py` script.

3. Write a script that uses `sys.argv` to accept a filename as a command-line
   argument, reads the file, and prints the number of lines, words, and
   characters.

4. Use `collections.Counter` to count the frequency of each character in a
   string, then print the top 5 most common characters.

5. Use `itertools.groupby` to group a list of dicts by a common key. For
   example, group a list of people by their city.

6. Write a module `config.py` that loads settings from a JSON file on import
   and exposes them as module-level variables. Add a `reload()` function that
   re-reads the file.

7. Demonstrate the `if __name__ == "__main__"` pattern: write a module with
   two functions and a main block. Import the module from another script and
   verify that the main block does not run.

8. Use `datetime` and `timedelta` to write a function `days_until(date_str:
   str) -> int` that returns the number of days from today until the given
   date (in `"YYYY-MM-DD"` format).

---

## 7. Key Takeaways

- A module is any `.py` file. Import it with `import module` or
  `from module import name`.
- Use `import module` when you want to keep names in the module's namespace.
  Use `from module import name` for convenience, but be explicit about what
  you import.
- Avoid `from module import *` in production code — it obscures where names
  come from.
- Python searches for modules in `sys.modules` (cache), built-ins, and then
  `sys.path`.
- Never name your files the same as standard library modules.
- Use `if __name__ == "__main__":` to guard runnable code so it does not
  execute on import.
- A package is a directory with an `__init__.py` file. Use dot notation to
  import from packages.
- Use relative imports (`.module`, `..module`) inside packages to avoid
  hardcoding the package name.
- The standard library is large and covers most common tasks. Check it before
  adding a third-party dependency.
- Circular imports are a sign of poor structure. Refactor shared code into a
  separate module.

---

### Further Reading

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Import System](https://docs.python.org/3/reference/import.html)

### What's Next

Ready to continue? Head to the next chapter: **Virtual Environments and pip**.

→ [Chapter 15 — Virtual Environments and pip](15-virtual-environments-pip.md)

*See also:*
- [Exercise](../exercises/14-modules-packages-imports.md)
- [Solution](../solutions/14-modules-packages-imports.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
