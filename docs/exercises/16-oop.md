# Chapter 16: Object-Oriented Programming — Exercises

## Overview

These exercises help you master classes, objects, inheritance, and other OOP concepts. By the end, you will write well-structured, reusable code using OOP principles.

---

## How to Use These Exercises

- Create a folder called `chapter-16` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Create a Simple Class

Create a file called `simple_class.py`:

```python
class Book:
    """Represents a book."""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def summary(self):
        return f"{self.title} ({self.pages} pages)"

# Create instances
book1 = Book("Fluent Python", "Luciano Ramalho", 792)
book2 = Book("Clean Code", "Robert Martin", 431)

print(book1)
print(book2)
print(book1.summary())
print(book2.summary())
```

Run it and observe class creation.

---

### Exercise 2: Add Methods to a Class

Create a file called `class_methods.py`:

```python
class BankAccount:
    """Represents a bank account."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Get current balance."""
        return self.balance
    
    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"

# Use the class
account = BankAccount("Alice", 1000)
print(account)

account.deposit(500)
account.withdraw(200)
print(f"Final balance: ${account.get_balance()}")
```

Run it and observe methods.

---

### Exercise 3: Use Class Attributes

Create a file called `class_attributes.py`:

```python
class Dog:
    """Represents a dog."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"

# Create instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Species: {Dog.species}")
print(f"Dog 1: {dog1}")
print(f"Dog 2: {dog2}")
print(dog1.bark())
print(dog2.bark())

# Modify class attribute
Dog.species = "Canis lupus familiaris"
print(f"Updated species: {Dog.species}")
```

Run it and observe class attributes.

---

### Exercise 4: Understand Inheritance

Create a file called `inheritance.py`:

```python
class Animal:
    """Base class for animals."""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

class Dog(Animal):
    """Dog inherits from Animal."""
    
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    """Cat inherits from Animal."""
    
    def speak(self):
        return f"{self.name} says: Meow!"

class Bird(Animal):
    """Bird inherits from Animal."""
    
    def speak(self):
        return f"{self.name} says: Tweet!"

# Create instances
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety"),
]

for animal in animals:
    print(animal)
    print(animal.speak())
```

Run it and observe inheritance.

---

## Practice Exercises

### Exercise 5: Use super() for Inheritance

Create a file called `super_inheritance.py`:

```python
class Vehicle:
    """Base class for vehicles."""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Car inherits from Vehicle."""
    
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def info(self):
        return f"{super().info()} ({self.doors} doors)"

class Truck(Vehicle):
    """Truck inherits from Vehicle."""
    
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity
    
    def info(self):
        return f"{super().info()} (capacity: {self.capacity} tons)"

# Create instances
car = Car("Toyota", "Camry", 4)
truck = Truck("Ford", "F-150", 2)

print(car.info())
print(truck.info())
```

Run it and observe super().

---

### Exercise 6: Implement Special Methods

Create a file called `special_methods.py`:

```python
class Point:
    """Represents a 2D point."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

# Use special methods
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 1)

print(f"p1: {p1}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p3: {p1 < p3}")
print(f"p1 + p3: {p1 + p3}")
print(f"len(p1): {len(p1)}")
```

Run it and observe special methods.

---

### Exercise 7: Create a Class Hierarchy

Create a file called `class_hierarchy.py`:

```python
class Employee:
    """Base class for employees."""
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"{self.name}: ${self.salary}"
    
    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    """Manager inherits from Employee."""
    
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def get_info(self):
        return f"{super().get_info()} (manages {self.team_size} people)"

class Developer(Employee):
    """Developer inherits from Employee."""
    
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def get_info(self):
        return f"{super().get_info()} (specializes in {self.language})"

# Create instances
employees = [
    Manager("Alice", 100000, 5),
    Developer("Bob", 80000, "Python"),
    Developer("Carol", 85000, "JavaScript"),
]

for emp in employees:
    print(emp.get_info())

# Give raises
for emp in employees:
    emp.give_raise(5000)

print("\nAfter raises:")
for emp in employees:
    print(emp.get_info())
```

Run it and observe class hierarchy.

---

## Challenge Exercises

### Challenge 1: Build a Game Character System

Create a file called `game_characters.py`:

```python
class Character:
    """Base class for game characters."""
    
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health += amount
    
    def __str__(self):
        return f"{self.name} (HP: {self.health}, Mana: {self.mana})"

class Warrior(Character):
    """Warrior character."""
    
    def __init__(self, name, health, mana, strength):
        super().__init__(name, health, mana)
        self.strength = strength
    
    def attack(self):
        damage = self.strength * 1.5
        return f"{self.name} attacks with {damage} damage!"

class Mage(Character):
    """Mage character."""
    
    def __init__(self, name, health, mana, intelligence):
        super().__init__(name, health, mana)
        self.intelligence = intelligence
    
    def cast_spell(self):
        if self.mana < 20:
            return f"{self.name} doesn't have enough mana!"
        self.mana -= 20
        damage = self.intelligence * 2
        return f"{self.name} casts a spell for {damage} damage!"

# Create characters
warrior = Warrior("Conan", 100, 20, 15)
mage = Mage("Gandalf", 60, 100, 18)

print(warrior)
print(mage)

print(warrior.attack())
print(mage.cast_spell())

warrior.take_damage(10)
print(warrior)
```

Run it and observe the game system.

---

### Challenge 2: Implement a Data Container

Create a file called `data_container.py`:

```python
class Person:
    """Represents a person."""
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.email}')"
    
    def __eq__(self, other):
        return self.email == other.email
    
    def __lt__(self, other):
        return self.age < other.age

# Create and sort people
people = [
    Person("Alice", 30, "alice@example.com"),
    Person("Bob", 25, "bob@example.com"),
    Person("Carol", 28, "carol@example.com"),
]

print("Original:")
for person in people:
    print(f"  {person}")

print("\nSorted by age:")
for person in sorted(people):
    print(f"  {person}")

print("\nFind Alice:")
alice = Person("Alice", 30, "alice@example.com")
print(f"  Found: {alice in people}")
```

Run it and observe the data container.

---

## Hints

**AttributeError: 'X' object has no attribute 'Y'** → The attribute doesn't exist. Check the `__init__` method or use `hasattr()` to check.

**TypeError: __init__() missing required positional argument** → You forgot to pass a required argument when creating an instance.

**Inheritance not working** → Check that the child class calls `super().__init__()` to initialize the parent class.

**Method not overriding** → Ensure the method name and signature match exactly.

---

## What to Review If You Get Stuck

- **Classes and objects** → Handbook section 2.1
- **Instance attributes and methods** → Handbook section 2.2
- **Class attributes** → Handbook section 2.3
- **Inheritance** → Handbook section 2.4
- **Special methods** → Handbook section 2.5
- **When to use classes** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Create classes with attributes and methods
- Use `__init__` to initialize objects
- Implement special methods like `__str__` and `__repr__`
- Use inheritance to create class hierarchies
- Override methods in subclasses
- Use `super()` to call parent methods
- Implement comparison operators
- Design well-structured OOP code
- Know when to use classes vs. functions

