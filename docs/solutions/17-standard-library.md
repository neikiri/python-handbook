# Solutions 17: Standard Library

## Overview

Chapter 17 exercises cover key standard library modules: `string`, `textwrap`, `collections`, `datetime`, `math`, `random`, `itertools`, `os`, `sys`, and `functools`. This guide explains the reasoning behind each solution and highlights the most useful tools in each module.

---

## Notes Before Checking Solutions

The standard library is one of Python's greatest strengths. Before reaching for a third-party package, check whether the standard library already has what you need. The modules covered in this chapter handle the vast majority of everyday programming tasks.

---

## Warm-up Exercise Solutions

### Exercise 1: Use String and Text Modules

```python
import string
import textwrap
import random

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Generate a random string
random_string = "".join(random.choices(string.ascii_letters, k=10))
print(random_string)  # e.g., "xKpLmNqRsT"

# Text wrapping
long_text = "Python is a powerful and flexible programming language that is easy to learn and use."
wrapped = textwrap.fill(long_text, width=40)
print(wrapped)
# Python is a powerful and flexible
# programming language that is easy to
# learn and use.

# Dedent
indented = """
    This is indented
    text that we want
    to dedent
"""
print(textwrap.dedent(indented))
```

**`string.ascii_letters`** is useful for generating random strings, validating input, or building character sets. It is more readable than writing `"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"` manually.

**`textwrap.fill()`** wraps a long string to a specified width. **`textwrap.dedent()`** removes common leading whitespace from all lines — useful for multiline strings defined inside indented code.

---

### Exercise 2: Use Collections Module

```python
from collections import Counter, defaultdict, namedtuple

# Counter
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(items)
print(counts)                    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts.most_common(2))     # [('apple', 3), ('banana', 2)]

# defaultdict
word_lengths = defaultdict(list)
words = ["apple", "banana", "cherry", "date", "fig"]
for word in words:
    word_lengths[len(word)].append(word)
print(dict(word_lengths))
# {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date'], 3: ['fig']}

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p)      # Point(x=3, y=4)
print(p.x)    # 3
print(p[0])   # 3 — also accessible by index

Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
person = Person("Alice", 30)
print(person)  # Person(name='Alice', age=30, city='Unknown')
```

**`Counter`** is the right tool for counting hashable items. It is much faster than a manual `dict` loop for large datasets.

**`defaultdict(list)`** automatically creates an empty list for any new key. This eliminates the `if key not in d: d[key] = []` pattern.

**`namedtuple`** creates a tuple subclass with named fields. It is lighter than a full class and immutable, making it good for simple data containers. For mutable data containers, consider `dataclasses` (Python 3.7+).

---

### Exercise 3: Use Datetime Module

```python
from datetime import datetime, timedelta, date

now = datetime.now()
print(now)           # 2024-01-15 14:30:00.123456
print(now.date())    # 2024-01-15
print(now.time())    # 14:30:00.123456

birthday = datetime(1990, 5, 15)

tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)

# Calculate age
today = date.today()
birth_date = date(1990, 5, 15)
age = (today - birth_date).days // 365
print(f"Age: {age} years")

# Format
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-01-15 14:30:00

# Parse
parsed = datetime.strptime("2023-12-25", "%Y-%m-%d")
print(parsed)  # 2023-12-25 00:00:00
```

**`timedelta`** represents a duration. You can add or subtract it from `datetime` objects. Common units: `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours`, `weeks`.

**`strftime()` formats** a datetime as a string. **`strptime()` parses** a string into a datetime. The format codes are the same: `%Y` (4-digit year), `%m` (month), `%d` (day), `%H` (hour, 24h), `%M` (minute), `%S` (second).

**`datetime` is timezone-naive by default.** For timezone-aware datetimes, use `datetime.now(timezone.utc)` or the `zoneinfo` module (Python 3.9+).

---

### Exercise 4: Use Math and Random Modules

```python
import math
import random

print(math.sqrt(16))          # 4.0
print(math.ceil(3.2))         # 4
print(math.floor(3.8))        # 3
print(math.pi)                # 3.141592653589793
print(math.e)                 # 2.718281828459045
print(math.sin(math.pi / 2))  # 1.0

print(random.random())              # float in [0.0, 1.0)
print(random.randint(1, 10))        # int in [1, 10]
print(random.choice(["a", "b"]))    # random element

numbers = list(range(1, 11))
sample = random.sample(numbers, 3)  # 3 unique elements
random.shuffle(numbers)             # in-place shuffle

# Reproducible results
random.seed(42)
print(random.randint(1, 100))  # always the same value
random.seed(42)
print(random.randint(1, 100))  # same value again
```

**`random.seed()`** initializes the random number generator with a fixed value, producing the same sequence every time. Use this in tests or when you need reproducible results.

**`random.sample()` vs. `random.choices()`:** `sample()` picks without replacement (no duplicates); `choices()` picks with replacement (duplicates possible).

---

## Practice Exercise Solutions

### Exercise 5: Use Itertools Module

```python
from itertools import combinations, permutations, product, chain

items = [1, 2, 3]

combos = list(combinations(items, 2))
# [(1, 2), (1, 3), (2, 3)]

perms = list(permutations(items, 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = list(product(colors, sizes))
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ...]

chained = list(chain([1, 2, 3], [4, 5, 6]))
# [1, 2, 3, 4, 5, 6]
```

**`combinations` vs. `permutations`:** Combinations do not care about order — `(1, 2)` and `(2, 1)` are the same combination. Permutations do care about order — they are different permutations.

**`product`** is the Cartesian product — every combination of one element from each iterable. It is equivalent to nested `for` loops.

**`chain`** concatenates iterables without creating a new list. It is memory-efficient for large sequences.

---

### Exercise 6: Use OS and Sys Modules

```python
import os
import sys
from pathlib import Path

print(sys.version)
print(sys.platform)   # 'win32', 'darwin', or 'linux'
print(sys.executable) # path to Python interpreter

print(os.environ.get("HOME", "Not set"))
print(os.getcwd())

# List files
for item in os.listdir("."):
    if os.path.isfile(item):
        print(item)

# Create and remove directories
test_dir = Path("test_directory")
test_dir.mkdir(exist_ok=True)
test_file = test_dir / "test.txt"
test_file.write_text("Hello")
test_file.unlink()
test_dir.rmdir()
```

**`os.environ.get("KEY", default)`** safely reads environment variables. Using `os.environ["KEY"]` raises `KeyError` if the variable is not set.

**`sys.platform`** is useful for writing cross-platform code. Check it when behavior must differ between operating systems.

---

### Exercise 7: Use Functools Module

```python
from functools import reduce, lru_cache, partial

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# 120  (1 * 2 * 3 * 4 * 5)

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))           # 55
print(fibonacci.cache_info())  # CacheInfo(hits=8, misses=11, ...)

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))   # 10

triple = partial(multiply, 3)
print(triple(5))   # 15
```

**`@lru_cache`** memoizes function results. The first call to `fibonacci(10)` computes the result; subsequent calls return the cached value instantly. This transforms the naive recursive Fibonacci from O(2^n) to O(n).

**`partial()`** creates a new function with some arguments pre-filled. `double = partial(multiply, 2)` creates a function that always passes `2` as the first argument to `multiply`. This is useful for adapting functions to different interfaces.

**`reduce()`** applies a function cumulatively to a sequence. `reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])` computes `((((1 * 2) * 3) * 4) * 5) = 120`. For simple cases like sum and product, use `sum()` and `math.prod()` instead.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Task Scheduler

```python
from datetime import datetime, timedelta
from collections import defaultdict

class TaskScheduler:
    def __init__(self):
        self.tasks = defaultdict(list)

    def add_task(self, date, task):
        self.tasks[date].append(task)

    def get_tasks(self, date):
        return self.tasks.get(date, [])

    def get_upcoming(self, days=7):
        upcoming = {}
        today = datetime.now().date()
        for i in range(days):
            date = today + timedelta(days=i)
            if date in self.tasks:
                upcoming[date] = self.tasks[date]
        return upcoming

scheduler = TaskScheduler()
today = datetime.now().date()
scheduler.add_task(today, "Buy groceries")
scheduler.add_task(today + timedelta(days=1), "Gym")

for date, tasks in scheduler.get_upcoming(7).items():
    print(f"{date}: {tasks}")
```

**`defaultdict(list)`** eliminates the need to check whether a key exists before appending. This is a common pattern when grouping items by a key.

---

### Challenge 2: Analyze Text Statistics

```python
from collections import Counter
import string

def analyze_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_counts = Counter(words)
    chars = [c for c in text if c.isalpha()]
    char_counts = Counter(chars)
    return {
        "total_words": len(words),
        "unique_words": len(word_counts),
        "most_common_words": word_counts.most_common(5),
        "total_chars": len(chars),
        "most_common_chars": char_counts.most_common(5),
    }

text = "Python is great. Python is powerful. Python is fun."
stats = analyze_text(text)
print(stats)
```

**`str.translate(str.maketrans("", "", string.punctuation))`** removes all punctuation characters in one pass. It is faster than a loop or regex for simple character removal.

---

### Challenge 3: Generate Random Data

```python
import random
import string
from datetime import datetime, timedelta

def generate_random_person():
    first_names = ["Alice", "Bob", "Carol", "David", "Eve"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    return {
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "age": random.randint(18, 80),
        "email": "".join(random.choices(string.ascii_lowercase, k=8)) + "@example.com",
    }

def generate_random_date(start_date, end_date):
    days = (end_date - start_date).days
    return start_date + timedelta(days=random.randint(0, days))

for _ in range(3):
    print(generate_random_person())
```

---

## Common Mistakes

**`Counter` on non-hashable items.** `Counter` requires hashable elements. You cannot count lists directly — convert them to tuples first.

**Timezone-naive datetime comparisons.** Comparing a timezone-aware datetime with a timezone-naive one raises `TypeError`. Be consistent: either use all naive or all aware datetimes.

**Forgetting that `random` is not cryptographically secure.** For passwords, tokens, or security-sensitive values, use `secrets.token_hex()` or `secrets.choice()` from the `secrets` module.

**`reduce()` with an empty sequence.** `reduce(f, [])` raises `TypeError`. Provide an initial value: `reduce(f, [], initial_value)`.

---

## What to Review Next

- Chapter 11: Comprehensions and Generators — `itertools` pairs well with generator expressions
- Chapter 18: Testing and Code Quality — testing code that uses `datetime` and `random`
- Chapter 21: Working with Data — applying `Counter`, `defaultdict`, and `datetime` to real datasets
