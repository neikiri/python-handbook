# Chapter 17: Standard Library Tour

## 1. Overview

Python ships with a large standard library — hundreds of modules covering
everything from file I/O to networking to data manipulation. You do not need
to install anything extra; these modules are available in every standard
Python installation.

This chapter tours eleven of the most useful modules for everyday programming.
Some you will reach for in almost every project; others solve specific problems
cleanly when you need them. The goal is not to memorize every function, but to
know what is available so you can reach for the right tool.

---

## 2. What You Will Learn

- Manipulating filesystem paths with `pathlib`
- Serializing and deserializing data with `json`
- Working with dates, times, and durations with `datetime`
- Generating random values with `random`
- Efficient data structures with `collections`
- Lazy iteration utilities with `itertools`
- Higher-order function tools with `functools`
- Parsing command-line arguments with `argparse`
- Structured application logging with `logging`
- Pattern matching in text with `re`
- Basic descriptive statistics with `statistics`

---

## 3. Core Concepts

### 3.1 `pathlib` — Path Objects

`pathlib` represents filesystem paths as objects rather than plain strings.
Path objects know about their components, support the `/` operator for joining,
and have methods for reading, writing, and querying the filesystem.

Chapter 13 covers file I/O in depth. This section focuses on path manipulation.

```python
from pathlib import Path

# Build paths with /
base = Path("data")
report = base / "2024" / "report.csv"
print(report)          # data/2024/report.csv

# Inspect components
p = Path("docs/handbook/17-standard-library.md")
print(p.name)          # 17-standard-library.md
print(p.stem)          # 17-standard-library
print(p.suffix)        # .md
print(p.parent)        # docs/handbook
print(p.parts)         # ('docs', 'handbook', '17-standard-library.md')
```


#### Changing parts of a path

```python
p = Path("reports/draft.txt")

# Change the suffix
print(p.with_suffix(".md"))    # reports/draft.md

# Change the name
print(p.with_name("final.txt"))  # reports/final.txt

# Change the stem only
print(p.with_stem("published"))  # reports/published.txt
```

#### Checking existence and listing

```python
p = Path("docs")

print(p.exists())    # True or False
print(p.is_file())   # True if it is a file
print(p.is_dir())    # True if it is a directory

# All items in a directory
for item in p.iterdir():
    print(item.name)

# Recursive glob — all Python files under docs/
for py_file in p.rglob("*.py"):
    print(py_file)
```

#### Creating directories and files

```python
# Create a directory tree
Path("output/reports/2024").mkdir(parents=True, exist_ok=True)

# Create an empty file
Path("placeholder.txt").touch()

# Remove a file (no error if missing)
Path("temp.txt").unlink(missing_ok=True)
```

---

### 3.2 `json` — Serialization

`json` converts Python objects to JSON strings and back. Chapter 13 covers
the full API. The pattern below is the one you will use most often.

```python
import json
from pathlib import Path

# Serialize to a file
data = {"name": "Alice", "scores": [95, 87, 92], "active": True}
Path("user.json").write_text(json.dumps(data, indent=2), encoding="utf-8")

# Deserialize from a file
loaded = json.loads(Path("user.json").read_text(encoding="utf-8"))
print(loaded["name"])    # Alice
print(loaded["scores"])  # [95, 87, 92]
```


Use `json.load(f)` / `json.dump(data, f)` when you already have an open file
object. Use `json.loads(s)` / `json.dumps(data)` when working with strings.

---

### 3.3 `datetime` — Dates and Times

The `datetime` module provides three main types: `date` (year/month/day),
`datetime` (date + time), and `timedelta` (a duration).

```python
from datetime import date, datetime, timedelta

# Today's date
today = date.today()
print(today)                  # 2024-03-15

# Current date and time
now = datetime.now()
print(now)                    # 2024-03-15 09:30:45.123456

# Construct specific values
birthday = date(1990, 7, 4)
meeting = datetime(2024, 3, 20, 14, 30)   # March 20 at 14:30
```

#### Arithmetic with `timedelta`

```python
from datetime import date, timedelta

today = date.today()
in_two_weeks = today + timedelta(weeks=2)
yesterday = today - timedelta(days=1)

delta = date(2024, 12, 31) - today
print(f"{delta.days} days until end of year")
```

#### Formatting with `strftime`

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))           # 2024-03-15
print(now.strftime("%d/%m/%Y %H:%M"))     # 15/03/2024 09:30
print(now.strftime("%A, %B %d, %Y"))      # Friday, March 15, 2024
```

Common format codes: `%Y` year, `%m` month, `%d` day, `%H` hour (24h),
`%M` minute, `%S` second, `%A` weekday name, `%B` month name.

#### Parsing with `strptime`

```python
from datetime import datetime

raw = "2024-03-15 09:30"
dt = datetime.strptime(raw, "%Y-%m-%d %H:%M")
print(dt.year)    # 2024
print(dt.hour)    # 9
```

`strptime` is the inverse of `strftime`: give it a string and the format it
was written in, and it returns a `datetime` object.

---

### 3.4 `random` — Random Values

The `random` module generates pseudo-random numbers and makes random choices.
Always call `random.seed(n)` in tests or simulations where you need
reproducible results.

```python
import random

# Random integer in [a, b] inclusive
n = random.randint(1, 6)       # simulates a die roll

# Random float in [0.0, 1.0)
f = random.random()

# Random choice from a sequence
colours = ["red", "green", "blue"]
pick = random.choice(colours)

# Multiple unique choices (no replacement)
sample = random.sample(range(100), k=5)   # 5 unique numbers from 0–99

# Shuffle a list in place
deck = list(range(1, 53))
random.shuffle(deck)
```


#### Reproducible results with `seed`

```python
import random

random.seed(42)
print(random.randint(1, 100))   # always the same value for seed 42
print(random.choice(["a", "b", "c"]))
```

---

### 3.5 `collections` — Specialized Data Structures

`collections` extends Python's built-in containers with four types you will
reach for regularly.

#### `Counter`

Counts hashable objects. Pass any iterable and get a dict-like object mapping
items to their counts.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts["apple"])          # 3
print(counts.most_common(2))    # [('apple', 3), ('banana', 2)]

# Counters support arithmetic
a = Counter("aabbc")
b = Counter("abcd")
print(a + b)    # Counter({'a': 3, 'b': 3, 'c': 2, 'd': 1})
```

#### `defaultdict`

Like a regular `dict`, but automatically creates a default value for missing
keys instead of raising `KeyError`.

```python
from collections import defaultdict

# Group words by first letter
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
by_letter: defaultdict[str, list[str]] = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)

print(dict(by_letter))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

The argument to `defaultdict` is a callable that produces the default value:
`list` for lists, `int` for zero-initialized counters, `set` for sets, etc.

#### `namedtuple`

Creates a tuple subclass with named fields. Useful for lightweight, immutable
data records without writing a full class.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(p.x, p.y)    # 3 4
print(p[0])        # 3  — still indexable like a tuple
print(p)           # Point(x=3, y=4)

# Unpack like a regular tuple
x, y = p
```

For mutable records or when you need methods, prefer a dataclass (see
Chapter 16). Use `namedtuple` when you want a simple, immutable value object.

#### `deque`

A double-ended queue. Appending and popping from either end is O(1), unlike
a list where `insert(0, ...)` and `pop(0)` are O(n).

```python
from collections import deque

q: deque[str] = deque()
q.append("a")       # add to right
q.append("b")
q.appendleft("z")   # add to left

print(q)            # deque(['z', 'a', 'b'])
print(q.popleft())  # 'z'
print(q.pop())      # 'b'

# Fixed-size sliding window — oldest item is dropped automatically
recent = deque(maxlen=3)
for n in range(6):
    recent.append(n)
print(recent)       # deque([3, 4, 5], maxlen=3)
```

---

### 3.6 `itertools` — Lazy Iteration

`itertools` provides functions that return iterators — they produce values on
demand rather than building a full list in memory. This makes them efficient
for large or infinite sequences.

```python
import itertools
```

#### `chain` — flatten iterables

```python
from itertools import chain

a = [1, 2, 3]
b = [4, 5]
c = [6]

combined = list(chain(a, b, c))
print(combined)   # [1, 2, 3, 4, 5, 6]

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5]]
flat = list(chain.from_iterable(nested))
print(flat)       # [1, 2, 3, 4, 5]
```

#### `islice` — slice an iterator

```python
from itertools import islice

def integers():
    n = 0
    while True:
        yield n
        n += 1

first_ten = list(islice(integers(), 10))
print(first_ten)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


#### `product` — Cartesian product

```python
from itertools import product

sizes = ["S", "M", "L"]
colours = ["red", "blue"]

for size, colour in product(sizes, colours):
    print(f"{size}-{colour}")
# S-red, S-blue, M-red, M-blue, L-red, L-blue
```

#### `combinations` and `permutations`

```python
from itertools import combinations, permutations

items = ["A", "B", "C"]

# All 2-item combinations (order does not matter)
print(list(combinations(items, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# All 2-item permutations (order matters)
print(list(permutations(items, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

---

### 3.7 `functools` — Higher-Order Functions

`functools` provides tools for working with functions as values.

#### `partial` — fix some arguments

`partial` creates a new function with some arguments pre-filled.

```python
from functools import partial

def power(base: float, exponent: float) -> float:
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

print(square(5))   # 25.0
print(cube(3))     # 27.0
```

#### `lru_cache` — memoize expensive calls

`lru_cache` caches the return value of a function for each unique set of
arguments. Repeated calls with the same arguments return the cached result
instantly.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))   # fast — each value computed only once
print(fibonacci.cache_info())
```

Use `@lru_cache` on pure functions (same inputs always produce the same
output) that are called repeatedly with the same arguments.

#### `reduce` — fold a sequence

`reduce` applies a two-argument function cumulatively to a sequence, reducing
it to a single value.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)   # 15

# Product of all elements
product = reduce(lambda acc, x: acc * x, numbers)
print(product)   # 120
```

For simple cases like summing or multiplying, prefer `sum()` or `math.prod()`.
`reduce` is most useful when the combining operation is non-trivial.

---

### 3.8 `argparse` — Command-Line Arguments

`argparse` parses `sys.argv` and turns it into a structured namespace. Chapter
20 covers CLI programs in depth. This section shows the basic pattern.

```python
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet a user.")
    parser.add_argument("name", help="Name to greet")
    parser.add_argument("--count", "-n", type=int, default=1,
                        help="Number of times to greet (default: 1)")
    parser.add_argument("--shout", action="store_true",
                        help="Print in uppercase")
    args = parser.parse_args()

    message = f"Hello, {args.name}!"
    if args.shout:
        message = message.upper()
    for _ in range(args.count):
        print(message)


if __name__ == "__main__":
    main()
```

Run it:

```bash
python greet.py Alice --count 3 --shout
# HELLO, ALICE!  (printed 3 times)

python greet.py --help
# usage: greet.py [-h] [--count COUNT] [--shout] name
```

`argparse` generates `--help` automatically from the descriptions you provide.


---

### 3.9 `logging` — Structured Application Logging

`print()` is fine for quick debugging, but `logging` is better for real
applications. It lets you control which messages appear, where they go, and
what format they use — without changing your code.

#### Log levels

| Level | Value | When to use |
|---|---|---|
| `DEBUG` | 10 | Detailed diagnostic information |
| `INFO` | 20 | Confirmation that things are working |
| `WARNING` | 30 | Something unexpected, but the program continues |
| `ERROR` | 40 | A serious problem; some functionality failed |
| `CRITICAL` | 50 | A severe error; the program may not continue |

#### Basic setup

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("Starting up")
logging.info("Processing file: report.csv")
logging.warning("File not found, using defaults")
logging.error("Failed to connect to database")
```

Output:

```text
2024-03-15 09:30:00  DEBUG     Starting up
2024-03-15 09:30:00  INFO      Processing file: report.csv
2024-03-15 09:30:00  WARNING   File not found, using defaults
2024-03-15 09:30:00  ERROR     Failed to connect to database
```

#### Named loggers

In larger programs, create a logger per module. This makes log output easier
to trace and lets you control verbosity per module.

```python
import logging

logger = logging.getLogger(__name__)   # name is the module name

def process(data: list) -> None:
    logger.info("Processing %d items", len(data))
    for item in data:
        logger.debug("Item: %s", item)
```

#### Logging to a file

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)
logging.info("Application started")
```

---

### 3.10 `re` — Regular Expressions

Regular expressions are patterns for matching and manipulating text. The `re`
module provides the core functions.

#### The four main functions

| Function | What it does |
|---|---|
| `re.match(pattern, s)` | Match at the start of `s` |
| `re.search(pattern, s)` | Find first match anywhere in `s` |
| `re.findall(pattern, s)` | Return all non-overlapping matches as a list |
| `re.sub(pattern, repl, s)` | Replace all matches with `repl` |

```python
import re

text = "Order #1042 placed on 2024-03-15, total: $49.99"

# search — find first match anywhere
m = re.search(r"\d{4}-\d{2}-\d{2}", text)
if m:
    print(m.group())   # 2024-03-15

# findall — all matches
numbers = re.findall(r"\d+", text)
print(numbers)   # ['1042', '2024', '03', '15', '49', '99']

# sub — replace
clean = re.sub(r"\$[\d.]+", "[PRICE]", text)
print(clean)   # Order #1042 placed on 2024-03-15, total: [PRICE]
```


#### Common pattern elements

| Pattern | Matches |
|---|---|
| `.` | Any character except newline |
| `\d` | A digit `[0-9]` |
| `\w` | A word character `[a-zA-Z0-9_]` |
| `\s` | Whitespace (space, tab, newline) |
| `^` | Start of string |
| `$` | End of string |
| `*` | Zero or more of the preceding |
| `+` | One or more of the preceding |
| `?` | Zero or one of the preceding |
| `{n}` | Exactly n of the preceding |
| `[abc]` | Any of a, b, or c |
| `(...)` | Capture group |

Always use raw strings (`r"..."`) for regex patterns to avoid double-escaping
backslashes.

#### Capture groups

```python
import re

log_line = "2024-03-15 09:30:45 ERROR Failed to open file"
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"

m = re.match(pattern, log_line)
if m:
    date, time, level, message = m.groups()
    print(date)     # 2024-03-15
    print(level)    # ERROR
    print(message)  # Failed to open file
```

#### Compiling patterns

If you use the same pattern many times, compile it once for better performance.

```python
import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

def find_emails(text: str) -> list[str]:
    return EMAIL_RE.findall(text)
```

---

### 3.11 `statistics` — Descriptive Statistics

The `statistics` module provides basic statistical functions for small to
medium datasets. For large datasets or advanced statistics, use NumPy or
pandas instead.

```python
from statistics import mean, median, mode, stdev, variance

scores = [72, 85, 90, 88, 76, 92, 85, 68, 95, 80]

print(f"Mean:     {mean(scores):.1f}")      # 83.1
print(f"Median:   {median(scores):.1f}")    # 86.5
print(f"Mode:     {mode(scores)}")          # 85
print(f"Std dev:  {stdev(scores):.1f}")     # 8.8
```

`stdev` computes the sample standard deviation (divides by n−1). For
population statistics use `pstdev`. `mode` raises `StatisticsError` if there
is no unique mode; use `multimode` when ties are possible.

```python
from statistics import multimode

print(multimode([1, 1, 2, 2, 3]))   # [1, 2]
```

---

## 4. Practical Examples

### 4.1 Dated Log File with `datetime` and `pathlib`

Write log entries to a file named after today's date.

```python
from datetime import datetime
from pathlib import Path


def log_event(message: str, log_dir: str | Path = "logs") -> None:
    """Append a timestamped message to today's log file."""
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = Path(log_dir) / f"{today}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%H:%M:%S")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


log_event("Application started")
log_event("Processed 42 records")
log_event("Application stopped")
```

---

### 4.2 Word Frequency Analysis with `Counter` and `re`

Count the most common words in a block of text, ignoring punctuation.

```python
import re
from collections import Counter


def top_words(text: str, n: int = 10) -> list[tuple[str, int]]:
    """Return the n most common words in text."""
    words = re.findall(r"\b[a-z]+\b", text.lower())
    return Counter(words).most_common(n)


sample = """
Python is an interpreted high-level general-purpose programming language.
Python's design philosophy emphasizes code readability. Python is dynamically
typed and garbage-collected. It supports multiple programming paradigms.
"""

for word, count in top_words(sample):
    print(f"{word:<15} {count}")
```


---

### 4.3 Cached Fibonacci with `lru_cache` and `statistics`

Compute Fibonacci numbers efficiently and report statistics on a range.

```python
from functools import lru_cache
from statistics import mean, stdev


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_stats(start: int, end: int) -> None:
    """Print statistics for Fibonacci numbers in [start, end]."""
    values = [fibonacci(n) for n in range(start, end + 1)]
    print(f"Range:   fib({start}) to fib({end})")
    print(f"Min:     {min(values)}")
    print(f"Max:     {max(values)}")
    print(f"Mean:    {mean(values):.1f}")
    print(f"Std dev: {stdev(values):.1f}")


fib_stats(10, 20)
```

---

### 4.4 Random Sampler with `random` and `namedtuple`

Pick a random subset of items from a named record collection.

```python
import random
from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "year"])

LIBRARY = [
    Book("Clean Code",          "Robert Martin",  2008),
    Book("The Pragmatic Programmer", "Hunt & Thomas", 1999),
    Book("Python Cookbook",     "Beazley & Jones", 2013),
    Book("Fluent Python",       "Luciano Ramalho", 2022),
    Book("Design Patterns",     "Gang of Four",   1994),
]


def reading_list(books: list[Book], n: int, seed: int | None = None) -> list[Book]:
    """Return n randomly chosen books."""
    random.seed(seed)
    return random.sample(books, k=min(n, len(books)))


for book in reading_list(LIBRARY, 3, seed=7):
    print(f"{book.title} ({book.year}) — {book.author}")
```

---

### 4.5 File Inventory with `itertools` and `pathlib`

Scan a directory tree and produce a summary grouped by file extension.

```python
from collections import defaultdict
from itertools import chain
from pathlib import Path


def file_inventory(roots: list[str | Path]) -> dict[str, list[Path]]:
    """
    Return a dict mapping file extension to list of matching paths,
    scanning all given root directories.
    """
    by_ext: defaultdict[str, list[Path]] = defaultdict(list)

    all_files = chain.from_iterable(
        Path(root).rglob("*") for root in roots
    )

    for path in all_files:
        if path.is_file():
            by_ext[path.suffix.lower()].append(path)

    return dict(by_ext)


def print_inventory(roots: list[str]) -> None:
    inventory = file_inventory(roots)
    for ext, files in sorted(inventory.items()):
        print(f"{ext or '(no ext)':12}  {len(files):4} file(s)")


# print_inventory(["docs", "examples"])
```

---

### 4.6 CLI Tool with `argparse` and `logging`

A script that reads a text file and reports the most common words.

```python
import argparse
import logging
from collections import Counter
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyse word frequencies.")
    parser.add_argument("file", type=Path, help="Text file to analyse")
    parser.add_argument("--top", "-n", type=int, default=10,
                        help="Number of top words (default: 10)")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    if not args.file.exists():
        logger.error("File not found: %s", args.file)
        raise SystemExit(1)

    text = args.file.read_text(encoding="utf-8").lower()
    words = text.split()
    counts = Counter(words)
    logger.info("Words: %d total, %d unique", len(words), len(counts))

    print(f"\nTop {args.top} words in {args.file.name}:")
    for word, n in counts.most_common(args.top):
        print(f"  {word:<20} {n}")


if __name__ == "__main__":
    main()
```


---

## 5. Common Mistakes

### 5.1 Using `re.match` When You Mean `re.search`

`re.match` only matches at the start of the string. If the pattern can appear
anywhere, use `re.search`.

```python
import re

text = "Error: file not found"

# Wrong — match only checks the start
m = re.match(r"file", text)
print(m)   # None — "file" is not at the start

# Correct
m = re.search(r"file", text)
print(m.group())   # file
```

---

### 5.2 Forgetting `random.seed` in Tests

Without a seed, `random` produces different results every run. Tests that
depend on random output will be flaky.

```python
import random

# Flaky — different result each run
random.shuffle(items)

# Deterministic — same result every run
random.seed(0)
random.shuffle(items)
```

---

### 5.3 Calling `lru_cache` on a Method

`lru_cache` does not work correctly on instance methods because `self` is part
of the cache key, preventing garbage collection of instances.

```python
from functools import lru_cache

# Wrong — self is cached, instances are never freed
class Converter:
    @lru_cache(maxsize=128)
    def convert(self, value: float) -> float:
        return value * 1.609

# Correct — cache a standalone function, call it from the method
@lru_cache(maxsize=128)
def _km_to_miles(km: float) -> float:
    return km * 0.621

class Converter:
    def convert(self, value: float) -> float:
        return _km_to_miles(value)
```

---

### 5.4 Mutating a `defaultdict` While Iterating

Accessing a missing key in a `defaultdict` creates it. Doing this inside a
loop over the dict raises `RuntimeError: dictionary changed size during iteration`.

```python
from collections import defaultdict

d: defaultdict[str, int] = defaultdict(int)
d["a"] = 1
d["b"] = 2

# Wrong — accessing d["c"] creates a new key mid-iteration
for key in d:
    print(d[key.upper()])   # RuntimeError

# Correct — collect keys first
for key in list(d):
    print(d[key.upper()])
```

---

### 5.5 Using `logging.basicConfig` More Than Once

`basicConfig` only takes effect the first time it is called. Calling it again
(e.g., in a module that is imported) has no effect.

```python
import logging

# First call — takes effect
logging.basicConfig(level=logging.DEBUG)

# Second call — silently ignored
logging.basicConfig(level=logging.WARNING)

logging.debug("This appears — DEBUG level is still active")
```

Configure logging once, at the entry point of your application (usually
`main()` or the top of your script).

---

### 5.6 Ignoring `strptime` Format Mismatches

`strptime` raises `ValueError` if the string does not match the format exactly.
Always handle this in production code.

```python
from datetime import datetime

raw = "15-03-2024"

# Wrong format — raises ValueError
try:
    dt = datetime.strptime(raw, "%Y-%m-%d")
except ValueError as e:
    print(f"Parse error: {e}")

# Correct format
dt = datetime.strptime(raw, "%d-%m-%Y")
print(dt)   # 2024-03-15 00:00:00
```

---

### 5.7 Using `reduce` for Simple Aggregations

`reduce` is harder to read than a loop or a built-in. Prefer `sum()`,
`max()`, `min()`, or `math.prod()` for common cases.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Unnecessarily complex
total = reduce(lambda a, b: a + b, numbers)

# Clear and idiomatic
total = sum(numbers)
```

Reserve `reduce` for operations that genuinely have no built-in equivalent.

---

## 6. Practice Tasks

1. Write a function `age_in_days(birthdate: str) -> int` that accepts a date
   string in `"YYYY-MM-DD"` format and returns how many days old that person
   is today. Use `datetime.strptime` and `date.today`.

2. Write a function `group_by_extension(directory: str) -> dict[str, list[str]]`
   that returns a dict mapping each file extension to a list of filenames
   (not full paths) found in that directory (non-recursive). Use `pathlib`
   and `defaultdict`.

3. Write a function `simulate_dice(n_rolls: int, seed: int = 0) -> Counter`
   that simulates rolling a six-sided die `n_rolls` times and returns a
   `Counter` of the results. Use `random.seed` and `random.randint`.

4. Write a function `extract_urls(text: str) -> list[str]` that uses `re`
   to find all URLs starting with `http://` or `https://` in a string.

5. Write a function `memoized_factorial(n: int) -> int` that computes `n!`
   using recursion and `@lru_cache`. Verify it handles `n = 0` and `n = 1`.

6. Write a function `parse_log_lines(path: str) -> list[dict]` that reads a
   log file where each line has the format `"YYYY-MM-DD HH:MM:SS LEVEL message"`,
   and returns a list of dicts with keys `"timestamp"`, `"level"`, and
   `"message"`. Use `re` to parse each line.

7. Write a script that accepts a directory path as a CLI argument (using
   `argparse`) and prints the five largest files in that directory tree,
   with their sizes in kilobytes. Use `pathlib` and `logging`.

8. Write a function `describe(values: list[float]) -> dict[str, float]` that
   returns a dict with keys `"mean"`, `"median"`, `"stdev"`, `"min"`, and
   `"max"` for the given list. Use the `statistics` module.

---

## 7. Key Takeaways

- `pathlib.Path` is the right tool for all filesystem path work. Use `/` to
  join components, `.stem`/`.suffix`/`.parent` to inspect them, and
  `.rglob()` to search recursively.
- `json.loads`/`json.dumps` work with strings; `json.load`/`json.dump` work
  with file objects. Always use `indent=2` for human-readable output.
- `datetime.strptime` parses strings into `datetime` objects; `strftime`
  formats them back. Use `timedelta` for date arithmetic.
- `random.seed` makes random output reproducible — essential for tests and
  simulations.
- `Counter` counts items; `defaultdict` avoids `KeyError` for missing keys;
  `namedtuple` creates lightweight immutable records; `deque` gives O(1)
  appends and pops from both ends.
- `itertools` functions are lazy — they produce values on demand. Use `chain`
  to flatten, `islice` to limit, `product`/`combinations`/`permutations` for
  combinatorics.
- `functools.partial` pre-fills arguments; `lru_cache` memoizes pure
  functions; `reduce` folds a sequence — but prefer built-ins for simple
  aggregations.
- `argparse` generates `--help` automatically. Always wrap your CLI entry
  point in `if __name__ == "__main__":`.
- Configure `logging` once at the application entry point. Use named loggers
  (`logging.getLogger(__name__)`) in library code.
- Use raw strings (`r"..."`) for regex patterns. Prefer `re.search` over
  `re.match` unless you specifically need to anchor to the start.
- `statistics.mean`/`median`/`mode`/`stdev` cover everyday descriptive
  statistics for small datasets.

---

### Further Reading

- [Standard Library](https://docs.python.org/3/library/index.html)
- [Python Module Index](https://docs.python.org/3/py-modindex.html)
- [The Python Standard Library by Example](https://docs.python.org/3/library/index.html)

### What's Next

Ready to continue? Head to the next chapter: **Testing and Code Quality**.

→ [Chapter 18 — Testing and Code Quality](18-testing-code-quality.md)

*See also:*
- [Exercise](../exercises/17-standard-library.md)
- [Solution](../solutions/17-standard-library.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
