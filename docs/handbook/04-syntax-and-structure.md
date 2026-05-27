# Chapter 04: Syntax and Structure

## 1. Overview

Every programming language has rules about how code must be written. These rules
are called **syntax**. Python's syntax is built around one core idea: code should
be easy to read. Guido van Rossum, Python's creator, captured this in the
language's design philosophy — "readability counts." That principle shapes every
aspect of how Python code looks and how it is organized.

Unlike languages that use curly braces `{}` to group blocks of code, Python uses
**indentation** — the whitespace at the start of a line. This forces a consistent
visual structure on every Python program. A well-written Python file looks almost
like structured English prose.

This chapter covers the foundational rules of Python syntax: how indentation
works, how to write comments and docstrings, how to name things, how to continue
long lines, and how Python reads and executes your program from top to bottom.
These rules apply to every Python file you will ever write, so getting them right
from the start matters.

---

## 2. What You Will Learn

- Why Python uses indentation instead of braces, and exactly how it works
- The difference between statements and expressions
- How to continue a long line across multiple lines (implicit and explicit)
- How colons and indentation define code blocks in `if`, `for`, `def`, `class`, etc.
- How to write single-line comments with `#`
- The convention for multi-line comments using multiple `#` lines
- What docstrings are, how to write them, and when to use them
- Naming conventions from PEP 8: `snake_case`, `PascalCase`, `UPPER_CASE`
- Python's reserved keywords and why you cannot use them as names
- Why Python is case-sensitive and what that means in practice
- Blank line and whitespace conventions
- The `pass` statement and when it is needed
- An overview of PEP 8 — the essentials you need right now

---

## 3. Core Concepts

### 3.1 Indentation-Based Block Structure

In Python, **indentation defines code blocks**. A code block is a group of
statements that belong together — the body of a function, the body of an `if`
statement, the body of a loop, and so on.

The standard is **4 spaces per indentation level**. This is specified in PEP 8,
Python's official style guide, and followed by virtually all Python code you will
encounter.

```python
if True:
    print("This line is indented 4 spaces.")
    print("So is this one. They are in the same block.")

print("This line is back at the top level.")
```

You can nest blocks inside blocks. Each level adds another 4 spaces:

```python
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")
```

#### Why indentation instead of braces?

Most languages use curly braces to mark the start and end of a block:

```text
// JavaScript
if (x > 0) {
    console.log("positive");
}
```

Python's designers made a deliberate choice: if indentation is required anyway
for readability, why not make it the actual syntax? The result is that Python
code cannot be written in a visually inconsistent way — the structure you see
is the structure Python enforces.

#### Tabs vs. spaces

Python 3 does **not** allow you to mix tabs and spaces for indentation. If you
do, Python raises a `TabError`:

```text
TabError: inconsistent use of tabs and spaces in indentation
```

The rule is simple: **always use spaces, never tabs.** Configure your editor to
insert 4 spaces when you press the Tab key. Every major editor (VS Code,
PyCharm, Sublime Text) supports this setting.

#### IndentationError

If your indentation is wrong — missing where required, or present where not
expected — Python raises an `IndentationError` before your program even runs.

```python
# WRONG — missing indentation
def add(a, b):
return a + b
```

```text
IndentationError: expected an indented block after function definition on line 1
```

```python
# CORRECT
def add(a, b):
    return a + b
```

An unexpected indent also causes an error:

```python
# WRONG — unexpected indent
x = 10
    y = 20
```

```text
IndentationError: unexpected indent
```

Python sees the indented `y = 20` and expects it to be inside a block, but
there is no block header above it.

---

### 3.2 Statements and Expressions

Understanding the difference between a **statement** and an **expression** helps
you read Python error messages and understand how code is structured.

An **expression** is any piece of code that produces a value:

```python
2 + 3          # evaluates to 5
len("hello")   # evaluates to 5
x > 0          # evaluates to True or False
"hello"        # evaluates to the string "hello"
```

A **statement** is an instruction that performs an action:

```python
x = 10             # assignment statement
print("hello")     # expression statement (a function call used as a statement)
if x > 0:          # compound statement — has a header and a body
    print("positive")
return x           # return statement (only valid inside a function)
```

Some things are both. A function call like `print("hello")` is an expression
(it returns `None`) used as a statement. Python allows any expression to stand
alone as a statement — the result is simply discarded.

In practice, you do not need to memorize this distinction to write Python. It
becomes useful when reading documentation or error messages that say "expression
expected" or "statement not allowed here."

---

### 3.3 Line Continuation

Python normally treats each physical line as one logical line. But sometimes a
single logical statement is too long to fit on one line. Python gives you two
ways to continue a statement across multiple lines.

#### Implicit continuation (preferred)

Any expression inside **parentheses `()`**, **square brackets `[]`**, or
**curly braces `{}`** can span multiple lines without any special character.
Python knows the expression is not finished until the closing bracket:

```python
# Long function call — split across lines inside parentheses
result = some_function(
    argument_one,
    argument_two,
    argument_three,
)

# Long list — split across lines inside square brackets
colors = [
    "red",
    "green",
    "blue",
    "yellow",
]

# Long dictionary — split across lines inside curly braces
config = {
    "host": "localhost",
    "port": 5432,
    "database": "mydb",
}

# Long condition — wrap the whole thing in parentheses
if (
    user_is_logged_in
    and user_has_permission
    and not account_is_suspended
):
    grant_access()
```

This is the preferred style. It is clean, readable, and requires no special
syntax beyond the brackets you would write anyway.

#### Explicit continuation (backslash)

You can also use a backslash `\` at the end of a line to tell Python the
statement continues on the next line:

```python
total = first_value + second_value + \
        third_value + fourth_value
```

This works, but it is fragile. If there is any whitespace after the backslash —
even a single space — Python raises a `SyntaxError`. Prefer implicit
continuation with parentheses whenever possible.

---

### 3.4 Colons and Code Blocks

In Python, a **code block** is introduced by a line that ends with a colon `:`
followed by one or more indented lines. The block ends when the indentation
returns to the previous level.

This pattern appears everywhere:

```python
# if / elif / else
if condition:
    do_something()
elif other_condition:
    do_something_else()
else:
    fallback()

# for loop
for item in collection:
    process(item)

# while loop
while condition:
    update()

# function definition
def my_function(x):
    return x * 2

# class definition
class MyClass:
    def method(self):
        pass

# with statement
with open("file.txt") as f:
    data = f.read()

# try / except
try:
    risky_operation()
except ValueError:
    handle_error()
```

Every one of these follows the same pattern: **header line ending in `:`, then
indented body**. Once you recognize this pattern, Python's structure becomes
very predictable. Forgetting the colon is one of the most common beginner
mistakes — Python will tell you immediately with a `SyntaxError`.

---

### 3.5 Comments

A **comment** is text in your source code that Python ignores completely.
Comments are for human readers — you, your teammates, or your future self.

#### Single-line comments

Use the `#` character to start a comment. Everything from `#` to the end of
the line is ignored:

```python
# This is a full-line comment.
x = 10  # This is an inline comment.

# Explain why, not just what:
# We add 1 here because the API uses 1-based indexing.
page_number = current_page + 1
```

Good comments explain **why** something is done, not **what** the code does.
The code itself shows what it does. Comments add context that the code cannot
express on its own.

#### Multi-line comments (convention)

Python has no dedicated multi-line comment syntax like `/* ... */` in C or
Java. To write a block of comments, use multiple `#` lines:

```python
# This function calculates compound interest.
# Formula: A = P * (1 + r/n) ** (n * t)
# Where:
#   P = principal amount
#   r = annual interest rate (as a decimal)
#   n = number of times interest compounds per year
#   t = time in years
def compound_interest(principal, rate, n, t):
    return principal * (1 + rate / n) ** (n * t)
```

You will sometimes see triple-quoted strings used as block comments, but that
is not their intended purpose. Their intended purpose is docstrings, covered
next.

---

### 3.6 Docstrings

A **docstring** is a string literal that appears as the **first statement** in
a module, function, class, or method. It documents what that thing does. Python
stores it in the object's `__doc__` attribute, and tools like `help()`, IDEs,
and documentation generators can read it automatically.

#### Syntax

Docstrings use triple quotes — either `"""..."""` or `'''...'''`. The
convention is `"""..."""`:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

For longer docstrings, the first line is a short summary, followed by a blank
line, then more detail:

```python
def divide(a, b):
    """
    Divide a by b and return the result.

    Raises ZeroDivisionError if b is zero.
    """
    return a / b
```

#### Where docstrings go

**Module docstring** — at the very top of a `.py` file, before any imports:

```python
"""
utilities.py

Helper functions for string processing.
"""

import re
```

**Function docstring** — immediately after the `def` line:

```python
def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"
```

**Class docstring** — immediately after the `class` line:

```python
class Rectangle:
    """A rectangle defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
```

**Method docstring** — immediately after the `def` line inside a class:

```python
class Rectangle:
    """A rectangle defined by width and height."""

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height
```

#### Accessing docstrings

Python stores the docstring in the `__doc__` attribute:

```python
def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"

print(greet.__doc__)
# Return a greeting string for the given name.
```

You can also use the built-in `help()` function:

```python
help(greet)
```

```text
Help on function greet in module __main__:

greet(name)
    Return a greeting string for the given name.
```

Write docstrings for every public function, class, and module. They are one of
the most useful habits you can build as a Python programmer.

---

### 3.7 Naming Conventions (PEP 8)

Names in Python — for variables, functions, classes, constants, and modules —
follow conventions defined in **PEP 8**. These are not enforced by the language
itself, but they are followed by virtually all Python code you will encounter.
Sticking to them makes your code immediately readable to other Python
programmers.

#### Variables and functions: `snake_case`

Use lowercase letters with words separated by underscores:

```python
user_name = "Alice"
total_price = 49.99
item_count = 0

def calculate_tax(price, rate):
    return price * rate

def get_user_by_id(user_id):
    pass
```

#### Classes: `PascalCase`

Each word starts with a capital letter, no underscores:

```python
class ShoppingCart:
    pass

class HttpRequestHandler:
    pass

class UserProfile:
    pass
```

#### Constants: `UPPER_CASE`

Constants are values that are not meant to change. Python does not enforce
immutability for constants — it is purely a naming convention that signals
intent:

```python
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
PI = 3.14159265358979
BASE_URL = "https://api.example.com"
```

#### Private names: leading underscore `_name`

A single leading underscore signals that a name is intended for internal use.
It is a convention, not a language restriction:

```python
_internal_counter = 0

def _helper_function():
    pass
```

#### Dunder names: `__name__`

Names with double leading and trailing underscores are called **dunder** names.
They are reserved for Python's internal use — special methods, special
attributes, and built-in hooks. Do not invent your own `__dunder__` names:

```python
__init__   # constructor method
__str__    # string representation
__doc__    # docstring
__name__   # module name
```

---

### 3.8 Keywords and Reserved Words

Some names are reserved by Python and cannot be used as variable names, function
names, or any other identifier. Trying to use them raises a `SyntaxError`:

```python
# WRONG — these all cause SyntaxError:
# class = "math"
# for = 10
# if = True
# return = "value"
```

To see the full list of reserved keywords:

```python
import keyword
print(keyword.kwlist)
```

```text
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
 'while', 'with', 'yield']
```

You can check whether a specific string is a keyword:

```python
import keyword

print(keyword.iskeyword("for"))    # True
print(keyword.iskeyword("total"))  # False
print(keyword.iskeyword("match"))  # False — match is a soft keyword
```

Note that `match` and `type` are **soft keywords** in Python 3.10+. They have
special meaning in specific contexts (like `match` statements) but can still be
used as variable names. The `keyword` module also has `keyword.softkwlist` for
these.

Beyond reserved keywords, Python also has **built-in names** like `list`,
`type`, `input`, `print`, `len`, and `id`. These are not keywords — Python will
not stop you from using them as variable names — but doing so shadows the
built-in and causes confusing errors:

```python
# WRONG — shadows the built-in list type
list = [1, 2, 3]
new_list = list("hello")   # TypeError: 'list' object is not callable
```

Use descriptive names that do not clash with built-ins:

```python
# CORRECT
numbers = [1, 2, 3]
```

---

### 3.9 Case Sensitivity

Python is **case-sensitive**. `name`, `Name`, and `NAME` are three completely
different identifiers:

```python
name = "Alice"
Name = "Bob"
NAME = "Carol"

print(name)   # Alice
print(Name)   # Bob
print(NAME)   # Carol
```

This applies everywhere: variable names, function names, class names, module
names, and keywords. The keyword `True` is valid; `true` is not. The keyword
`None` is valid; `none` is not.

```python
print(True)    # True
# print(true)  # NameError: name 'true' is not defined

print(None)    # None
# print(none)  # NameError: name 'none' is not defined
```

Case sensitivity is why naming conventions matter. If you name a class
`shoppingcart` instead of `ShoppingCart`, it will work — but it will look wrong
to every Python programmer who reads it, and it will be harder to distinguish
from a variable or function name at a glance.

---

### 3.10 Blank Lines and Whitespace Conventions

Blank lines are not just cosmetic — they are part of Python's style and affect
readability significantly.

#### Two blank lines between top-level definitions

Use **two blank lines** before and after top-level function and class
definitions:

```python
def first_function():
    pass


def second_function():
    pass


class MyClass:
    pass


def third_function():
    pass
```

#### One blank line between methods inside a class

Use **one blank line** between methods inside a class:

```python
class MyClass:
    def first_method(self):
        pass

    def second_method(self):
        pass

    def third_method(self):
        pass
```

#### Blank lines inside functions

Use blank lines sparingly inside functions to separate logical sections. Do not
add blank lines just to fill space:

```python
def process_order(order):
    """Process a customer order."""
    # Validate the order
    if not order.get("items"):
        raise ValueError("Order has no items.")

    # Calculate totals
    subtotal = sum(item["price"] for item in order["items"])
    tax = subtotal * 0.08
    total = subtotal + tax

    # Return the result
    return {"subtotal": subtotal, "tax": tax, "total": total}
```

#### Spaces around operators

Put one space on each side of binary operators:

```python
# CORRECT
x = 10
y = x + 5
result = x * y - 1

# WRONG
x=10
y=x+5
result=x*y-1
```

Exception: no spaces around `=` in keyword arguments or default parameter
values:

```python
# CORRECT
def connect(host, port=5432):
    pass

connect(host="localhost", port=5432)

# WRONG
def connect(host, port = 5432):
    pass
```

#### No trailing whitespace

Do not leave spaces at the end of lines. Most editors can be configured to
strip trailing whitespace automatically on save.

---

### 3.11 The `pass` Statement

Sometimes you need to define a block but have nothing to put in it yet — a
function you plan to implement later, a class with no methods yet, or an `if`
branch you want to handle but have not written yet.

Python requires that every block have at least one statement. An empty block is
a `SyntaxError`. The `pass` statement is a **no-op** — it does nothing — and it
satisfies Python's requirement for a non-empty block:

```python
def todo_function():
    pass   # implement this later


class EmptyClass:
    pass


if some_condition:
    pass   # handle this case later
else:
    do_something()
```

`pass` is also useful in `except` blocks when you intentionally want to ignore
an exception (though this should be done carefully and with a comment explaining
why):

```python
try:
    result = int(user_input)
except ValueError:
    pass   # non-numeric input is acceptable here; result stays None
```

`pass` is a placeholder, not a permanent solution. When you see `pass` in your
own code, it is a reminder that something still needs to be implemented.

---

### 3.12 PEP 8: Style Guide Overview

**PEP 8** is Python's official style guide, written by Guido van Rossum and
others. It covers everything from naming conventions to line length to import
ordering. You do not need to memorize all of it — here are the essentials.

#### Line length

PEP 8 recommends a maximum line length of **79 characters**. Many modern
projects use **88 characters** (the default for the `black` formatter). The
goal is to keep lines readable without horizontal scrolling.

```python
# WRONG — too long, hard to read at a glance
result = some_very_long_function_name(argument_one, argument_two, argument_three, argument_four)

# CORRECT — split across lines using implicit continuation
result = some_very_long_function_name(
    argument_one,
    argument_two,
    argument_three,
    argument_four,
)
```

#### Import ordering

Imports go at the top of the file, after the module docstring. Group them in
this order, with a blank line between each group:

1. Standard library imports
2. Third-party imports
3. Local application imports

```python
"""My module."""

import os
import sys

import requests

from mypackage import utils
```

#### Automatic formatters

Reading PEP 8 and applying it manually is useful for learning. In practice,
most Python projects use an automatic formatter.

**`black`** is an opinionated formatter that reformats your entire file
according to a consistent style (largely PEP 8, with 88-character line length):

```bash
pip install black
black myfile.py
```

**`autopep8`** is more conservative — it only fixes PEP 8 violations without
changing your overall style:

```bash
pip install autopep8
autopep8 --in-place myfile.py
```

Both tools integrate with VS Code, PyCharm, and most other editors, so you can
format on save automatically. Using one of them from the start saves a lot of
manual effort.

---

## 4. Practical Examples

### Example 1: A Well-Structured Python File

This example shows a complete, small Python file that follows all the
conventions covered in this chapter. Read through it and notice how each rule
is applied.

```python
"""
geometry.py

Functions for calculating properties of basic 2D shapes.
"""

import math

# Constants follow UPPER_CASE naming
PI = math.pi
DEFAULT_PRECISION = 2


def circle_area(radius):
    """Return the area of a circle with the given radius."""
    return PI * radius ** 2


def circle_circumference(radius):
    """Return the circumference of a circle with the given radius."""
    return 2 * PI * radius


def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def rectangle_perimeter(width, height):
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


def format_result(label, value, precision=DEFAULT_PRECISION):
    """Return a formatted string showing a label and rounded value."""
    return f"{label}: {round(value, precision)}"


if __name__ == "__main__":
    r = 5
    print(format_result("Circle area", circle_area(r)))
    print(format_result("Circle circumference", circle_circumference(r)))

    w, h = 4, 6
    print(format_result("Rectangle area", rectangle_area(w, h)))
    print(format_result("Rectangle perimeter", rectangle_perimeter(w, h)))
```

```text
Circle area: 78.54
Circle circumference: 31.42
Rectangle area: 24
Rectangle perimeter: 20
```

What to notice:
- Module docstring at the very top, before imports
- Imports after the docstring
- Constants in `UPPER_CASE`
- Functions in `snake_case`, each with a docstring
- Two blank lines between every top-level definition
- `if __name__ == "__main__":` guard at the bottom

---

### Example 2: Indentation in Nested Blocks

This example shows how indentation levels stack up in real code. Each level of
nesting adds 4 spaces, and the structure is immediately visible from the
indentation alone.

```python
def classify_temperature(temp):
    """Classify a temperature reading into a category."""
    if temp < 0:
        category = "freezing"
        if temp < -20:
            warning = "extreme cold warning"
        else:
            warning = "cold weather advisory"
    elif temp < 15:
        category = "cold"
        warning = None
    elif temp < 25:
        category = "comfortable"
        warning = None
    elif temp < 35:
        category = "warm"
        warning = None
    else:
        category = "hot"
        if temp > 40:
            warning = "heat emergency"
        else:
            warning = "heat advisory"

    if warning:
        return f"{category} ({warning})"
    return category


temperatures = [-25, -5, 10, 20, 30, 38, 42]
for t in temperatures:
    print(f"{t}°C → {classify_temperature(t)}")
```

```text
-25°C → freezing (extreme cold warning)
-5°C → freezing (cold weather advisory)
10°C → cold
20°C → comfortable
30°C → warm
38°C → hot (heat advisory)
42°C → hot (heat emergency)
```

---

### Example 3: Line Continuation in Practice

```python
# Long import — implicit continuation inside parentheses
from os.path import (
    join,
    exists,
    dirname,
    basename,
)

# Long condition — wrap in parentheses
def is_valid_user(user):
    """Return True if the user passes all validation checks."""
    return (
        user is not None
        and user.get("name")
        and user.get("email")
        and "@" in user.get("email", "")
        and user.get("age", 0) >= 18
    )

# Long string — adjacent string literals are joined automatically
error_message = (
    "The provided value is outside the acceptable range. "
    "Please enter a number between 1 and 100."
)

# Long function call
result = sorted(
    user_list,
    key=lambda u: u["last_name"],
    reverse=False,
)
```

Notice that adjacent string literals inside parentheses are automatically
concatenated by Python. This is a clean way to write long strings without
backslash continuation.

---

### Example 4: Naming Conventions in a Real Context

```python
"""
user_account.py

Manages user account data.
"""

# Constant — UPPER_CASE
MAX_LOGIN_ATTEMPTS = 5

# Module-level variables — snake_case
current_attempt = 0
is_locked = False


class UserAccount:
    """Represents a user account in the system."""

    def __init__(self, username, email):
        """Initialize a new user account."""
        self.username = username    # public attribute — snake_case
        self.email = email          # public attribute — snake_case
        self._login_count = 0       # private by convention — _leading_underscore

    def log_in(self, password):
        """Attempt to log in with the given password."""
        if self._login_count >= MAX_LOGIN_ATTEMPTS:
            return "Account locked."
        if self._check_password(password):
            self._login_count += 1
            return "Login successful."
        return "Incorrect password."

    def _check_password(self, password):
        """Internal method — check if the password is correct."""
        # In real code, compare against a hashed password
        return password == "secret"

    def get_login_count(self):
        """Return the number of successful logins."""
        return self._login_count


# PascalCase for the class, snake_case for the variable
my_account = UserAccount(username="alice", email="alice@example.com")
print(my_account.log_in("wrong"))    # Incorrect password.
print(my_account.log_in("secret"))   # Login successful.
print(my_account.get_login_count())  # 1
```

---

### Example 5: Comments and Docstrings Together

```python
"""
converter.py

Unit conversion utilities.
"""

# Conversion factors — defined once as constants to avoid magic numbers
MILES_PER_KM = 0.621371
KG_PER_LB = 0.453592
CM_PER_INCH = 2.54


def km_to_miles(km):
    """Convert kilometers to miles."""
    return km * MILES_PER_KM


def miles_to_km(miles):
    """Convert miles to kilometers."""
    # Divide by the conversion factor rather than defining a separate constant
    return miles / MILES_PER_KM


def kg_to_lbs(kg):
    """Convert kilograms to pounds."""
    return kg / KG_PER_LB


def lbs_to_kg(lbs):
    """Convert pounds to kilograms."""
    return lbs * KG_PER_LB


def inches_to_cm(inches):
    """Convert inches to centimeters."""
    return inches * CM_PER_INCH


if __name__ == "__main__":
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"5 miles = {miles_to_km(5):.2f} km")
    print(f"70 kg = {kg_to_lbs(70):.1f} lbs")
    print(f"154 lbs = {lbs_to_kg(154):.1f} kg")
    print(f"6 inches = {inches_to_cm(6):.1f} cm")
```

```text
10 km = 6.21 miles
5 miles = 8.05 km
70 kg = 154.3 lbs
154 lbs = 69.9 kg
6 inches = 15.2 cm
```

---

### Example 6: The `pass` Statement in Practice

```python
# Stub out a class before implementing it
class DatabaseConnection:
    """Manages a connection to the database."""

    def connect(self):
        """Open the database connection."""
        pass   # TODO: implement

    def disconnect(self):
        """Close the database connection."""
        pass   # TODO: implement

    def execute(self, query):
        """Execute a SQL query and return results."""
        pass   # TODO: implement


# Stub out functions in a module
def send_email(to, subject, body):
    """Send an email message."""
    pass


def send_sms(phone_number, message):
    """Send an SMS message."""
    pass


# Use pass while building logic incrementally
def process_payment(amount, method):
    """Process a payment using the specified method."""
    if method == "credit_card":
        pass   # implement credit card flow
    elif method == "paypal":
        pass   # implement PayPal flow
    else:
        raise ValueError(f"Unknown payment method: {method}")
```

---

### Example 7: Keywords and Case Sensitivity

```python
import keyword

# Print all reserved keywords
print(f"Python has {len(keyword.kwlist)} reserved keywords:")
print(keyword.kwlist)

# Check specific names
names_to_check = ["for", "match", "type", "total", "class", "MyClass"]
for name in names_to_check:
    status = "keyword" if keyword.iskeyword(name) else "not a keyword"
    print(f"  {name!r:12} → {status}")
```

```text
Python has 35 reserved keywords:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
 'while', 'with', 'yield']
  'for'        → keyword
  'match'      → not a keyword
  'type'       → not a keyword
  'total'      → not a keyword
  'class'      → keyword
  'MyClass'    → not a keyword
```

Case sensitivity in action:

```python
# These are three completely different names
value = 10
Value = 20
VALUE = 30

print(value, Value, VALUE)   # 10 20 30

# Keywords are case-sensitive
print(True)    # True
# print(true)  # NameError: name 'true' is not defined

print(None)    # None
# print(none)  # NameError: name 'none' is not defined
```

---

## 5. Common Mistakes

### Mistake 1: Mixing Tabs and Spaces

This is one of the most common sources of confusion for beginners, especially
when copying code from different sources or editors.

```text
# WRONG — tab on one line, spaces on another
def greet(name):
	print(f"Hello, {name}!")   # tab character
    print("How are you?")      # 4 spaces
```

```text
TabError: inconsistent use of tabs and spaces in indentation
```

**Fix:** Configure your editor to always insert spaces when you press Tab. In
VS Code, add this to your settings:

```json
"editor.insertSpaces": true,
"editor.tabSize": 4
```

---

### Mistake 2: Wrong Indentation Level

Indenting by the wrong amount — 2 spaces instead of 4, or 3 spaces — can cause
an `IndentationError` or, worse, silently change the logic of your program.

```python
# WRONG — print runs inside the loop (5 times), not after it
total = 0
for i in range(5):
    total += i
    print(f"Final total: {total}")   # indented — runs every iteration
```

```python
# CORRECT — print runs once, after the loop finishes
total = 0
for i in range(5):
    total += i
print(f"Final total: {total}")   # not indented — runs after the loop
```

Always double-check which block a line belongs to by looking at its indentation
level relative to the block header above it.

---

### Mistake 3: Forgetting the Colon

Every block header must end with a colon. Forgetting it is a `SyntaxError`:

```python
# WRONG
def greet(name)
    print(f"Hello, {name}!")
```

```text
SyntaxError: expected ':'
```

```python
# CORRECT
def greet(name):
    print(f"Hello, {name}!")
```

This applies to `if`, `elif`, `else`, `for`, `while`, `with`, `try`, `except`,
`finally`, `class`, and `def` — every block header.

---

### Mistake 4: Using a Built-in Name as a Variable

Built-in names like `list`, `type`, `input`, `print`, `len`, and `id` are not
reserved keywords, so Python will not stop you from using them. But doing so
shadows the built-in and causes confusing errors later:

```python
# WRONG — shadows the built-in list type
list = [1, 2, 3]
new_list = list("hello")   # TypeError: 'list' object is not callable
```

```python
# CORRECT — use a descriptive name
numbers = [1, 2, 3]
```

If you accidentally shadow a built-in, restart your Python session or use
`del list` to remove the shadowing name.

---

### Mistake 5: Putting the Docstring After Another Statement

A docstring must be the **first statement** in a function, class, or module.
If you put it after another statement, it is just a string literal that gets
evaluated and discarded — it will not be stored in `__doc__`:

```python
# WRONG — not a docstring, just a string literal
def greet(name):
    print("Starting greet")
    """Return a greeting."""   # too late — this is not the docstring
    return f"Hello, {name}!"

print(greet.__doc__)   # None
```

```python
# CORRECT — docstring is the first statement
def greet(name):
    """Return a greeting."""
    print("Starting greet")
    return f"Hello, {name}!"

print(greet.__doc__)   # Return a greeting.
```

---

### Mistake 6: Backslash Continuation with Trailing Whitespace

A backslash at the end of a line continues the statement, but only if there is
**no character after the backslash** — not even a space:

```python
# WRONG — space after backslash causes SyntaxError
total = first + second + \ 
        third
```

```python
# CORRECT — use implicit continuation with parentheses instead
total = (
    first + second +
    third
)
```

---

### Mistake 7: Naming a Variable After a Keyword

Reserved keywords cannot be used as names at all:

```python
# WRONG — SyntaxError
# for = 10
# class = "math"
# if = True
```

If you need a name that is close to a keyword, add a trailing underscore by
convention:

```python
# CORRECT — trailing underscore avoids the conflict
for_ = 10
class_ = "math"
type_ = "integer"
```

This is the PEP 8-recommended approach for avoiding keyword conflicts.

---

### Mistake 8: Inconsistent Naming Style

Mixing naming styles within a project makes code harder to read:

```python
# WRONG — inconsistent style
userName = "Alice"       # camelCase
User_Age = 30            # mixed
TOTAL_price = 49.99      # mixed case constant

def GetUserName():       # PascalCase for a function
    pass

class user_profile:      # snake_case for a class
    pass
```

```python
# CORRECT — consistent PEP 8 style
user_name = "Alice"
user_age = 30
total_price = 49.99

def get_user_name():
    pass

class UserProfile:
    pass
```

---

## 6. Practice Tasks

These tasks reinforce the concepts from this chapter. Try each one before
looking at the solutions.

---

### Task 1: Fix the Indentation Errors

The following code has indentation problems. Identify and fix all of them so
the function works correctly.

```python
def calculate_bmi(weight_kg, height_m):
result = weight_kg / (height_m ** 2)
if result < 18.5:
category = "underweight"
elif result < 25:
    category = "normal"
elif result < 30:
  category = "overweight"
else:
        category = "obese"
return category, round(result, 1)

bmi_category, bmi_value = calculate_bmi(70, 1.75)
print(f"BMI: {bmi_value} ({bmi_category})")
```

---

### Task 2: Add Docstrings

Add appropriate docstrings to the following module, functions, and class. Use
the single-line format for simple functions and the multi-line format where
more explanation is needed.

```python
import math

MAX_SIDES = 12

def polygon_interior_angle(sides):
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    return (sides - 2) * 180 / sides

def polygon_exterior_angle(sides):
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    return 360 / sides

class RegularPolygon:
    def __init__(self, sides, side_length):
        if sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = sides
        self.side_length = side_length

    def perimeter(self):
        return self.sides * self.side_length

    def interior_angle(self):
        return polygon_interior_angle(self.sides)
```

---

### Task 3: Apply PEP 8 Naming Conventions

Rename the following identifiers to follow PEP 8 conventions. Rewrite the
code with the corrected names.

```python
MaxRetries = 3
defaultTimeout = 30

def GetUserName(UserID):
    return f"user_{UserID}"

def calculateTotalPrice(ItemPrice, taxRate):
    return ItemPrice * (1 + taxRate)

class shopping_cart:
    def __init__(self):
        self.Items = []

    def AddItem(self, item):
        self.Items.append(item)

    def GetTotal(self):
        return sum(self.Items)
```

---

### Task 4: Rewrite Using Implicit Line Continuation

Rewrite the following code to use implicit line continuation (parentheses)
instead of backslash continuation. Also fix the long lines to stay within
88 characters.

```python
def is_eligible(age, income, credit_score, has_existing_loan, years_employed):
    return age >= 18 and income >= 30000 and credit_score >= 650 and not has_existing_loan and years_employed >= 2

total_cost = item_price + shipping_cost + \
             handling_fee + \
             tax_amount - \
             discount_amount
```

---

### Task 5: Use `pass` to Stub Out a Module

Create a stub for a `NotificationService` class with the following methods
(all using `pass`):

- `send_email(to, subject, body)` — sends an email
- `send_sms(phone, message)` — sends an SMS
- `send_push_notification(device_id, title, body)` — sends a push notification
- `get_delivery_status(notification_id)` — returns the delivery status

Each method should have a docstring. The class itself should have a docstring.

---

### Task 6: Explore Keywords

Write a short script that:

1. Imports the `keyword` module
2. Prints the total number of reserved keywords in Python
3. Prints all keywords that start with the letter `"f"`
4. Checks whether `"match"` is a keyword and prints the result
5. Checks whether `"type"` is a keyword and prints the result

---

### Task 7: Identify the Mistake

Each snippet below contains one mistake related to this chapter. Identify the
mistake and explain how to fix it. Do not just fix the code — explain what
rule was broken.

**Snippet A:**

```python
def greet():
    name = "Alice"
        print(f"Hello, {name}!")
```

**Snippet B:**

```python
class my_calculator:
    def Add(self, a, b):
        return a + b
```

**Snippet C:**

```python
def process():
    """Process the data."""
    pass
    """This function processes incoming data and stores results."""
```

**Snippet D:**

```python
MAX_SIZE = 100
del MAX_SIZE
print(MAX_SIZE)
```

**Snippet E:**

```python
input = input("Enter your name: ")
print(f"Hello, {input}!")
name2 = input("Enter another name: ")
```

---

### Task 8: Trace the Execution Order

Without running the code, write down the order in which each `print` statement
executes and what it prints. Then run the code to verify.

```python
print("A")

def first():
    print("B")

def second():
    print("C")
    first()
    print("D")

print("E")
second()
print("F")
first()
print("G")
```

---

### Task 9: Write a PEP 8-Compliant Module

Write a small Python module called `temperature_converter.py` that:

- Has a module docstring
- Defines three constants: `ABSOLUTE_ZERO_C`, `ABSOLUTE_ZERO_F`,
  `ABSOLUTE_ZERO_K`
- Defines three functions: `celsius_to_fahrenheit`, `fahrenheit_to_celsius`,
  `celsius_to_kelvin`
- Each function has a docstring
- All names follow PEP 8 conventions
- Lines are no longer than 88 characters
- Has an `if __name__ == "__main__":` block that demonstrates all three
  functions

---

Solutions for these tasks are in
[`docs/solutions/04-syntax-and-structure.md`](../solutions/04-syntax-and-structure.md).

---

## 7. Key Takeaways

**Indentation is syntax, not style.**
Python uses indentation to define code blocks. Four spaces per level is the
standard. Never mix tabs and spaces. An `IndentationError` means your
indentation is wrong — fix it before anything else.

**Every block header ends with a colon.**
`if`, `elif`, `else`, `for`, `while`, `def`, `class`, `with`, `try`, `except`,
`finally` — all of them end with `:` and are followed by an indented block.
Forgetting the colon is a `SyntaxError`.

**Statements perform actions; expressions produce values.**
Most lines of Python code are statements. Expressions can appear inside
statements. The distinction matters when reading error messages and
documentation.

**Prefer implicit line continuation.**
Wrap long expressions in parentheses `()`, brackets `[]`, or braces `{}` to
continue them across lines. Avoid backslash continuation — it is fragile and
breaks silently if there is trailing whitespace.

**Comments explain why; code explains what.**
Use `#` for single-line comments. There is no multi-line comment syntax — use
multiple `#` lines. Write comments that add context the code cannot express on
its own.

**Docstrings document your code for tools and humans.**
A docstring is a `"""..."""` string as the first statement in a module,
function, class, or method. Python stores it in `__doc__`. Write one for every
public function and class.

**Follow PEP 8 naming conventions.**
- `snake_case` for variables and functions
- `PascalCase` for classes
- `UPPER_CASE` for constants
- `_single_leading_underscore` for internal/private names
- `__dunder__` names are reserved for Python's use

**Never use a reserved keyword as a name.**
Use `import keyword; print(keyword.kwlist)` to see the full list. Also avoid
shadowing built-in names like `list`, `type`, `input`, and `id`.

**Python is case-sensitive.**
`name`, `Name`, and `NAME` are three different identifiers. `True` is a
keyword; `true` is not. `None` is a keyword; `none` is not.

**Use `pass` for empty blocks.**
Python requires at least one statement in every block. `pass` is a no-op that
satisfies this requirement. Use it to stub out functions, classes, or branches
you plan to implement later.

**Blank lines are part of the style.**
Two blank lines between top-level definitions. One blank line between methods
inside a class. Blank lines inside functions only to separate logical sections.

**PEP 8 sets the standard.**
Keep lines under 79 or 88 characters. Put imports at the top, grouped by
standard library, third-party, and local. Use `black` or `autopep8` to apply
formatting automatically.

---

## Further Reading

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 20 — The Zen of Python](https://peps.python.org/pep-0020/)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [black documentation](https://black.readthedocs.io/)
- [autopep8 on PyPI](https://pypi.org/project/autopep8/)
- Python docs: [`keyword` module](https://docs.python.org/3/library/keyword.html)

---

*Next chapter: [Chapter 05 — Values, Variables, and Types](05-values-variables-types.md)*
