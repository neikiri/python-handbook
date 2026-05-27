# Solutions 02: Installation and Setup

## Overview

Chapter 02 exercises are mostly verification and setup tasks rather than coding problems. This solution guide explains what correct output looks like, how to interpret it, and how to fix the most common problems.

---

## Notes Before Checking Solutions

Most of these exercises have no single "correct" answer — the output depends on your operating system, Python version, and installation method. The goal is to confirm that Python is installed and working, not to match a specific string.

---

## Warm-up Exercise Solutions

### Exercise 1: Verify Your Python Installation

**What correct output looks like:**

```text
Python 3.11.4
```

or

```text
Python 3.12.0
```

Any version starting with `3.10` or higher is fine. If you see `Python 2.7.x`, that is Python 2 — you need to install Python 3 separately.

**On macOS and Linux**, the system Python is often Python 2. Use `python3` instead of `python`:

```bash
python3 --version
```

**On Windows**, the Microsoft Store version of Python sets up `python` to point to Python 3. The `python3` alias may or may not work depending on how you installed it.

**If pip is missing:**

```bash
python -m pip --version
```

This uses the pip bundled with Python directly. If that also fails, reinstall Python and make sure to check "Add pip" during installation.

---

### Exercise 2: Explore the Python REPL

Expected outputs for each expression:

```python
>>> 2 + 2
4

>>> "hello" + " world"
'hello world'

>>> len("Python")
6

>>> 10 / 3
3.3333333333333335

>>> 10 // 3
3

>>> 2 ** 8
256
```

Key observations:
- `/` always returns a float, even when the result is a whole number (`10 / 2` gives `5.0`).
- `//` is floor division — it rounds down to the nearest integer.
- `**` is the exponentiation operator (not `^`, which is bitwise XOR in Python).
- String concatenation with `+` works, but the strings must both be strings — `"hello" + 5` raises a `TypeError`.

---

### Exercise 3: Create Your First Python File

The expected output is exactly:

```text
Hello, Python!
```

If you see nothing, the file may not have been saved. If you see an error, check:
1. The file is named `hello.py` (not `hello.py.txt`)
2. You are in the correct directory when you run `python hello.py`
3. The `print` call has parentheses — `print("Hello, Python!")` not `print "Hello, Python!"`

---

## Practice Exercise Solutions

### Exercise 4: Run a Script with User Input

```python
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python.")
```

**How it works:**
- `input()` pauses the program and waits for the user to type something and press Enter.
- Whatever the user types is returned as a string and stored in `name`.
- The f-string `f"Hello, {name}!"` inserts the value of `name` into the string at runtime.

**Common mistake:** Forgetting that `input()` always returns a string. If you need a number, you must convert it: `age = int(input("Age: "))`.

---

### Exercise 5: Understand the Python Interpreter

```python
import sys

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Platform: {sys.platform}")
```

**Example output on macOS:**

```text
Python version: 3.11.4 (main, Jul 5 2023, 13:45:01) [Clang 14.0.3]
Python executable: /usr/local/bin/python3
Platform: darwin
```

**Example output on Windows:**

```text
Python version: 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
Python executable: C:\Users\Alice\AppData\Local\Programs\Python\Python311\python.exe
Platform: win32
```

`sys.executable` tells you exactly which Python binary is running. This is useful when you have multiple Python versions installed and want to confirm which one is active.

---

### Exercise 6: REPL Calculations

```python
>>> 15 * 23
345

>>> 100 / 7
14.285714285714286

>>> 100 // 7
14

>>> 2 ** 10
1024

>>> 100 % 7
2
```

The `%` operator returns the remainder after division. `100 % 7 = 2` because `7 * 14 = 98` and `100 - 98 = 2`.

---

### Exercise 7: Editor Run Button

There is no code to verify here. The key thing to confirm:
- The output panel shows `Hello, Python!`
- No error messages appear

If VS Code shows "Python extension not installed," install the Microsoft Python extension from the Extensions panel. It enables the run button, syntax highlighting, and IntelliSense.

---

## Challenge Exercise Solutions

### Challenge 1: Multi-Step Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print(f"Unknown operation: {operation}")
    result = None

if operation in ("+", "-", "*") or (operation == "/" and num2 != 0):
    print(f"{num1} {operation} {num2} = {result}")
```

**Why `float()` instead of `int()`?** Using `float()` lets the calculator handle decimal numbers like `3.5`. If you used `int()`, entering `3.5` would raise a `ValueError`.

**Why check for division by zero?** Dividing by zero raises a `ZeroDivisionError`. It is better to check for it explicitly and print a helpful message than to let the program crash.

A cleaner version separates the logic into a function:

```python
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
    else:
        return f"Unknown operation: {op}"

a = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
b = float(input("Enter second number: "))
print(f"{a} {op} {b} = {calculate(a, b, op)}")
```

---

### Challenge 2: Explore pip and Install a Package

```bash
pip list
```

This shows all installed packages. Common ones you will see even on a fresh install: `pip`, `setuptools`, `wheel`.

```bash
pip install requests
```

After installing, `pip list` should include `requests` and its dependencies (`certifi`, `charset-normalizer`, `idna`, `urllib3`).

```python
import requests

response = requests.get("https://httpbin.org/get")
print(f"Status code: {response.status_code}")
```

A status code of `200` means the request succeeded. If you get a `ConnectionError`, check your internet connection.

**Note:** You will learn more about virtual environments in Chapter 15. For now, installing packages globally is fine for learning.

---

### Challenge 3: Project Folder Structure

There is no code to verify. The goal is to build a habit of organizing your work. A clean folder structure makes it easier to find files and avoids confusion when you have dozens of scripts.

Suggested structure:

```text
python-learning/
    chapter-02/
        hello.py
        greet.py
        check_python.py
        calculator.py
    chapter-03/
    chapter-04/
```

---

### Challenge 4: Virtual Environments (Preview)

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate.bat     # Windows CMD
.venv\Scripts\Activate.ps1     # Windows PowerShell
```

After activation, your prompt changes to show `(.venv)`. Any packages you install now go into `.venv/lib/` instead of the global Python installation.

```bash
deactivate
```

This returns you to the global Python environment.

**Why this matters:** Virtual environments let each project have its own set of packages at specific versions. Without them, installing a package for one project can break another. Chapter 15 covers this in detail.

---

## Common Mistakes

**Using `python` when you need `python3`.** On macOS and Linux, `python` often points to Python 2. Always check with `python --version` first.

**Running scripts from the wrong directory.** If you run `python hello.py` from a different folder, Python cannot find the file. Use `cd` to navigate to the correct folder first, or provide the full path.

**Forgetting to save the file.** Most editors show an unsaved indicator (a dot or asterisk in the tab). Always save before running.

**Mixing tabs and spaces.** Python requires consistent indentation. Configure your editor to insert 4 spaces when you press Tab.

---

## What to Review Next

- Chapter 03: Running Python Programs — command-line arguments, the `__main__` guard, and reading error messages
- Chapter 04: Syntax and Structure — indentation, naming conventions, and code organization
