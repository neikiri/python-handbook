# Chapter 04: Syntax and Structure — Exercises

## Overview

These exercises help you master Python's syntax rules: indentation, naming conventions, comments, docstrings, and code organization. By the end, you will write clean, readable Python code that follows the community's standards.

---

## How to Use These Exercises

- Create a folder called `chapter-04` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program to verify it works.
- Pay attention to indentation, naming, and structure — these are the focus of this chapter.

---

## Warm-up Exercises

### Exercise 1: Fix Indentation Errors

Each of these files has an indentation error. Identify and fix it.

**File 1: `indent_error1.py`**

```python
def greet(name):
print(f"Hello, {name}!")

greet("Alice")
```

**File 2: `indent_error2.py`**

```python
if True:
    print("This is indented.")
  print("This is not indented correctly.")
```

**File 3: `indent_error3.py`**

```python
for i in range(3):
    print(i)
        print("Extra indent here.")
```

For each file:
1. Copy the code into a `.py` file
2. Try to run it — you should get an `IndentationError`
3. Fix the indentation
4. Run it again — it should work

---

### Exercise 2: Understand Naming Conventions

Look at these variable and function names. For each, decide if it follows PEP 8 conventions. If not, rewrite it correctly.

1. `UserName` (should be a variable)
2. `calculate_total_price` (correct? yes/no)
3. `MAX_RETRIES` (should be a variable, not a constant)
4. `myFunction` (should be a function)
5. `total_price` (correct? yes/no)
6. `HTTPServer` (should be a class)
7. `get_user_by_id` (correct? yes/no)
8. `TIMEOUT` (should be a constant)

Write the corrected versions for the ones that are wrong.

---

### Exercise 3: Write Comments and Docstrings

Create a file called `documented.py` with this skeleton:

```python
"""
documented.py

A module that demonstrates comments and docstrings.
"""

def calculate_discount(price, discount_percent):
    # TODO: add docstring
    # TODO: add comments explaining the logic
    discounted = price * (1 - discount_percent / 100)
    return discounted

def apply_tax(price, tax_rate):
    # TODO: add docstring
    # TODO: add comments explaining the logic
    total = price * (1 + tax_rate / 100)
    return total

if __name__ == "__main__":
    original_price = 100
    discounted_price = calculate_discount(original_price, 20)
    final_price = apply_tax(discounted_price, 8)
    print(f"Original: ${original_price}")
    print(f"After 20% discount: ${discounted_price}")
    print(f"After 8% tax: ${final_price}")
```

Now:
1. Add a docstring to each function explaining what it does
2. Add comments explaining the calculation logic
3. Run the file to verify it works

---

## Practice Exercises

### Exercise 4: Follow PEP 8 Conventions

Create a file called `pep8_practice.py` that violates PEP 8 in several ways:

```python
# Bad style — violates PEP 8
x=10
y=20
z=x+y
print(z)

def myFunction(a,b):
    result=a*b
    return result

class myClass:
    def __init__(self,name):
        self.name=name
```

Now rewrite it following PEP 8:

1. Use proper spacing around operators
2. Use `snake_case` for variables and functions
3. Use `PascalCase` for classes
4. Add a module docstring
5. Add docstrings to functions and classes
6. Add comments where helpful

Run both versions to verify they work the same way.

---

### Exercise 5: Use the `pass` Statement

Create a file called `stubs.py` with function and class stubs:

```python
def function_to_implement_later():
    pass

def another_function():
    pass

class MyClass:
    pass

if True:
    pass
else:
    print("This will never run.")
```

Run it. It should work without errors (even though the functions do nothing).

Now implement the functions:

```python
def function_to_implement_later():
    """Return a greeting."""
    return "Hello!"

def another_function():
    """Return the sum of 1 and 2."""
    return 1 + 2

class MyClass:
    """A simple class."""
    def __init__(self):
        self.value = 42

if True:
    print("This runs.")
else:
    print("This will never run.")
```

Run it again. It should now produce output.

---

### Exercise 6: Understand Line Continuation

Create a file called `line_continuation.py`:

```python
# Implicit continuation inside parentheses
result = (
    10 + 20 + 30 +
    40 + 50
)
print(f"Sum: {result}")

# Long list split across lines
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
]
print(f"Colors: {colors}")

# Long condition
if (
    result > 100
    and len(colors) > 3
    and "red" in colors
):
    print("All conditions are true!")

# Long function call
def describe(name, age, city, job):
    return f"{name}, {age}, from {city}, works as {job}"

description = describe(
    name="Alice",
    age=30,
    city="New York",
    job="Engineer",
)
print(description)
```

Run it. All lines should work correctly.

---

### Exercise 7: Practice Naming Conventions in Context

Create a file called `naming_practice.py` that uses all naming conventions correctly:

```python
"""
naming_practice.py

Demonstrates proper naming conventions for variables, functions, classes, and constants.
"""

# Constants in UPPER_CASE
MAX_USERS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# Variables in snake_case
user_count = 0
is_active = True
total_price = 99.99

def calculate_total(items):
    """Calculate the total price of items."""
    return sum(items)

def get_user_by_id(user_id):
    """Retrieve a user by their ID."""
    # Implementation would go here
    pass

class UserAccount:
    """Represents a user account."""
    
    def __init__(self, username, email):
        """Initialize a new user account."""
        self.username = username
        self.email = email
    
    def get_profile(self):
        """Return the user's profile information."""
        return f"{self.username} ({self.email})"

# Private function (by convention)
def _internal_helper():
    """An internal helper function not meant for external use."""
    pass

if __name__ == "__main__":
    account = UserAccount("alice", "alice@example.com")
    print(account.get_profile())
    print(f"Max users: {MAX_USERS}")
    print(f"Default timeout: {DEFAULT_TIMEOUT}s")
```

Run it and verify it works. Notice how the naming conventions make the code immediately readable.

---

## Challenge Exercises

### Challenge 1: Refactor Poorly Written Code

Here is a poorly written program. Refactor it to follow all PEP 8 conventions and best practices:

```python
# bad code
def f(x,y):
    z=x+y
    return z
class C:
    def __init__(self,n):
        self.n=n
    def m(self):
        return self.n*2
x=C(5)
print(f(10,20))
print(x.m())
```

Your refactored version should:
1. Have a module docstring
2. Use proper naming conventions
3. Have docstrings for functions and classes
4. Have proper spacing and indentation
5. Use meaningful variable names
6. Include a `if __name__ == "__main__":` guard

---

### Challenge 2: Write a Well-Documented Module

Create a file called `geometry.py` that calculates properties of shapes. Include:

1. A module docstring explaining what the module does
2. Constants for mathematical values (e.g., `PI`)
3. Functions for calculating area and perimeter of at least two shapes
4. Docstrings for each function
5. Comments explaining any non-obvious logic
6. A `if __name__ == "__main__":` block that tests the functions

Example functions:
- `circle_area(radius)`
- `circle_circumference(radius)`
- `rectangle_area(width, height)`
- `rectangle_perimeter(width, height)`

---

### Challenge 3: Create a Class with Proper Documentation

Create a file called `bank_account.py` with a `BankAccount` class:

```python
"""
bank_account.py

A simple bank account class for learning purposes.
"""

class BankAccount:
    """Represents a bank account with deposit and withdrawal functionality."""
    
    def __init__(self, owner, initial_balance=0):
        """Initialize a bank account."""
        # TODO: implement
        pass
    
    def deposit(self, amount):
        """Add money to the account."""
        # TODO: implement
        pass
    
    def withdraw(self, amount):
        """Remove money from the account."""
        # TODO: implement
        pass
    
    def get_balance(self):
        """Return the current balance."""
        # TODO: implement
        pass

if __name__ == "__main__":
    # TODO: test the class
    pass
```

Now implement the class:
1. Store the owner name and balance
2. Implement each method
3. Add comments explaining the logic
4. Test it in the `if __name__ == "__main__":` block

---

### Challenge 4: Analyze Code Style

Find a Python file online (from a GitHub repository, tutorial, or documentation). Analyze it for:

1. Naming conventions — are they followed?
2. Indentation — is it consistent?
3. Comments and docstrings — are they present and helpful?
4. Line length — are lines too long?
5. Spacing — is there proper spacing around operators?

Write a short report (3–5 paragraphs) analyzing the code style. What does the code do well? What could be improved?

---

## Hints

**IndentationError** → Check that you are using 4 spaces per level, not tabs. Configure your editor to insert spaces when you press Tab.

**NameError with a variable** → Check the spelling and capitalization. Python is case-sensitive.

**SyntaxError with a colon** → Make sure every `if`, `for`, `while`, `def`, and `class` statement ends with a colon.

**Line too long** → Use implicit continuation with parentheses to split long lines.

**Unsure about naming** → Check PEP 8: variables and functions use `snake_case`, classes use `PascalCase`, constants use `UPPER_CASE`.

---

## What to Review If You Get Stuck

- **Indentation** → Handbook section 3.1
- **Naming conventions** → Handbook section 3.7
- **Comments** → Handbook section 3.5
- **Docstrings** → Handbook section 3.6
- **Line continuation** → Handbook section 3.3
- **The `pass` statement** → Handbook section 3.11
- **PEP 8 overview** → Handbook section 3.12

---

## Key Takeaways

After completing these exercises, you should be able to:

- Write code with correct indentation
- Follow PEP 8 naming conventions
- Write clear comments and docstrings
- Use line continuation for long lines
- Organize code in a readable, professional way
- Understand why code style matters
