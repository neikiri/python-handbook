# Chapter 19: Type Hints — Exercises

## Overview

These exercises help you use type hints to make your code clearer and catch errors early. By the end, you will write well-typed Python code that is easier to understand and maintain.

---

## How to Use These Exercises

- Create a folder called `chapter-19` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Use `mypy` to check types: `pip install mypy && mypy filename.py`.

---

## Warm-up Exercises

### Exercise 1: Add Basic Type Hints

Create a file called `basic_types.py`:

```python
"""Basic type hints."""

def greet(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide two floats."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_positive(n: int) -> bool:
    """Check if a number is positive."""
    return n > 0

# Use the functions
print(greet("Alice"))
print(add(5, 3))
print(divide(10.0, 2.0))
print(is_positive(5))
```

Run it and check with mypy:

```bash
mypy basic_types.py
```

---

### Exercise 2: Use Collection Type Hints

Create a file called `collection_types.py`:

```python
"""Collection type hints."""

from typing import List, Dict, Set, Tuple

def sum_numbers(numbers: List[int]) -> int:
    """Sum a list of numbers."""
    return sum(numbers)

def get_names(people: List[Dict[str, str]]) -> List[str]:
    """Extract names from a list of people."""
    return [person["name"] for person in people]

def count_items(items: List[str]) -> Dict[str, int]:
    """Count occurrences of items."""
    counts: Dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

def get_unique(items: List[int]) -> Set[int]:
    """Get unique items."""
    return set(items)

def get_coordinates() -> Tuple[int, int]:
    """Get x, y coordinates."""
    return (10, 20)

# Use the functions
print(sum_numbers([1, 2, 3, 4, 5]))

people = [
    {"name": "Alice", "age": "30"},
    {"name": "Bob", "age": "25"},
]
print(get_names(people))

print(count_items(["a", "b", "a", "c", "b", "a"]))
print(get_unique([1, 2, 2, 3, 3, 3]))
print(get_coordinates())
```

Run it and check with mypy.

---

### Exercise 3: Use Optional Type Hints

Create a file called `optional_types.py`:

```python
"""Optional type hints."""

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    """Find a user by ID, return None if not found."""
    users = {1: "Alice", 2: "Bob", 3: "Carol"}
    return users.get(user_id)

def get_age(name: str) -> Optional[int]:
    """Get age by name, return None if not found."""
    ages = {"Alice": 30, "Bob": 25, "Carol": 28}
    return ages.get(name)

def process_value(value: Optional[int]) -> int:
    """Process a value, default to 0 if None."""
    return value if value is not None else 0

# Use the functions
print(find_user(1))
print(find_user(99))

print(get_age("Alice"))
print(get_age("Unknown"))

print(process_value(42))
print(process_value(None))
```

Run it and check with mypy.

---

### Exercise 4: Use Union Type Hints

Create a file called `union_types.py`:

```python
"""Union type hints."""

from typing import Union

def process_input(value: Union[int, str]) -> str:
    """Process input that can be int or str."""
    if isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"String: {value}"

def get_value(key: str) -> Union[int, str, None]:
    """Get a value that could be int, str, or None."""
    data = {
        "age": 30,
        "name": "Alice",
        "email": None,
    }
    return data.get(key)

def convert_to_number(value: Union[int, str, float]) -> float:
    """Convert various types to float."""
    return float(value)

# Use the functions
print(process_input(42))
print(process_input("hello"))

print(get_value("age"))
print(get_value("name"))
print(get_value("email"))

print(convert_to_number(42))
print(convert_to_number("3.14"))
print(convert_to_number(2.71))
```

Run it and check with mypy.

---

## Practice Exercises

### Exercise 5: Type Hint a Class

Create a file called `typed_class.py`:

```python
"""Class with type hints."""

from typing import List, Optional

class Person:
    """Represents a person."""
    
    def __init__(self, name: str, age: int, email: Optional[str] = None) -> None:
        self.name: str = name
        self.age: int = age
        self.email: Optional[str] = email
    
    def get_info(self) -> str:
        """Get person info."""
        return f"{self.name} ({self.age})"
    
    def set_email(self, email: str) -> None:
        """Set email."""
        self.email = email
    
    def is_adult(self) -> bool:
        """Check if person is an adult."""
        return self.age >= 18

class Team:
    """Represents a team of people."""
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.members: List[Person] = []
    
    def add_member(self, person: Person) -> None:
        """Add a member to the team."""
        self.members.append(person)
    
    def get_members(self) -> List[Person]:
        """Get all members."""
        return self.members.copy()
    
    def get_average_age(self) -> float:
        """Get average age of members."""
        if not self.members:
            return 0.0
        total_age = sum(person.age for person in self.members)
        return total_age / len(self.members)

# Use the classes
person1 = Person("Alice", 30, "alice@example.com")
person2 = Person("Bob", 25)

team = Team("Developers")
team.add_member(person1)
team.add_member(person2)

print(f"Team: {team.name}")
for member in team.get_members():
    print(f"  {member.get_info()}")
print(f"Average age: {team.get_average_age():.1f}")
```

Run it and check with mypy.

---

### Exercise 6: Use Callable Type Hints

Create a file called `callable_types.py`:

```python
"""Callable type hints."""

from typing import Callable, List

def apply_function(func: Callable[[int], int], value: int) -> int:
    """Apply a function to a value."""
    return func(value)

def map_function(func: Callable[[int], int], values: List[int]) -> List[int]:
    """Apply a function to a list of values."""
    return [func(v) for v in values]

def filter_function(func: Callable[[int], bool], values: List[int]) -> List[int]:
    """Filter values using a function."""
    return [v for v in values if func(v)]

def compose(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], int]:
    """Compose two functions."""
    def composed(x: int) -> int:
        return f(g(x))
    return composed

# Use the functions
def double(x: int) -> int:
    return x * 2

def is_even(x: int) -> bool:
    return x % 2 == 0

print(apply_function(double, 5))
print(map_function(double, [1, 2, 3, 4, 5]))
print(filter_function(is_even, [1, 2, 3, 4, 5]))

def add_one(x: int) -> int:
    return x + 1

composed = compose(double, add_one)
print(composed(5))  # (5 + 1) * 2 = 12
```

Run it and check with mypy.

---

### Exercise 7: Use Generic Type Hints

Create a file called `generic_types.py`:

```python
"""Generic type hints."""

from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
    """A generic stack."""
    
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self) -> T:
        """Pop an item from the stack."""
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self.items) == 0

# Use the generic class
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack.pop())  # 3
print(int_stack.pop())  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # "world"
```

Run it and check with mypy.

---

## Challenge Exercises

### Challenge 1: Type Hint a Complex Application

Create a file called `todo_app.py`:

```python
"""Todo application with type hints."""

from typing import List, Optional
from datetime import datetime

class Todo:
    """Represents a todo item."""
    
    def __init__(self, title: str, description: str = "") -> None:
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.created_at: datetime = datetime.now()
    
    def mark_complete(self) -> None:
        """Mark todo as complete."""
        self.completed = True
    
    def get_info(self) -> str:
        """Get todo info."""
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"

class TodoList:
    """Represents a list of todos."""
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.todos: List[Todo] = []
    
    def add_todo(self, title: str, description: str = "") -> None:
        """Add a todo."""
        todo = Todo(title, description)
        self.todos.append(todo)
    
    def get_todos(self) -> List[Todo]:
        """Get all todos."""
        return self.todos.copy()
    
    def get_completed(self) -> List[Todo]:
        """Get completed todos."""
        return [t for t in self.todos if t.completed]
    
    def get_pending(self) -> List[Todo]:
        """Get pending todos."""
        return [t for t in self.todos if not t.completed]
    
    def complete_todo(self, index: int) -> None:
        """Mark a todo as complete."""
        if 0 <= index < len(self.todos):
            self.todos[index].mark_complete()

# Use the application
todo_list = TodoList("My Tasks")
todo_list.add_todo("Buy groceries")
todo_list.add_todo("Write code")
todo_list.add_todo("Exercise")

print(f"Todo List: {todo_list.name}")
for i, todo in enumerate(todo_list.get_todos()):
    print(f"  {i}: {todo.get_info()}")

todo_list.complete_todo(0)
print("\nAfter completing first todo:")
for todo in todo_list.get_todos():
    print(f"  {todo.get_info()}")
```

Run it and check with mypy.

---

### Challenge 2: Use Type Checking with mypy

Create a file called `mypy_config.ini`:

```ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

Create a file called `strict_types.py`:

```python
"""Strictly typed code."""

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def greet(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"

# This will pass mypy
result: int = add(5, 3)
greeting: str = greet("Alice")
print(result)
print(greeting)
```

Run mypy with config:

```bash
mypy --config-file=mypy_config.ini strict_types.py
```

---

## Hints

**Type error not caught** → Run `mypy` to check types. It won't catch errors at runtime.

**Optional vs Union[X, None]** → `Optional[X]` is equivalent to `Union[X, None]`. Use `Optional` for clarity.

**Generic type not working** → Ensure you import `Generic` and `TypeVar` from `typing`.

**Mypy too strict** → Use `# type: ignore` comments to suppress specific errors, or adjust mypy config.

---

## What to Review If You Get Stuck

- **Basic type hints** → Handbook section 2.1
- **Collection types** → Handbook section 2.2
- **Optional and Union** → Handbook section 2.3
- **Function types** → Handbook section 2.4
- **Class types** → Handbook section 2.5
- **Generic types** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Add type hints to functions and variables
- Use collection types like List, Dict, Set, Tuple
- Use Optional for nullable values
- Use Union for multiple types
- Type hint classes and methods
- Use Callable for function types
- Create generic classes
- Use mypy to check types
- Write clear, well-typed Python code

