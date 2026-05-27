# Chapter 16: Object-Oriented Programming

## 1. Overview

Object-oriented programming (OOP) is a way of organising code around
**objects** — bundles of data and the functions that operate on that data.
Instead of writing a collection of separate variables and functions, you
define a **class** that describes what an object looks like and what it can
do, then create as many instances of that class as you need.

Python supports OOP fully, but it does not force you to use it. Simple
scripts and pure functions are often the right choice. OOP becomes valuable
when you have a concept that naturally carries both state (data) and behaviour
(actions), and when you need multiple independent copies of that concept in
the same program.

---

## 2. What You Will Learn

- What a class is and when to use one
- Defining a class with `class`
- Creating objects (instances)
- Instance attributes and `__init__`
- What `self` is and why it is needed
- Instance methods
- Class attributes vs. instance attributes
- The `__str__` and `__repr__` dunder methods
- Inheritance: subclasses and `super()`
- Method overriding
- The `@dataclass` decorator as a simpler alternative
- Brief overview of `__eq__` and `__lt__`
- When NOT to use classes

---

## 3. Core Concepts

### 3.1 What Is a Class?

A **class** is a blueprint. It defines what data an object holds and what
operations it supports. An **object** (also called an **instance**) is a
concrete thing built from that blueprint.

Think of a class as a cookie cutter and objects as the cookies. The cutter
defines the shape; each cookie is a separate, independent thing.

```python
class Book:
    pass   # empty class — valid Python, does nothing yet
```

You create an instance by calling the class like a function:

```python
b = Book()
print(type(b))   # <class '__main__.Book'>
```

---

### 3.2 `__init__` and Instance Attributes

The `__init__` method runs automatically when a new instance is created. Use
it to set up the object's initial state by assigning **instance attributes**.

```python
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
```

Create instances by passing arguments to the class:

```python
b1 = Book("Fluent Python", "Luciano Ramalho", 792)
b2 = Book("Clean Code", "Robert Martin", 431)

print(b1.title)    # Fluent Python
print(b2.author)   # Robert Martin
print(b1.pages)    # 792
```

Each instance has its own copy of the attributes. Changing `b1.title` does
not affect `b2.title`.

---

### 3.3 `self` — What It Is and Why It Is Needed

`self` is a reference to the instance the method is being called on. Python
passes it automatically as the first argument to every instance method.

```python
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title    # store on this specific instance
        self.author = author
        self.pages = pages
```

When you write `b1 = Book("Fluent Python", ...)`, Python calls
`Book.__init__(b1, "Fluent Python", ...)` behind the scenes. `self` is `b1`.

The name `self` is a convention, not a keyword. You could use any name, but
always use `self` — every Python programmer expects it.

---

### 3.4 Instance Methods

An **instance method** is a function defined inside a class that operates on
an instance. It always takes `self` as its first parameter.

```python
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self) -> str:
        """Return a one-line description of the book."""
        return f'"{self.title}" by {self.author} ({self.pages} pages)'

    def is_long(self) -> bool:
        """Return True if the book has more than 500 pages."""
        return self.pages > 500


b = Book("Fluent Python", "Luciano Ramalho", 792)
print(b.summary())    # "Fluent Python" by Luciano Ramalho (792 pages)
print(b.is_long())    # True
```

Calling `b.summary()` is shorthand for `Book.summary(b)`. Python fills in
`self` for you.

---

### 3.5 Class Attributes vs. Instance Attributes

An **instance attribute** belongs to one specific object. A **class
attribute** belongs to the class itself and is shared by all instances.

```python
class Book:
    # Class attribute — shared by all Book instances
    media_type: str = "print"

    def __init__(self, title: str, author: str, pages: int) -> None:
        # Instance attributes — unique to each object
        self.title = title
        self.author = author
        self.pages = pages


b1 = Book("Fluent Python", "Luciano Ramalho", 792)
b2 = Book("Clean Code", "Robert Martin", 431)

print(b1.media_type)   # print
print(b2.media_type)   # print
print(Book.media_type) # print — accessible on the class too
```

If you assign to `b1.media_type`, you create a new instance attribute that
shadows the class attribute for that object only. The class attribute and
other instances are unaffected.

```python
b1.media_type = "ebook"
print(b1.media_type)   # ebook  — instance attribute
print(b2.media_type)   # print  — still the class attribute
print(Book.media_type) # print  — class attribute unchanged
```

A common use for class attributes is a counter that tracks how many instances
have been created:

```python
class Book:
    count: int = 0   # class attribute

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        Book.count += 1   # update the class attribute, not self.count


b1 = Book("Fluent Python", "Luciano Ramalho", 792)
b2 = Book("Clean Code", "Robert Martin", 431)
print(Book.count)   # 2
```

---

### 3.6 `__str__` and `__repr__`

Python calls `__str__` when you pass an object to `print()` or `str()`. It
should return a human-readable string.

Python calls `__repr__` when you inspect an object in the REPL or call
`repr()`. It should return an unambiguous string — ideally one that could be
used to recreate the object.

```python
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author}'

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r}, {self.pages!r})"


b = Book("Fluent Python", "Luciano Ramalho", 792)

print(b)       # "Fluent Python" by Luciano Ramalho
print(repr(b)) # Book('Fluent Python', 'Luciano Ramalho', 792)
print([b])     # [Book('Fluent Python', 'Luciano Ramalho', 792)]
```

If you only define one, define `__repr__`. Python falls back to `__repr__`
when `__str__` is not defined. Without either, you get something like
`<__main__.Book object at 0x...>`, which is not helpful.

---

### 3.7 `__eq__` and `__lt__` (Brief Overview)

By default, two instances are equal only if they are the same object in
memory. Define `__eq__` to compare by value, and `__lt__` to support
`sorted()` and comparison operators.

```python
class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __lt__(self, other: "Book") -> bool:
        return self.title < other.title   # sort alphabetically by title


b1 = Book("Clean Code", "Robert Martin", 431)
b2 = Book("Clean Code", "Robert Martin", 500)
b3 = Book("Fluent Python", "Luciano Ramalho", 792)

print(b1 == b2)                       # True  — same title and author
print(sorted([b3, b1])[0].title)      # Clean Code
```

`@dataclass(order=True)` generates all comparison methods automatically, so
you rarely need to write these by hand.

---

### 3.8 Inheritance

**Inheritance** lets one class (the **subclass**) build on another (the
**parent class** or **superclass**). The subclass gets all the attributes and
methods of the parent and can add or override them.

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.name!r})"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Meow!"


dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())   # Rex says: Woof!
print(cat.speak())   # Whiskers says: Meow!
print(dog)           # Dog('Rex')
```

`Dog` and `Cat` inherit `__init__` and `__str__` from `Animal`. They only
override `speak`.

#### `isinstance()` and `issubclass()`

```python
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True — Dog is a subclass of Animal
print(isinstance(dog, Cat))     # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False
```

---

### 3.9 `super()`

`super()` gives you access to the parent class. Use it in `__init__` to call
the parent's initialiser before adding subclass-specific setup.

```python
class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def describe(self) -> str:
        return f"{self.name}, age {self.age}"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)   # call Animal.__init__
        self.breed = breed            # add Dog-specific attribute

    def describe(self) -> str:
        base = super().describe()     # call Animal.describe
        return f"{base}, breed: {self.breed}"


d = Dog("Rex", 3, "Labrador")
print(d.describe())   # Rex, age 3, breed: Labrador
print(d.name)         # Rex — set by Animal.__init__ via super()
```

Always call `super().__init__(...)` in a subclass `__init__` unless you have
a specific reason not to. Forgetting it means the parent's setup code never
runs.

---

### 3.10 Method Overriding

A subclass can **override** any method from the parent by defining a method
with the same name. The subclass version replaces the parent version for
instances of the subclass.

```python
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area().")

    def describe(self) -> str:
        return f"{type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(shape.describe())

# Circle with area 78.54
# Rectangle with area 24.00
```

Notice that `describe()` is defined once in `Shape` and works correctly for
all subclasses because it calls `self.area()`, which dispatches to the right
override at runtime. This is called **polymorphism**.

---

### 3.11 `@dataclass` — A Simpler Alternative

Writing `__init__`, `__repr__`, and `__eq__` by hand for every data-holding
class is repetitive. The `dataclasses` module (standard library, Python 3.7+)
generates them for you.

```python
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
```

That is the entire class. Python generates:

- `__init__(self, title, author, pages)`
- `__repr__` that shows all fields
- `__eq__` that compares all fields

```python
b1 = Book("Fluent Python", "Luciano Ramalho", 792)
b2 = Book("Fluent Python", "Luciano Ramalho", 792)
b3 = Book("Clean Code", "Robert Martin", 431)

print(b1)          # Book(title='Fluent Python', author='Luciano Ramalho', pages=792)
print(b1 == b2)    # True  — same field values
print(b1 == b3)    # False
```

#### Default values

```python
from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    pages: int
    tags: list[str] = field(default_factory=list)   # mutable default
    rating: float = 0.0                              # immutable default


b = Book("Fluent Python", "Luciano Ramalho", 792)
b.tags.append("python")
print(b)
# Book(title='Fluent Python', author='Luciano Ramalho', pages=792, tags=['python'], rating=0.0)
```

Use `field(default_factory=list)` for mutable defaults (lists, dicts). Never
use `tags: list[str] = []` directly — that is the same mutable-default bug
that affects regular functions.

#### Ordering and frozen dataclasses

Pass `order=True` to generate comparison methods (`__lt__`, `__le__`, etc.)
based on field order. Pass `frozen=True` to make instances immutable:

```python
@dataclass(order=True)
class Book:
    title: str
    author: str
    pages: int


books = [
    Book("Fluent Python", "Luciano Ramalho", 792),
    Book("Clean Code", "Robert Martin", 431),
]
print(sorted(books)[0].title)   # Clean Code — sorted by title first


@dataclass(frozen=True)
class Point:
    x: float
    y: float


p = Point(1.0, 2.0)
# p.x = 3.0   # FrozenInstanceError
```

#### When to use `@dataclass` vs. a regular class

Use `@dataclass` when the class is primarily a container for data with little
or no custom behaviour. Use a regular class when you need fine-grained control
over `__init__`, complex validation, or significant custom logic.

---

### 3.12 When NOT to Use Classes

OOP is a tool, not a requirement. Avoid classes when:

- **A simple function does the job.** If you only need to transform some input
  into output, a function is cleaner.
- **There is no meaningful state.** A class with only one method and no
  instance attributes is usually better written as a function.
- **You are writing a short script.** Top-level code with functions is fine
  for scripts under ~100 lines.
- **You are grouping utility functions.** A module with functions is simpler
  than a class full of static methods.

```python
# Unnecessary class — just use a function
class Greeter:
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

g = Greeter()
print(g.greet("Alice"))

# Simpler
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))
```

Use classes when you have multiple instances that each carry their own state,
or when inheritance and polymorphism genuinely simplify the design.

---

## 4. Practical Examples

### 4.1 A `BankAccount` Class

A bank account has state (balance) and behaviour (deposit, withdraw). This is
a natural fit for a class.

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance   # leading underscore = "private by convention"

    @property
    def balance(self) -> float:
        """Read-only access to the balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive, got {amount}.")
        self._balance += amount
        print(f"Deposited {amount:.2f}. Balance: {self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive, got {amount}.")
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds: tried to withdraw {amount:.2f}, "
                f"balance is {self._balance:.2f}."
            )
        self._balance -= amount
        print(f"Withdrew {amount:.2f}. Balance: {self._balance:.2f}")

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"

    def __repr__(self) -> str:
        return f"BankAccount({self.owner!r}, {self._balance!r})"


account = BankAccount("Alice", 100.0)
account.deposit(50.0)     # Deposited 50.00. Balance: 150.00
account.withdraw(30.0)    # Withdrew 30.00. Balance: 120.00
print(account.balance)    # 120.0
print(account)            # BankAccount(owner='Alice', balance=120.00)
```

The `@property` decorator lets you expose `balance` as a read-only attribute.
Callers write `account.balance`, not `account.balance()`.

---

### 4.2 Inheritance: `SavingsAccount`

```python
class SavingsAccount(BankAccount):
    """A bank account that earns interest."""

    def __init__(self, owner: str, balance: float = 0.0,
                 interest_rate: float = 0.02) -> None:
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """Add interest to the balance."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(
            f"Interest applied: {interest:.2f} "
            f"({self.interest_rate:.1%}). Balance: {self._balance:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"SavingsAccount({self.owner!r}, {self._balance!r}, "
            f"{self.interest_rate!r})"
        )


savings = SavingsAccount("Bob", 1000.0, interest_rate=0.05)
savings.deposit(200.0)       # Deposited 200.00. Balance: 1200.00
savings.apply_interest()     # Interest applied: 60.00 (5.0%). Balance: 1260.00
print(savings.balance)       # 1260.0

# isinstance checks
print(isinstance(savings, SavingsAccount))  # True
print(isinstance(savings, BankAccount))     # True
```

`SavingsAccount` inherits `deposit`, `withdraw`, `balance`, and `__str__`
from `BankAccount`. It adds `apply_interest` and overrides `__repr__`.

---

### 4.3 A `Book` Catalogue with `@dataclass`

```python
from dataclasses import dataclass, field


@dataclass(order=True)
class Book:
    title: str
    author: str
    year: int
    pages: int
    tags: list[str] = field(default_factory=list, compare=False)

    def is_recent(self, since: int = 2015) -> bool:
        return self.year >= since

    def short_description(self) -> str:
        return f"{self.title} ({self.year}) — {self.author}"


class Catalogue:
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add(self, book: Book) -> None:
        self._books.append(book)

    def find_by_author(self, author: str) -> list[Book]:
        return [b for b in self._books if b.author.lower() == author.lower()]

    def recent_books(self, since: int = 2015) -> list[Book]:
        return sorted(b for b in self._books if b.is_recent(since))

    def __len__(self) -> int:
        return len(self._books)

    def __repr__(self) -> str:
        return f"Catalogue({len(self)} books)"


catalogue = Catalogue()
catalogue.add(Book("Fluent Python", "Luciano Ramalho", 2022, 792, ["python", "advanced"]))
catalogue.add(Book("Clean Code", "Robert Martin", 2008, 431, ["practices"]))
catalogue.add(Book("The Pragmatic Programmer", "David Thomas", 2019, 352))

print(catalogue)                          # Catalogue(3 books)
print(len(catalogue))                     # 3

for book in catalogue.recent_books(2015):
    print(book.short_description())
# Fluent Python (2022) — Luciano Ramalho
# The Pragmatic Programmer (2019) — David Thomas
```

---

### 4.4 Polymorphism with Shapes

```python
import math
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def describe(self) -> str:
        return (
            f"Circle(r={self.radius}) — "
            f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"
        )


@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def describe(self) -> str:
        return (
            f"Rectangle({self.width}x{self.height}) — "
            f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"
        )


@dataclass
class Triangle:
    base: float
    height: float
    side_a: float
    side_b: float

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        return self.base + self.side_a + self.side_b

    def describe(self) -> str:
        return (
            f"Triangle(base={self.base}, h={self.height}) — "
            f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"
        )


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5, 4)]

total_area = 0.0
for shape in shapes:
    print(shape.describe())
    total_area += shape.area()

print(f"\nTotal area: {total_area:.2f}")
# Circle(r=5) — area=78.54, perimeter=31.42
# Rectangle(4x6) — area=24.00, perimeter=20.00
# Triangle(base=3, h=4) — area=6.00, perimeter=12.00
#
# Total area: 108.54
```

Each shape class has its own `area()` and `perimeter()`. The loop calls them
without knowing which specific shape it is dealing with — that is
polymorphism.

---

### 4.5 A Simple `Stack` Class

```python
class Stack:
    """A last-in, first-out (LIFO) data structure."""

    def __init__(self) -> None:
        self._items: list = []

    def push(self, item) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek at an empty stack.")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)          # Stack([1, 2, 3])
print(s.peek())   # 3
print(s.pop())    # 3
print(len(s))     # 2
```

---

### 4.6 Using `__str__` and `__repr__` Together

```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        return self.celsius + 273.15

    def __str__(self) -> str:
        return f"{self.celsius:.1f}°C"

    def __repr__(self) -> str:
        return f"Temperature({self.celsius!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

    def __lt__(self, other: "Temperature") -> bool:
        return self.celsius < other.celsius


boiling = Temperature(100)
freezing = Temperature(0)
body = Temperature(37)

print(boiling)                  # 100.0°C
print(repr(boiling))            # Temperature(100)
print(boiling.fahrenheit)       # 212.0
print(boiling.kelvin)           # 373.15

temps = [boiling, body, freezing]
print(sorted(temps))            # [0.0°C, 37.0°C, 100.0°C]
```

---

## 5. Common Mistakes

### 5.1 Forgetting `self` in Method Definitions

Every instance method must have `self` as its first parameter. Forgetting it
causes a `TypeError` when you call the method.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment():   # Wrong — missing self
        self.count += 1


c = Counter()
c.increment()
# TypeError: Counter.increment() takes 0 positional arguments but 1 was given
```

Fix: add `self`.

```python
def increment(self):
    self.count += 1
```

---

### 5.2 Assigning to the Class Instead of the Instance

If you forget `self.` when setting an attribute in `__init__`, you create a
local variable that disappears when `__init__` returns.

```python
class Book:
    def __init__(self, title: str) -> None:
        title = title   # Wrong — local variable, not an attribute

b = Book("Fluent Python")
print(b.title)   # AttributeError: 'Book' object has no attribute 'title'
```

Fix: use `self.title = title`.

---

### 5.3 Mutable Default Arguments in `__init__`

The same mutable-default bug that affects functions also affects `__init__`.

```python
class Playlist:
    def __init__(self, name: str, songs=[]) -> None:   # Wrong
        self.name = name
        self.songs = songs


p1 = Playlist("Rock")
p2 = Playlist("Pop")
p1.songs.append("Song A")
print(p2.songs)   # ['Song A'] — shared list!
```

Fix: use `None` and create the list inside `__init__`.

```python
class Playlist:
    def __init__(self, name: str, songs: list[str] | None = None) -> None:
        self.name = name
        self.songs = songs if songs is not None else []
```

Or use `@dataclass` with `field(default_factory=list)`.

---

### 5.4 Forgetting to Call `super().__init__()`

When a subclass defines `__init__`, it must call `super().__init__()` to
ensure the parent class is properly initialised.

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        # Forgot super().__init__(name)
        self.breed = breed


d = Dog("Rex", "Labrador")
print(d.breed)   # Labrador
print(d.name)    # AttributeError: 'Dog' object has no attribute 'name'
```

Fix: call `super().__init__(name)` first.

---

### 5.5 Overusing Classes for Simple Tasks

Not everything needs a class. A function is simpler and easier to test.

```python
# Unnecessary
class TaxCalculator:
    def calculate(self, price: float, rate: float) -> float:
        return price * (1 + rate)

calc = TaxCalculator()
print(calc.calculate(100, 0.2))

# Simpler
def calculate_tax(price: float, rate: float) -> float:
    return price * (1 + rate)

print(calculate_tax(100, 0.2))
```

---

### 5.6 Confusing Class Attributes and Instance Attributes

Mutating a mutable class attribute (like a list) through an instance modifies
it for all instances. This is almost never what you want.

```python
class Team:
    members = []   # class attribute — shared by all instances

    def add_member(self, name: str) -> None:
        self.members.append(name)   # modifies the shared list!


t1 = Team()
t2 = Team()
t1.add_member("Alice")
print(t2.members)   # ['Alice'] — unexpected!
```

Fix: create the list as an instance attribute in `__init__`.

```python
class Team:
    def __init__(self) -> None:
        self.members: list[str] = []   # each instance gets its own list

    def add_member(self, name: str) -> None:
        self.members.append(name)
```

---

### 5.7 Not Defining `__repr__`

Without `__repr__`, debugging is painful because you see unhelpful output
like `<__main__.Book object at 0x7f3a1b2c3d40>`.

Always define at least `__repr__` for any class you write. If you use
`@dataclass`, it is generated for you automatically.

---

## 6. Practice Tasks

1. Define a `Rectangle` class with `width` and `height` attributes. Add
   methods `area()`, `perimeter()`, and `is_square()`. Add `__str__` and
   `__repr__`.

2. Define a `Student` class with `name`, `grade` (0–100), and a method
   `letter_grade()` that returns `"A"`, `"B"`, `"C"`, `"D"`, or `"F"` based
   on the score. Add `__str__`.

3. Define a `Vehicle` base class with `make`, `model`, and `year` attributes
   and a `description()` method. Create subclasses `Car` (add `num_doors`)
   and `Truck` (add `payload_kg`). Override `description()` in each subclass
   to include the extra attribute.

4. Rewrite the `Student` class from task 2 as a `@dataclass`. Add
   `order=True` so students can be sorted by grade.

5. Define a `Queue` class (first-in, first-out) with `enqueue(item)`,
   `dequeue()`, `peek()`, `is_empty()`, `__len__`, and `__repr__`. Raise
   `IndexError` when dequeuing or peeking an empty queue.

6. Define a `BankAccount` class (similar to section 4.1) and a subclass
   `CreditAccount` that has a `credit_limit` and allows the balance to go
   negative down to `-credit_limit`. Override `withdraw` to enforce the
   limit.

7. Define a `Fraction` class with `numerator` and `denominator`. Implement
   `__str__` (e.g., `"3/4"`), `__repr__`, and `__eq__`. Reduce the fraction
   to lowest terms in `__init__` using `math.gcd`.

8. Write a `Catalogue` class that stores a list of `@dataclass` `Movie`
   objects (with `title`, `year`, `rating` fields). Add methods to find
   movies by year range and to return the top-N highest-rated movies.

---

## 7. Key Takeaways

- A **class** is a blueprint; an **object** (instance) is a concrete thing
  built from that blueprint.
- `__init__` runs when an instance is created. Use it to set instance
  attributes with `self.attribute = value`.
- `self` is a reference to the current instance. Python passes it
  automatically as the first argument to every instance method.
- **Instance attributes** belong to one object. **Class attributes** are
  shared by all instances — be careful with mutable class attributes.
- Define `__str__` for human-readable output and `__repr__` for
  unambiguous, developer-facing output. Always define at least `__repr__`.
- **Inheritance** lets a subclass reuse and extend a parent class. Use
  `super().__init__(...)` to call the parent's initialiser.
- **Method overriding** replaces a parent method in the subclass. The right
  version is called automatically based on the object's type (polymorphism).
- `@dataclass` generates `__init__`, `__repr__`, and `__eq__` automatically.
  Use it for data-holding classes. Use `field(default_factory=list)` for
  mutable defaults.
- `__eq__` controls `==` comparisons; `__lt__` (and friends) control
  ordering and `sorted()`.
- Not everything needs a class. Use functions for stateless transformations
  and simple scripts. Reach for classes when you have multiple independent
  objects that each carry their own state.

---

### Further Reading

- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming](https://docs.python.org/3/tutorial/oop.html)
- [Data Classes](https://docs.python.org/3/library/dataclasses.html)

### What's Next

Ready to continue? Head to the next chapter: **Standard Library**.

→ [Chapter 17 — Standard Library](17-standard-library.md)

*See also:*
- [Exercise](../exercises/16-oop.md)
- [Solution](../solutions/16-oop.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
