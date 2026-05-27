"""
Inheritance - Class Inheritance and Method Overriding

This example demonstrates:
- Basic inheritance with super()
- Method overriding
- Multiple inheritance
- The issubclass() and isinstance() functions
"""

print("=== Basic Inheritance ===")


class Animal:
    """Base Animal class."""
    
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
    
    def speak(self) -> str:
        """Make the animal speak."""
        return f"{self.name} makes a sound."
    
    def __str__(self) -> str:
        return f"{self.name} ({self.species})"


class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name: str, breed: str):
        # Call parent __init__ using super()
        super().__init__(name, species="Canis lupus familiaris")
        self.breed = breed
    
    def speak(self) -> str:
        """Override speak method to bark."""
        return f"{self.name} barks: Woof!"
    
    def fetch(self, item: str) -> str:
        """Dog-specific method."""
        return f"{self.name} fetches the {item}!"


class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name: str, color: str):
        super().__init__(name, species="Felis catus")
        self.color = color
    
    def speak(self) -> str:
        """Override speak method to meow."""
        return f"{self.name} meows: Meow!"
    
    def scratch(self, furniture: str) -> str:
        """Cat-specific method."""
        return f"{self.name} scratches the {furniture}!"


# Create instances
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(f"dog: {dog}")
print(f"cat: {cat}")
print()

print("=== Method Overriding ===")

print(f"dog.speak(): {dog.speak()}")
print(f"cat.speak(): {cat.speak()}")

# Call parent class method using super()
print(f"super().speak() from dog: {super(Dog, dog).speak()}")
print()

print("=== Multiple Inheritance ===")


class Swimmer:
    """Mixin class for swimming ability."""
    
    def swim(self) -> str:
        return "Swimming..."


class Flyer:
    """Mixin class for flying ability."""
    
    def fly(self) -> str:
        return "Flying..."


class Duck(Animal, Swimmer, Flyer):
    """Duck class with multiple inheritance."""
    
    def __init__(self, name: str):
        super().__init__(name, species="Anas platyrhynchos")
    
    def speak(self) -> str:
        return f"{self.name} quacks: Quack!"


duck = Duck("Donald")
print(f"duck: {duck}")
print(f"duck.speak(): {duck.speak()}")
print(f"duck.swim(): {duck.swim()}")
print(f"duck.fly(): {duck.fly()}")
print()

print("=== issubclass() and isinstance() ===")

print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"issubclass(Animal, Dog): {issubclass(Animal, Dog)}")
print(f"issubclass(Dog, Dog): {issubclass(Dog, Dog)}")
print()

print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"isinstance(dog, Swimmer): {isinstance(dog, Swimmer)}")
print(f"isinstance(duck, Duck): {isinstance(duck, Duck)}")
print(f"isinstance(duck, Swimmer): {isinstance(duck, Swimmer)}")
print()

print("=== Method Resolution Order (MRO) ===")

# The order in which Python looks for methods
print(f"Duck.__mro__:")
for cls in Duck.__mro__:
    print(f"  {cls}")
print()

print("=== super() with Multiple Inheritance ===")


class Base:
    """Base class for MRO example."""
    
    def __init__(self):
        print("Base.__init__")
    
    def do_something(self):
        print("Base.do_something")


class A(Base):
    """Class A."""
    
    def __init__(self):
        print("A.__init__")
        super().__init__()
    
    def do_something(self):
        print("A.do_something")
        super().do_something()


class B(Base):
    """Class B."""
    
    def __init__(self):
        print("B.__init__")
        super().__init__()
    
    def do_something(self):
        print("B.do_something")
        super().do_something()


class C(A, B):
    """Class C inherits from A and B."""
    
    def __init__(self):
        print("C.__init__")
        super().__init__()
    
    def do_something(self):
        print("C.do_something")
        super().do_something()


print("Creating C():")
c = C()
print()

print("Calling c.do_something():")
c.do_something()
print()

print("=== Abstract Base Classes (ABC) ===")

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


class Rectangle(Shape):
    """Rectangle class implementing Shape."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle class implementing Shape."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


# This would fail:
# shape = Shape()  # Can't instantiate abstract class

rectangle = Rectangle(3, 4)
circle = Circle(5)

print(f"rectangle.area(): {rectangle.area()}")
print(f"rectangle.perimeter(): {rectangle.perimeter()}")
print(f"circle.area(): {circle.area():.2f}")
print(f"circle.perimeter(): {circle.perimeter():.2f}")
