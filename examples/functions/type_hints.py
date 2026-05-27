"""
Type Hints - Type Annotations for Functions

This example demonstrates:
- Basic type hints for parameters and return values
- Common type hints (int, str, float, bool, list, dict)
- Optional and Union types
- Type hints with *args and **kwargs
"""

from typing import List, Dict, Optional, Union, Tuple, Any


print("=== Basic Type Hints ===")

def greet(name: str) -> str:
    """Greet someone with type hints."""
    return f"Hello, {name}!"


result = greet("Alice")
print(result)

# Type hints don't enforce types at runtime
print(greet(123))  # Works, but not recommended
print()

print("=== Common Type Hints ===")

def process_data(count: int, name: str, price: float, active: bool) -> dict:
    """Process data with various types."""
    return {
        "count": count,
        "name": name,
        "price": price,
        "active": active,
    }


result = process_data(10, "widget", 9.99, True)
print(f"Result: {result}")
print()

print("=== List and Dict Types ===")

def sum_numbers(numbers: List[float]) -> float:
    """Sum a list of numbers."""
    return sum(numbers)


def get_person_info(person: Dict[str, Union[str, int]]) -> str:
    """Get person info as a string."""
    return f"{person['name']} is {person['age']} years old."


print(f"sum_numbers([1.5, 2.5, 3.0]) = {sum_numbers([1.5, 2.5, 3.0])}")
print(f"get_person_info({{'name': 'Alice', 'age': 30}}) = {get_person_info({'name': 'Alice', 'age': 30})}")
print()

print("=== Optional Type ===")

def find_item(items: List[str], target: str) -> Optional[str]:
    """Find an item, return None if not found."""
    for item in items:
        if item == target:
            return item
    return None


fruits = ["apple", "banana", "cherry"]
print(f"find_item(fruits, 'banana'): {find_item(fruits, 'banana')}")
print(f"find_item(fruits, 'orange'): {find_item(fruits, 'orange')}")
print()

print("=== Union Type ===")

def process_value(value: Union[int, str]) -> str:
    """Process a value that can be int or str."""
    if isinstance(value, int):
        return f"Integer: {value}"
    else:
        return f"String: {value}"


print(f"process_value(42): {process_value(42)}")
print(f"process_value('hello'): {process_value('hello')}")
print()

print("=== Tuple Type ===")

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)


x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})")
print()

print("=== Any Type ===")

def process_any(value: Any) -> str:
    """Process any type of value."""
    return f"Received: {value} (type: {type(value).__name__})"


print(process_any(42))
print(process_any("hello"))
print(process_any([1, 2, 3]))
print()

print("=== Type Hints with *args and **kwargs ===")

def log_messages(*messages: str) -> None:
    """Log multiple string messages."""
    for msg in messages:
        print(f"Log: {msg}")


log_messages("Info", "Warning", "Error")
print()


def configure(**options: str) -> Dict[str, str]:
    """Configure with string options."""
    return options


config = configure(host="localhost", port="8080")
print(f"Config: {config}")
print()

print("=== Type Hints with Default Values ===")

def greet(name: str = "Guest", age: int = 0) -> str:
    """Greet with default values."""
    return f"Hello, {name}! You are {age} years old."


print(greet())
print(greet("Alice", 30))
print()

print("=== Type Hints with Optional Parameters ===")

def create_person(name: str, age: int = 0, email: Optional[str] = None) -> dict:
    """Create a person dict with optional email."""
    person = {"name": name, "age": age}
    if email is not None:
        person["email"] = email
    return person


print(create_person("Alice", 30))
print(create_person("Bob", 25, "bob@example.com"))
print()

print("=== Type Hints Don't Enforce at Runtime ===")

def add(a: int, b: int) -> int:
    """Add two integers (type hints say int, but won't enforce)."""
    return a + b


# These work even though types don't match hints:
print(add(1, 2))        # Correct
print(add("a", "b"))    # String concatenation
print(add([1], [2]))    # List concatenation

print("\nNote: Type hints are for documentation and static analysis tools.")
print("Use mypy for static type checking: mypy script.py")
