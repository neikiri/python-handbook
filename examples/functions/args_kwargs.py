"""
*args and **kwargs - Variable-Length Arguments

This example demonstrates:
- *args for variable positional arguments
- **kwargs for variable keyword arguments
- Combining *args, **kwargs with regular arguments
- Unpacking with * and **
"""

print("=== *args (Variable Positional Arguments) ===")

def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total


print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10) = {sum_all(10)}")
print(f"sum_all() = {sum_all()}")

# Pass a list with *
numbers = [1, 2, 3, 4, 5]
print(f"sum_all(*[1, 2, 3, 4, 5]) = {sum_all(*numbers)}")
print()

print("=== *args with Regular Arguments ===")

def greet_many(greeting, *names):
    """Greet multiple people."""
    for name in names:
        print(f"{greeting}, {name}!")


greet_many("Hello", "Alice", "Bob", "Charlie")
print()

print("=== **kwargs (Variable Keyword Arguments) ===")

def print_info(**kwargs):
    """Print any keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, city="New York")
print()

print("=== **kwargs with Regular Arguments ===")

def create_person(name, age, **extra_info):
    """Create a person dict with optional extra info."""
    person = {"name": name, "age": age}
    person.update(extra_info)
    return person


person = create_person("Alice", 30, city="New York", job="Engineer")
print(f"Person: {person}")
print()

print("=== Combining *args and **kwargs ===")

def func(required, *args, **kwargs):
    """Function with all argument types."""
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


func("hello", 1, 2, 3, name="Alice", age=30)
print()

print("=== Unpacking with * and ** ===")

# Unpacking a list with *
numbers = [1, 2, 3]
print(f"print(*[1, 2, 3]):", end=" ")
print(*numbers)  # Equivalent to print(1, 2, 3)

# Unpacking a dict with **
info = {"name": "Alice", "age": 30}
print(f"print(**{{'name': 'Alice', 'age': 30}}):", end=" ")
# print(**info)  # This won't work with print, but works with function calls


def greet(name, age):
    print(f"{name} is {age} years old")


greet(**info)  # Unpack dict as keyword arguments
print()

print("=== Practical Example: Wrapper Function ===")

def log_function_call(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_function_call
def add(a, b):
    return a + b


@log_function_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


add(3, 5)
greet("Alice")
greet("Bob", greeting="Hi")
print()

print("=== Practical Example: Flexible Calculator ===")

def calculate(operation, *numbers):
    """Calculate with any number of arguments."""
    if not numbers:
        return 0
    
    result = numbers[0]
    
    if operation == "add":
        for num in numbers[1:]:
            result += num
    elif operation == "subtract":
        for num in numbers[1:]:
            result -= num
    elif operation == "multiply":
        for num in numbers[1:]:
            result *= num
    elif operation == "divide":
        for num in numbers[1:]:
            result /= num
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    return result


print(f"calculate('add', 1, 2, 3, 4) = {calculate('add', 1, 2, 3, 4)}")
print(f"calculate('multiply', 2, 3, 4) = {calculate('multiply', 2, 3, 4)}")
print()

print("=== Practical Example: Configuration Handler ===")

def configure(settings, **options):
    """Update settings with options."""
    settings.update(options)
    return settings


default_settings = {"host": "localhost", "port": 8080}
print(f"Default: {default_settings}")

configured = configure(default_settings, debug=True, timeout=30)
print(f"Configured: {configured}")
