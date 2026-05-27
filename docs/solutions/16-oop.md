# Solutions 16: Object-Oriented Programming

## Overview

Chapter 16 exercises cover creating classes, using instance and class attributes, implementing special methods, inheritance, `super()`, and designing class hierarchies. This guide explains the reasoning behind each solution and highlights when OOP is the right tool.

---

## Notes Before Checking Solutions

OOP is a tool for organizing code, not a requirement. Use classes when you have data and behavior that naturally belong together, or when you need multiple instances of the same structure. For simple scripts and utility functions, plain functions are often cleaner.

---

## Warm-up Exercise Solutions

### Exercise 1: Create a Simple Class

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

book1 = Book("Fluent Python", "Luciano Ramalho", 792)
print(book1)           # Fluent Python by Luciano Ramalho
print(repr(book1))     # Book('Fluent Python', 'Luciano Ramalho', 792)
print(book1.summary()) # Fluent Python (792 pages)
```

**`__str__` vs. `__repr__`:**
- `__str__` is for human-readable output. It is called by `print()` and `str()`.
- `__repr__` is for developer-readable output. It should ideally be a valid Python expression that recreates the object. It is called by `repr()` and shown in the REPL.
- If you only define one, define `__repr__` — Python falls back to it for `__str__` if `__str__` is not defined.

---

### Exercise 2: Add Methods to a Class

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"

account = BankAccount("Alice", 1000)
account.deposit(500)   # Deposited $500. New balance: $1500
account.withdraw(200)  # Withdrew $200. New balance: $1300
```

**Raise exceptions for invalid operations** rather than returning error codes or printing errors. The caller can decide how to handle the error. This makes the class reusable in different contexts (CLI, web app, tests).

**`get_balance()`** returns the balance rather than accessing `account.balance` directly. This is a simple form of encapsulation — if you later want to add logic (like rounding), you only change one place.

---

### Exercise 3: Use Class Attributes

```python
class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(Dog.species)   # Canis familiaris
print(dog1.species)  # Canis familiaris (inherited from class)

Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Canis lupus familiaris (all instances see the change)
```

**Class attributes are shared across all instances.** Modifying `Dog.species` changes it for every `Dog` instance. Instance attributes (set with `self.x = ...`) are unique to each instance.

**Be careful with mutable class attributes.** If a class attribute is a list or dict, all instances share the same object. Appending to it from one instance affects all instances. Use instance attributes for mutable data.

---

### Exercise 4: Understand Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal)         # uses __str__ from Animal
    print(animal.speak()) # uses overridden speak()
```

**`self.__class__.__name__`** returns the name of the actual class of the instance, not the class where the method is defined. So `str(Dog("Buddy"))` prints `Buddy (Dog)`, not `Buddy (Animal)`.

**Polymorphism:** The `for` loop calls `animal.speak()` without knowing whether `animal` is a `Dog` or `Cat`. Python dispatches to the correct method based on the actual type. This is polymorphism — the same interface, different behavior.

---

## Practice Exercise Solutions

### Exercise 5: Use super() for Inheritance

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # initialize parent
        self.doors = doors

    def info(self):
        return f"{super().info()} ({self.doors} doors)"

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        return f"{super().info()} (capacity: {self.capacity} tons)"

car = Car("Toyota", "Camry", 4)
print(car.info())   # Toyota Camry (4 doors)

truck = Truck("Ford", "F-150", 2)
print(truck.info()) # Ford F-150 (capacity: 2 tons)
```

**Always call `super().__init__()`** in a subclass `__init__` to ensure the parent class is properly initialized. Forgetting this means the parent's attributes are never set, leading to `AttributeError` when you try to use them.

**`super().info()`** calls the parent's `info()` method. This avoids duplicating the parent's logic and ensures that if the parent changes, the child automatically benefits.

---

### Exercise 6: Implement Special Methods

```python
class Point:
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

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 1)

print(p1 == p2)    # True
print(p1 < p3)     # False (distance of p1 is 5, p3 is ~1.4)
print(p1 + p3)     # (4, 5)
print(len(p1))     # 5
```

**Special methods (dunder methods)** let your objects work with Python's built-in operators and functions. `__eq__` enables `==`, `__lt__` enables `<` (and, with `functools.total_ordering`, all comparison operators), `__add__` enables `+`, `__len__` enables `len()`.

**`__eq__` also affects `in` and `==` in collections.** If you define `__eq__`, also define `__hash__` if you want instances to be usable as dictionary keys or in sets. If you define `__eq__` without `__hash__`, Python sets `__hash__` to `None`, making instances unhashable.

---

### Exercise 7: Create a Class Hierarchy

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name}: ${self.salary}"

    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_info(self):
        return f"{super().get_info()} (manages {self.team_size} people)"

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_info(self):
        return f"{super().get_info()} (specializes in {self.language})"

employees = [
    Manager("Alice", 100000, 5),
    Developer("Bob", 80000, "Python"),
]

for emp in employees:
    print(emp.get_info())

for emp in employees:
    emp.give_raise(5000)  # inherited from Employee

print("\nAfter raises:")
for emp in employees:
    print(emp.get_info())
```

**`give_raise()` is defined once in `Employee`** and inherited by both `Manager` and `Developer`. This is the key benefit of inheritance — shared behavior lives in one place.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Game Character System

```python
class Character:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def heal(self, amount):
        self.health += amount

    def __str__(self):
        return f"{self.name} (HP: {self.health}, Mana: {self.mana})"

class Warrior(Character):
    def __init__(self, name, health, mana, strength):
        super().__init__(name, health, mana)
        self.strength = strength

    def attack(self):
        damage = self.strength * 1.5
        return f"{self.name} attacks for {damage:.0f} damage!"

class Mage(Character):
    def __init__(self, name, health, mana, intelligence):
        super().__init__(name, health, mana)
        self.intelligence = intelligence

    def cast_spell(self):
        if self.mana < 20:
            return f"{self.name} doesn't have enough mana!"
        self.mana -= 20
        damage = self.intelligence * 2
        return f"{self.name} casts a spell for {damage} damage!"

warrior = Warrior("Conan", 100, 20, 15)
mage = Mage("Gandalf", 60, 100, 18)

print(warrior.attack())    # Conan attacks for 22 damage!
print(mage.cast_spell())   # Gandalf casts a spell for 36 damage!
warrior.take_damage(10)
print(warrior)             # Conan (HP: 90, Mana: 20)
```

**`max(0, self.health - damage)`** prevents health from going below zero without an `if` statement. This is a common pattern for clamping values.

---

### Challenge 2: Implement a Data Container

```python
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.email}')"

    def __eq__(self, other):
        return self.email == other.email  # unique identifier

    def __lt__(self, other):
        return self.age < other.age

people = [
    Person("Alice", 30, "alice@example.com"),
    Person("Bob", 25, "bob@example.com"),
    Person("Carol", 28, "carol@example.com"),
]

print(sorted(people))  # sorted by age: Bob, Carol, Alice

alice = Person("Alice", 30, "alice@example.com")
print(alice in people)  # True — uses __eq__ (compares email)
```

**Using email as the equality key** makes sense because email addresses are unique identifiers. Two `Person` objects with the same email are the same person, even if the name or age differs.

---

## Common Mistakes

**Forgetting `self` in method definitions.** Every instance method must have `self` as its first parameter. `def bark():` inside a class will fail with `TypeError` when called.

**Not calling `super().__init__()`** in a subclass. The parent's `__init__` sets up the parent's attributes. Without calling it, those attributes do not exist.

**Mutable class attributes.** Using a list or dict as a class attribute means all instances share the same object. Use instance attributes for mutable data.

```python
# Bug: all Dog instances share the same tricks list
class Dog:
    tricks = []  # class attribute — shared!

    def add_trick(self, trick):
        self.tricks.append(trick)

# Fix: use an instance attribute
class Dog:
    def __init__(self):
        self.tricks = []  # instance attribute — unique per dog
```

**Overusing inheritance.** Inheritance is for "is-a" relationships. If `Car` is a `Vehicle`, inheritance makes sense. If you just want to reuse some methods, consider composition (storing an instance of another class as an attribute) instead.

---

## What to Review Next

- Chapter 17: Standard Library — using `dataclasses` for simpler data containers
- Chapter 18: Testing and Code Quality — testing classes with pytest
- Chapter 19: Type Hints — adding type annotations to class methods
