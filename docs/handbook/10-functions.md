# Chapter 10: Functions

## 1. Overview

Functions are the primary tool for organizing code. Instead of writing the
same logic in multiple places, you define it once, give it a name, and call it
whenever you need it. This makes programs shorter, easier to read, and easier
to change.

Python functions are first-class objects — you can assign them to variables,
pass them as arguments, and return them from other functions. That flexibility
opens up powerful patterns that you will use throughout your Python career.

---

## 2. What You Will Learn

- How to define and call functions with `def`
- Positional, keyword, default, and variable-length parameters
- How `return` works, including returning multiple values
- What scope means and how Python resolves names (LEGB rule)
- The difference between local and global variables
- Type hints on function signatures
- Docstrings and why they matter
- Lambda functions for short, anonymous operations
- Functions as first-class objects: passing and returning functions
- Recursion and when to use it
- Common built-in functions: `map()`, `filter()`, `sorted()` with `key`

---

## 3. Core Concepts

### 3.1 Defining and Calling a Function

Use the `def` keyword to define a function. The body must be indented.

```python
def greet():
    print("Hello, world!")


greet()   # Hello, world!
```

A function does nothing until you call it. The parentheses `()` are required
both when defining and when calling.

---

### 3.2 Parameters and Arguments

**Parameters** are the names listed in the function definition. **Arguments**
are the values you pass when calling the function.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
```

#### Positional arguments

Arguments are matched to parameters by position.

```python
def describe(animal, color):
    print(f"A {color} {animal}.")


describe("cat", "black")    # A black cat.
describe("black", "cat")    # A cat black.  — wrong order, wrong result
```

#### Keyword arguments

Pass arguments by name to make the call clearer and order-independent.

```python
describe(color="black", animal="cat")   # A black cat.
```

You can mix positional and keyword arguments, but positional ones must come
first.

```python
describe("cat", color="black")   # A black cat.
```

#### Default parameter values

Give a parameter a default value so it becomes optional.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")              # Hello, Alice!
greet("Bob", "Good morning")  # Good morning, Bob!
greet("Charlie", greeting="Hi")  # Hi, Charlie!
```

Parameters with defaults must come after parameters without defaults.

```python
# SyntaxError — non-default parameter after default parameter
def bad(x=1, y):
    pass

# Correct
def good(x, y=1):
    pass
```

**Important:** never use a mutable object (list, dict) as a default value.
Use `None` instead and create the object inside the function.

```python
# Wrong
def append_to(item, target=[]):
    target.append(item)
    return target

# Correct
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

#### `*args`: variable positional arguments

Use `*args` to accept any number of positional arguments. They arrive as a
tuple.

```python
def total(*numbers):
    return sum(numbers)


print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100
```

#### `**kwargs`: variable keyword arguments

Use `**kwargs` to accept any number of keyword arguments. They arrive as a
dict.

```python
def show_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")


show_info(name="Alice", age=30, city="Paris")
# name: Alice
# age: 30
# city: Paris
```

#### Combining parameter types

The order must be: positional, `*args`, keyword-only, `**kwargs`.

```python
def mixed(a, b, *args, sep=", ", **kwargs):
    print(f"a={a}, b={b}")
    print(f"extra positional: {args}")
    print(f"sep={sep!r}")
    print(f"extra keyword: {kwargs}")


mixed(1, 2, 3, 4, sep=" | ", x=10, y=20)
# a=1, b=2
# extra positional: (3, 4)
# sep=' | '
# extra keyword: {'x': 10, 'y': 20}
```

Parameters after `*args` (or after a bare `*`) are **keyword-only** — they
must be passed by name.

```python
def draw(shape, *, color="black", filled=False):
    print(f"{shape}: color={color}, filled={filled}")


draw("circle", color="red", filled=True)
draw("square")
# draw("square", "blue")  # TypeError — color must be keyword
```

#### Unpacking arguments with `*` and `**`

You can unpack a list or tuple into positional arguments, and a dict into
keyword arguments.

```python
def add(x, y, z):
    return x + y + z


values = [1, 2, 3]
print(add(*values))   # 6

params = {"x": 1, "y": 2, "z": 3}
print(add(**params))  # 6
```

---

### 3.3 The `return` Statement

`return` sends a value back to the caller and exits the function immediately.

```python
def square(n):
    return n ** 2


result = square(5)
print(result)   # 25
```

A function without a `return` statement (or with a bare `return`) returns
`None`.

```python
def say_hi():
    print("Hi!")


result = say_hi()
print(result)   # None
```

#### Returning multiple values

Python functions can return multiple values as a tuple.

```python
def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


low, high = min_max([4, 7, 2, 9, 1])
print(low, high)   # 1 9
```

#### Early return

Use `return` early to exit a function when a condition is met. This avoids
deep nesting.

```python
def find_first(items: list, target) -> int:
    """Return the index of the first occurrence of target, or -1."""
    for i, item in enumerate(items):
        if item == target:
            return i    # exit immediately
    return -1           # only reached if target was not found
```

---

### 3.4 Scope and the LEGB Rule

**Scope** determines where a name is visible. Python looks up names in this
order, stopping at the first match:

1. **L**ocal — inside the current function
2. **E**nclosing — in any enclosing function (for nested functions)
3. **G**lobal — at the module (file) level
4. **B**uilt-in — Python's built-in names (`len`, `print`, `range`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)       # enclosing

outer()
print(x)           # global
```

#### Local variables

Variables assigned inside a function are local to that function. They do not
exist outside it.

```python
def compute():
    result = 42
    return result


compute()
print(result)   # NameError: name 'result' is not defined
```

#### Reading global variables

A function can read a global variable without any special declaration.

```python
PI = 3.14159

def circle_area(radius: float) -> float:
    return PI * radius ** 2


print(circle_area(5))   # 78.53975
```

#### Modifying global variables with `global`

To assign to a global variable inside a function, declare it with `global`.
This is rarely needed — prefer passing values as arguments and returning
results.

```python
count = 0

def increment():
    global count
    count += 1


increment()
increment()
print(count)   # 2
```

#### `nonlocal` for enclosing scope

Use `nonlocal` to assign to a variable in an enclosing (but not global) scope.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3
```

---

### 3.5 Type Hints

Type hints document what types a function expects and returns. They are not
enforced at runtime but help editors, linters, and readers understand the code.

```python
def add(x: int, y: int) -> int:
    return x + y


def greet(name: str) -> str:
    return f"Hello, {name}!"


def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

For optional values, use `type | None` (Python 3.10+) or `Optional[type]`
from `typing`.

```python
def find(items: list[str], target: str) -> int | None:
    for i, item in enumerate(items):
        if item == target:
            return i
    return None
```

Type hints are especially valuable in larger codebases and when writing
functions that others will call.

---

### 3.6 Docstrings

A **docstring** is a string literal placed immediately after the `def` line.
It documents what the function does, its parameters, and its return value.

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.
    """
    return celsius * 9 / 5 + 32
```

Access a docstring with `help()` or the `__doc__` attribute.

```python
help(celsius_to_fahrenheit)
print(celsius_to_fahrenheit.__doc__)
```

Write a docstring for every function that is not completely obvious. A single
sentence is enough for simple functions; use the multi-line format for anything
with parameters, return values, or side effects.

---

### 3.7 Lambda Functions

A **lambda** is a small, anonymous function defined in a single expression.

```python
lambda parameters: expression
```

```python
square = lambda x: x ** 2
print(square(5))   # 25

add = lambda x, y: x + y
print(add(3, 4))   # 7
```

Lambdas are most useful as short callbacks — for example, as the `key`
argument to `sorted()`.

```python
words = ["banana", "apple", "fig", "cherry"]
print(sorted(words, key=lambda w: len(w)))
# ['fig', 'apple', 'banana', 'cherry']

students = [{"name": "Bob", "grade": 92}, {"name": "Alice", "grade": 88}]
print(sorted(students, key=lambda s: s["grade"], reverse=True))
# [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 88}]
```

Use a named function when the logic is more than a single expression, or when
you need to reuse it.

---

### 3.8 Functions as First-Class Objects

In Python, functions are objects. You can assign them to variables, store them
in lists or dicts, pass them as arguments, and return them from other
functions.

#### Passing functions as arguments

```python
def apply(func, value):
    return func(value)


def double(x):
    return x * 2


def square(x):
    return x ** 2


print(apply(double, 5))   # 10
print(apply(square, 5))   # 25
```

#### Returning functions (closures)

A function that returns another function is called a **higher-order function**.
The returned function "closes over" variables from the enclosing scope.

```python
def make_multiplier(factor: int):
    def multiply(x: int) -> int:
        return x * factor
    return multiply


triple = make_multiplier(3)
print(triple(7))    # 21
print(triple(10))   # 30
```

#### Storing functions in data structures

```python
operations = {
    "add":      lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide":   lambda x, y: x / y,
}

op = "multiply"
result = operations[op](6, 7)
print(f"{op}: {result}")   # multiply: 42
```

---

### 3.9 Built-in Higher-Order Functions

#### `map()`

Apply a function to every item in an iterable. Returns an iterator.

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]
```

In modern Python, a list comprehension is usually clearer:

```python
squares = [x ** 2 for x in numbers]
```

#### `filter()`

Keep only items for which a function returns `True`. Returns an iterator.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8]
```

Again, a comprehension is often clearer:

```python
evens = [x for x in numbers if x % 2 == 0]
```

#### `sorted()` with `key`

`sorted()` accepts a `key` function that extracts a comparison value from each
item.

```python
words = ["Banana", "apple", "Cherry", "date"]

# Case-insensitive sort
print(sorted(words, key=str.lower))
# ['apple', 'Banana', 'Cherry', 'date']

# Sort by length, then alphabetically
print(sorted(words, key=lambda w: (len(w), w.lower())))
# ['date', 'apple', 'Banana', 'Cherry']
```

---

### 3.10 Recursion

A **recursive** function calls itself. Every recursive function needs:

1. A **base case** that stops the recursion.
2. A **recursive case** that moves toward the base case.

```python
def factorial(n: int) -> int:
    """Return n! (n factorial)."""
    if n == 0:
        return 1          # base case
    return n * factorial(n - 1)   # recursive case


print(factorial(5))   # 120
print(factorial(0))   # 1
```

Trace of `factorial(4)`:

```text
factorial(4)
  = 4 * factorial(3)
  = 4 * 3 * factorial(2)
  = 4 * 3 * 2 * factorial(1)
  = 4 * 3 * 2 * 1 * factorial(0)
  = 4 * 3 * 2 * 1 * 1
  = 24
```

Python has a default recursion limit of 1000 calls. For deep recursion,
consider an iterative approach instead.

```python
def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

Recursion is natural for problems with a recursive structure — trees, nested
data, divide-and-conquer algorithms.

```python
def flatten(nested):
    """Recursively flatten a nested list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(flatten([1, [2, [3, 4]], [5, 6]]))   # [1, 2, 3, 4, 5, 6]
```

---

## 4. Practical Examples

### 4.1 Temperature Converter

```python
def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return c + 273.15


temps_c = [0, 20, 37, 100]

print(f"{'°C':>6} {'°F':>8} {'K':>8}")
print("-" * 26)
for c in temps_c:
    f = celsius_to_fahrenheit(c)
    k = celsius_to_kelvin(c)
    print(f"{c:>6.1f} {f:>8.1f} {k:>8.2f}")

# Output:
#    °C       °F        K
# --------------------------
#   0.0     32.0   273.15
#  20.0     68.0   293.15
#  37.0     98.6   310.15
# 100.0    212.0   373.15
```

---

### 4.2 Input Validator with a Callback

```python
def get_valid_input(prompt: str, validator, error_msg: str) -> str:
    """Keep asking for input until the validator returns True."""
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(error_msg)


def is_positive_int(s: str) -> bool:
    return s.isdigit() and int(s) > 0


def is_non_empty(s: str) -> bool:
    return len(s.strip()) > 0


# Usage (interactive — uncomment to run):
# age = get_valid_input("Enter your age: ", is_positive_int, "Please enter a positive number.")
# name = get_valid_input("Enter your name: ", is_non_empty, "Name cannot be empty.")
```

---

### 4.3 Statistics Functions

```python
def mean(numbers: list[float]) -> float:
    """Return the arithmetic mean."""
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list.")
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """Return the median value."""
    if not numbers:
        raise ValueError("Cannot compute median of an empty list.")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def mode(numbers: list[float]) -> float:
    """Return the most frequent value."""
    if not numbers:
        raise ValueError("Cannot compute mode of an empty list.")
    counts: dict[float, int] = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    return max(counts, key=counts.get)


data = [4, 7, 2, 9, 1, 7, 5, 7, 3]
print(f"Mean:   {mean(data):.2f}")    # Mean:   5.00
print(f"Median: {median(data):.2f}")  # Median: 5.00
print(f"Mode:   {mode(data)}")        # Mode:   7
```

---

### 4.4 Decorator Pattern (Preview)

A **decorator** is a function that wraps another function to add behavior.
This is a common Python pattern you will see in frameworks and libraries.

```python
def log_calls(func):
    """Decorator that prints a message before and after each call."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper


@log_calls
def add(x: int, y: int) -> int:
    return x + y


add(3, 4)
# Calling add...
# add returned 7
```

The `@log_calls` syntax is shorthand for `add = log_calls(add)`.

---

### 4.5 Recursive Binary Search

```python
def binary_search(items: list[int], target: int,
                  low: int = 0, high: int | None = None) -> int:
    """Return the index of target in a sorted list, or -1 if not found."""
    if high is None:
        high = len(items) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if items[mid] == target:
        return mid
    elif items[mid] < target:
        return binary_search(items, target, mid + 1, high)
    else:
        return binary_search(items, target, low, mid - 1)


sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(sorted_list, 7))    # 3
print(binary_search(sorted_list, 10))   # -1
```

---

### 4.6 Function Dispatch Table

```python
def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


OPERATIONS: dict[str, callable] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(x: float, op: str, y: float) -> float:
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operator: {op!r}")
    return OPERATIONS[op](x, y)


print(calculate(10, "+", 5))   # 15.0
print(calculate(10, "/", 4))   # 2.5
```

---

### 4.7 Memoization with a Dict Cache

```python
def make_fibonacci():
    """Return a Fibonacci function with a built-in cache."""
    cache: dict[int, int] = {}

    def fib(n: int) -> int:
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

    return fib


fib = make_fibonacci()
print([fib(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Python's standard library provides `functools.lru_cache` for this pattern:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## 5. Common Mistakes

### 5.1 Mutable Default Arguments

```python
# Wrong — the list is created once and shared across all calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b']  — unexpected!

# Correct
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

### 5.2 Forgetting to `return` a Value

```python
def double(x):
    x * 2   # computed but not returned

result = double(5)
print(result)   # None — forgot return
```

Fix: add `return`.

```python
def double(x):
    return x * 2
```

---

### 5.3 Shadowing Built-in Names

Naming a variable or function the same as a built-in silently replaces it.

```python
# Bad — shadows the built-in list()
list = [1, 2, 3]
print(list([4, 5]))   # TypeError: 'list' object is not callable

# Bad — shadows the built-in len()
def len(s):
    return 0
```

Avoid names like `list`, `dict`, `set`, `type`, `id`, `input`, `print`,
`sum`, `min`, `max`, `range`, `sorted`, `filter`, `map`.

---

### 5.4 Confusing `return` and `print`

`print()` displays a value on screen. `return` sends a value back to the
caller. A function that only prints cannot be used in an expression.

```python
def add(x, y):
    print(x + y)   # displays, but returns None

result = add(3, 4)   # prints 7
print(result * 2)    # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

Fix: use `return`.

```python
def add(x, y):
    return x + y
```

---

### 5.5 Modifying a Global Variable Without `global`

```python
count = 0

def increment():
    count += 1   # UnboundLocalError: local variable 'count' referenced before assignment

increment()
```

Python sees the assignment `count += 1` and treats `count` as a local
variable. Since it has no local value yet, it raises an error. Fix with
`global count` — or better, redesign to avoid global state.

---

### 5.6 Infinite Recursion

Forgetting the base case causes infinite recursion and a `RecursionError`.

```python
# Wrong — no base case
def countdown(n):
    print(n)
    countdown(n - 1)   # RecursionError after ~1000 calls

# Correct
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)
```

---

### 5.7 Overusing Lambda

Lambdas are for short, throwaway functions. If the logic is complex or you
need to reuse it, write a named function.

```python
# Hard to read
process = lambda x: x ** 2 if x > 0 else -x ** 2

# Clearer
def process(x: int) -> int:
    """Square x, negated if x is negative."""
    if x > 0:
        return x ** 2
    return -(x ** 2)
```

---

## 6. Practice Tasks

1. Write a function `clamp(value: float, low: float, high: float) -> float`
   that returns `value` constrained to the range `[low, high]`.

2. Write a function `is_palindrome(s: str) -> bool` that returns `True` if
   the string reads the same forwards and backwards (ignoring case and spaces).

3. Write a function `flatten(nested: list) -> list` that recursively flattens
   a list of lists to any depth.

4. Write a function `count_vowels(s: str) -> int` that counts the vowels in a
   string (case-insensitive).

5. Write a function `make_adder(n: int)` that returns a function which adds
   `n` to its argument. For example, `add5 = make_adder(5); add5(3)` returns
   `8`.

6. Write a function `apply_all(funcs: list, value)` that applies each function
   in `funcs` to `value` in sequence and returns the final result.

7. Write a recursive function `power(base: int, exp: int) -> int` that
   computes `base ** exp` without using the `**` operator.

8. Write a function `most_frequent(items: list)` that returns the item that
   appears most often. If there is a tie, return any one of them.

---

## 7. Key Takeaways

- Define functions with `def`. Call them with `()`.
- Parameters receive arguments by position or by keyword.
- Default values make parameters optional — never use mutable objects as
  defaults.
- `*args` collects extra positional arguments into a tuple; `**kwargs`
  collects extra keyword arguments into a dict.
- `return` sends a value back to the caller. A function without `return`
  returns `None`.
- Python resolves names using the LEGB rule: Local → Enclosing → Global →
  Built-in.
- Type hints document expected types but are not enforced at runtime.
- Docstrings explain what a function does and should be written for every
  non-trivial function.
- Lambdas are anonymous one-expression functions, best used as short
  callbacks.
- Functions are first-class objects — you can pass them, return them, and
  store them.
- Recursion is elegant for recursive problems but requires a base case and
  has a depth limit.

---

### Further Reading

- [Function Definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Function Attributes](https://docs.python.org/3/reference/datamodel.html#function-objects)
- [Lambda Expressions](https://docs.python.org/3/reference/expressions.html#lambda)

### What's Next

Ready to continue? Head to the next chapter: **Comprehensions and Generators**.

→ [Chapter 11 — Comprehensions and Generators](11-comprehensions-generators.md)

*See also:*
- [Exercise](../exercises/10-functions.md)
- [Solution](../solutions/10-functions.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
