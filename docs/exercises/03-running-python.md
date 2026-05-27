# Chapter 03: Running Python Programs — Exercises

## Overview

These exercises help you understand how Python runs your code, the different ways to execute Python, and how to read error messages. By the end, you will be comfortable running programs in multiple ways and debugging basic errors.

---

## How to Use These Exercises

- Create a folder called `chapter-03` in your `python-learning` directory.
- Write each program in a separate `.py` file in that folder.
- Run each program from the terminal using `python filename.py`.
- If you get an error, read it carefully and try to understand what went wrong.

---

## Warm-up Exercises

### Exercise 1: Run a Simple Script

Create a file called `simple.py`:

```python
print("Python is running!")
print("This is line 2.")
print("This is line 3.")
```

Run it:

```bash
python simple.py
```

**Expected output:**

```text
Python is running!
This is line 2.
This is line 3.
```

---

### Exercise 2: Understand Script Arguments with `sys.argv`

Create a file called `show_args.py`:

```python
import sys

print(f"Script name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")
print(f"Number of arguments: {len(sys.argv) - 1}")
```

Run it with different arguments:

```bash
python show_args.py
python show_args.py hello
python show_args.py hello world
python show_args.py one two three
```

Write down what `sys.argv` contains in each case.

**Expected behavior:** `sys.argv[0]` is always the script name. Additional arguments appear at indices 1, 2, 3, etc.

---

### Exercise 3: Use Command-Line Arguments

Create a file called `greet_arg.py`:

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python greet_arg.py <name>")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}!")
```

Run it:

```bash
python greet_arg.py Alice
python greet_arg.py Bob
python greet_arg.py
```

**Expected behavior:** When you provide a name, it greets you. When you do not, it shows a usage message.

---

## Practice Exercises

### Exercise 4: Understand the `if __name__ == "__main__":` Guard

Create a file called `math_utils.py`:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

if __name__ == "__main__":
    print("Testing math_utils:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
```

Run it:

```bash
python math_utils.py
```

**Expected output:**

```text
Testing math_utils:
add(5, 3) = 8
multiply(5, 3) = 15
```

Now create a file called `use_math_utils.py`:

```python
from math_utils import add, multiply

result1 = add(10, 20)
result2 = multiply(10, 20)

print(f"add(10, 20) = {result1}")
print(f"multiply(10, 20) = {result2}")
```

Run it:

```bash
python use_math_utils.py
```

**Expected output:**

```text
add(10, 20) = 30
multiply(10, 20) = 200
```

Notice that the test code in `math_utils.py` did not run when you imported it. That is what the `if __name__ == "__main__":` guard does.

---

### Exercise 5: Read and Understand Error Messages

Create a file called `errors.py` with this intentional error:

```python
x = 10
y = 0
result = x / y
print(result)
```

Run it:

```bash
python errors.py
```

**Expected output:** A traceback showing a `ZeroDivisionError`.

Read the error message carefully and answer:

1. What type of error occurred?
2. On which line did the error occur?
3. What was Python trying to do when the error happened?

Now fix the error by checking if `y` is zero before dividing:

```python
x = 10
y = 0

if y == 0:
    print("Cannot divide by zero!")
else:
    result = x / y
    print(result)
```

Run it again. It should work without errors.

---

### Exercise 6: Use `print()` for Debugging

Create a file called `debug_example.py`:

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

Run it:

```bash
python debug_example.py
```

**Expected output:** You see the debug output showing what happens at each step, plus the final result.

---

### Exercise 7: Understand Syntax Errors

Create a file called `syntax_error.py` with this intentional error:

```python
def greet(name)
    print(f"Hello, {name}!")
```

Run it:

```bash
python syntax_error.py
```

**Expected output:** A `SyntaxError` pointing to the missing colon.

Fix it by adding the colon:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

Run it again. It should work.

---

## Challenge Exercises

### Challenge 1: Write a Script That Takes Multiple Arguments

Create a file called `add_numbers.py` that:

1. Takes any number of arguments from the command line
2. Converts each to a number
3. Adds them all together
4. Prints the result

Example run:

```bash
python add_numbers.py 10 20 30
```

**Expected output:**

```text
10 + 20 + 30 = 60
```

**Hint:** Use a loop to iterate over `sys.argv[1:]` and convert each to `int()` or `float()`.

---

### Challenge 2: Create a Module and Use It

Create a file called `string_utils.py`:

```python
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

Run it to test:

```bash
python string_utils.py
```

Now create a file called `use_string_utils.py`:

```python
from string_utils import reverse_string, count_vowels

text = "Programming is fun!"
print(f"Text: {text}")
print(f"Reversed: {reverse_string(text)}")
print(f"Vowel count: {count_vowels(text)}")
```

Run it:

```bash
python use_string_utils.py
```

---

### Challenge 3: Handle Errors Gracefully

Create a file called `safe_divide.py`:

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

Test it with different inputs:

```bash
python safe_divide.py 10 2
python safe_divide.py 10 0
python safe_divide.py hello 2
python safe_divide.py 10
```

**Expected behavior:** It handles all error cases gracefully and prints helpful messages.

---

### Challenge 4: Create a Main Function

Refactor one of your earlier programs to use a `main()` function. For example, refactor `add_numbers.py`:

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

Run it:

```bash
python add_numbers.py 5 10 15 20
```

---

## Hints

**"ModuleNotFoundError: No module named..."** → Make sure the module file is in the same folder as the script that imports it.

**"SyntaxError: invalid syntax"** → Check for missing colons, unmatched parentheses, or incorrect indentation.

**"NameError: name '...' is not defined"** → You used a variable or function that does not exist. Check the spelling.

**"TypeError: unsupported operand type(s)"** → You tried to use an operator with incompatible types (e.g., adding a string and a number).

**"IndexError: list index out of range"** → You tried to access an index that does not exist in a list or `sys.argv`.

---

## What to Review If You Get Stuck

- **How Python runs code** → Handbook section 3.1
- **The REPL** → Handbook section 3.3
- **Running script files** → Handbook section 3.4
- **Command-line arguments** → Handbook section 3.5
- **The `if __name__ == "__main__":` guard** → Handbook section 3.6
- **Reading error messages** → Handbook section 3.9
- **Using `print()` for debugging** → Handbook section 3.10

---

## Key Takeaways

After completing these exercises, you should be able to:

- Run Python scripts from the terminal
- Pass command-line arguments to scripts
- Understand and use the `if __name__ == "__main__":` guard
- Read and interpret error messages
- Use `print()` for debugging
- Create modules and import functions from them
- Handle errors gracefully with try/except
