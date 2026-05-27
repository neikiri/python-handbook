# Chapter 11: Comprehensions and Generators

## 1. Overview

Python gives you concise, readable syntax for building collections and
processing sequences without writing explicit loops every time. These tools —
comprehensions and generators — are among the most distinctively Pythonic
features of the language.

**Comprehensions** let you build lists, sets, and dicts in a single expression.
**Generators** let you produce values one at a time, on demand, without
building the entire sequence in memory first.

Used well, these features make code shorter and often faster. Used carelessly,
they produce unreadable one-liners. This chapter shows you both how to use
them and when to reach for a plain loop instead.

---

## 2. What You Will Learn

- List comprehensions: syntax, filtering, and nesting
- Set comprehensions
- Dictionary comprehensions
- Generator expressions: lazy evaluation and memory efficiency
- Generator functions with `yield`
- The difference between a generator and a list
- `yield from` for delegating to sub-generators
- When to use comprehensions vs. loops vs. generators
- Common built-in functions that work with iterables: `any()`, `all()`,
  `sum()`, `min()`, `max()`, `enumerate()`, `zip()`

---

## 3. Core Concepts

### 3.1 List Comprehensions

A **list comprehension** builds a new list by applying an expression to each
item in an iterable.

```python
# Basic form
[expression for item in iterable]

# With a filter
[expression for item in iterable if condition]
```

Compare the loop version with the comprehension version:

```python
# Loop
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# Comprehension — same result, one line
squares = [n ** 2 for n in range(1, 6)]

print(squares)   # [1, 4, 9, 16, 25]
```

#### Filtering with `if`

Add an `if` clause to include only items that meet a condition.

```python
# Only even numbers
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10]

# Words longer than 4 characters
words = ["apple", "fig", "banana", "kiwi", "cherry"]
long_words = [w for w in words if len(w) > 4]
print(long_words)   # ['apple', 'banana', 'cherry']
```

#### Transforming items

The expression can be any valid Python expression.

```python
names = ["alice", "bob", "charlie"]
upper = [name.upper() for name in names]
print(upper)   # ['ALICE', 'BOB', 'CHARLIE']

# Extract a field from a list of dicts
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 92},
]
grades = [s["grade"] for s in students]
print(grades)   # [88, 92]
```

#### Nested comprehensions

You can nest `for` clauses to iterate over multiple iterables.

```python
# All pairs (x, y) where x != y
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(pairs)
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

This is equivalent to nested loops:

```python
pairs = []
for x in range(1, 4):
    for y in range(1, 4):
        if x != y:
            pairs.append((x, y))
```

Flattening a matrix is a common use case:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in matrix for value in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Conditional expression in the output

You can use a ternary expression in the output part (not the filter part) to
transform items differently based on a condition.

```python
# Replace negatives with 0
numbers = [4, -1, 7, -3, 2, -5]
clamped = [n if n >= 0 else 0 for n in numbers]
print(clamped)   # [4, 0, 7, 0, 2, 0]
```

The structure is:
```python
[value_if_true if condition else value_if_false for item in iterable]
```

---

### 3.2 Set Comprehensions

A **set comprehension** builds a set using the same syntax as a list
comprehension, but with curly braces.

```python
{expression for item in iterable if condition}
```

```python
# Unique lengths of words
words = ["apple", "fig", "banana", "kiwi", "cherry", "plum"]
lengths = {len(w) for w in words}
print(lengths)   # {3, 4, 5, 6}  — order not guaranteed
```

Duplicates are automatically removed, just like a regular set.

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in numbers}
print(unique_squares)   # {1, 4, 9, 16}
```

---

### 3.3 Dictionary Comprehensions

A **dict comprehension** builds a dictionary from an iterable.

```python
{key_expression: value_expression for item in iterable if condition}
```

```python
# Map each word to its length
words = ["apple", "fig", "banana"]
lengths = {word: len(word) for word in words}
print(lengths)   # {'apple': 5, 'fig': 3, 'banana': 6}

# Squares dict
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Inverting a dictionary

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}
```

#### Filtering a dictionary

```python
scores = {"Alice": 88, "Bob": 55, "Charlie": 92, "Diana": 47}
passing = {name: score for name, score in scores.items() if score >= 60}
print(passing)   # {'Alice': 88, 'Charlie': 92}
```

---

### 3.4 Generator Expressions

A **generator expression** looks like a list comprehension but uses
parentheses instead of square brackets. It does not build a list in memory —
it produces values one at a time, on demand.

```python
# List comprehension — builds the whole list immediately
squares_list = [n ** 2 for n in range(1_000_000)]   # uses ~8 MB

# Generator expression — produces values lazily
squares_gen = (n ** 2 for n in range(1_000_000))    # uses ~200 bytes
```

You iterate over a generator the same way you iterate over a list.

```python
gen = (n ** 2 for n in range(5))

for value in gen:
    print(value, end=" ")
# 0 1 4 9 16
```

But a generator can only be iterated **once**. After it is exhausted, it
produces no more values.

```python
gen = (n ** 2 for n in range(3))
print(list(gen))   # [0, 1, 4]
print(list(gen))   # []  — already exhausted
```

#### Passing a generator to a function

When a generator expression is the only argument to a function, you can omit
the extra parentheses.

```python
total = sum(n ** 2 for n in range(1, 6))
print(total)   # 55

largest = max(len(w) for w in ["apple", "fig", "banana"])
print(largest)   # 6

any_negative = any(n < 0 for n in [1, 2, -3, 4])
print(any_negative)   # True
```

This is more memory-efficient than building a list first.

---

### 3.5 Generator Functions

A **generator function** uses `yield` instead of `return`. Each time the
caller asks for the next value, the function resumes from where it left off.

```python
def count_up(start: int, stop: int):
    """Yield integers from start to stop (inclusive)."""
    current = start
    while current <= stop:
        yield current
        current += 1


for n in count_up(1, 5):
    print(n, end=" ")
# 1 2 3 4 5
```

The function body does not run when you call `count_up(1, 5)`. It runs
incrementally each time the caller requests the next value.

#### How `yield` works

1. The caller calls the generator function — Python returns a generator object
   without running any code.
2. The caller calls `next()` on the generator (or iterates with `for`).
3. The function runs until it hits `yield`, returns that value, and **pauses**.
4. The next call to `next()` resumes from the line after `yield`.
5. When the function returns (or falls off the end), `StopIteration` is raised.

```python
def simple():
    print("before first yield")
    yield 1
    print("before second yield")
    yield 2
    print("after last yield")


gen = simple()
print(next(gen))   # before first yield → 1
print(next(gen))   # before second yield → 2
# next(gen)        # after last yield → StopIteration
```

#### Infinite generators

Generators can produce an infinite sequence because they never build the whole
thing in memory.

```python
def integers_from(n: int):
    """Yield integers starting from n, forever."""
    while True:
        yield n
        n += 1


gen = integers_from(1)
for _ in range(5):
    print(next(gen), end=" ")
# 1 2 3 4 5
```

#### Generating Fibonacci numbers

```python
def fibonacci():
    """Yield Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_ten = [next(fib) for _ in range(10)]
print(first_ten)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### 3.6 `yield from`

`yield from` delegates to another iterable or generator, yielding each of its
values in turn.

```python
def chain(*iterables):
    """Yield all items from each iterable in sequence."""
    for iterable in iterables:
        yield from iterable


for item in chain([1, 2], [3, 4], [5]):
    print(item, end=" ")
# 1 2 3 4 5
```

Without `yield from`, you would need an inner loop:

```python
def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item
```

`yield from` is also useful for recursive generators:

```python
def flatten(nested):
    """Recursively yield all non-list items from a nested structure."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


print(list(flatten([1, [2, [3, 4]], [5, 6]])))
# [1, 2, 3, 4, 5, 6]
```

---

### 3.7 Generators vs. Lists

| | List | Generator |
|---|---|---|
| Memory | Stores all values | Stores only current state |
| Speed to create | Immediate | Immediate (no work done yet) |
| Iteration | Multiple times | Once only |
| Indexing | Yes (`items[2]`) | No |
| `len()` | Yes | No |
| Best for | Small data, multiple passes | Large/infinite data, single pass |

**Use a list when:**
- You need to iterate over the data more than once.
- You need random access by index.
- You need `len()`.
- The data is small enough to fit comfortably in memory.

**Use a generator when:**
- The data is large or infinite.
- You only need one pass.
- You want to pipeline transformations without intermediate lists.

---

### 3.8 Useful Built-in Functions for Iterables

These functions work with any iterable — lists, generators, sets, dicts, etc.

#### `any()` and `all()`

```python
numbers = [2, 4, 6, 7, 8]

print(any(n % 2 != 0 for n in numbers))   # True  — at least one odd
print(all(n > 0 for n in numbers))        # True  — all positive
print(all(n % 2 == 0 for n in numbers))   # False — not all even
```

`any()` short-circuits on the first `True`. `all()` short-circuits on the
first `False`. This makes them efficient with generators.

#### `sum()`, `min()`, `max()`

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]

print(sum(data))          # 31
print(min(data))          # 1
print(max(data))          # 9

# With a key function
words = ["banana", "apple", "fig"]
print(min(words, key=len))   # fig
print(max(words, key=len))   # banana
```

#### `enumerate()` and `zip()`

These were covered in Chapter 8 but are worth repeating here because they
return iterators (not lists) and work naturally with comprehensions.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

# Enumerate
indexed = [(i, name) for i, name in enumerate(names, start=1)]
print(indexed)   # [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]

# Zip
paired = {name: score for name, score in zip(names, scores)}
print(paired)   # {'Alice': 88, 'Bob': 92, 'Charlie': 75}
```

---

## 4. Practical Examples

### 4.1 Cleaning a Dataset

```python
raw_data = ["  Alice ", "BOB", "", "  charlie", None, "Diana  "]

cleaned = [
    name.strip().title()
    for name in raw_data
    if name and name.strip()
]
print(cleaned)   # ['Alice', 'Bob', 'Charlie', 'Diana']
```

---

### 4.2 Building a Lookup Table

```python
# Map each character to its ASCII code
ascii_table = {char: ord(char) for char in "abcdefghijklmnopqrstuvwxyz"}
print(ascii_table["a"])   # 97
print(ascii_table["z"])   # 122
```

---

### 4.3 Transposing a Matrix

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

for row in transposed:
    print(row)
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
```

Using `zip(*matrix)` is more idiomatic:

```python
transposed = [list(row) for row in zip(*matrix)]
```

---

### 4.4 Lazy File Processing

Reading a large file line by line with a generator avoids loading the whole
file into memory.

```python
def read_non_empty_lines(path: str):
    """Yield non-empty, stripped lines from a file."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                yield stripped


# Usage:
# for line in read_non_empty_lines("data.txt"):
#     process(line)
```

---

### 4.5 Generating a Multiplication Table

```python
size = 5
table = {(i, j): i * j for i in range(1, size + 1) for j in range(1, size + 1)}

# Print it
for i in range(1, size + 1):
    row = [f"{table[(i, j)]:3}" for j in range(1, size + 1)]
    print(" ".join(row))

#   1   2   3   4   5
#   2   4   6   8  10
#   3   6   9  12  15
#   4   8  12  16  20
#   5  10  15  20  25
```

---

### 4.6 Infinite Counter with `itertools.islice`

```python
from itertools import islice


def naturals():
    """Yield 1, 2, 3, ... forever."""
    n = 1
    while True:
        yield n
        n += 1


# Take the first 10 natural numbers
first_ten = list(islice(naturals(), 10))
print(first_ten)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sum of first 100 squares
total = sum(n ** 2 for n in islice(naturals(), 100))
print(total)   # 338350
```

---

### 4.7 Pipeline of Generators

Generators can be chained into a pipeline where each stage processes values
from the previous one, all lazily.

```python
def read_numbers(data: list[str]):
    """Yield each string from the input."""
    yield from data


def parse_ints(strings):
    """Yield integers, skipping non-numeric strings."""
    for s in strings:
        if s.strip().lstrip("-").isdigit():
            yield int(s.strip())


def only_positive(numbers):
    """Yield only positive numbers."""
    for n in numbers:
        if n > 0:
            yield n


raw = ["3", "  -1 ", "hello", "7", "0", "  4 ", "bad", "-2"]

pipeline = only_positive(parse_ints(read_numbers(raw)))
print(list(pipeline))   # [3, 7, 4]
```

Each stage is a generator — no intermediate lists are created.

---

### 4.8 Checking Conditions Across a Collection

```python
scores = [88, 92, 75, 60, 45, 98]

# Did anyone fail?
print(any(s < 60 for s in scores))    # True

# Did everyone pass?
print(all(s >= 60 for s in scores))   # False

# How many passed?
passed = sum(1 for s in scores if s >= 60)
print(f"{passed}/{len(scores)} passed")   # 5/6 passed

# Average of passing scores
passing_scores = [s for s in scores if s >= 60]
avg = sum(passing_scores) / len(passing_scores)
print(f"Average passing score: {avg:.1f}")   # Average passing score: 82.6
```

---

### 4.9 Unique Words in Order

```python
def unique_words(text: str) -> list[str]:
    """Return unique words in the order they first appear."""
    seen: set[str] = set()
    return [
        word
        for word in text.lower().split()
        if word not in seen and not seen.add(word)
    ]


text = "the cat sat on the mat the cat"
print(unique_words(text))   # ['the', 'cat', 'sat', 'on', 'mat']
```

Note: `seen.add(word)` returns `None` (falsy), so `not seen.add(word)` is
always `True` — it is used purely for its side effect of adding to the set.
This is a clever trick, but a plain loop is clearer for most readers:

```python
def unique_words(text: str) -> list[str]:
    seen: set[str] = set()
    result = []
    for word in text.lower().split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result
```

---

### 4.10 Batching an Iterable

```python
def batched(iterable, size: int):
    """Yield successive chunks of `size` items from iterable."""
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


data = list(range(1, 12))
for chunk in batched(data, 3):
    print(chunk)

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10, 11]
```

Python 3.12 added `itertools.batched()` for this exact purpose.

---

## 5. Common Mistakes

### 5.1 Writing Unreadable Comprehensions

Comprehensions should be easy to read at a glance. If you need to squint,
use a loop.

```python
# Hard to read — too much going on
result = [f"{k}={v}" for d in data for k, v in d.items() if v is not None and k != "id"]

# Clearer as a loop
result = []
for d in data:
    for k, v in d.items():
        if v is not None and k != "id":
            result.append(f"{k}={v}")
```

A good rule of thumb: if a comprehension does not fit comfortably on two
lines, write a loop.

---

### 5.2 Exhausting a Generator Accidentally

A generator can only be iterated once. Iterating it a second time yields
nothing.

```python
gen = (n ** 2 for n in range(5))

print(list(gen))   # [0, 1, 4, 9, 16]
print(list(gen))   # []  — already exhausted

# Fix: recreate the generator, or use a list if you need multiple passes
squares = [n ** 2 for n in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
print(squares)   # [0, 1, 4, 9, 16]
```

---

### 5.3 Using a List Comprehension When a Generator Would Do

If you only need to iterate once and pass the result to a function like
`sum()`, `any()`, or `max()`, a generator expression is more memory-efficient.

```python
# Builds a full list in memory, then sums it
total = sum([n ** 2 for n in range(1_000_000)])

# Sums lazily — no list created
total = sum(n ** 2 for n in range(1_000_000))
```

---

### 5.4 Confusing the Filter Position

The `if` clause in a comprehension filters which items are included. It is
not the same as a ternary expression in the output.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Filter: only include even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6]

# Transform: replace odd numbers with 0
zeroed = [n if n % 2 == 0 else 0 for n in numbers]
print(zeroed)  # [0, 2, 0, 4, 0, 6]
```

The filter `if` goes at the end. The ternary `if/else` goes in the expression
at the front.

---

### 5.5 Forgetting That `yield` Makes a Function a Generator

Once a function contains `yield`, calling it returns a generator object — it
does not run the body immediately.

```python
def gen():
    print("start")
    yield 1
    print("end")


g = gen()          # nothing printed yet
print(next(g))     # start → 1
print(next(g))     # end → StopIteration
```

If you expect the function to run immediately, use `return` instead of
`yield`.

---

### 5.6 Nested Comprehension Loop Order

The loop order in a nested comprehension matches the order you would write
nested `for` loops — outer loop first, inner loop second.

```python
# Outer: rows, Inner: columns
flat = [matrix[r][c] for r in range(3) for c in range(3)]

# Equivalent loops:
flat = []
for r in range(3):       # outer
    for c in range(3):   # inner
        flat.append(matrix[r][c])
```

A common mistake is reversing the order and getting unexpected results.

---

## 6. Practice Tasks

1. Write a list comprehension that produces all multiples of 3 between 1 and
   50 (inclusive).

2. Write a dict comprehension that maps each word in a list to `True` if it
   starts with a vowel, `False` otherwise.

3. Write a generator function `evens_up_to(n)` that yields all even numbers
   from 0 to `n` (inclusive).

4. Write a generator function `running_total(numbers)` that yields the
   cumulative sum after each item. For example, `[1, 2, 3, 4]` yields
   `1, 3, 6, 10`.

5. Use `any()` and `all()` with generator expressions to check whether a list
   of strings contains any empty string, and whether all strings are
   lowercase.

6. Write a set comprehension that produces the set of all first letters (
   lowercase) from a list of words.

7. Write a function `take(n, iterable)` that returns the first `n` items from
   any iterable as a list, without consuming the rest.

8. Rewrite the following loop as a list comprehension:

   ```python
   result = []
   for sentence in paragraphs:
       for word in sentence.split():
           if len(word) > 5:
               result.append(word.lower())
   ```

---

## 7. Key Takeaways

- **List comprehensions** build lists concisely: `[expr for x in iterable if
  cond]`. They are clearer than loops for simple transformations and filters.
- **Set comprehensions** `{expr for x in iterable}` build sets — duplicates
  are removed automatically.
- **Dict comprehensions** `{k: v for x in iterable}` build dictionaries from
  any iterable.
- **Generator expressions** `(expr for x in iterable)` are lazy — they
  produce values on demand and use almost no memory.
- **Generator functions** use `yield` to pause and resume execution. They are
  ideal for large or infinite sequences.
- A generator can only be iterated once. Use a list if you need multiple
  passes.
- `yield from` delegates to another iterable, simplifying recursive and
  chained generators.
- `any()`, `all()`, `sum()`, `min()`, and `max()` all accept generator
  expressions directly — no intermediate list needed.
- Keep comprehensions readable. If the logic is complex, a plain loop is
  clearer.
- Prefer generator expressions over list comprehensions when you only need
  one pass and are passing the result to a consuming function.

---

### What's Next

Chapter 12 covers **errors, exceptions, and debugging** — how to handle things
that go wrong, write defensive code, and track down bugs when they happen.

---

*See also:*
- [Exercises for Chapter 11](../exercises/11-comprehensions-generators.md)
- [Solutions for Chapter 11](../solutions/11-comprehensions-generators.md)
- [Cheatsheet: Syntax](../cheatsheets/syntax.md)
