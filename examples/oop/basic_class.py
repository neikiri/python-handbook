"""
Basic Class - Creating and Using Simple Classes

This example demonstrates:
- Defining a class with class keyword
- Creating instances (objects)
- Instance attributes
- Instance methods
- The self parameter
"""

print("=== Defining a Class ===")


class Dog:
    """A simple Dog class."""
    
    def __init__(self, name, age):
        """Initialize the dog with name and age."""
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says: Woof!"
    
    def get_human_years(self):
        """Calculate dog's age in human years."""
        return self.age * 7


print("Class defined. Now creating instances...")
print()

print("=== Creating Instances (Objects) ===")

# Create instances of Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"dog1: {dog1}")
print(f"dog2: {dog2}")
print(f"Are they the same object? {dog1 is dog2}")
print()

print("=== Accessing Attributes ===")

print(f"dog1.name: {dog1.name}")
print(f"dog1.age: {dog1.age}")
print(f"dog2.name: {dog2.name}")
print(f"dog2.age: {dog2.age}")
print()

print("=== Calling Methods ===")

print(dog1.bark())
print(dog2.bark())
print(f"dog1 in human years: {dog1.get_human_years()}")
print(f"dog2 in human years: {dog2.get_human_years()}")
print()

print("=== Modifying Attributes ===")

# Directly modify an attribute
dog1.age = 4
print(f"dog1.age after modification: {dog1.age}")
print(f"dog1.bark(): {dog1.bark()}")
print()

print("=== Adding Attributes After Creation ===")

# You can add attributes to an instance after creation
dog1.breed = "Golden Retriever"
print(f"dog1.breed: {dog1.breed}")

# But this attribute only exists on this instance
try:
    print(f"dog2.breed: {dog2.breed}")
except AttributeError as e:
    print(f"AttributeError: {e}")
print()

print("=== Class vs Instance Attributes ===")


class Cat:
    """Cat class with class and instance attributes."""
    
    # Class attribute (shared by all instances)
    species = "Felis catus"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age


cat1 = Cat("Whiskers", 2)
cat2 = Cat("Mittens", 4)

print(f"cat1.species: {cat1.species}")
print(f"cat2.species: {cat2.species}")
print(f"Cat.species: {Cat.species}")  # Access via class

# Modify class attribute
Cat.species = "Felis catus domesticus"
print(f"\nAfter modifying class attribute:")
print(f"cat1.species: {cat1.species}")
print(f"cat2.species: {cat2.species}")
print()

print("=== __str__ Method (String Representation) ===")


class Bird:
    """Bird class with __str__ method."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        """Return a string representation of the bird."""
        return f"{self.name} ({self.species})"
    
    def chirp(self):
        return f"{self.name} chirps!"


bird = Bird("Tweety", "Canary")
print(f"bird: {bird}")  # Uses __str__()
print(bird.chirp())
print()

print("=== __repr__ Method (Developer-Friendly Representation) ===")


class Point:
    """Point class with __repr__ method."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Return a developer-friendly representation."""
        return f"Point(x={self.x}, y={self.y})"
    
    def __str__(self):
        """Return a user-friendly representation."""
        return f"({self.x}, {self.y})"


point = Point(3, 4)
print(f"point (str): {point}")       # Uses __str__()
print(f"point (repr): {repr(point)}")  # Uses __repr__()
print()

print("=== Comparing Objects ===")


class Rectangle:
    """Rectangle class with comparison methods."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __eq__(self, other):
        """Check if two rectangles have the same area."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()
    
    def __lt__(self, other):
        """Check if this rectangle has smaller area."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()


rect1 = Rectangle(3, 4)  # Area: 12
rect2 = Rectangle(2, 6)  # Area: 12
rect3 = Rectangle(5, 5)  # Area: 25

print(f"rect1 (3x4): area={rect1.area()}")
print(f"rect2 (2x6): area={rect2.area()}")
print(f"rect3 (5x5): area={rect3.area()}")
print()

print(f"rect1 == rect2: {rect1 == rect2}")  # True (same area)
print(f"rect1 == rect3: {rect1 == rect3}")  # False
print(f"rect1 < rect3: {rect1 < rect3}")    # True (12 < 25)
