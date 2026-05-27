# Chapter 05: Values, Variables, and Types

## 1. Overview

Every Python program works with data. That data might be a number, a piece of
text, a list of items, or the absence of a value entirely. Before you can write
useful programs, you need to understand how Python stores and organizes data.

This chapter covers the foundational ideas: what a value is, how you attach a
name to it, what types Python uses to categorize values, and how those types
behave. These concepts appear in every Python program you will ever read or
write, so getting them right early pays off immediately.

---

## 2. What You Will Learn

- The difference between a value and a variable
- How assignment works in Python
- What dynamic typing means and why it matters
- The built-in types: `int`, `float`, `complex`, `bool`, `str`, `NoneType`,
  and a brief look at `list`, `tuple`, `dict`, and `set`
- How to check and convert types
- How variables are references, not containers
- The difference between mutable and immutable objects
- How to use `id()`, `is`, and `==` correctly
- Multiple assignment and unpacking
- Constants by convention
- Augmented assignment operators
- A preview of variable scope

---

## 3. Core Concepts

### 3.1 Values and Variables

A **value** is a piece of data. `42`, `"hello"`, `3.14`, and `True` are all
values. They exist on their own, independent of any name.

A **variable** is a name that refers to a value. When you write:

```python
x = 42
```

you are telling Python: "create the integer object `42`, and bind the name `x`
to it." The `=` sign is the **assignment operator**. It does not mean
"x equals 42" in the mathematical sense — it means "attach the label `x` to
the object `42`."

You can think of a variable as a sticky note attached to an object. The note
has a name on it, and it points to the object. Multiple notes can point to the
same object, and you can move a note to a different object at any time.

```python
message = "Hello, world!"
count = 100
price = 9.99
is_active = True
nothing = None
```

Each line creates an object and binds a name to it.


### 3.2 Dynamic Typing

Python is **dynamically typed**. This means that variables do not have types —
objects do. A variable is just a name, and you can rebind it to any object at
any time, regardless of what it pointed to before.

```python
x = 10        # x refers to an int
x = "hello"   # x now refers to a str
x = [1, 2, 3] # x now refers to a list
```

This is different from statically typed languages like Java or C, where a
variable declared as `int` can only ever hold an integer.

The type belongs to the object, not the name. You can verify this with the
`type()` function.

```python
x = 42
print(type(x))   # <class 'int'>

x = "hello"
print(type(x))   # <class 'str'>
```

Dynamic typing makes Python flexible and fast to write, but it also means you
need to be aware of what type a variable currently holds, especially when
passing values to functions.

---

### 3.3 The `type()` Function

`type(value)` returns the type of any object. The result is a **type object**,
not a string.

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
print(type([1, 2, 3])) # <class 'list'>
```

You can compare the result of `type()` directly:

```python
x = 42
print(type(x) == int)   # True
print(type(x) == str)   # False
```

However, for type checking in real code, `isinstance()` is almost always
preferred. See section 3.10 for the reason.

---

### 3.4 Built-in Types

Python comes with a set of built-in types that cover the most common kinds of
data. Here is an overview of each one.

#### `int` — Integers

An `int` is a whole number with no decimal point. Python integers have no
fixed size limit — they can be as large as your available memory allows.

```python
age = 30
population = 8_000_000_000   # underscore as a thousands separator
negative = -17
zero = 0
```

The underscore separator (`_`) is purely visual. Python ignores it. You can
place it anywhere in a numeric literal to improve readability:

```python
one_million = 1_000_000
hex_color = 0xFF_AA_00
```

Python supports integer literals in four bases:

```python
decimal     = 255        # base 10 (default)
binary      = 0b11111111 # base 2  — prefix 0b
octal       = 0o377      # base 8  — prefix 0o
hexadecimal = 0xFF       # base 16 — prefix 0x

# All four are the same value
print(decimal == binary == octal == hexadecimal)  # True
```


#### `float` — Floating-Point Numbers

A `float` is a number with a decimal point. Python floats follow the IEEE 754
double-precision standard, which gives about 15–17 significant decimal digits
of precision.

```python
pi = 3.14159
temperature = -12.5
scientific = 1.5e10   # 1.5 × 10^10 = 15000000000.0
small = 2.7e-4        # 2.7 × 10^-4 = 0.00027
```

**Precision issues**

Floats cannot represent every decimal number exactly. This is a fundamental
property of binary floating-point arithmetic, not a Python bug.

```python
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False
```

When you need to compare floats, use `math.isclose()` instead of `==`:

```python
import math

a = 0.1 + 0.2
b = 0.3

print(math.isclose(a, b))  # True
```

`math.isclose()` checks whether two values are close enough to be considered
equal, within a small relative and absolute tolerance. The default tolerances
work well for most practical cases.

For financial calculations where exact decimal arithmetic is required, use the
`decimal` module from the standard library instead of `float`.

#### `complex` — Complex Numbers

Python has built-in support for complex numbers. The imaginary part uses `j`
as its suffix.

```python
z = 3 + 4j
print(z.real)   # 3.0
print(z.imag)   # 4.0
print(type(z))  # <class 'complex'>
```

Complex numbers are used in scientific and engineering applications. If you are
not working in those domains, you can safely skip them for now.

#### `bool` — Booleans

A `bool` has exactly two values: `True` and `False`. Note the capital letters —
Python is case-sensitive.

```python
is_logged_in = True
has_errors = False
```

`bool` is a subclass of `int` in Python. `True` behaves like `1` and `False`
behaves like `0` in arithmetic contexts:

```python
print(True + True)    # 2
print(True * 5)       # 5
print(False + 1)      # 1
print(int(True))      # 1
print(int(False))     # 0
```

This is occasionally useful (for example, counting how many items in a list
satisfy a condition), but do not rely on it in code that needs to be readable.

**Truthiness**

Every Python object has a truth value. When used in a boolean context (like an
`if` statement), objects are evaluated as either truthy or falsy.

Falsy values:
- `False`
- `None`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}`, `set()` (empty collections)

Everything else is truthy.

```python
if "hello":
    print("truthy")   # this runs

if "":
    print("truthy")   # this does not run

if 0:
    print("truthy")   # this does not run

if 42:
    print("truthy")   # this runs
```


#### `str` — Strings

A `str` is a sequence of Unicode characters. Strings are created with single
quotes, double quotes, or triple quotes.

```python
name = "Alice"
greeting = 'Hello'
paragraph = """This is a
multi-line string."""
```

Strings are covered in depth in Chapter 07. For now, the key points are:

- Strings are immutable — you cannot change a character in place.
- You can concatenate strings with `+` and repeat them with `*`.
- You can check the length with `len()`.

```python
language = "Python"
print(len(language))          # 6
print(language + " 3.10")     # Python 3.10
print(language[0])            # P
```

#### `NoneType` — The Absence of a Value

`None` is Python's way of representing "no value" or "nothing here." It is the
only value of the `NoneType` type.

```python
result = None
print(result)         # None
print(type(result))   # <class 'NoneType'>
```

Common uses of `None`:

- A function that does not explicitly return a value returns `None`.
- A variable that has not been assigned a meaningful value yet.
- A default argument that signals "no argument was provided."

```python
def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")

greet()          # Hello, stranger!
greet("Alice")   # Hello, Alice!
```

Always check for `None` using `is None` or `is not None`, not `== None`. The
reason is explained in section 3.9.

#### `list`, `tuple`, `dict`, `set` — Collections

Python has four built-in collection types. They are introduced briefly here and
covered in full in Chapter 09.

```python
# list — ordered, mutable sequence
fruits = ["apple", "banana", "cherry"]

# tuple — ordered, immutable sequence
coordinates = (10.5, 20.3)

# dict — key-value mapping
person = {"name": "Alice", "age": 30}

# set — unordered collection of unique values
unique_ids = {1, 2, 3, 4}
```

The key distinction for now: lists and dicts are **mutable** (you can change
them after creation), while tuples are **immutable** (you cannot). This matters
for how Python handles them in memory, which is covered in section 3.8.

---

### 3.5 Variable Naming Rules

Python has strict rules for variable names and strong conventions.

**Rules (enforced by Python):**

- Names can contain letters, digits, and underscores.
- Names cannot start with a digit.
- Names are case-sensitive: `count`, `Count`, and `COUNT` are three different
  variables.
- Names cannot be Python keywords (`if`, `for`, `class`, `return`, etc.).

```python
# Valid names
user_name = "Alice"
_private = 42
count2 = 0
MAX_SIZE = 100

# Invalid names — these cause SyntaxError
# 2count = 0
# my-var = 5
# class = "math"
```

**Conventions (PEP 8):**

- Use `snake_case` for variables and functions: `user_name`, `total_price`.
- Use `UPPER_SNAKE_CASE` for constants: `MAX_RETRIES`, `PI`.
- Use `PascalCase` for class names: `UserAccount`, `HttpClient`.
- Avoid single-letter names except for short loop counters (`i`, `j`, `k`) or
  mathematical variables where the letter is conventional (`x`, `y`, `n`).
- Choose descriptive names: `user_age` is better than `ua` or `a`.


### 3.6 Type Conversion (Casting)

You can convert a value from one type to another using the built-in conversion
functions: `int()`, `float()`, `str()`, `bool()`, `list()`, and `tuple()`.

#### `int()`

Converts a value to an integer.

```python
int("42")       # 42   — string of digits
int(3.9)        # 3    — truncates toward zero, does not round
int(True)       # 1
int(False)      # 0
int("0xFF", 16) # 255  — parse hex string with explicit base
```

`int()` raises `ValueError` if the string cannot be parsed as an integer:

```python
int("hello")    # ValueError: invalid literal for int() with base 10: 'hello'
int("3.14")     # ValueError: invalid literal for int() with base 10: '3.14'
```

Note that `int("3.14")` fails even though `float("3.14")` would succeed. If
you have a float-formatted string and want an integer, convert in two steps:

```python
value = int(float("3.14"))   # 3
```

#### `float()`

Converts a value to a float.

```python
float("3.14")   # 3.14
float(42)       # 42.0
float(True)     # 1.0
float("1e5")    # 100000.0
```

`float()` also raises `ValueError` on unparseable strings:

```python
float("abc")    # ValueError
```

#### `str()`

Converts any value to its string representation.

```python
str(42)         # "42"
str(3.14)       # "3.14"
str(True)       # "True"
str(None)       # "None"
str([1, 2, 3])  # "[1, 2, 3]"
```

`str()` never raises an error — every Python object has a string
representation.

#### `bool()`

Converts a value to `True` or `False` using Python's truthiness rules.

```python
bool(1)         # True
bool(0)         # False
bool("hello")   # True
bool("")        # False
bool([1, 2])    # True
bool([])        # False
bool(None)      # False
```

#### `list()` and `tuple()`

Convert an iterable to a list or tuple.

```python
list("abc")          # ['a', 'b', 'c']
list((1, 2, 3))      # [1, 2, 3]
tuple([1, 2, 3])     # (1, 2, 3)
tuple("hello")       # ('h', 'e', 'l', 'l', 'o')
```

#### What cannot be converted

Not every conversion makes sense. Python will raise an error when a conversion
is impossible:

```python
int("hello")     # ValueError
float("abc")     # ValueError
int([1, 2, 3])   # TypeError: int() argument must be a string, a bytes-like
                 # object or a real number, not 'list'
```

Always handle potential `ValueError` or `TypeError` when converting user input
or data from external sources.

```python
raw = input("Enter a number: ")
try:
    number = int(raw)
    print(f"You entered: {number}")
except ValueError:
    print(f"'{raw}' is not a valid integer.")
```

---

### 3.7 `isinstance()` vs `type()`

There are two ways to check the type of an object. They behave differently and
are used in different situations.

**`type(x) == SomeType`** checks for an exact type match. It returns `False`
if `x` is an instance of a subclass.

**`isinstance(x, SomeType)`** checks whether `x` is an instance of
`SomeType` or any subclass of it. This is almost always what you want.

```python
print(type(True) == bool)       # True
print(type(True) == int)        # False  — even though bool is a subclass of int

print(isinstance(True, bool))   # True
print(isinstance(True, int))    # True  — because bool is a subclass of int
```

`isinstance()` also accepts a tuple of types to check against multiple types
at once:

```python
x = 42
print(isinstance(x, (int, float)))   # True — x is an int, which is in the tuple

y = "hello"
print(isinstance(y, (int, float)))   # False
```

**Rule of thumb:** use `isinstance()` for type checks in real code. Use
`type()` when you specifically need to know the exact type and want to exclude
subclasses (which is rare).


### 3.8 Variables Are References

This is one of the most important concepts in Python, and it is the source of
many beginner surprises.

In Python, a variable does not contain a value. It holds a **reference** to an
object. When you write `x = 42`, Python creates the integer object `42` in
memory and makes `x` point to it.

#### The `id()` Function

`id(obj)` returns the unique identity of an object — its memory address in
CPython. Two objects that are equal may or may not have the same identity.

```python
x = 42
print(id(x))   # some integer, e.g. 140234567890

y = x
print(id(y))   # same integer — y points to the same object as x
```

When you assign `y = x`, you are not copying the value. You are making `y`
point to the same object that `x` already points to.

#### `is` vs `==`

- `==` checks **value equality**: do the two objects have the same value?
- `is` checks **identity**: are the two names pointing to the exact same object
  in memory?

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  — same values
print(a is b)   # False — different objects in memory

c = a
print(a is c)   # True  — c and a point to the same object
```

Use `==` when you want to compare values. Use `is` only when you want to check
object identity — the most common case being `is None` and `is not None`.

```python
result = None

if result is None:
    print("No result yet.")
```

Never write `if result == None`. It works in practice, but `is None` is the
correct idiom and is enforced by linters.

#### Mutability vs Immutability

Whether a variable assignment creates a new object or modifies an existing one
depends on whether the type is **mutable** or **immutable**.

**Immutable types** cannot be changed after creation. Any operation that
appears to modify them actually creates a new object:

- `int`, `float`, `complex`, `bool`
- `str`
- `tuple`
- `NoneType`

```python
x = "hello"
print(id(x))   # some address, e.g. 140000000001

x = x + " world"
print(id(x))   # different address — a new string object was created
```

**Mutable types** can be changed in place. Operations that modify them do not
create a new object:

- `list`
- `dict`
- `set`

```python
numbers = [1, 2, 3]
print(id(numbers))   # some address, e.g. 140000000002

numbers.append(4)
print(id(numbers))   # same address — the same list object was modified
print(numbers)       # [1, 2, 3, 4]
```

#### Why This Matters: Shared References

Because variables are references, two variables can point to the same mutable
object. Modifying the object through one variable affects the other.

```python
a = [1, 2, 3]
b = a            # b points to the same list as a

b.append(4)

print(a)         # [1, 2, 3, 4] — a was affected too!
print(a is b)    # True
```

This is not a bug — it is intentional Python behavior. If you want an
independent copy of a list, use `list()` or the `.copy()` method:

```python
a = [1, 2, 3]
b = list(a)      # b is a new list with the same values

b.append(4)

print(a)         # [1, 2, 3] — a is unchanged
print(a is b)    # False
```

With immutable types, this is never an issue because you cannot modify the
object in place anyway.


### 3.9 Multiple Assignment and Unpacking

Python lets you assign multiple variables in a single line.

#### Assigning the Same Value to Multiple Variables

```python
x = y = z = 0
print(x, y, z)   # 0 0 0
```

All three names point to the same object. For immutable types like `int`, this
is perfectly safe. For mutable types, be careful:

```python
a = b = []       # a and b point to the same list
a.append(1)
print(b)         # [1] — b was affected too
```

If you want separate empty lists, use:

```python
a = []
b = []
```

#### Tuple Unpacking

You can assign multiple variables from a sequence in one line:

```python
x, y = 10, 20
print(x)   # 10
print(y)   # 20
```

The right side is a tuple `(10, 20)`. Python unpacks it and assigns each value
to the corresponding name on the left.

This works with any iterable:

```python
first, second, third = [1, 2, 3]
a, b, c = "abc"

# Swap two variables without a temporary variable
x, y = y, x
```

The number of names on the left must match the number of values on the right,
or Python raises a `ValueError`:

```python
a, b = 1, 2, 3   # ValueError: too many values to unpack
a, b, c = 1, 2   # ValueError: not enough values to unpack
```

#### Extended Unpacking with `*`

The `*` operator collects remaining values into a list:

```python
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*start, last = [1, 2, 3, 4, 5]
print(start)   # [1, 2, 3, 4]
print(last)    # 5

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5
```

---

### 3.10 Constants

Python does not have a built-in mechanism for constants. There is no `const`
keyword. By convention, a name written in `UPPER_SNAKE_CASE` signals to other
programmers that the value should not be changed.

```python
PI = 3.14159265358979
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
APP_NAME = "MyApp"
```

Nothing prevents you from reassigning these names — Python will not complain.
The convention is purely a communication tool. If you need enforced constants,
you can use `typing.Final` (covered in Chapter 19):

```python
from typing import Final

PI: Final = 3.14159265358979
```

Type checkers like `mypy` will flag any attempt to reassign a `Final` variable,
but Python itself still allows it at runtime.

---

### 3.11 Augmented Assignment

Augmented assignment operators combine an arithmetic operation with assignment.
They are shorthand for updating a variable based on its current value.

```python
x = 10

x += 3    # equivalent to: x = x + 3   → 13
x -= 2    # equivalent to: x = x - 2   → 11
x *= 4    # equivalent to: x = x * 4   → 44
x /= 2    # equivalent to: x = x / 2   → 22.0  (always float)
x //= 3   # equivalent to: x = x // 3  → 7     (floor division)
x %= 3    # equivalent to: x = x % 3   → 1     (remainder)
x **= 4   # equivalent to: x = x ** 4  → 1     (exponentiation)

print(x)  # 1
```

Note that `/=` always produces a `float`, even if both operands are integers:

```python
n = 10
n /= 2
print(n)          # 5.0
print(type(n))    # <class 'float'>
```

Use `//=` if you want integer floor division.

Augmented assignment also works with strings and lists:

```python
greeting = "Hello"
greeting += ", world!"
print(greeting)   # Hello, world!

items = [1, 2]
items += [3, 4]   # equivalent to items.extend([3, 4])
print(items)      # [1, 2, 3, 4]
```


### 3.12 Variable Scope (Preview)

A variable's **scope** is the region of code where it is accessible. Python
has four scope levels, often called LEGB:

- **L**ocal — inside the current function
- **E**nclosing — in an outer function (for nested functions)
- **G**lobal — at the top level of the module
- **B**uilt-in — names built into Python itself

For now, the key rule is: variables created inside a function are local to that
function and cannot be accessed from outside it.

```python
def calculate():
    result = 42   # local variable
    return result

print(result)     # NameError: name 'result' is not defined
```

Variables created at the top level of a script are global and can be read
inside functions, but modifying them requires the `global` keyword.

Scope is covered in full in Chapter 10. For now, just be aware that where you
define a variable determines where you can use it.

---

## 4. Practical Examples

### Example 1: Working with Numeric Types

```python
# Integer arithmetic
apples = 12
oranges = 7
total_fruit = apples + oranges
print(f"Total fruit: {total_fruit}")   # Total fruit: 19

# Integer division vs float division
print(10 / 3)    # 3.3333333333333335  (float division)
print(10 // 3)   # 3                   (floor division)
print(10 % 3)    # 1                   (remainder)

# Large integers — Python handles them natively
factorial_20 = 1
for i in range(1, 21):
    factorial_20 *= i
print(factorial_20)   # 2432902008176640000

# Float precision
import math

a = 0.1 + 0.2
b = 0.3
print(a == b)                  # False
print(math.isclose(a, b))      # True
print(f"a = {a:.20f}")         # a = 0.30000000000000004441
print(f"b = {b:.20f}")         # b = 0.29999999999999998890
```

### Example 2: Type Checking and Conversion

```python
def describe_value(value):
    """Print the value, its type, and whether it is truthy."""
    print(f"Value:   {value!r}")
    print(f"Type:    {type(value).__name__}")
    print(f"Truthy:  {bool(value)}")
    print()

describe_value(42)
describe_value(0)
describe_value("hello")
describe_value("")
describe_value([1, 2, 3])
describe_value([])
describe_value(None)
```

Output:

```text
Value:   42
Type:    int
Truthy:  True

Value:   0
Type:    int
Truthy:  False

Value:   'hello'
Type:    str
Truthy:  True

Value:   ''
Type:    str
Truthy:  False

Value:   [1, 2, 3]
Type:    list
Truthy:  True

Value:   []
Type:    list
Truthy:  False

Value:   None
Type:    NoneType
Truthy:  False
```


### Example 3: Safe Type Conversion from User Input

```python
def get_integer(prompt: str) -> int | None:
    """
    Ask the user for an integer. Return the integer if valid,
    or None if the input cannot be converted.
    """
    raw = input(prompt)
    try:
        return int(raw)
    except ValueError:
        print(f"Error: '{raw}' is not a valid integer.")
        return None


age = get_integer("Enter your age: ")
if age is not None:
    print(f"In 10 years you will be {age + 10}.")
```

### Example 4: Mutability in Practice

```python
# Immutable: strings
original = "hello"
modified = original.upper()

print(original)   # hello  — unchanged
print(modified)   # HELLO  — new object

# Mutable: lists
numbers = [3, 1, 4, 1, 5]
numbers.sort()

print(numbers)    # [1, 1, 3, 4, 5] — modified in place

# Shared reference trap
list_a = [1, 2, 3]
list_b = list_a          # same object

list_b.append(99)
print(list_a)            # [1, 2, 3, 99] — affected!

# Correct way to copy
list_c = list_a.copy()   # independent copy
list_c.append(100)
print(list_a)            # [1, 2, 3, 99] — not affected
print(list_c)            # [1, 2, 3, 99, 100]
```

### Example 5: Multiple Assignment and Unpacking

```python
# Swap without a temporary variable
x = 10
y = 20
x, y = y, x
print(x, y)   # 20 10

# Unpack a function return value
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 7, 2, 9, 3])
print(f"Min: {low}, Max: {high}")   # Min: 1, Max: 9

# Extended unpacking
scores = [95, 88, 72, 65, 50]
best, *rest = scores
print(f"Best score: {best}")        # Best score: 95
print(f"Other scores: {rest}")      # Other scores: [88, 72, 65, 50]

# Ignore values with _
first, _, third = (1, 2, 3)
print(first, third)   # 1 3
```

### Example 6: Constants and Augmented Assignment

```python
# Constants by convention
MAX_RETRIES = 3
BASE_URL = "https://api.example.com"
TIMEOUT_SECONDS = 30

# Augmented assignment in a loop
total = 0
for value in [10, 20, 30, 40, 50]:
    total += value
print(f"Total: {total}")   # Total: 150

# Building a string incrementally
report = "Report:\n"
report += f"  Items processed: {len([10, 20, 30])}\n"
report += f"  Total: {sum([10, 20, 30])}\n"
print(report)
```

Output:

```text
Report:
  Items processed: 3
  Total: 60
```

### Example 7: Using `id()` to Observe Object Identity

```python
# Small integers are cached by CPython
a = 100
b = 100
print(a is b)    # True  — CPython caches small ints (-5 to 256)

a = 1000
b = 1000
print(a is b)    # False — large ints are not cached (implementation detail)

# Strings may or may not be interned
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True  — CPython interns short strings (implementation detail)

# Never rely on is for value comparison
# Always use == for values, is only for identity (None, True, False)
print(s1 == s2)  # True  — always correct for value comparison
```

> **Note:** The behavior of `is` with integers and strings is an implementation
> detail of CPython. Do not write code that depends on it. Use `==` for value
> comparisons and `is` only for `None`, `True`, and `False`.


---

## 5. Common Mistakes

### Mistake 1: Using `==` to Check for `None`

```python
# Wrong
if result == None:
    print("no result")

# Correct
if result is None:
    print("no result")
```

`is None` is the correct idiom. `== None` works in most cases but can produce
unexpected results if an object defines a custom `__eq__` method that returns
something unexpected when compared to `None`. Linters like `flake8` and
`ruff` will flag `== None` as a style error.

---

### Mistake 2: Confusing `=` and `==`

```python
# This is assignment — it always succeeds
x = 5

# This is comparison — it returns True or False
x == 5
```

Using `=` inside a condition is a `SyntaxError` in Python (unlike C or Java,
where it is a common bug):

```python
if x = 5:   # SyntaxError: invalid syntax
    pass
```

Python 3.8 introduced the walrus operator `:=` for assignment inside
expressions, but that is a different, intentional feature.

---

### Mistake 3: Assuming `int()` Rounds

`int()` does not round — it truncates toward zero.

```python
print(int(3.9))    # 3  — not 4
print(int(-3.9))   # -3 — not -4
```

If you want rounding, use `round()`:

```python
print(round(3.9))    # 4
print(round(-3.9))   # -4
print(round(3.5))    # 4  — rounds to even (banker's rounding)
print(round(2.5))    # 2  — rounds to even
```

---

### Mistake 4: Mutating a Shared Reference

```python
# Wrong — both variables point to the same list
defaults = [1, 2, 3]
my_list = defaults
my_list.append(4)
print(defaults)   # [1, 2, 3, 4] — unintended mutation

# Correct — make an explicit copy
my_list = defaults.copy()
my_list.append(4)
print(defaults)   # [1, 2, 3] — unchanged
```

This mistake is especially common when using a mutable object as a default
function argument. That specific case is covered in Chapter 10.

---

### Mistake 5: Comparing Types with `type()` Instead of `isinstance()`

```python
# Wrong — misses subclasses
def process(value):
    if type(value) == int:
        print("integer")

process(True)   # prints nothing — bool is a subclass of int, not int itself

# Correct
def process(value):
    if isinstance(value, int):
        print("integer")

process(True)   # prints "integer"
```

---

### Mistake 6: Expecting `0.1 + 0.2 == 0.3`

```python
# This is False — a common beginner surprise
print(0.1 + 0.2 == 0.3)   # False

# Use math.isclose() for float comparisons
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True
```

---

### Mistake 7: Reassigning a Constant

```python
PI = 3.14159

# Python will not stop you from doing this
PI = 3   # no error, but this is wrong by convention

# If you need enforcement, use typing.Final
from typing import Final
PI: Final = 3.14159
# A type checker will now flag any reassignment of PI
```

---

### Mistake 8: Unpacking with the Wrong Number of Values

```python
a, b = 1, 2, 3   # ValueError: too many values to unpack (expected 2)
a, b, c = 1, 2   # ValueError: not enough values to unpack (expected 3)
```

If you are not sure how many values a sequence contains, use extended
unpacking with `*` to collect the extras:

```python
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]
```


---

## 6. Practice Tasks

Work through these tasks to reinforce the concepts in this chapter. Try each
one before looking at the solutions in
[`docs/solutions/05-values-variables-types.md`](../solutions/05-values-variables-types.md).

---

**Task 1: Type Explorer**

Write a script that creates one variable of each of the following types:
`int`, `float`, `bool`, `str`, `NoneType`. For each variable, print:

- The value
- The type (using `type()`)
- Whether it is truthy (using `bool()`)

Expected output format:

```text
Value: 42 | Type: int | Truthy: True
Value: 0.0 | Type: float | Truthy: False
...
```

---

**Task 2: Safe Converter**

Write a function `safe_int(value)` that:

- Accepts any value
- Returns the value converted to `int` if the conversion succeeds
- Returns `None` if the conversion fails (catches `ValueError` and `TypeError`)

Test it with these inputs: `"42"`, `"3.14"`, `"hello"`, `True`, `None`,
`[1, 2]`.

---

**Task 3: Integer Bases**

Write a script that:

1. Defines the number 255 using decimal, binary, octal, and hexadecimal
   literals.
2. Prints all four variables and confirms they are equal.
3. Converts the decimal 255 to its binary, octal, and hex string
   representations using `bin()`, `oct()`, and `hex()`.

---

**Task 4: Float Precision**

Write a script that demonstrates the float precision problem:

1. Compute `0.1 + 0.2` and print the result.
2. Check if `0.1 + 0.2 == 0.3` and print the result.
3. Use `math.isclose()` to check the same comparison and print the result.
4. Print both values to 20 decimal places using an f-string format spec
   (`:.20f`) to show why they differ.

---

**Task 5: Mutability Test**

Write a script that:

1. Creates a list `original = [1, 2, 3]`.
2. Creates `alias = original` (a reference, not a copy).
3. Creates `copy = original.copy()` (an independent copy).
4. Appends `99` to `alias`.
5. Prints `original`, `alias`, and `copy`.
6. Uses `is` to confirm that `original` and `alias` are the same object, and
   that `original` and `copy` are not.

---

**Task 6: Unpacking Practice**

Given the list `data = [10, 20, 30, 40, 50]`:

1. Unpack the first element into `first` and the rest into `remaining`.
2. Unpack the last element into `last` and the rest into `beginning`.
3. Unpack the first and last elements, collecting the middle into `middle`.
4. Print all results.

---

**Task 7: Augmented Assignment Counter**

Write a script that simulates a simple score tracker:

1. Start with `score = 0`.
2. Add 10 points three times using `+=`.
3. Subtract 5 points once using `-=`.
4. Double the score using `*=`.
5. Print the final score.

What is the expected final score?

---

**Task 8: Constants Module**

Create a small Python file called `constants.py` that defines at least five
constants relevant to a simple application of your choice (for example, a
quiz app, a unit converter, or a simple game). Use `UPPER_SNAKE_CASE` naming.
Then write a second script that imports and uses those constants.

---

**Task 9: Identity vs Equality**

Write a script that demonstrates the difference between `is` and `==`:

1. Create two lists with the same values. Show that `==` returns `True` but
   `is` returns `False`.
2. Create two variables pointing to the same list. Show that both `==` and
   `is` return `True`.
3. Check `None` using both `== None` and `is None`. Show that both return
   `True` for a `None` value, but explain why `is None` is preferred.

---

**Task 10: Type Conversion Chain**

Starting with the string `"  42  "` (note the surrounding spaces):

1. Strip the whitespace using `.strip()`.
2. Convert to `int`.
3. Multiply by 2.
4. Convert back to `str`.
5. Concatenate with the string `" is the answer"`.
6. Print the final result.

This simulates a common pattern when processing user input or data from files.


---

## 7. Key Takeaways

- A **value** is a piece of data. A **variable** is a name bound to a value
  using the assignment operator `=`.

- Python is **dynamically typed**: variables have no type, objects do. You can
  rebind a name to any object at any time.

- Use `type(x)` to inspect the type of any object. Use `isinstance(x, T)` for
  type checks in real code — it handles subclasses correctly.

- Python's core built-in types are `int`, `float`, `complex`, `bool`, `str`,
  `NoneType`, `list`, `tuple`, `dict`, and `set`.

- `int` has no size limit in Python. Use `0b`, `0o`, `0x` prefixes for
  binary, octal, and hex literals. Use `_` as a visual separator in large
  numbers.

- `float` has precision limits. Never use `==` to compare floats — use
  `math.isclose()` instead.

- `bool` is a subclass of `int`. `True == 1` and `False == 0`. Every Python
  object has a truth value.

- `None` is Python's null value. Always check for it with `is None` or
  `is not None`, never with `== None`.

- Use `int()`, `float()`, `str()`, `bool()`, `list()`, and `tuple()` to
  convert between types. Handle `ValueError` and `TypeError` when converting
  untrusted input.

- Variables are **references** to objects, not containers. Two variables can
  point to the same object.

- **Immutable** types (`int`, `float`, `str`, `tuple`, `bool`, `None`) cannot
  be changed in place. **Mutable** types (`list`, `dict`, `set`) can.

- Use `id()` to inspect object identity. Use `is` to compare identity and `==`
  to compare values. Use `is` only for `None`, `True`, and `False` in
  production code.

- Python supports multiple assignment (`x = y = 0`), tuple unpacking
  (`a, b = 1, 2`), and extended unpacking (`first, *rest = items`).

- Constants are a naming convention (`UPPER_SNAKE_CASE`). Python does not
  enforce them, but `typing.Final` lets type checkers flag reassignments.

- Augmented assignment operators (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`)
  update a variable based on its current value. Note that `/=` always produces
  a `float`.

- Variable **scope** determines where a name is accessible. Variables defined
  inside a function are local to that function. Full scope rules are covered in
  Chapter 10.

---

*Next chapter: [Chapter 06 — Operators, Expressions, and Input](./06-operators-expressions-input.md)*
