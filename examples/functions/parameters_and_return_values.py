"""
Parameters and Return Values - Function Arguments and Returns

This example demonstrates:
- Positional arguments
- Keyword arguments
- Return values (single and multiple)
- Variable scope
"""

print("=== Positional Arguments ===")

def greet(name, message):
    """Greet someone with a message."""
    print(f"{message}, {name}!")


# Arguments are matched by position
greet("Alice", "Hello")      # Correct order
greet("Goodbye", "Bob")      # Wrong order - still works but message is wrong
print()

print("=== Keyword Arguments ===")

# Arguments matched by name, not position
greet(name="Alice", message="Hello")  # Clear and explicit
greet(message="Goodbye", name="Bob")  # Order doesn't matter
print()

print("=== Mixing Positional and Keyword Arguments ===")

def describe_person(name, age, city):
    """Describe a person."""
    print(f"{name} is {age} years old and lives in {city}.")


# Positional first, then keyword
describe_person("Alice", age=30, city="New York")

# All keyword
describe_person(name="Bob", age=25, city="Boston")
print()

print("=== Return Values ===")

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


result = add(3, 5)
print(f"add(3, 5) = {result}")

# Return different types
def get_info():
    """Return different types based on condition."""
    return "hello"  # Can return str, int, list, dict, etc.


print(f"get_info() = {get_info()}")
print()

print("=== Returning Multiple Values ===")

def min_max_average(numbers):
    """Return min, max, and average of a list."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average


nums = [1, 5, 3, 9, 2]
minimum, maximum, average = min_max_average(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.1f}")

# Or get as a tuple
result = min_max_average(nums)
print(f"As tuple: {result}")
print()

print("=== Returning None ===")

def find_item(items, target):
    """Find an item in a list, return None if not found."""
    for item in items:
        if item == target:
            return item
    return None  # Explicit return (or omit and it returns None)


fruits = ["apple", "banana", "cherry"]
print(f"find_item(fruits, 'banana'): {find_item(fruits, 'banana')}")
print(f"find_item(fruits, 'orange'): {find_item(fruits, 'orange')}")
print()

print("=== Variable Scope ===")

# Global variable
global_var = "I'm global"


def test_scope():
    """Test variable scope."""
    # Local variable
    local_var = "I'm local"
    print(f"Inside function:")
    print(f"  global_var: {global_var}")
    print(f"  local_var: {local_var}")


test_scope()
print(f"Outside function:")
print(f"  global_var: {global_var}")

try:
    print(f"  local_var: {local_var}")  # This will fail
except NameError:
    print("  local_var: Not accessible (NameError)")
print()

print("=== Modifying Global Variables ===")

counter = 0


def increment():
    """Increment the global counter."""
    global counter  # Tell Python to use the global variable
    counter += 1
    return counter


print(f"Initial counter: {counter}")
print(f"After increment(): {increment()}")
print(f"After increment(): {increment()}")
print()

print("=== Default Parameter Values ===")

def greet_with_default(name="Guest"):
    """Greet with a default name."""
    print(f"Hello, {name}!")


greet_with_default("Alice")  # Use provided name
greet_with_default()         # Use default name
print()

print("=== Mutable Default Arguments (Be Careful!) ===")

def add_item(item, items=[]):
    """Add item to list (problematic with default list)."""
    items.append(item)
    return items


# First call
result1 = add_item("apple")
print(f"First call: {result1}")  # ['apple']

# Second call - same list is reused!
result2 = add_item("banana")
print(f"Second call: {result2}")  # ['apple', 'banana']

# Better approach: use None and create new list
def add_item_safe(item, items=None):
    """Add item to list (safe version)."""
    if items is None:
        items = []
    items.append(item)
    return items


result1 = add_item_safe("apple")
result2 = add_item_safe("banana")
print(f"Safe version: {result1}, {result2}")
