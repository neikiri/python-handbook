# Solutions 11: Comprehensions and Generators

## Overview

Chapter 11 exercises cover list, set, and dictionary comprehensions, generator expressions, generator functions, and built-in functions that work with iterables. This guide explains the reasoning behind each solution and highlights when to prefer each approach.

---

## Notes Before Checking Solutions

Comprehensions are not just a shorter syntax — they communicate intent. A list comprehension says "I am building a new list by transforming or filtering this sequence." A generator says "I am producing values one at a time, lazily." Choosing the right tool matters for both readability and performance.

---

## Warm-up Exercise Solutions

### Exercise 1: Basic List Comprehensions

```python
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25]

evens = [n for n in range(1, 11) if n % 2 == 0]
# [2, 4, 6, 8, 10]

words = ["apple", "banana", "cherry"]
upper = [w.upper() for w in words]
# ['APPLE', 'BANANA', 'CHERRY']

students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 92},
]
names = [s["name"] for s in students]
# ['Alice', 'Bob', 'Carol']

values = [1, 2, 3, 4, 5]
result = ["even" if v % 2 == 0 else "odd" for v in values]
# ['odd', 'even', 'odd', 'even', 'odd']
```

**The conditional expression** `"even" if v % 2 == 0 else "odd"` is the ternary operator. It goes in the *output expression* position (before `for`), not in the filter position (after `for`). The filter position only keeps or drops items; the output expression transforms them.

---

### Exercise 2: Set and Dictionary Comprehensions

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {n for n in numbers}
# {1, 2, 3, 4}  — order not guaranteed

words = ["apple", "banana", "cherry"]
word_lengths = {w: len(w) for w in words}
# {'apple': 5, 'banana': 6, 'cherry': 6}

pairs = [("a", 1), ("b", 2), ("c", 3)]
d = {k: v for k, v in pairs}
# {'a': 1, 'b': 2, 'c': 3}

numbers = range(1, 6)
squares = {n: n ** 2 for n in numbers if n % 2 == 0}
# {2: 4, 4: 16}

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

**Inverting a dictionary** works cleanly when values are unique. If two keys share the same value, the last one wins. Always check that values are unique before inverting.

**Set comprehensions** use `{}` like dict comprehensions, but without the `:`. The result is a `set`, not a `dict`.

---

### Exercise 3: Generator Expressions

```python
import sys

numbers = range(1, 6)
squared_gen = (n ** 2 for n in numbers)
# <generator object <genexpr> at 0x...>

# Consume it
for value in squared_gen:
    print(value)  # 1, 4, 9, 16, 25

# Use with aggregation functions
total = sum(n ** 2 for n in range(1, 6))
# 55

# Memory comparison
list_comp = [n ** 2 for n in range(1000)]
gen_exp = (n ** 2 for n in range(1000))
print(sys.getsizeof(list_comp))  # ~8856 bytes
print(sys.getsizeof(gen_exp))    # ~208 bytes
```

**Generators are lazy.** They produce one value at a time and do not store the entire sequence in memory. This makes them ideal for large datasets or infinite sequences.

**A generator can only be iterated once.** After it is exhausted, iterating it again yields nothing. Convert to a list if you need to iterate multiple times: `values = list(gen_exp)`.

**When to use a generator expression vs. a list comprehension:**
- Use a generator when you only need to iterate once, or when passing to `sum()`, `max()`, `any()`, `all()`.
- Use a list when you need random access, need to iterate multiple times, or need `len()`.

---

### Exercise 4: Generator Functions

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

list(count_up(5))  # [1, 2, 3, 4, 5]

def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

list(squares(5))  # [1, 4, 9, 16, 25]

def double_items(items):
    for item in items:
        yield item * 2

list(double_items([1, 2, 3, 4, 5]))  # [2, 4, 6, 8, 10]
```

**`yield` suspends the function** and returns a value to the caller. The next time the generator is advanced (by `next()` or a `for` loop), execution resumes from where it left off. This is fundamentally different from `return`, which ends the function.

**Generator functions are useful when:**
- The sequence is too large to hold in memory
- You want to express a sequence as a loop with state
- You are building a pipeline of transformations

---

## Practice Exercise Solutions

### Exercise 5: Process Collections with Comprehensions

```python
# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]
```

**Nested comprehension order:** Read it as nested `for` loops. The outer loop (`for sublist in nested`) comes first, the inner loop (`for item in sublist`) comes second. This matches the order you would write them as regular loops.

```python
# Count occurrences
items = ["a", "b", "a", "c", "b", "a"]
counts = {item: items.count(item) for item in set(items)}
# {'a': 3, 'b': 2, 'c': 1}
```

**Note:** `items.count(item)` scans the entire list for each unique item, making this O(n²). For large lists, use `collections.Counter(items)` instead — it is O(n).

```python
from collections import Counter
counts = dict(Counter(items))
```

---

### Exercise 6: Use Built-in Functions with Iterables

```python
numbers = [2, 4, 6, 8]
all(n % 2 == 0 for n in numbers)  # True

numbers = [2, 4, 5, 8]
any(n % 2 == 1 for n in numbers)  # True

words = ["apple", "banana", "cherry"]
for i, word in enumerate(words):
    print(f"{i}: {word}")
# 0: apple, 1: banana, 2: cherry

names = ["Alice", "Bob", "Carol"]
ages = [30, 25, 28]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

**`enumerate()`** is the right way to get both index and value. Avoid `for i in range(len(words)): words[i]` — it is verbose and error-prone.

**`zip()`** stops at the shortest iterable. If the lists have different lengths, the extra elements are silently dropped. Use `itertools.zip_longest()` if you need to handle unequal lengths.

**`any()` and `all()` short-circuit.** `any()` stops as soon as it finds a `True` value. `all()` stops as soon as it finds a `False` value. This makes them efficient with generator expressions.

---

### Exercise 7: Combine Comprehensions and Generators

```python
def process_data(data):
    for item in data:
        if item > 0:
            yield item ** 2

numbers = [-2, -1, 0, 1, 2, 3]
list(process_data(numbers))  # [1, 4, 9]

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiple conditions
numbers = range(1, 21)
result = [n for n in numbers if n % 2 == 0 if n % 3 == 0]
# [6, 12, 18]
```

**Multiple `if` clauses** in a comprehension are equivalent to `and`: `if n % 2 == 0 and n % 3 == 0`. Both styles work; the `and` form is often clearer.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Data Pipeline

```python
def read_data():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even(data):
    return (n for n in data if n % 2 == 0)

def square(data):
    return (n ** 2 for n in data)

def sum_results(data):
    return sum(data)

data = read_data()
result = sum_results(square(filter_even(data)))
# 220  (4 + 16 + 36 + 64 + 100)

# Equivalent one-liner
result2 = sum(n ** 2 for n in data if n % 2 == 0)
# 220
```

**Generator pipelines** are memory-efficient because each stage produces one value at a time. `filter_even` yields a value, `square` immediately squares it, and `sum_results` adds it — no intermediate lists are created.

---

### Challenge 2: Analyze Text with Comprehensions

```python
text = "The quick brown fox jumps over the lazy dog"
words = text.lower().split()

word_counts = {w: words.count(w) for w in set(words)}

chars = [c for c in text if c.isalpha()]
char_counts = {c: chars.count(c) for c in set(chars)}

vowels = [c for c in text.lower() if c in "aeiou"]
consonants = [c for c in text.lower() if c.isalpha() and c not in "aeiou"]
print(f"Vowels: {len(vowels)}, Consonants: {len(consonants)}")
```

Again, `Counter` is more efficient for counting, but comprehensions work fine for small texts.

---

### Challenge 3: Generate Sequences

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

list(fibonacci(10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def primes(limit):
    for num in range(2, limit):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

list(primes(30))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**The prime check** uses `all()` with a generator expression. It checks that no integer from 2 to √num divides evenly into num. Checking up to √num is sufficient — if num has a factor larger than √num, it must also have one smaller than √num.

---

## Common Mistakes

**Exhausted generator.** A generator can only be iterated once. If you need to iterate it again, either convert it to a list or recreate the generator.

```python
gen = (x for x in range(5))
list(gen)  # [0, 1, 2, 3, 4]
list(gen)  # []  — already exhausted
```

**Comprehension too complex.** If a comprehension needs more than two `for` clauses or complex conditions, a regular loop is clearer. Readability matters more than brevity.

**Using a list comprehension when a generator would do.** If you only need to pass the result to `sum()`, `max()`, or `any()`, use a generator expression — it avoids building an intermediate list.

```python
# Unnecessary list
total = sum([n ** 2 for n in range(1000)])

# Better — generator expression
total = sum(n ** 2 for n in range(1000))
```

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 12 - Errors, Exceptions, Debugging](../handbook/12-errors-exceptions-debugging.md)
