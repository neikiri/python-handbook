# Solutions 10: Functions

## Overview

Chapter 10 exercises cover defining and calling functions, default parameters, keyword arguments, variable scope, type hints, lambda functions, and recursion. This solution guide explains the reasoning behind each exercise and highlights best practices for writing clean, reusable functions.

---

## Notes Before Checking Solutions

Functions are the most important tool for organizing Python code. The key habit to build is writing small, focused functions that do one thing well. A function that is hard to name is usually doing too much.

---

## Warm-up Exercise Solutions

### Exercise 1: Define and Call Functions

```python
def greet():
    """Say hello."""
    print("Hello, world!")

greet()

def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")  # 8

def get_min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9
```

**Returning multiple values:** `return min(numbers), max(numbers)` returns a tuple. Python unpacks it automatically when you write `minimum, maximum = get_min_max(...)`. This is cleaner than returning a list or a dictionary for simple cases.

**Why write docstrings?** Docstrings appear in `help()` output and IDE tooltips. They document what the function does, what it expects, and what it returns. Write them even for simple functions — it is a good habit.

---

### Exercise 2: Use Default Parameters

```python
def greet(name, greeting="Hello"):
    """Greet someone with a custom greeting."""
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Carol", greeting="Hey")  # Hey, Carol!
```

**Default parameter rules:**
- Parameters with defaults must come after parameters without defaults.
- `def greet(greeting="Hello", name):` is a `SyntaxError`.
- Default values are evaluated once when the function is defined, not each time it is called.

**The mutable default argument trap:**

```python
# WRONG — the list is shared across all calls
def add_item(item, items=[]):
    items.append(item)
    return items

# RIGHT — use None as the default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

Never use a mutable object (list, dict, set) as a default parameter value. Use `None` and create the object inside the function.

---

### Exercise 3: Use Keyword Arguments

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# All three styles work
describe_person("Alice", 30, "New York")
describe_person(name="Bob", age=25, city="Los Angeles")
describe_person("Carol", city="Chicago", age=28)  # mixed
```

**`*args` — variable positional arguments:**

```python
def sum_all(*numbers):
    """Sum any number of arguments."""
    return sum(numbers)

sum_all(1, 2, 3)        # 6
sum_all(1, 2, 3, 4, 5)  # 15
```

Inside the function, `numbers` is a tuple containing all positional arguments.

**`**kwargs` — variable keyword arguments:**

```python
def print_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

Inside the function, `info` is a dictionary containing all keyword arguments.

---

### Exercise 4: Understand Variable Scope

```python
global_var = "I am global"

def function1():
    print(f"In function1: {global_var}")  # can read global

function1()

def function2():
    local_var = "I am local"
    print(f"In function2: {local_var}")

function2()
# print(local_var)  # NameError — local_var does not exist here
```

**Scope rules (LEGB):**
1. **L**ocal — variables defined inside the current function
2. **E**nclosing — variables in enclosing functions (for nested functions)
3. **G**lobal — variables defined at the module level
4. **B**uilt-in — Python's built-in names (`len`, `print`, `range`, etc.)

Python searches in this order. The first match wins.

**Shadowing:**

```python
x = 10

def function3():
    x = 20  # local x, shadows the global x
    print(f"In function3: x = {x}")  # 20

print(f"Before: x = {x}")  # 10
function3()
print(f"After: x = {x}")   # 10 — global x unchanged
```

Creating a local variable with the same name as a global variable *shadows* the global — the function uses its own local copy. The global is not modified.

**`global` keyword (use sparingly):**

```python
counter = 0

def increment():
    global counter  # declare intent to modify the global
    counter += 1
```

Using `global` is generally a sign that the design could be improved. Consider using a class or passing the value as a parameter and returning the updated value instead.

---

### Exercise 5: Use Type Hints

```python
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"

def get_user(user_id: int) -> dict | None:
    """Get a user by ID, or None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
```

**Type hints are documentation, not enforcement.** Python does not check types at runtime. `add("hello", "world")` will not raise an error — it will return `"helloworld"`. Type hints are for:
- Documenting what types a function expects and returns
- Enabling IDE autocompletion and error detection
- Static analysis tools like `mypy`

**`dict | None` (Python 3.10+):** The `|` syntax means "either `dict` or `None`." In older Python, you would write `Optional[dict]` from the `typing` module.

---

## Practice Exercise Solutions

### Exercise 6: Write Reusable Functions

```python
def is_valid_email(email: str) -> bool:
    """Check if an email looks valid."""
    return "@" in email and "." in email

def is_valid_age(age: int) -> bool:
    """Check if an age is valid."""
    return 0 < age < 150

def is_valid_password(password: str) -> bool:
    """Check if a password is strong."""
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
    )

def format_name(first: str, last: str) -> str:
    """Format a full name."""
    return f"{first.capitalize()} {last.capitalize()}"

def format_phone(phone: str) -> str:
    """Format a phone number."""
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone  # return as-is if not 10 digits
```

**Why return the original phone if it is not 10 digits?** Returning `None` would require the caller to check for `None` before using the result. Returning the original string is a reasonable fallback — the caller gets something back and can decide what to do with it.

---

### Exercise 7: Use Lambda Functions

```python
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda x, y: x + y
print(add(3, 4))  # 7
```

**When to use lambdas:** Lambdas are best for short, throwaway functions passed as arguments to other functions. They are not a replacement for `def` — if the function is more than one expression, use `def`.

```python
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 92},
]

# Sort by grade, highest first
sorted_by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
```

`sorted()` accepts a `key` function that extracts the comparison value from each element. The lambda `lambda s: s["grade"]` extracts the grade from each student dictionary.

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
```

In modern Python, list comprehensions are often preferred over `map()` and `filter()` with lambdas:

```python
squared = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

Both approaches work. Use whichever is more readable in context.

---

### Exercise 8: Use Recursion

```python
def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n <= 1:      # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))  # 120 (5 * 4 * 3 * 2 * 1)
```

**How recursion works:**
1. `factorial(5)` calls `factorial(4)`
2. `factorial(4)` calls `factorial(3)`
3. ... and so on until `factorial(1)` returns `1`
4. Then the results unwind: `2 * 1 = 2`, `3 * 2 = 6`, `4 * 6 = 24`, `5 * 24 = 120`

**Every recursive function needs a base case** — a condition that stops the recursion. Without it, the function calls itself forever until Python raises a `RecursionError`.

```python
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Note:** This recursive Fibonacci is simple but slow — it recalculates the same values many times. For large `n`, use an iterative approach or memoization. For learning purposes, the recursive version is fine.

```python
def sum_list(items: list) -> int:
    """Sum a list recursively."""
    if not items:   # base case: empty list
        return 0
    return items[0] + sum_list(items[1:])
```

`items[1:]` creates a new list with the first element removed. Each recursive call works on a smaller list until it reaches the empty list.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Calculator with Functions

```python
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(a: float, b: float, operation: str) -> float:
    """Perform a calculation."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return operations[operation](a, b)
```

**Why store functions in a dictionary?** The `operations` dictionary maps operator strings to function objects. `operations[operation](a, b)` looks up the function and calls it. This is cleaner than a long `if/elif` chain and makes it easy to add new operations.

**Why `raise ValueError` instead of returning an error string?** Raising an exception lets the caller decide how to handle the error. Returning an error string forces the caller to check the return value every time. Exceptions are the standard Python way to signal errors.

---

### Challenge 2: Create a Text Processing Module

```python
def count_words(text: str) -> int:
    """Count the number of words."""
    return len(text.split())

def count_sentences(text: str) -> int:
    """Count the number of sentences."""
    return text.count(".") + text.count("!") + text.count("?")

def count_vowels(text: str) -> int:
    """Count the number of vowels."""
    return sum(1 for c in text if c in "aeiouAEIOU")

def most_common_word(text: str) -> str:
    """Find the most common word."""
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return max(word_counts, key=word_counts.get)

def summarize(text: str) -> dict:
    """Summarize text statistics."""
    return {
        "words": count_words(text),
        "sentences": count_sentences(text),
        "vowels": count_vowels(text),
        "most_common": most_common_word(text),
    }
```

**`max(word_counts, key=word_counts.get)`:** `max()` with a `key` function finds the element that produces the highest key value. Here, `word_counts.get` is used as the key function — it returns the count for each word. So `max()` returns the word with the highest count.

**Why break the logic into small functions?** Each function does one thing. `summarize()` calls the others. This makes each function easy to test independently and easy to reuse in other contexts.

---

### Challenge 3: Implement a Decorator (Preview)

```python
def my_decorator(func):
    """A simple decorator that prints before and after."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Calling greet
# Hello, Alice!
# Finished greet
```

**How decorators work:** `@my_decorator` is syntactic sugar for `greet = my_decorator(greet)`. The decorator receives the original function, wraps it in `wrapper`, and returns `wrapper`. When you call `greet("Alice")`, you are actually calling `wrapper("Alice")`.

`*args` and `**kwargs` in `wrapper` allow it to accept any arguments and pass them through to the original function. This makes the decorator work with any function signature.

---

### Challenge 4: Build a Function Library

```python
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple."""
    return abs(a * b) // gcd(a, b)

def is_perfect_square(n: int) -> bool:
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def digits_sum(n: int) -> int:
    """Calculate the sum of digits."""
    return sum(int(d) for d in str(abs(n)))
```

**Euclid's algorithm for GCD:** `while b: a, b = b, a % b`. This works because `gcd(a, b) == gcd(b, a % b)`. When `b` becomes `0`, `a` is the GCD. It is one of the oldest known algorithms and still the standard approach.

**`abs(a * b) // gcd(a, b)` for LCM:** The relationship between GCD and LCM is `lcm(a, b) = |a * b| / gcd(a, b)`. Using `abs()` handles negative inputs correctly.

---

## Common Mistakes

**Forgetting `return`.** A function without a `return` statement returns `None`. If you assign the result of such a function, you get `None`.

**Using a mutable default argument.** `def f(items=[]):` shares the same list across all calls. Use `def f(items=None): if items is None: items = []`.

**Calling a function before defining it.** Python executes files top to bottom. A function must be defined before it is called at the module level. (Inside another function, the call is not executed until the outer function runs, so order matters less there.)

**Infinite recursion.** Every recursive function needs a base case that stops the recursion. If the base case is missing or unreachable, Python raises `RecursionError: maximum recursion depth exceeded`.

**Modifying a global variable without `global`.** Inside a function, `x = 5` creates a local variable. To modify a global, you must declare `global x` first.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 11 - Comprehensions and Generators](../handbook/11-comprehensions-generators.md)
