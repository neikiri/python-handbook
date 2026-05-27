# Solutions 03: Running Python Programs

## Overview

Chapter 03 exercises focus on running scripts, using command-line arguments, understanding the `if __name__ == "__main__":` guard, and reading error messages. This solution guide walks through each exercise with explanations.

---

## Notes Before Checking Solutions

Many of these exercises are about *observing* behavior rather than producing a specific output. The goal is to understand how Python executes code, not just to make something print. Read the explanations carefully — they explain the *why*, not just the *what*.

---

## Warm-up Exercise Solutions

### Exercise 1: Run a Simple Script

```python
print("Python is running!")
print("This is line 2.")
print("This is line 3.")
```

**Expected output:**

```text
Python is running!
This is line 2.
This is line 3.
```

Python executes statements from top to bottom, one at a time. Each `print()` call outputs a line and moves to the next.

---

### Exercise 2: Understand `sys.argv`

```python
import sys

print(f"Script name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")
print(f"Number of arguments: {len(sys.argv) - 1}")
```

**Running with different arguments:**

```bash
python show_args.py
# sys.argv = ['show_args.py']
# Number of arguments: 0

python show_args.py hello
# sys.argv = ['show_args.py', 'hello']
# Number of arguments: 1

python show_args.py hello world
# sys.argv = ['show_args.py', 'hello', 'world']
# Number of arguments: 2
```

`sys.argv` is always a list of strings. `sys.argv[0]` is always the script name. Additional arguments start at index 1. Everything is a string — if you pass `42`, you get the string `"42"`, not the integer `42`.

---

### Exercise 3: Use Command-Line Arguments

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python greet_arg.py <name>")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}!")
```

**Why `sys.exit(1)`?** By convention, a program exits with code `0` on success and a non-zero code on failure. `sys.exit(1)` signals to the shell that something went wrong. This matters when scripts are called from other scripts or CI pipelines.

---

## Practice Exercise Solutions

### Exercise 4: The `if __name__ == "__main__":` Guard

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    print("Testing math_utils:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
```

**Why this guard exists:**

When Python imports a module, it executes all the code in that file. Without the guard, importing `math_utils` would run the test code — printing output you did not ask for.

The special variable `__name__` is set to `"__main__"` when the file is run directly, and to the module name (e.g., `"math_utils"`) when it is imported. The guard checks which case applies.

```python
# use_math_utils.py
from math_utils import add, multiply

result1 = add(10, 20)
result2 = multiply(10, 20)

print(f"add(10, 20) = {result1}")
print(f"multiply(10, 20) = {result2}")
```

Running `use_math_utils.py` imports `math_utils` but does not trigger the test code. Only the two function calls produce output.

**Rule of thumb:** Always put script-level code (anything that runs when the file is executed) inside `if __name__ == "__main__":`. This makes your files safe to import.

---

### Exercise 5: Read and Understand Error Messages

**The broken code:**

```python
x = 10
y = 0
result = x / y
print(result)
```

**The error:**

```text
Traceback (most recent call last):
  File "errors.py", line 3, in <module>
    result = x / y
ZeroDivisionError: division by zero
```

Reading a traceback:
1. **"Traceback (most recent call last)"** — Python is about to show you the call stack.
2. **File and line number** — `errors.py`, line 3. Go to that line.
3. **The offending code** — `result = x / y`. This is what Python was executing.
4. **The error type and message** — `ZeroDivisionError: division by zero`. This tells you exactly what went wrong.

**The fix:**

```python
x = 10
y = 0

if y == 0:
    print("Cannot divide by zero!")
else:
    result = x / y
    print(result)
```

Always check for division by zero before dividing when the denominator comes from user input or external data.

---

### Exercise 6: Use `print()` for Debugging

```python
def calculate_average(numbers):
    print(f"[debug] numbers received: {numbers}")
    
    total = sum(numbers)
    print(f"[debug] total: {total}")
    
    count = len(numbers)
    print(f"[debug] count: {count}")
    
    average = total / count
    print(f"[debug] average: {average}")
    
    return average

result = calculate_average([10, 20, 30, 40])
print(f"Final result: {result}")
```

**Expected output:**

```text
[debug] numbers received: [10, 20, 30, 40]
[debug] total: 100
[debug] count: 4
[debug] average: 25.0
Final result: 25.0
```

The `[debug]` prefix makes it easy to find and remove debug prints later. This technique is simple and effective for beginners. As you advance, you will learn about the `logging` module, which is more powerful for production code.

---

### Exercise 7: Understand Syntax Errors

**The broken code:**

```python
def greet(name)
    print(f"Hello, {name}!")
```

**The error:**

```text
  File "syntax_error.py", line 1
    def greet(name)
                   ^
SyntaxError: expected ':'
```

Python detected the error at the end of line 1 — the colon is missing after the function signature. Python cannot even start running the file; it fails during parsing.

**The fix:**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

Every `def`, `if`, `for`, `while`, `class`, and `with` statement must end with a colon.

---

## Challenge Exercise Solutions

### Challenge 1: Script That Takes Multiple Arguments

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python add_numbers.py <num1> <num2> ...")
    sys.exit(1)

# sys.argv[1:] skips the script name
numbers = [float(arg) for arg in sys.argv[1:]]

# Build a readable expression string
expression = " + ".join(sys.argv[1:])
total = sum(numbers)

print(f"{expression} = {total}")
```

**How it works:**
- `sys.argv[1:]` is a slice that skips the first element (the script name).
- The list comprehension `[float(arg) for arg in sys.argv[1:]]` converts each string argument to a float.
- `sum()` adds them all up.

**Running it:**

```bash
python add_numbers.py 10 20 30
# 10 + 20 + 30 = 60.0
```

---

### Challenge 2: Create a Module and Use It

```python
# string_utils.py
def reverse_string(s):
    """Return the string reversed."""
    return s[::-1]

def count_vowels(s):
    """Return the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    test_string = "Hello, Python!"
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Vowels: {count_vowels(test_string)}")
```

**Why `s[::-1]` reverses a string:** Slicing with a step of `-1` reads the string from the end to the beginning. It is a common Python idiom.

**Why `sum(1 for char in s if char in vowels)`:** This is a generator expression. For each character in `s`, if it is a vowel, it contributes `1` to the sum. It is equivalent to a loop that counts matching characters.

```python
# use_string_utils.py
from string_utils import reverse_string, count_vowels

text = "Programming is fun!"
print(f"Text: {text}")
print(f"Reversed: {reverse_string(text)}")
print(f"Vowel count: {count_vowels(text)}")
```

Notice that importing `string_utils` does not print anything — the `if __name__ == "__main__":` guard prevents the test code from running.

---

### Challenge 3: Handle Errors Gracefully

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python safe_divide.py <numerator> <denominator>")
    sys.exit(1)

try:
    numerator = float(sys.argv[1])
    denominator = float(sys.argv[2])
    result = numerator / denominator
    print(f"{numerator} / {denominator} = {result}")
except ValueError:
    print("Error: Both arguments must be numbers.")
    sys.exit(1)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)
```

**Why separate `except` clauses?** Each error type has a different cause and a different message. Catching them separately lets you give the user a precise explanation. Catching everything with a bare `except:` hides the cause and makes debugging harder.

**Test cases:**

```bash
python safe_divide.py 10 2      # 10.0 / 2.0 = 5.0
python safe_divide.py 10 0      # Error: Cannot divide by zero.
python safe_divide.py hello 2   # Error: Both arguments must be numbers.
python safe_divide.py 10        # Usage message
```

---

### Challenge 4: Create a Main Function

```python
import sys

def add_numbers(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_numbers.py <num1> <num2> ...")
        sys.exit(1)
    
    numbers = [float(arg) for arg in sys.argv[1:]]
    result = add_numbers(numbers)
    print(f"Sum: {result}")

if __name__ == "__main__":
    main()
```

**Why use a `main()` function?** It keeps the top-level logic in one place, makes the code easier to test (you can call `main()` from a test), and avoids polluting the module namespace with variables that only belong to the script's entry point.

This pattern — a `main()` function called from `if __name__ == "__main__":` — is the standard way to structure Python scripts.

---

## Common Mistakes

**Forgetting that `sys.argv` contains strings.** If you pass `10` as an argument, `sys.argv[1]` is `"10"`, not `10`. Always convert with `int()` or `float()` before doing arithmetic.

**Checking `len(sys.argv) == 2` when you want at least one argument.** Use `len(sys.argv) < 2` to check that at least one argument was provided.

**Putting code outside `if __name__ == "__main__":`.** Any code at the module level runs when the file is imported. Keep side effects (printing, file I/O, network calls) inside the guard.

**Ignoring the traceback.** The traceback tells you exactly where the error occurred and what type it is. Read it from the bottom up — the last line is the error, the lines above show the call chain.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 04 - Syntax and Structure](../handbook/04-syntax-and-structure.md)
