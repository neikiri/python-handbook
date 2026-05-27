"""
When Not to Use OOP - Knowing When to Use Functions Instead

This example demonstrates:
- When simple functions are better than classes
- When classes are appropriate
- The principle: "Prefer functions over classes for simple tasks"
"""

print("=== Example 1: Simple Calculation ===")

print("Bad: Using a class for a simple calculation")


class AreaCalculator:
    """Unnecessary class for a simple calculation."""
    
    def __init__(self):
        pass
    
    def rectangle(self, width, height):
        return width * height


calc = AreaCalculator()
area = calc.rectangle(3, 4)
print(f"Area (using class): {area}")


# Good: Using a simple function
def rectangle_area(width, height):
    """Calculate rectangle area."""
    return width * height


area = rectangle_area(3, 4)
print(f"Area (using function): {area}")
print()

print("=== Example 2: Data Container ===")

print("Bad: Using a class as a simple data container")


class PersonData:
    """Unnecessary class for storing data."""
    
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


person = PersonData("Alice", 30, "New York")
print(f"Person: {person.name}, {person.age}, {person.city}")


# Good: Using a dict or dataclass
person_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person (dict): {person_dict['name']}, {person_dict['age']}, {person_dict['city']}")

# Or use a dataclass (when you need methods later)
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str


person = Person("Alice", 30, "New York")
print(f"Person (dataclass): {person}")
print()

print("=== Example 3: One-Time Use Logic ===")

print("Bad: Using a class for one-time logic")


class DataProcessor:
    """Unnecessary class for one-time processing."""
    
    def __init__(self, data):
        self.data = data
    
    def process(self):
        return [x * 2 for x in self.data if x > 0]


processor = DataProcessor([1, -2, 3, -4, 5])
result = processor.process()
print(f"Result (using class): {result}")


# Good: Using a simple function
def process_data(data):
    """Process data: double positive numbers."""
    return [x * 2 for x in data if x > 0]


result = process_data([1, -2, 3, -4, 5])
print(f"Result (using function): {result}")
print()

print("=== Example 4: Stateful vs Stateless ===")

print("Good: Using a class when state matters")


class Counter:
    """Counter that maintains state."""
    
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count
    
    def reset(self):
        self.count = 0


counter = Counter()
counter.increment()
counter.increment()
print(f"Counter count: {counter.get_count()}")
counter.reset()
print(f"After reset: {counter.get_count()}")
print()

print("Bad: Using a class for stateless operations")


class StringProcessor:
    """Unnecessary class for stateless string operations."""
    
    def __init__(self):
        pass
    
    def capitalize(self, text):
        return text.upper()
    
    def reverse(self, text):
        return text[::-1]


processor = StringProcessor()
print(f"Capitalized: {processor.capitalize('hello')}")
print(f"Reversed: {processor.reverse('hello')}")


# Good: Using functions
def capitalize(text):
    return text.upper()


def reverse(text):
    return text[::-1]


print(f"Capitalized: {capitalize('hello')}")
print(f"Reversed: {reverse('hello')}")
print()

print("=== Example 5: When to Use Each ===")

print("Use a CLASS when:")
print("  - You need to maintain state across multiple method calls")
print("  - You have related data and behavior that belongs together")
print("  - You need inheritance and polymorphism")
print("  - You're modeling a real-world entity with behavior")
print()

print("Use a FUNCTION when:")
print("  - You're doing a simple calculation or transformation")
print("  - You don't need to maintain state")
print("  - You're just transforming input to output")
print("  - The logic is a single, self-contained operation")
print()

print("=== Rule of Thumb ===")

print("If you find yourself doing this:")
print("  obj = MyClass()")
print("  result = obj.method(data)")
print()
print("And you don't reuse obj, consider:")
print("  result = function(data)")
