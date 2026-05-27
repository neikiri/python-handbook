# Chapter 10: Functions — Exercises

## Overview

These exercises help you master Python's functions: defining them, using parameters, returning values, and understanding scope. By the end, you will write clean, reusable functions that form the foundation of larger programs.

---

## How to Use These Exercises

- Create a folder called `chapter-10` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and test with different inputs.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Define and Call Functions

Create a file called `functions_basic.py`:

```python
# Simple function with no parameters
def greet():
    """Say hello."""
    print("Hello, world!")

greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple return values
def get_min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
minimum, maximum = get_min_max(numbers)
print(f"Min: {minimum}, Max: {maximum}")
```

Run it and observe function calls.

---

### Exercise 2: Use Default Parameters

Create a file called `default_params.py`:

```python
# Function with default parameters
def greet(name, greeting="Hello"):
    """Greet someone with a custom greeting."""
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
greet("Carol", greeting="Hey")

# Function with multiple defaults
def create_user(username, email=None, active=True):
    """Create a user account."""
    return {
        "username": username,
        "email": email,
        "active": active,
    }

user1 = create_user("alice")
user2 = create_user("bob", "bob@example.com")
user3 = create_user("carol", "carol@example.com", False)

print(f"User 1: {user1}")
print(f"User 2: {user2}")
print(f"User 3: {user3}")
```

Run it and observe default parameters.

---

### Exercise 3: Use Keyword Arguments

Create a file called `keyword_args.py`:

```python
# Function with multiple parameters
def describe_person(name, age, city):
    """Describe a person."""
    print(f"{name} is {age} years old and lives in {city}.")

# Positional arguments
describe_person("Alice", 30, "New York")

# Keyword arguments
describe_person(name="Bob", age=25, city="Los Angeles")

# Mixed
describe_person("Carol", city="Chicago", age=28)

# Function with *args (variable number of arguments)
def sum_all(*numbers):
    """Sum any number of arguments."""
    return sum(numbers)

print(f"\nsum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# Function with **kwargs (keyword arguments)
def print_info(**info):
    """Print key-value pairs."""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\nPerson info:")
print_info(name="Alice", age=30, city="New York")
```

Run it and observe different argument styles.

---

### Exercise 4: Understand Variable Scope

Create a file called `scope.py`:

```python
# Global variable
global_var = "I am global"

def function1():
    """Access global variable."""
    print(f"In function1: {global_var}")

function1()

# Local variable
def function2():
    """Create a local variable."""
    local_var = "I am local"
    print(f"In function2: {local_var}")

function2()
# print(local_var)  # This would cause NameError

# Shadowing global variable
x = 10

def function3():
    """Create a local variable that shadows the global."""
    x = 20
    print(f"In function3: x = {x}")

print(f"Before function3: x = {x}")
function3()
print(f"After function3: x = {x}")

# Modifying global variable (not recommended)
counter = 0

def increment():
    """Increment the global counter."""
    global counter
    counter += 1

print(f"Counter: {counter}")
increment()
print(f"Counter: {counter}")
increment()
print(f"Counter: {counter}")
```

Run it and observe scope behavior.

---

### Exercise 5: Use Type Hints

Create a file called `type_hints.py`:

```python
# Function with type hints
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")

# Type hints with different types
def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"

greeting = greet("Alice")
print(greeting)

# Type hints with collections
def process_numbers(numbers: list) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

average = process_numbers([1, 2, 3, 4, 5])
print(f"Average: {average}")

# Type hints with optional values
def get_user(user_id: int) -> dict | None:
    """Get a user by ID, or None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"User 1: {get_user(1)}")
print(f"User 3: {get_user(3)}")
```

Run it and observe type hints (they do not enforce types, just document them).

---

## Practice Exercises

### Exercise 6: Write Reusable Functions

Create a file called `reusable.py`:

```python
# Validation functions
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

# Formatting functions
def format_name(first: str, last: str) -> str:
    """Format a full name."""
    return f"{first.capitalize()} {last.capitalize()}"

def format_phone(phone: str) -> str:
    """Format a phone number."""
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone

# Test the functions
print(f"Valid email: {is_valid_email('alice@example.com')}")
print(f"Valid age: {is_valid_age(30)}")
print(f"Valid password: {is_valid_password('SecurePass123')}")
print(f"Formatted name: {format_name('alice', 'smith')}")
print(f"Formatted phone: {format_phone('5551234567')}")
```

Run it and observe reusable functions.

---

### Exercise 7: Use Lambda Functions

Create a file called `lambda_functions.py`:

```python
# Simple lambda
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"add(3, 4) = {add(3, 4)}")

# Lambda with sorted()
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 92},
]

sorted_by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print(f"\nSorted by grade:")
for student in sorted_by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nSquared: {squared}")

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")
```

Run it and observe lambda functions.

---

### Exercise 8: Use Recursion

Create a file called `recursion.py`:

```python
# Factorial (recursive)
def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")

# Fibonacci (recursive)
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(10) = {fibonacci(10)}")

# Sum of list (recursive)
def sum_list(items: list) -> int:
    """Sum a list recursively."""
    if not items:
        return 0
    return items[0] + sum_list(items[1:])

print(f"sum_list([1, 2, 3, 4, 5]) = {sum_list([1, 2, 3, 4, 5])}")

# Count down (recursive)
def countdown(n: int) -> None:
    """Count down from n to 1."""
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

print("\nCountdown:")
countdown(5)
```

Run it and observe recursion.

---

## Challenge Exercises

### Challenge 1: Build a Calculator with Functions

Create a file called `calculator.py`:

```python
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
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

# Interactive calculator
print("Calculator")
while True:
    try:
        a = float(input("First number: "))
        op = input("Operation (+, -, *, /): ")
        b = float(input("Second number: "))
        result = calculate(a, b, op)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
```

Run it and test the calculator.

---

### Challenge 2: Create a Text Processing Module

Create a file called `text_processor.py`:

```python
def count_words(text: str) -> int:
    """Count the number of words."""
    return len(text.split())

def count_sentences(text: str) -> int:
    """Count the number of sentences."""
    return text.count(".") + text.count("!") + text.count("?")

def count_vowels(text: str) -> int:
    """Count the number of vowels."""
    vowels = "aeiouAEIOU"
    return sum(1 for c in text if c in vowels)

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

# Test
text = "Python is great. Python is powerful. Python is fun!"
summary = summarize(text)
print(f"Summary: {summary}")
```

Run it and observe text processing.

---

### Challenge 3: Implement a Decorator (Preview)

Create a file called `decorators_preview.py`:

```python
# Simple decorator
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
    """Greet someone."""
    print(f"Hello, {name}!")

greet("Alice")

# Timing decorator
import time

def timer(func):
    """Decorator that measures execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """A function that takes time."""
    time.sleep(1)
    return "Done"

slow_function()
```

Run it and observe decorators (this is a preview; decorators are covered in later chapters).

---

### Challenge 4: Build a Function Library

Create a file called `math_lib.py`:

```python
"""A simple math library."""

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple."""
    return abs(a * b) // gcd(a, b)

def is_perfect_square(n: int) -> bool:
    """Check if a number is a perfect square."""
    root = int(n ** 0.5)
    return root * root == n

def digits_sum(n: int) -> int:
    """Calculate the sum of digits."""
    return sum(int(d) for d in str(abs(n)))

# Test the library
print(f"is_prime(17): {is_prime(17)}")
print(f"gcd(48, 18): {gcd(48, 18)}")
print(f"lcm(12, 18): {lcm(12, 18)}")
print(f"is_perfect_square(16): {is_perfect_square(16)}")
print(f"digits_sum(12345): {digits_sum(12345)}")
```

Run it and test the math library.

---

## Hints

**NameError for a function** → Make sure the function is defined before you call it.

**TypeError with arguments** → Check that you are passing the right number and type of arguments.

**RecursionError** → Your recursive function is not reaching a base case. Add a condition to stop the recursion.

**Unexpected scope behavior** → Remember that variables created inside a function are local. Use `global` to modify global variables (not recommended).

---

## What to Review If You Get Stuck

- **Defining and calling functions** → Handbook section 3.1
- **Parameters and arguments** → Handbook section 3.2
- **Return values** → Handbook section 3.3
- **Scope** → Handbook section 3.4
- **Type hints** → Handbook section 3.5
- **Docstrings** → Handbook section 3.6
- **Lambda functions** → Handbook section 3.7
- **Functions as first-class objects** → Handbook section 3.8
- **Recursion** → Handbook section 3.9
- **Built-in functions** → Handbook section 3.10

---

## Key Takeaways

After completing these exercises, you should be able to:

- Define and call functions with various parameter types
- Use default and keyword arguments
- Return single and multiple values
- Understand variable scope
- Write type hints for functions
- Use lambda functions for simple operations
- Implement recursive functions
- Build reusable function libraries
- Understand functions as first-class objects
