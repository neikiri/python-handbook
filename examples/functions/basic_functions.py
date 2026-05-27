"""
Basic Functions - Creating and Calling Functions

This example demonstrates:
- Defining functions with def
- Calling functions
- docstrings (function documentation)
- The None return value
"""

print("=== Defining a Function ===")

# Define a function with def
def greet():
    """Print a greeting message."""
    print("Hello, world!")


# Call the function
greet()
greet()
print()

print("=== Functions with Parameters ===")

def greet_person(name):
    """Greet a specific person by name."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")
print()

print("=== Functions with Return Values ===")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b


result = add(3, 5)
print(f"add(3, 5) = {result}")

# Return multiple values as a tuple
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)


nums = [1, 5, 3, 9, 2]
minimum, maximum = min_max(nums)
print(f"min_max([1, 5, 3, 9, 2]) = {minimum}, {maximum}")
print()

print("=== Functions with No Return (Implicit None) ===")

def print_info(message):
    """Print a message and return None."""
    print(f"Info: {message}")
    # No return statement, implicitly returns None


result = print_info("This is a message")
print(f"Return value: {result}")  # None
print()

print("=== Function with docstring ===")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area (length * width).
    """
    return length * width


# Access docstring
print(f"Function docstring:\n{calculate_area.__doc__}")
print()

# Use the function
area = calculate_area(10, 5)
print(f"Area of 10x5 rectangle: {area}")
print()

print("=== Nested Functions ===")

def outer_function():
    """Outer function with nested function."""
    print("Outer function")
    
    def inner_function():
        """Inner function, only visible inside outer_function."""
        print("Inner function")
    
    inner_function()


outer_function()
print()

# Inner function is not accessible outside
try:
    inner_function()
except NameError as e:
    print(f"Error: {e}")
print()

print("=== Function Annotations ===")

def greet(name: str, age: int) -> str:
    """Greet someone with their name and age."""
    return f"Hello, {name}! You are {age} years old."


# Annotations are stored in __annotations__
print(f"Annotations: {greet.__annotations__}")
print(greet("Alice", 30))
print()

print("=== Lambda Functions (Anonymous) ===")

# Small anonymous function defined with lambda
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"add(3, 4) = {add(3, 4)}")

# Lambda in a function
def apply_operation(numbers, operation):
    """Apply an operation to each number."""
    return [operation(n) for n in numbers]


numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, lambda x: x ** 2)
print(f"Squared: {squared}")
