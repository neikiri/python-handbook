# Standard Library Modules Reference

Comprehensive reference for commonly used Python standard library modules.

## pathlib — Object-Oriented Filesystem Paths

**When to use**: Working with file paths and filesystem operations.

```python
from pathlib import Path

# Create paths
p = Path("file.txt")
p = Path("folder") / "file.txt"

# Path properties
p.exists()
p.is_file()
p.is_dir()
p.parent
p.name
p.stem
p.suffix

# Path operations
p.mkdir(parents=True, exist_ok=True)
p.read_text(encoding="utf-8")
p.write_text("content", encoding="utf-8")
p.glob("*.txt")
```

**Prefer over**: `os.path` (older, string-based API)

## os — Operating System Interface

**When to use**: System-level operations, environment variables, process management.

```python
import os

# Directory operations
os.getcwd()
os.chdir("folder")
os.listdir(".")
os.mkdir("folder")
os.makedirs("a/b/c")

# Path operations
os.path.exists("file.txt")
os.path.join("folder", "file.txt")
os.path.dirname("folder/file.txt")
os.path.basename("folder/file.txt")

# Environment
os.environ["HOME"]
os.getenv("HOME", "default")

# Process
os.system("command")
```

**Note**: Prefer `pathlib` for path operations.

## sys — System-Specific Parameters

**When to use**: Command-line arguments, Python version, exit codes.

```python
import sys

# Command-line arguments
sys.argv  # List of arguments

# Python info
sys.version
sys.platform
sys.executable

# Exit
sys.exit(0)  # Exit with code 0
sys.exit(1)  # Exit with error code 1

# Standard streams
sys.stdout
sys.stderr
sys.stdin
```

## json — JSON Encoder and Decoder

**When to use**: Reading/writing JSON data, API responses.

```python
import json

# Parse JSON string
data = json.loads('{"name": "Alice"}')

# Convert to JSON string
json_str = json.dumps(data, indent=2)

# Read from file
with open("file.json") as f:
    data = json.load(f)

# Write to file
with open("file.json", "w") as f:
    json.dump(data, f, indent=2)
```

## csv — CSV File Reading and Writing

**When to use**: Reading/writing CSV files.

```python
import csv

# Read
with open("file.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read as dictionaries
with open("file.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Write
with open("file.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
```

## datetime — Date and Time

**When to use**: Working with dates, times, and timestamps.

```python
from datetime import datetime, date, timedelta

# Current date/time
now = datetime.now()
today = date.today()

# Create specific date/time
d = datetime(2024, 5, 27, 14, 30, 0)

# Formatting
d.strftime("%Y-%m-%d")  # "2024-05-27"
d.strftime("%H:%M:%S")  # "14:30:00"

# Parsing
d = datetime.fromisoformat("2024-05-27T14:30:00")

# Arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

## time — Time Access and Conversions

**When to use**: Measuring elapsed time, sleeping, timestamps.

```python
import time

# Current time
time.time()  # Seconds since epoch

# Sleep
time.sleep(1)  # Sleep for 1 second

# Formatting
time.strftime("%Y-%m-%d %H:%M:%S")
```

## random — Random Number Generation

**When to use**: Generating random numbers, shuffling, sampling.

```python
import random

# Random float
random.random()  # 0.0 to 1.0

# Random integer
random.randint(1, 10)  # 1 to 10 inclusive

# Random choice
random.choice([1, 2, 3])

# Shuffle
lst = [1, 2, 3]
random.shuffle(lst)

# Sample
random.sample([1, 2, 3, 4, 5], 3)  # 3 random items
```

**Note**: Use `secrets` for cryptographic randomness.

## secrets — Secure Random Numbers

**When to use**: Generating tokens, passwords, security-sensitive random values.

```python
import secrets

# Secure random integer
secrets.randbelow(100)

# Secure random choice
secrets.choice([1, 2, 3])

# Random token
secrets.token_hex(16)
secrets.token_urlsafe(16)
```

## collections — Specialized Collection Types

**When to use**: Specialized data structures beyond list/dict/set.

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter
counts = Counter([1, 1, 2, 2, 2, 3])
counts[1]  # 2
counts.most_common(2)

# defaultdict
d = defaultdict(list)
d["key"].append(1)

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

# deque
d = deque([1, 2, 3])
d.appendleft(0)
d.pop()
```

## itertools — Iteration Tools

**When to use**: Creating iterators for efficient looping.

```python
from itertools import combinations, permutations, chain, repeat, cycle

# Combinations
combinations([1, 2, 3], 2)

# Permutations
permutations([1, 2, 3], 2)

# Chain
chain([1, 2], [3, 4])

# Repeat
repeat(1, 3)

# Cycle
cycle([1, 2, 3])
```

## functools — Function Tools

**When to use**: Function composition, memoization, partial functions.

```python
from functools import reduce, lru_cache, partial

# reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])

# lru_cache (memoization)
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# partial
add_five = partial(lambda x, y: x + y, 5)
add_five(3)  # 8
```

## statistics — Statistics

**When to use**: Computing basic statistics.

```python
from statistics import mean, median, stdev, variance

data = [1, 2, 3, 4, 5]
mean(data)  # 3.0
median(data)  # 3
stdev(data)  # Standard deviation
variance(data)  # Variance
```

## argparse — Command-Line Argument Parser

**When to use**: Parsing command-line arguments for scripts.

```python
import argparse

parser = argparse.ArgumentParser(description="My program")
parser.add_argument("name", help="Your name")
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()
print(args.name)
```

## logging — Logging Facility

**When to use**: Recording events and debugging information.

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

**When to use**: Pattern matching and text processing.

```python
import re

# Search
match = re.search(r"\d+", "abc123def")
if match:
    print(match.group())

# Find all
matches = re.findall(r"\d+", "abc123def456")

# Replace
result = re.sub(r"\d+", "X", "abc123def456")

# Split
parts = re.split(r"\s+", "a  b   c")
```

## subprocess — Subprocess Management

**When to use**: Running external programs and capturing output.

```python
import subprocess

# Run command
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)
```

## math — Mathematical Functions

**When to use**: Mathematical operations beyond basic operators.

```python
import math

math.sqrt(16)  # 4.0
math.ceil(3.2)  # 4
math.floor(3.8)  # 3
math.pi  # 3.14159...
math.e  # 2.71828...
math.sin(math.pi / 2)  # 1.0
```

## unittest / pytest — Testing

**When to use**: Writing and running tests.

```python
# unittest (built-in)
import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

# pytest (requires installation)
def test_addition():
    assert 2 + 2 == 4
```

## When to Use Each Module

| Task | Module |
|------|--------|
| File paths | `pathlib` |
| JSON data | `json` |
| CSV files | `csv` |
| Dates/times | `datetime` |
| Random numbers | `random` |
| Secure random | `secrets` |
| Statistics | `statistics` |
| Command-line args | `argparse` |
| Logging | `logging` |
| Pattern matching | `re` |
| External programs | `subprocess` |
| Math functions | `math` |
| Testing | `unittest` or `pytest` |