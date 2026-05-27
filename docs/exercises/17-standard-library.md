# Chapter 17: Standard Library — Exercises

## Overview

These exercises help you explore and use Python's standard library effectively. By the end, you will confidently use common modules for real-world tasks.

---

## How to Use These Exercises

- Create a folder called `chapter-17` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Use String and Text Modules

Create a file called `string_text.py`:

```python
import string
import textwrap

# String module
print("ASCII letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)

# Generate a random string
import random
random_string = "".join(random.choices(string.ascii_letters, k=10))
print(f"Random string: {random_string}")

# Text wrapping
long_text = "Python is a powerful and flexible programming language that is easy to learn and use."
wrapped = textwrap.fill(long_text, width=40)
print(f"\nWrapped text:\n{wrapped}")

# Dedent
indented = """
    This is indented
    text that we want
    to dedent
"""
dedented = textwrap.dedent(indented)
print(f"Dedented:\n{dedented}")
```

Run it and observe string utilities.

---

### Exercise 2: Use Collections Module

Create a file called `collections_module.py`:

```python
from collections import Counter, defaultdict, namedtuple

# Counter
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(items)
print(f"Counts: {counts}")
print(f"Most common: {counts.most_common(2)}")

# defaultdict
word_lengths = defaultdict(list)
words = ["apple", "banana", "cherry", "date", "fig"]
for word in words:
    word_lengths[len(word)].append(word)
print(f"\nWords by length: {dict(word_lengths)}")

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\nPoint: {p}")
print(f"X: {p.x}, Y: {p.y}")

# namedtuple with defaults
Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
person = Person("Alice", 30)
print(f"Person: {person}")
```

Run it and observe collections.

---

### Exercise 3: Use Datetime Module

Create a file called `datetime_module.py`:

```python
from datetime import datetime, timedelta, date

# Current date and time
now = datetime.now()
print(f"Now: {now}")
print(f"Date: {now.date()}")
print(f"Time: {now.time()}")

# Create specific dates
birthday = datetime(1990, 5, 15)
print(f"\nBirthday: {birthday}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")

# Calculate age
today = date.today()
birth_date = date(1990, 5, 15)
age = (today - birth_date).days // 365
print(f"\nAge: {age} years")

# Format dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")

# Parse dates
date_string = "2023-12-25"
parsed = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed: {parsed}")
```

Run it and observe datetime operations.

---

### Exercise 4: Use Math and Random Modules

Create a file called `math_random.py`:

```python
import math
import random

# Math module
print(f"sqrt(16): {math.sqrt(16)}")
print(f"ceil(3.2): {math.ceil(3.2)}")
print(f"floor(3.8): {math.floor(3.8)}")
print(f"pi: {math.pi}")
print(f"e: {math.e}")
print(f"sin(pi/2): {math.sin(math.pi / 2)}")

# Random module
print(f"\nRandom float: {random.random()}")
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['a', 'b', 'c'])}")

# Random sample
numbers = list(range(1, 11))
sample = random.sample(numbers, 3)
print(f"Random sample: {sample}")

# Shuffle
deck = list(range(1, 53))
random.shuffle(deck)
print(f"Shuffled deck (first 5): {deck[:5]}")

# Random with seed (reproducible)
random.seed(42)
print(f"Seeded random: {random.randint(1, 100)}")
random.seed(42)
print(f"Same seed: {random.randint(1, 100)}")
```

Run it and observe math and random.

---

## Practice Exercises

### Exercise 5: Use Itertools Module

Create a file called `itertools_module.py`:

```python
from itertools import combinations, permutations, product, chain

# Combinations
items = [1, 2, 3]
combos = list(combinations(items, 2))
print(f"Combinations: {combos}")

# Permutations
perms = list(permutations(items, 2))
print(f"Permutations: {perms}")

# Product (Cartesian product)
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = list(product(colors, sizes))
print(f"Product: {products}")

# Chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = list(chain(list1, list2))
print(f"Chained: {chained}")

# Practical example: generate all possible passwords
import string
chars = string.ascii_lowercase
passwords = ["".join(p) for p in permutations(chars, 3)]
print(f"First 5 3-letter passwords: {passwords[:5]}")
```

Run it and observe itertools.

---

### Exercise 6: Use OS and Sys Modules

Create a file called `os_sys_module.py`:

```python
import os
import sys
from pathlib import Path

# System information
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")

# Environment variables
print(f"\nPATH: {os.environ.get('PATH', 'Not set')}")
print(f"HOME: {os.environ.get('HOME', 'Not set')}")

# Current directory
print(f"\nCurrent directory: {os.getcwd()}")

# List files
print("\nFiles in current directory:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"  {item}")

# Create and remove directories
test_dir = Path("test_directory")
test_dir.mkdir(exist_ok=True)
print(f"\nCreated: {test_dir}")

test_file = test_dir / "test.txt"
test_file.write_text("Hello")
print(f"Created: {test_file}")

# Clean up
test_file.unlink()
test_dir.rmdir()
print("Cleaned up")
```

Run it and observe OS operations.

---

### Exercise 7: Use Functools Module

Create a file called `functools_module.py`:

```python
from functools import reduce, lru_cache

# Reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# LRU cache for memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    """Calculate Fibonacci number with caching."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFibonacci(10): {fibonacci(10)}")
print(f"Cache info: {fibonacci.cache_info()}")

# Partial function
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(f"\nDouble 5: {double(5)}")

triple = partial(multiply, 3)
print(f"Triple 5: {triple(5)}")
```

Run it and observe functools.

---

## Challenge Exercises

### Challenge 1: Build a Task Scheduler

Create a file called `task_scheduler.py`:

```python
from datetime import datetime, timedelta
from collections import defaultdict

class TaskScheduler:
    def __init__(self):
        self.tasks = defaultdict(list)
    
    def add_task(self, date, task):
        """Add a task for a specific date."""
        self.tasks[date].append(task)
    
    def get_tasks(self, date):
        """Get tasks for a specific date."""
        return self.tasks.get(date, [])
    
    def get_upcoming(self, days=7):
        """Get tasks for the next N days."""
        upcoming = {}
        today = datetime.now().date()
        for i in range(days):
            date = today + timedelta(days=i)
            if date in self.tasks:
                upcoming[date] = self.tasks[date]
        return upcoming

# Use the scheduler
scheduler = TaskScheduler()

today = datetime.now().date()
scheduler.add_task(today, "Buy groceries")
scheduler.add_task(today, "Call mom")
scheduler.add_task(today + timedelta(days=1), "Gym")
scheduler.add_task(today + timedelta(days=2), "Project deadline")

print("Today's tasks:")
for task in scheduler.get_tasks(today):
    print(f"  - {task}")

print("\nUpcoming tasks (7 days):")
for date, tasks in scheduler.get_upcoming(7).items():
    print(f"  {date}:")
    for task in tasks:
        print(f"    - {task}")
```

Run it and observe the task scheduler.

---

### Challenge 2: Analyze Text Statistics

Create a file called `text_statistics.py`:

```python
from collections import Counter
import string

def analyze_text(text):
    """Analyze text and return statistics."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Count words
    word_counts = Counter(words)
    
    # Count characters
    chars = [c for c in text if c.isalpha()]
    char_counts = Counter(chars)
    
    return {
        "total_words": len(words),
        "unique_words": len(word_counts),
        "most_common_words": word_counts.most_common(5),
        "total_chars": len(chars),
        "most_common_chars": char_counts.most_common(5),
    }

# Test
text = "Python is great. Python is powerful. Python is fun. Python is easy to learn."
stats = analyze_text(text)

print(f"Total words: {stats['total_words']}")
print(f"Unique words: {stats['unique_words']}")
print(f"Most common words: {stats['most_common_words']}")
print(f"Total characters: {stats['total_chars']}")
print(f"Most common characters: {stats['most_common_chars']}")
```

Run it and observe text analysis.

---

### Challenge 3: Generate Random Data

Create a file called `random_data.py`:

```python
import random
import string
from datetime import datetime, timedelta

def generate_random_person():
    """Generate a random person."""
    first_names = ["Alice", "Bob", "Carol", "David", "Eve"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    
    return {
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "age": random.randint(18, 80),
        "email": "".join(random.choices(string.ascii_lowercase, k=8)) + "@example.com",
    }

def generate_random_date(start_date, end_date):
    """Generate a random date between two dates."""
    time_between = (end_date - start_date).days
    random_days = random.randint(0, time_between)
    return start_date + timedelta(days=random_days)

# Generate random people
print("Random people:")
for _ in range(3):
    person = generate_random_person()
    print(f"  {person}")

# Generate random dates
print("\nRandom dates:")
start = datetime(2023, 1, 1)
end = datetime(2023, 12, 31)
for _ in range(3):
    date = generate_random_date(start, end)
    print(f"  {date.date()}")
```

Run it and observe random data generation.

---

## Hints

**Module not found** → Ensure the module is part of the standard library. Use `import sys; print(sys.modules)` to check.

**Unexpected datetime result** → Remember that `datetime` is timezone-naive by default. Use `timezone` for timezone-aware operations.

**Random results not reproducible** → Use `random.seed()` to set a seed for reproducible results.

**Counter not working as expected** → Remember that `Counter` counts hashable items. Convert unhashable types to tuples or strings first.

---

## What to Review If You Get Stuck

- **String and text modules** → Handbook section 2.1
- **Collections module** → Handbook section 2.2
- **Datetime module** → Handbook section 2.3
- **Math and random modules** → Handbook section 2.4
- **Itertools module** → Handbook section 2.5
- **OS and sys modules** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Use string and text utilities
- Work with collections like Counter and defaultdict
- Handle dates and times with datetime
- Use math and random functions
- Generate combinations and permutations with itertools
- Interact with the operating system
- Use functools for optimization
- Solve real-world problems with the standard library

