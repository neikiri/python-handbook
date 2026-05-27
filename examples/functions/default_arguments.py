"""
Default Arguments - Function Parameters with Default Values

This example demonstrates:
- Setting default values for parameters
- When default values are evaluated
- Common patterns with mutable defaults
"""

print("=== Basic Default Arguments ===")

def greet(name="Guest", message="Hello"):
    """Greet someone with default values."""
    print(f"{message}, {name}!")


# Use all defaults
greet()

# Use some defaults (keyword arguments)
greet(name="Alice")
greet(message="Goodbye")

# Override all defaults
greet("Bob", "Hi")
print()

print("=== Default Values Are Evaluated Once ===")

import time


def log(message, timestamp=time.time()):
    """Log a message with a timestamp."""
    print(f"[{timestamp}] {message}")


print("Calling log immediately:")
log("First message")

print("Waiting 2 seconds...")
time.sleep(2)

print("Calling log after 2 seconds:")
log("Second message")  # Same timestamp as first!

print("\nNote: timestamp was evaluated when function was defined, not when called.")
print()

print("=== Better Pattern: Use None ===")

def log_better(message, timestamp=None):
    """Log a message with current timestamp."""
    if timestamp is None:
        timestamp = time.time()
    print(f"[{timestamp}] {message}")


print("Calling log_better immediately:")
log_better("First message")

print("Waiting 2 seconds...")
time.sleep(2)

print("Calling log_better after 2 seconds:")
log_better("Second message")  # Different timestamp!
print()

print("=== Default with Mutable Types ===")

# Problem: Default list is shared between calls
def add_item_bad(item, items=[]):
    """Add item to list (problematic)."""
    items.append(item)
    return items


print("Bad version (shared default):")
result1 = add_item_bad("apple")
print(f"First call: {result1}")

result2 = add_item_bad("banana")
print(f"Second call: {result2}")  # Contains both items!

print("\nBoth results point to the same list:")
print(f"result1 is result2: {result1 is result2}")
print()

# Solution: Use None and create new list
def add_item_good(item, items=None):
    """Add item to list (correct)."""
    if items is None:
        items = []
    items.append(item)
    return items


print("Good version (separate lists):")
result1 = add_item_good("apple")
print(f"First call: {result1}")

result2 = add_item_good("banana")
print(f"Second call: {result2}")  # Only contains banana

print("\nResults are different lists:")
print(f"result1 is result2: {result1 is result2}")
print()

print("=== Default with Dict ===")

# Problem: Default dict is shared
def add_config_bad(key, value, config={}):
    """Add config (problematic)."""
    config[key] = value
    return config


print("Bad version (shared default):")
result1 = add_config_bad("host", "localhost")
print(f"First call: {result1}")

result2 = add_config_bad("port", 8080)
print(f"Second call: {result2}")  # Contains both keys!
print()

# Solution: Use None
def add_config_good(key, value, config=None):
    """Add config (correct)."""
    if config is None:
        config = {}
    config[key] = value
    return config


print("Good version (separate dicts):")
result1 = add_config_good("host", "localhost")
print(f"First call: {result1}")

result2 = add_config_good("port", 8080)
print(f"Second call: {result2}")
print()

print("=== Default with Function Calls ===")

def create_person(name, age=0, tags=None):
    """Create a person dictionary."""
    if tags is None:
        tags = []
    
    return {
        "name": name,
        "age": age,
        "tags": tags,
    }


person1 = create_person("Alice", 30)
person2 = create_person("Bob", 25, ["developer", "designer"])

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print()

print("=== Default with Type Hints ===")

from typing import Optional, List


def greet_with_hints(name: str = "Guest", message: str = "Hello") -> str:
    """Greet with type hints."""
    return f"{message}, {name}!"


def add_to_list(item: str, items: Optional[List[str]] = None) -> List[str]:
    """Add item to list with type hints."""
    if items is None:
        items = []
    items.append(item)
    return items


print(greet_with_hints("Alice"))
print(add_to_list("apple"))
