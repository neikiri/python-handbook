# Standard Library Cheatsheet

Quick reference for commonly used Python standard library modules.

## pathlib — File Paths

```python
from pathlib import Path

p = Path("file.txt")
p.exists()
p.is_file()
p.is_dir()
p.parent
p.name
p.stem
p.suffix
p.mkdir(parents=True, exist_ok=True)
p.read_text(encoding="utf-8")
p.write_text("content", encoding="utf-8")
```

## json — JSON Data

```python
import json

data = json.loads(json_string)  # Parse JSON string
json_string = json.dumps(data, indent=2)  # Convert to JSON string
json.load(file_object)  # Read from file
json.dump(data, file_object)  # Write to file
```

## csv — CSV Files

```python
import csv

# Read
with open("file.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Write
with open("file.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
```

## datetime — Dates and Times

```python
from datetime import datetime, date, timedelta

now = datetime.now()  # Current date and time
today = date.today()  # Current date

# Create specific date/time
d = datetime(2024, 5, 27, 14, 30, 0)
d = datetime.fromisoformat("2024-05-27T14:30:00")

# Formatting
d.strftime("%Y-%m-%d")  # "2024-05-27"
d.strftime("%H:%M:%S")  # "14:30:00"

# Arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

## random — Random Numbers

```python
import random

random.random()  # Float between 0.0 and 1.0
random.randint(1, 10)  # Integer between 1 and 10 (inclusive)
random.choice([1, 2, 3])  # Random item from list
random.shuffle(list)  # Shuffle list in place
random.sample([1, 2, 3, 4, 5], 3)  # 3 random items without replacement
```

## secrets — Secure Random Numbers

```python
import secrets

secrets.randbelow(100)  # Secure random integer
secrets.choice([1, 2, 3])  # Secure random choice
secrets.token_hex(16)  # Random hex token
```

## collections — Specialized Collections

```python
from collections import Counter, defaultdict, namedtuple

# Counter
counts = Counter([1, 1, 2, 2, 2, 3])
counts[1]  # 2
counts.most_common(2)  # [(2, 3), (1, 2)]

# defaultdict
d = defaultdict(list)
d["key"].append(1)  # No KeyError

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x  # 1
```

## itertools — Iteration Tools

```python
from itertools import combinations, permutations, chain, repeat

# Combinations
list(combinations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 3)]

# Permutations
list(permutations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 1), ...]

# Chain
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# Repeat
list(repeat(1, 3))  # [1, 1, 1]
```

## functools — Function Tools

```python
from functools import reduce

# reduce
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10

# lru_cache (memoization)
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## statistics — Statistics

```python
from statistics import mean, median, stdev

data = [1, 2, 3, 4, 5]
mean(data)  # 3.0
median(data)  # 3
stdev(data)  # Standard deviation
```

## argparse — Command-Line Arguments

```python
import argparse

parser = argparse.ArgumentParser(description="My program")
parser.add_argument("name", help="Your name")
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()
print(args.name)
print(args.age)
```

## logging — Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

## re — Regular Expressions

```python
import re

# Search
match = re.search(r"\d+", "abc123def")
if match:
    print(match.group())  # "123"

# Find all
matches = re.findall(r"\d+", "abc123def456")  # ["123", "456"]

# Replace
result = re.sub(r"\d+", "X", "abc123def456")  # "abcXdefX"

# Split
parts = re.split(r"\s+", "a  b   c")  # ["a", "b", "c"]
```

## os and sys — System Interaction

```python
import os
import sys

# os
os.getcwd()  # Current directory
os.listdir(".")  # List files
os.path.exists("file.txt")
os.path.join("folder", "file.txt")

# sys
sys.argv  # Command-line arguments
sys.exit(0)  # Exit program
sys.version  # Python version
```

## When to Check the Standard Library First

Before installing a third-party package, check if the standard library has what you need:

- **File paths**: Use `pathlib` (not `os.path`)
- **JSON**: Use `json` (built-in)
- **CSV**: Use `csv` (built-in)
- **Dates/times**: Use `datetime` (built-in)
- **Random numbers**: Use `random` (built-in)
- **Regular expressions**: Use `re` (built-in)
- **Command-line arguments**: Use `argparse` (built-in)
- **Logging**: Use `logging` (built-in)
- **Testing**: Use `unittest` or `pytest` (pytest requires install)

The standard library is powerful and well-tested. Many common tasks don't require external dependencies.