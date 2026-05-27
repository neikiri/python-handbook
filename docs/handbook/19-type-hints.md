# Chapter 19: Type Hints

## 1. Overview

Python is a dynamically typed language. That means you do not have to declare
what type a variable holds — Python figures it out at runtime. This flexibility
is one of the reasons Python is easy to learn and fast to write.

But as programs grow, that flexibility can become a liability. When a function
accepts a parameter called `data`, it is not obvious whether `data` should be
a string, a list, or a dictionary. When you come back to code you wrote three
months ago, or when a teammate reads your code for the first time, the lack of
type information slows everyone down.

Type hints are Python's answer to this problem. They let you annotate variables,
function parameters, and return values with type information — without changing
how the program runs. Python itself ignores type hints at runtime. Their value
comes from tooling: editors use them for autocomplete and inline documentation,
and static analysis tools like mypy use them to catch bugs before you run the
code.

Type hints are optional. You can add them to an entire codebase, to just the
public API of a module, or not at all. This chapter teaches you how to write
them, when they help, and when they are not worth the effort.

---

## 2. What You Will Learn

- What type hints are and why Python does not enforce them at runtime
- How to annotate function parameters and return types
- The common built-in types: `int`, `float`, `str`, `bool`, `bytes`
- Collection types using Python 3.10+ syntax: `list[str]`, `dict[str, int]`,
  `tuple[int, str]`, `set[float]`
- How to express optional values with `str | None`
- How to define type aliases to name complex types
- When type hints genuinely help and when they add noise
- How to install and run mypy for static type checking
- The `Any` type and why it is a last resort

---

## 3. Core Concepts

### 3.1 Type Hints Are Not Enforced at Runtime

Before writing a single annotation, understand this: Python does not check
type hints when your program runs. The following code runs without error even
though the types are wrong:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("hello", " world")
print(result)   # hello world — Python does not complain
```

The annotation `a: int` is metadata. It tells humans and tools what the
function expects, but Python does not enforce it. If you pass a string where
an int is expected, Python will happily run the code — and may produce a
surprising result or raise an error later, depending on what the function does.

This is intentional. Type hints are a documentation and tooling feature, not
a runtime constraint. If you want runtime validation, use `isinstance` checks
or a library like Pydantic.

---

### 3.2 Annotating Function Parameters and Return Types

The syntax for type hints uses a colon after the parameter name and an arrow
before the return type.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Breaking this down:

- `name: str` — the parameter `name` is expected to be a string
- `-> str` — the function returns a string

You can annotate as many parameters as you like:

```python
def calculate_area(width: float, height: float) -> float:
    return width * height
```

If a function returns nothing, annotate the return type as `None`:

```python
def print_greeting(name: str) -> None:
    print(f"Hello, {name}!")
```

`-> None` is not the same as omitting the return annotation. Omitting it means
"I have not annotated this yet." Writing `-> None` explicitly says "this
function intentionally returns nothing."

---

### 3.3 Annotating Variables

You can annotate variables too, though it is less common than annotating
function signatures.

```python
count: int = 0
name: str = "Alice"
ratio: float = 0.75
active: bool = True
```

Variable annotations are most useful when the type is not obvious from the
assigned value, or when you want to declare a variable before assigning it:

```python
result: int   # declared but not yet assigned

if some_condition:
    result = 42
else:
    result = 0
```

---

### 3.4 Common Built-in Types

The five most common primitive types you will annotate:

| Type | Python type | Example value |
|------|-------------|---------------|
| Integer | `int` | `42`, `-7`, `0` |
| Floating point | `float` | `3.14`, `-0.5` |
| String | `str` | `"hello"`, `"Alice"` |
| Boolean | `bool` | `True`, `False` |
| Bytes | `bytes` | `b"data"`, `b"\xff\xfe"` |

```python
def is_even(n: int) -> bool:
    return n % 2 == 0


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def encode_message(text: str) -> bytes:
    return text.encode("utf-8")
```

Note that `bool` is a subclass of `int` in Python, so a `bool` value is also
a valid `int`. This is a quirk of Python's type system, not something you need
to worry about in practice.

---

### 3.5 Collection Types

Python 3.9 introduced the ability to use built-in collection types directly
as generic annotations. Python 3.10+ is where this style is fully idiomatic.

#### Lists

```python
def total(values: list[int]) -> int:
    return sum(values)


def first_words(sentences: list[str]) -> list[str]:
    return [s.split()[0] for s in sentences if s.strip()]
```

`list[int]` means "a list where every element is an int." The type inside the
brackets is called the type argument.

#### Dictionaries

```python
def word_lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}
```

`dict[str, int]` means "a dict with string keys and integer values." The first
type argument is the key type, the second is the value type.

#### Tuples

Tuples are annotated differently depending on whether they have a fixed or
variable length.

Fixed-length tuple — list each element type:

```python
def min_max(values: list[float]) -> tuple[float, float]:
    return min(values), max(values)
```

`tuple[float, float]` means exactly two floats. The number of type arguments
matches the number of elements.

Variable-length tuple of one type — use an ellipsis:

```python
def sum_all(values: tuple[int, ...]) -> int:
    return sum(values)
```

`tuple[int, ...]` means "a tuple of any length where every element is an int."

#### Sets

```python
def unique_tags(tag_lists: list[list[str]]) -> set[str]:
    result: set[str] = set()
    for tags in tag_lists:
        result.update(tags)
    return result
```

`set[float]` means "a set where every element is a float."

---

### 3.6 Optional Values: `str | None`

A common situation is a value that might be present or might be absent. In
Python, the conventional way to represent "no value" is `None`.

Before Python 3.10, you had to write `Optional[str]` from the `typing` module.
Python 3.10 introduced the `|` union syntax, which is cleaner:

```python
def find_user(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)   # returns None if not found
```

`str | None` means "either a string or None." This is the idiomatic way to
say a value is optional.

The `|` syntax works for any union of types, not just `None`:

```python
def parse_number(value: str) -> int | float:
    if "." in value:
        return float(value)
    return int(value)
```

When a parameter has a default of `None`, annotate it as `type | None`:

```python
def greet(name: str, title: str | None = None) -> str:
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"
```

---

### 3.7 Type Aliases

When a type expression is long or used in many places, give it a name. This
makes the code easier to read and easier to change.

#### Python 3.12+ style (preferred)

Python 3.12 introduced the `type` statement for defining type aliases:

```python
type Vector = list[float]
type Matrix = list[list[float]]
type UserRecord = dict[str, str | int]
```

#### Older style (Python 3.10 and 3.11)

Assign the type expression to a variable. By convention, type alias names use
`PascalCase`:

```python
Vector = list[float]
Matrix = list[list[float]]
UserRecord = dict[str, str | int]
```

Both styles produce the same result for most purposes. Use the `type` statement
if you are on Python 3.12+; use the assignment style otherwise.

#### Using a type alias

```python
type Vector = list[float]


def dot_product(a: Vector, b: Vector) -> float:
    """Return the dot product of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    return sum(x * y for x, y in zip(a, b))


def scale(v: Vector, factor: float) -> Vector:
    """Multiply every element of a vector by a scalar."""
    return [x * factor for x in v]
```

The alias `Vector` makes the intent clear. Without it, `list[float]` appears
three times and the reader has to infer that all three refer to the same concept.

---

### 3.8 The `Any` Type

`Any` is a special type from the `typing` module that opts out of type
checking entirely. A value annotated as `Any` is compatible with every other
type — mypy will not report errors involving it.

```python
from typing import Any


def process(data: Any) -> None:
    # mypy will not check what you do with data
    print(data)
```

`Any` is a last resort. Use it when:

- You are gradually adding type hints to existing code and have not typed a
  particular value yet
- You are working with a third-party library that has no type stubs
- The type is genuinely dynamic and cannot be expressed otherwise

Do not use `Any` to silence type errors you do not want to think about. That
defeats the purpose of type hints. If you find yourself reaching for `Any`
often, it usually means the code needs to be restructured, or the types need
to be expressed more carefully.

---

### 3.9 Static Type Checking with mypy

mypy is the most widely used static type checker for Python. It reads your
source files, follows the type annotations, and reports inconsistencies —
without running the code.

#### Installing mypy

```bash
pip install mypy
```

#### Running mypy

```bash
mypy script.py
```

mypy will print any type errors it finds. If there are none, it prints:

```text
Success: no issues found in 1 source file
```

#### A simple example

Save this as `example.py`:

```python
def double(n: int) -> int:
    return n * 2


result: str = double(5)   # wrong: double returns int, not str
print(result)
```

Run mypy:

```bash
mypy example.py
```

Output:

```text
example.py:5: error: Incompatible types in assignment
    (expression has type "int", variable has type "str")
Found 1 error in 1 file (checked 1 source file)
```

mypy caught the bug before you ran the code.

#### Checking a whole package

```bash
mypy src/
```

#### Useful mypy flags

| Flag | What it does |
|------|--------------|
| `--strict` | Enables all optional checks; good for new projects |
| `--ignore-missing-imports` | Suppresses errors for untyped third-party libraries |
| `--pretty` | Nicer output with context lines |
| `--show-error-codes` | Shows error codes so you can suppress specific ones |

For a new project, start with `--strict` to catch everything. For an existing
codebase you are gradually annotating, start without it and add checks
incrementally.

#### mypy configuration

You can store mypy settings in `pyproject.toml` so you do not have to pass
flags every time:

```toml
[tool.mypy]
python_version = "3.12"
strict = true
ignore_missing_imports = true
```

---

### 3.10 When Type Hints Help

Type hints pay off most in these situations:

**Larger codebases.** When a project has many files and functions, type hints
act as machine-checked documentation. You can see what a function expects
without reading its body.

**Team projects.** When multiple people work on the same code, type hints
reduce the chance of passing the wrong kind of value to a function. mypy can
catch these mistakes in CI before they reach production.

**IDE autocomplete.** Editors like VS Code and PyCharm use type hints to
provide accurate autocomplete suggestions. Without hints, the editor has to
guess. With hints, it knows exactly what methods and attributes are available.

**Catching bugs early.** mypy finds a class of bugs — wrong argument types,
missing return values, incorrect attribute access — that would otherwise only
surface at runtime, possibly in production.

**Refactoring.** When you rename a function or change its signature, mypy
tells you every call site that needs to be updated.

---

### 3.11 When Not to Overdo Them

Type hints are not always worth the effort:

**Small scripts.** A 30-line script that you run once does not benefit much
from type annotations. The overhead of writing and maintaining them outweighs
the value.

**Prototypes.** When you are exploring an idea and the design is changing
rapidly, type hints slow you down. Add them once the design stabilizes.

**Beginner code.** If you are still learning Python fundamentals, focus on
getting the logic right first. Type hints are a layer of complexity you can
add later.

**Heavily dynamic code.** Some Python patterns — metaprogramming, decorators
that change signatures, dynamic attribute access — are difficult to type
accurately. Forcing type hints onto them can make the code harder to read
without adding much safety.

The practical rule: add type hints to functions that form a public interface
(functions other code calls), and skip them for purely internal implementation
details in small scripts.

---

## 4. Practical Examples

### 4.1 A Typed Utility Module

A small module with fully annotated functions.

```python
# utils.py

type FilePath = str


def clamp(value: float, low: float, high: float) -> float:
    """Return value clamped to the range [low, high]."""
    return max(low, min(high, value))


def slugify(text: str) -> str:
    """Convert a title string to a URL-friendly slug."""
    return text.lower().strip().replace(" ", "-")


def chunk(items: list, size: int) -> list[list]:
    """Split a list into chunks of at most `size` elements."""
    return [items[i : i + size] for i in range(0, len(items), size)]


def safe_divide(a: float, b: float) -> float | None:
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return a / b
```

Each function signature tells you exactly what it accepts and what it returns.
You do not need to read the body to know how to call it.

---

### 4.2 A Typed Data Record

Using a dataclass with type hints to represent structured data.

```python
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    grades: list[float] = field(default_factory=list)
    email: str | None = None

    def average_grade(self) -> float | None:
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def is_passing(self, threshold: float = 60.0) -> bool:
        avg = self.average_grade()
        if avg is None:
            return False
        return avg >= threshold


alice = Student(name="Alice", age=20, grades=[88.0, 92.5, 79.0])
print(alice.average_grade())   # 86.5
print(alice.is_passing())      # True

bob = Student(name="Bob", age=19)
print(bob.average_grade())     # None
print(bob.is_passing())        # False
```

The type hints on the dataclass fields serve as both documentation and input
for mypy. If you try to assign a string to `age`, mypy will catch it.

---

### 4.3 A Typed Configuration Parser

Parsing a configuration dictionary with clear type annotations.

```python
type Config = dict[str, str | int | bool]


def parse_config(raw: dict) -> Config:
    """
    Validate and normalize a raw configuration dictionary.
    Returns a typed Config dict.
    """
    config: Config = {}

    host = raw.get("host", "localhost")
    if not isinstance(host, str):
        raise TypeError(f"host must be a string, got {type(host).__name__}")
    config["host"] = host

    port = raw.get("port", 8080)
    if not isinstance(port, int):
        raise TypeError(f"port must be an int, got {type(port).__name__}")
    config["port"] = port

    debug = raw.get("debug", False)
    if not isinstance(debug, bool):
        raise TypeError(f"debug must be a bool, got {type(debug).__name__}")
    config["debug"] = debug

    return config


raw_input = {"host": "example.com", "port": 443, "debug": False}
cfg = parse_config(raw_input)
print(cfg)   # {'host': 'example.com', 'port': 443, 'debug': False}
```

The `Config` alias makes the return type readable. Without it, the return
annotation would be `dict[str, str | int | bool]` — correct but noisy.

---

### 4.4 Gradual Typing on an Existing Function

Suppose you have an existing function with no type hints:

```python
def summarize(records, key, top_n=5):
    counts = {}
    for record in records:
        value = record.get(key)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:top_n]
```

Adding type hints gradually — start with the signature:

```python
def summarize(
    records: list[dict[str, str]],
    key: str,
    top_n: int = 5,
) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for record in records:
        value = record.get(key)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:top_n]
```

The annotated version is self-documenting. A reader immediately knows:
- `records` is a list of string-to-string dicts
- `key` is a string
- the function returns a list of (string, count) pairs

---

### 4.5 Running mypy on a Real File

Save this as `inventory.py`:

```python
type ItemName = str
type Quantity = int
type Inventory = dict[ItemName, Quantity]


def add_item(inventory: Inventory, name: ItemName, qty: Quantity) -> None:
    """Add qty units of name to the inventory."""
    inventory[name] = inventory.get(name, 0) + qty


def remove_item(inventory: Inventory, name: ItemName, qty: Quantity) -> bool:
    """
    Remove qty units of name from the inventory.
    Returns True on success, False if there is not enough stock.
    """
    current = inventory.get(name, 0)
    if current < qty:
        return False
    inventory[name] = current - qty
    return True


def total_items(inventory: Inventory) -> int:
    """Return the total number of units across all items."""
    return sum(inventory.values())


stock: Inventory = {}
add_item(stock, "apple", 10)
add_item(stock, "banana", 5)
print(remove_item(stock, "apple", 3))   # True
print(remove_item(stock, "apple", 20))  # False
print(total_items(stock))               # 12
```

Run mypy:

```bash
mypy inventory.py
```

```text
Success: no issues found in 1 source file
```

Now introduce a bug — pass a string where an int is expected:

```python
add_item(stock, "cherry", "lots")   # wrong type
```

mypy catches it:

```text
inventory.py:28: error: Argument 3 to "add_item" has incompatible type "str";
    expected "int"
Found 1 error in 1 file (checked 1 source file)
```

---

## 5. Common Mistakes

### 5.1 Using `list` Without a Type Argument

An unparameterized `list` is valid but tells you nothing about the contents.

```python
# Vague — what does this list contain?
def process(items: list) -> list:
    return [str(x) for x in items]

# Clear
def process(items: list[int]) -> list[str]:
    return [str(x) for x in items]
```

Always include the type argument when you know what the collection holds.

---

### 5.2 Confusing `None` as a Return Type vs. `| None`

`-> None` means the function returns nothing. `-> str | None` means the
function returns either a string or `None`.

```python
# Wrong — says the function returns nothing, but it actually returns a value
def find(items: list[str], target: str) -> None:
    for item in items:
        if item == target:
            return item
    return None

# Correct
def find(items: list[str], target: str) -> str | None:
    for item in items:
        if item == target:
            return item
    return None
```

---

### 5.3 Annotating Mutable Default Arguments

This is a general Python mistake, but type hints can make it look more
legitimate than it is.

```python
# Wrong — the default list is shared across all calls
def append_item(item: str, result: list[str] = []) -> list[str]:
    result.append(item)
    return result

print(append_item("a"))   # ['a']
print(append_item("b"))   # ['a', 'b']  — unexpected!

# Correct — use None as the default, create a new list inside
def append_item(item: str, result: list[str] | None = None) -> list[str]:
    if result is None:
        result = []
    result.append(item)
    return result
```

---

### 5.4 Using `Any` to Silence Type Errors

`Any` disables type checking for that value. It is tempting to use it when
mypy reports an error you do not understand, but it hides real bugs.

```python
from typing import Any

# Wrong — using Any to avoid thinking about the type
def process(data: Any) -> Any:
    return data["key"] + data["value"]

# Better — be specific about what the function expects
def process(data: dict[str, int]) -> int:
    return data["key"] + data["value"]
```

If you genuinely do not know the type yet, use `Any` temporarily and add a
`# TODO: type this properly` comment so you come back to it.

---

### 5.5 Forgetting to Handle `None` After `| None`

When a function returns `str | None`, you must check for `None` before using
the value as a string. mypy will catch this if you have strict mode enabled.

```python
def get_username(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


name = get_username(99)

# Wrong — name might be None; calling .upper() will raise AttributeError
print(name.upper())

# Correct — check first
if name is not None:
    print(name.upper())
else:
    print("User not found")
```

---

### 5.6 Over-Annotating Simple Scripts

Adding type hints to every variable in a short script adds noise without
adding value.

```python
# Over-annotated — the types are obvious from context
x: int = 5
y: int = 10
result: int = x + y
message: str = f"The result is {result}"
print(message)

# Fine — no annotations needed here
x = 5
y = 10
result = x + y
print(f"The result is {result}")
```

Reserve annotations for function signatures and cases where the type is not
obvious from the assigned value.

---

### 5.7 Using the Old `typing` Module Syntax When Not Needed

Before Python 3.9, you had to import `List`, `Dict`, `Tuple`, etc. from
`typing`. On Python 3.10+, use the built-in types directly.

```python
# Old style — still works, but unnecessary on Python 3.10+
from typing import Dict, List, Optional, Tuple

def process(items: List[str]) -> Dict[str, int]:
    ...

def find(name: Optional[str] = None) -> Optional[str]:
    ...

# Modern style — Python 3.10+
def process(items: list[str]) -> dict[str, int]:
    ...

def find(name: str | None = None) -> str | None:
    ...
```

The old `typing` imports still work and you will see them in older codebases,
but new code should use the modern syntax.

---

## 6. Practice Tasks

1. Write a function `repeat(text: str, times: int) -> str` that returns
   `text` repeated `times` times, separated by spaces. Add full type hints
   and verify with mypy.

2. Write a function `flatten(nested: list[list[int]]) -> list[int]` that
   takes a list of lists of integers and returns a single flat list. Add
   type hints and a docstring.

3. Write a function `lookup(records: list[dict[str, str]], key: str,
   value: str) -> dict[str, str] | None` that searches a list of dicts for
   the first one where `record[key] == value`. Return `None` if not found.

4. Define a type alias `type Coordinate = tuple[float, float]`. Write a
   function `distance(a: Coordinate, b: Coordinate) -> float` that returns
   the Euclidean distance between two points.

5. Write a function `group_by(items: list[str], key_fn: ...) -> dict[str,
   list[str]]` that groups strings by the result of calling `key_fn` on each
   one. For the `key_fn` parameter, use the type `Callable[[str], str]` from
   the `typing` module (look it up in the docs). Test it by grouping words
   by their first letter.

6. Create a file `typed_stack.py` with a class `Stack` that wraps a
   `list[int]` and provides `push(value: int) -> None`,
   `pop() -> int | None`, and `peek() -> int | None` methods. Run mypy on
   the file and fix any errors it reports.

7. Take any function you wrote in a previous chapter that has no type hints
   and add them. Run mypy on the file. If mypy reports errors, fix them.

8. Write a function `safe_get(data: dict[str, int], key: str,
   default: int = 0) -> int` that returns `data[key]` if the key exists,
   otherwise returns `default`. Annotate it fully and verify with mypy.

---

## 7. Key Takeaways

- Type hints are optional metadata. Python does not enforce them at runtime —
  their value comes from editors and tools like mypy.
- Annotate function parameters with `name: type` and return types with
  `-> type`. Use `-> None` for functions that return nothing.
- The common built-in types are `int`, `float`, `str`, `bool`, and `bytes`.
- Use Python 3.10+ collection syntax: `list[str]`, `dict[str, int]`,
  `tuple[float, float]`, `set[int]`.
- Express optional values with `str | None`. Always check for `None` before
  using the value.
- Use type aliases (`type Vector = list[float]` on 3.12+, or
  `Vector = list[float]` on older versions) to name complex types that appear
  in multiple places.
- `Any` opts out of type checking entirely. Use it as a last resort, not as
  a way to silence errors you do not want to think about.
- Install mypy with `pip install mypy` and run it with `mypy script.py`.
  Start with `--strict` on new projects.
- Type hints pay off most in larger codebases, team projects, and public
  APIs. Skip them for small scripts and early prototypes.

---

### Further Reading

- [typing - Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP 585 - Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/)
- [PEP 563 - Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/)

### What's Next

Ready to continue? Head to the next chapter: **CLI Programs**.

→ [Chapter 20 — CLI Programs](20-cli-programs.md)

*See also:*
- [Exercise](../exercises/19-type-hints.md)
- [Solution](../solutions/19-type-hints.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
