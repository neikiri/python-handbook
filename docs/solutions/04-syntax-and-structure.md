# Solutions 04: Syntax and Structure

## Overview

Chapter 04 exercises focus on Python's syntax rules: indentation, naming conventions, comments, docstrings, and code organization. This solution guide shows corrected code and explains the reasoning behind each convention.

---

## Notes Before Checking Solutions

Syntax and style are not just about following rules — they are about making code readable for the next person (often yourself, six months later). The solutions below follow PEP 8, Python's official style guide. When in doubt, PEP 8 is the reference.

---

## Warm-up Exercise Solutions

### Exercise 1: Fix Indentation Errors

**File 1 — missing indentation in function body:**

```python
# Broken
def greet(name):
print(f"Hello, {name}!")

# Fixed
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

The function body must be indented by 4 spaces. Python uses indentation to define blocks — there are no curly braces.

**File 2 — inconsistent indentation:**

```python
# Broken
if True:
    print("This is indented.")
  print("This is not indented correctly.")

# Fixed
if True:
    print("This is indented.")
    print("This is also indented correctly.")
```

Both `print` calls are inside the `if` block, so both must be at the same indentation level (4 spaces).

**File 3 — over-indented line:**

```python
# Broken
for i in range(3):
    print(i)
        print("Extra indent here.")

# Fixed
for i in range(3):
    print(i)
    print("This is at the correct level.")
```

The second `print` was indented 8 spaces, which Python interprets as a nested block — but there is no statement that opens a new block before it. Both lines belong to the `for` loop body, so both get 4 spaces.

---

### Exercise 2: Naming Conventions

| Name | Context | Correct? | Fixed version |
|---|---|---|---|
| `UserName` | variable | No | `user_name` |
| `calculate_total_price` | function | Yes | — |
| `MAX_RETRIES` | variable (not constant) | No | `max_retries` |
| `myFunction` | function | No | `my_function` |
| `total_price` | variable | Yes | — |
| `HTTPServer` | class | Yes | — |
| `get_user_by_id` | function | Yes | — |
| `TIMEOUT` | constant | Yes | — |

**Rules:**
- Variables and functions: `snake_case` (all lowercase, words separated by underscores)
- Classes: `PascalCase` (each word capitalized, no underscores)
- Constants: `UPPER_CASE` (all uppercase, words separated by underscores)

`HTTPServer` is correct for a class — acronyms in class names keep all letters uppercase.

---

### Exercise 3: Write Comments and Docstrings

```python
"""
documented.py

A module that demonstrates comments and docstrings.
"""


def calculate_discount(price, discount_percent):
    """
    Return the discounted price after applying a percentage discount.

    Args:
        price: The original price.
        discount_percent: The discount as a percentage (e.g., 20 for 20%).

    Returns:
        The price after the discount is applied.
    """
    # Convert the percentage to a decimal and subtract from 1
    # e.g., 20% discount means we keep 80% of the price
    discounted = price * (1 - discount_percent / 100)
    return discounted


def apply_tax(price, tax_rate):
    """
    Return the price after adding a tax.

    Args:
        price: The pre-tax price.
        tax_rate: The tax rate as a percentage (e.g., 8 for 8%).

    Returns:
        The price including tax.
    """
    # Convert the percentage to a decimal and add to 1
    # e.g., 8% tax means we multiply by 1.08
    total = price * (1 + tax_rate / 100)
    return total


if __name__ == "__main__":
    original_price = 100
    discounted_price = calculate_discount(original_price, 20)
    final_price = apply_tax(discounted_price, 8)
    print(f"Original: ${original_price}")
    print(f"After 20% discount: ${discounted_price}")
    print(f"After 8% tax: ${final_price:.2f}")
```

**Docstring format:** The first line is a short summary. A blank line separates it from the longer description. `Args:` and `Returns:` sections document parameters and return values. This format is compatible with tools like Sphinx and VS Code's hover documentation.

---

## Practice Exercise Solutions

### Exercise 4: Follow PEP 8 Conventions

**Before (bad style):**

```python
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

**After (PEP 8 compliant):**

```python
"""
pep8_practice.py

Demonstrates PEP 8 style conventions.
"""


def multiply(a, b):
    """Return the product of a and b."""
    result = a * b
    return result


class MyClass:
    """A simple example class."""

    def __init__(self, name):
        """Initialize with a name."""
        self.name = name


if __name__ == "__main__":
    x = 10
    y = 20
    z = x + y
    print(z)

    obj = MyClass("example")
    print(multiply(x, y))
```

**Changes made:**
- Spaces around operators: `x = 10`, not `x=10`
- Spaces after commas: `def multiply(a, b)`, not `def multiply(a,b)`
- `snake_case` for function: `multiply`, not `myFunction`
- `PascalCase` for class: `MyClass`, not `myClass`
- Two blank lines between top-level definitions
- Docstrings added
- Module docstring added
- Script code moved inside `if __name__ == "__main__":`

---

### Exercise 5: Use the `pass` Statement

```python
def function_to_implement_later():
    pass

def another_function():
    pass

class MyClass:
    pass
```

`pass` is a no-op — it does nothing. It exists because Python requires at least one statement in every block. Without `pass`, an empty function body would be a syntax error.

**After implementing:**

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
```

`pass` is also useful as a placeholder when you are sketching out a program's structure before filling in the details.

---

### Exercise 6: Understand Line Continuation

```python
# Implicit continuation inside parentheses
result = (
    10 + 20 + 30 +
    40 + 50
)
print(f"Sum: {result}")  # 150
```

Python allows a statement to span multiple lines when it is inside parentheses `()`, brackets `[]`, or braces `{}`. This is called *implicit line continuation* and is the preferred approach.

The alternative is an explicit backslash `\` at the end of a line, but this is fragile (a trailing space after `\` breaks it) and less readable. Prefer parentheses.

```python
# Long condition — use parentheses, not backslash
if (
    result > 100
    and len(colors) > 3
    and "red" in colors
):
    print("All conditions are true!")
```

PEP 8 recommends putting the operator at the *start* of the continuation line (as shown above), not at the end. This makes it easier to see which operator connects which operands.

---

### Exercise 7: Naming Conventions in Context

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
    pass  # Implementation would go here


class UserAccount:
    """Represents a user account."""

    def __init__(self, username, email):
        """Initialize a new user account."""
        self.username = username
        self.email = email

    def get_profile(self):
        """Return the user's profile information."""
        return f"{self.username} ({self.email})"


def _internal_helper():
    """An internal helper function not meant for external use."""
    pass


if __name__ == "__main__":
    account = UserAccount("alice", "alice@example.com")
    print(account.get_profile())
    print(f"Max users: {MAX_USERS}")
    print(f"Default timeout: {DEFAULT_TIMEOUT}s")
```

The leading underscore in `_internal_helper` is a convention, not a language rule. It signals to other developers: "this is an implementation detail, do not use it from outside this module."

---

## Challenge Exercise Solutions

### Challenge 1: Refactor Poorly Written Code

**Before:**

```python
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

**After:**

```python
"""
refactored.py

A refactored version of a poorly written program.
Demonstrates PEP 8 conventions and best practices.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


class Counter:
    """A simple counter that can double its value."""

    def __init__(self, initial_value):
        """Initialize the counter with a starting value."""
        self.value = initial_value

    def doubled(self):
        """Return the counter's value multiplied by two."""
        return self.value * 2


if __name__ == "__main__":
    counter = Counter(5)
    print(add(10, 20))
    print(counter.doubled())
```

**What changed:**
- `f` → `add` (meaningful name)
- `C` → `Counter` (meaningful name, PascalCase)
- `n` → `initial_value` / `value` (meaningful names)
- `m` → `doubled` (meaningful name)
- Spaces around operators and after commas
- Docstrings added to everything
- Module docstring added
- Script code moved inside `if __name__ == "__main__":`

---

### Challenge 2: Well-Documented Geometry Module

```python
"""
geometry.py

Functions for calculating properties of common geometric shapes.
All measurements are in the same unit (e.g., all in centimeters).
"""

import math

# Mathematical constants
PI = math.pi


def circle_area(radius):
    """
    Return the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area as a float.
    """
    return PI * radius ** 2


def circle_circumference(radius):
    """
    Return the circumference of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The circumference as a float.
    """
    return 2 * PI * radius


def rectangle_area(width, height):
    """
    Return the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area as a float.
    """
    return width * height


def rectangle_perimeter(width, height):
    """
    Return the perimeter of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The perimeter as a float.
    """
    return 2 * (width + height)


if __name__ == "__main__":
    # Test circle functions
    r = 5
    print(f"Circle (radius={r}):")
    print(f"  Area: {circle_area(r):.2f}")
    print(f"  Circumference: {circle_circumference(r):.2f}")

    # Test rectangle functions
    w, h = 4, 6
    print(f"\nRectangle ({w}x{h}):")
    print(f"  Area: {rectangle_area(w, h)}")
    print(f"  Perimeter: {rectangle_perimeter(w, h)}")
```

---

### Challenge 3: BankAccount Class

```python
"""
bank_account.py

A simple bank account class for learning purposes.
"""


class BankAccount:
    """Represents a bank account with deposit and withdrawal functionality."""

    def __init__(self, owner, initial_balance=0):
        """
        Initialize a bank account.

        Args:
            owner: The name of the account owner.
            initial_balance: The starting balance (default 0).
        """
        self.owner = owner
        # Store balance as a float to handle decimal amounts
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """
        Add money to the account.

        Args:
            amount: The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Remove money from the account.

        Args:
            amount: The amount to withdraw. Must be positive and not exceed balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Balance: ${self.balance:.2f}")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """Return the current balance."""
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    print(f"Owner: {account.owner}")
    print(f"Balance: ${account.get_balance():.2f}")

    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)  # Should fail
    print(f"Final balance: ${account.get_balance():.2f}")
```

---

## Common Mistakes

**Using tabs instead of spaces.** Python allows tabs, but mixing tabs and spaces causes `TabError`. Configure your editor to insert 4 spaces when you press Tab.

**Forgetting two blank lines between top-level definitions.** PEP 8 requires two blank lines before and after each function and class at the module level. Inside a class, use one blank line between methods.

**Writing docstrings as regular comments.** A docstring is a string literal as the first statement in a function, class, or module. It must use quotes, not `#`. Tools like `help()` and IDEs read docstrings; they cannot read comments.

**Over-commenting obvious code.** `x = x + 1  # add 1 to x` is not a useful comment. Comments should explain *why*, not *what*. The code already shows what.

---

## What to Review Next

- Chapter 05: Values, Variables, and Types — how Python stores data
- Chapter 06: Operators, Expressions, and Input — arithmetic, comparisons, and user input
- PEP 8 (online) — the full style guide: https://peps.python.org/pep-0008/
