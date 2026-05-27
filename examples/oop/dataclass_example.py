"""
Dataclass Example - Using @dataclass for Simpler Classes

This example demonstrates:
- Using @dataclass decorator
- Automatic generation of __init__, __repr__, __eq__, etc.
- Field types and defaults
- Frozen dataclasses (immutable)
"""

from dataclasses import dataclass, field
from typing import List


print("=== Basic Dataclass ===")


@dataclass
class Person:
    """A simple Person class using dataclass."""
    name: str
    age: int
    city: str


# Create instances
person1 = Person("Alice", 30, "New York")
person2 = Person("Bob", 25, "Boston")

print(f"person1: {person1}")
print(f"person2: {person2}")
print()

print("=== Dataclass Methods ===")

# __repr__ is automatically generated
print(f"repr(person1): {repr(person1)}")

# __eq__ is automatically generated (compares all fields)
print(f"person1 == person2: {person1 == person2}")
print(f"person1 == Person('Alice', 30, 'New York'): {person1 == Person('Alice', 30, 'New York')}")
print()

print("=== Dataclass with Default Values ===")


@dataclass
class Product:
    """A product with default values."""
    name: str
    price: float = 0.0
    in_stock: bool = True


product1 = Product("Widget", 19.99)
product2 = Product("Gadget")
product3 = Product("Thingamajig", 9.99, False)

print(f"product1: {product1}")
print(f"product2: {product2}")
print(f"product3: {product3}")
print()

print("=== Dataclass with Complex Defaults ===")


@dataclass
class Team:
    """A team with a list of members."""
    name: str
    members: List[str] = field(default_factory=list)  # Use field() with default_factory


team1 = Team("Developers")
team2 = Team("Designers", ["Alice", "Bob"])

print(f"team1: {team1}")
print(f"team2: {team2}")

# Add members
team1.members.append("Charlie")
print(f"team1 after adding member: {team1}")
print()

print("=== Frozen Dataclass (Immutable) ===")


@dataclass(frozen=True)
class Point:
    """An immutable point."""
    x: float
    y: float


point = Point(3, 4)
print(f"point: {point}")
print(f"point.x: {point.x}")

# Try to modify (will raise an error)
try:
    point.x = 5
except Exception as e:
    print(f"\nError modifying frozen dataclass: {type(e).__name__}: {e}")
print()

print("=== Dataclass with Methods ===")


@dataclass
class Circle:
    """A circle with radius and methods."""
    radius: float = 1.0
    
    def area(self) -> float:
        """Calculate the area of the circle."""
        import math
        return math.pi * self.radius ** 2
    
    def circumference(self) -> float:
        """Calculate the circumference of the circle."""
        import math
        return 2 * math.pi * self.radius
    
    def scale(self, factor: float) -> None:
        """Scale the circle by a factor."""
        self.radius *= factor


circle = Circle(5)
print(f"circle: {circle}")
print(f"Area: {circle.area():.2f}")
print(f"Circumference: {circle.circumference():.2f}")

circle.scale(2)
print(f"After scaling by 2: {circle}")
print(f"New area: {circle.area():.2f}")
print()

print("=== Dataclass Inheritance ===")


@dataclass
class Animal:
    """Base Animal class."""
    name: str
    species: str


@dataclass
class Dog(Animal):
    """Dog class inheriting from Animal."""
    breed: str = "Unknown"
    
    def bark(self) -> str:
        return f"{self.name} says: Woof!"


dog = Dog("Buddy", "Golden Retriever", "Labrador")
print(f"dog: {dog}")
print(f"dog.bark(): {dog.bark()}")
print()

print("=== Dataclass with Custom __post_init__ ===")


@dataclass
class User:
    """User class with validation in __post_init__."""
    username: str
    age: int
    
    def __post_init__(self):
        """Validate after initialization."""
        if not self.username:
            raise ValueError("Username cannot be empty")
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if self.age > 150:
            raise ValueError("Age seems unrealistic")


# Valid user
try:
    user1 = User("alice", 30)
    print(f"Valid user: {user1}")
except ValueError as e:
    print(f"Error: {e}")

# Invalid user (negative age)
try:
    user2 = User("bob", -5)
    print(f"Valid user: {user2}")
except ValueError as e:
    print(f"Error creating user2: {e}")

# Invalid user (empty username)
try:
    user3 = User("", 25)
    print(f"Valid user: {user3}")
except ValueError as e:
    print(f"Error creating user3: {e}")
