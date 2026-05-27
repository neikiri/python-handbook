# Solutions 19: Type Hints

## Overview

Chapter 19 exercises cover adding type hints to functions, variables, and classes; using collection types, `Optional`, `Union`, `Callable`, and generic types; and checking types with mypy. This guide explains the reasoning behind each solution and highlights practical type annotation patterns.

---

## Notes Before Checking Solutions

Type hints are documentation that tools can check. Python does not enforce them at runtime — `add("hello", "world")` will not raise an error even if `add` is annotated as `(int, int) -> int`. The value comes from IDE autocompletion, mypy static analysis, and making code easier to understand.

---

## Warm-up Exercise Solutions

### Exercise 1: Add Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_positive(n: int) -> bool:
    return n > 0
```

Check with mypy:

```bash
mypy basic_types.py
```

**`-> None`** is the return type for functions that do not return a value (or return `None` implicitly). Always annotate the return type — it documents intent and helps mypy catch missing `return` statements.

**`int` vs. `float`:** In Python, `int` is not a subtype of `float` for mypy purposes. If a function accepts `float`, pass `float` values. If you pass an `int` where `float` is expected, mypy accepts it (because `int` is compatible with `float` in practice), but be explicit when possible.

---

### Exercise 2: Use Collection Type Hints

```python
from typing import List, Dict, Set, Tuple

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_names(people: List[Dict[str, str]]) -> List[str]:
    return [person["name"] for person in people]

def count_items(items: List[str]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

def get_unique(items: List[int]) -> Set[int]:
    return set(items)

def get_coordinates() -> Tuple[int, int]:
    return (10, 20)
```

**Python 3.9+ shorthand:** You can use built-in types directly instead of importing from `typing`:

```python
# Python 3.9+
def sum_numbers(numbers: list[int]) -> int: ...
def count_items(items: list[str]) -> dict[str, int]: ...
def get_coordinates() -> tuple[int, int]: ...
```

The `typing` module versions (`List`, `Dict`, etc.) still work in Python 3.9+ for backward compatibility.

**`Tuple[int, int]`** means a tuple with exactly two integers. `Tuple[int, ...]` means a tuple of any length containing integers.

---

### Exercise 3: Use Optional Type Hints

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob", 3: "Carol"}
    return users.get(user_id)

def get_age(name: str) -> Optional[int]:
    ages = {"Alice": 30, "Bob": 25}
    return ages.get(name)

def process_value(value: Optional[int]) -> int:
    return value if value is not None else 0
```

**`Optional[X]` is equivalent to `Union[X, None]`.** Use `Optional` when a value can be absent. It signals to the caller that they must handle the `None` case.

**Python 3.10+ shorthand:** `str | None` instead of `Optional[str]`.

```python
def find_user(user_id: int) -> str | None:
    ...
```

**Always check for `None` before using an `Optional` value.** mypy will warn you if you use an `Optional[str]` as if it were always a `str`.

---

### Exercise 4: Use Union Type Hints

```python
from typing import Union

def process_input(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"String: {value}"

def get_value(key: str) -> Union[int, str, None]:
    data = {"age": 30, "name": "Alice", "email": None}
    return data.get(key)

def convert_to_number(value: Union[int, str, float]) -> float:
    return float(value)
```

**`isinstance()` narrows the type.** Inside `if isinstance(value, int):`, mypy knows `value` is `int`. This is called type narrowing and is the correct way to handle `Union` types.

**Python 3.10+ shorthand:** `int | str` instead of `Union[int, str]`.

---

## Practice Exercise Solutions

### Exercise 5: Type Hint a Class

```python
from typing import List, Optional

class Person:
    def __init__(self, name: str, age: int, email: Optional[str] = None) -> None:
        self.name: str = name
        self.age: int = age
        self.email: Optional[str] = email

    def get_info(self) -> str:
        return f"{self.name} ({self.age})"

    def set_email(self, email: str) -> None:
        self.email = email

    def is_adult(self) -> bool:
        return self.age >= 18

class Team:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.members: List[Person] = []

    def add_member(self, person: Person) -> None:
        self.members.append(person)

    def get_members(self) -> List[Person]:
        return self.members.copy()

    def get_average_age(self) -> float:
        if not self.members:
            return 0.0
        return sum(p.age for p in self.members) / len(self.members)
```

**Annotate `__init__` with `-> None`.** The `__init__` method always returns `None`. Annotating it explicitly is good practice and required by strict mypy configurations.

**Annotate instance attributes in `__init__`.** `self.name: str = name` annotates the attribute type. This helps mypy and IDEs understand the class structure.

---

### Exercise 6: Use Callable Type Hints

```python
from typing import Callable, List

def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

def map_function(func: Callable[[int], int], values: List[int]) -> List[int]:
    return [func(v) for v in values]

def filter_function(func: Callable[[int], bool], values: List[int]) -> List[int]:
    return [v for v in values if func(v)]

def compose(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], int]:
    def composed(x: int) -> int:
        return f(g(x))
    return composed

def double(x: int) -> int:
    return x * 2

def is_even(x: int) -> bool:
    return x % 2 == 0

print(apply_function(double, 5))                    # 10
print(map_function(double, [1, 2, 3]))              # [2, 4, 6]
print(filter_function(is_even, [1, 2, 3, 4, 5]))   # [2, 4]

add_one = lambda x: x + 1
composed = compose(double, add_one)
print(composed(5))  # (5 + 1) * 2 = 12
```

**`Callable[[int], int]`** means a callable that takes one `int` argument and returns an `int`. The first list contains parameter types; the last element is the return type.

**`Callable[..., int]`** means a callable that returns `int` with any parameters. Use this when you do not care about the parameter types.

---

### Exercise 7: Use Generic Type Hints

```python
from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
print(str_stack.pop())  # "hello"
```

**`TypeVar("T")`** declares a type variable. `Generic[T]` makes the class generic over `T`. When you write `Stack[int]`, mypy knows that `push()` accepts `int` and `pop()` returns `int`.

**Generic classes** let you write type-safe containers without duplicating code. The same `Stack` class works for any type, and mypy catches type mismatches.

---

## Challenge Exercise Solutions

### Challenge 1: Type Hint a Complex Application

```python
from typing import List, Optional
from datetime import datetime

class Todo:
    def __init__(self, title: str, description: str = "") -> None:
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.created_at: datetime = datetime.now()

    def mark_complete(self) -> None:
        self.completed = True

    def get_info(self) -> str:
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"

class TodoList:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.todos: List[Todo] = []

    def add_todo(self, title: str, description: str = "") -> None:
        self.todos.append(Todo(title, description))

    def get_todos(self) -> List[Todo]:
        return self.todos.copy()

    def get_completed(self) -> List[Todo]:
        return [t for t in self.todos if t.completed]

    def get_pending(self) -> List[Todo]:
        return [t for t in self.todos if not t.completed]

    def complete_todo(self, index: int) -> None:
        if 0 <= index < len(self.todos):
            self.todos[index].mark_complete()
```

---

### Challenge 2: Use Type Checking with mypy

`mypy.ini` (or `mypy_config.ini`):

```ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

Run:

```bash
mypy --config-file=mypy.ini strict_types.py
```

**`disallow_untyped_defs = True`** requires all functions to have type annotations. This is a good setting for new projects. For existing codebases, start without it and add annotations gradually.

**`# type: ignore`** suppresses mypy errors on a specific line. Use sparingly — it hides real issues. Prefer fixing the type error or using a proper type annotation.

---

## Common Mistakes

**Using `list` instead of `List` in Python 3.8 and earlier.** `list[int]` as a type hint requires Python 3.9+. Use `from typing import List` for compatibility with older Python.

**Forgetting to handle `None` from `Optional`.** If a function returns `Optional[str]`, you must check `if result is not None:` before using it as a string. mypy will warn you if you forget.

**Annotating `self` in methods.** Do not annotate `self` — mypy infers its type automatically. `def method(self: MyClass, ...)` is unnecessary and clutters the code.

**Using `Any` too liberally.** `Any` disables type checking for that value. Use it only when you genuinely cannot know the type (e.g., when working with dynamic data). Overusing `Any` defeats the purpose of type hints.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 20 - CLI Programs](../handbook/20-cli-programs.md)
