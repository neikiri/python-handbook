# Chapter 11: Comprehensions and Generators — Exercises

## Overview

These exercises help you master list, set, and dictionary comprehensions, as well as generator expressions and generator functions. By the end, you will write concise, efficient code for processing sequences.

---

## How to Use These Exercises

- Create a folder called `chapter-11` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Basic List Comprehensions

Create a file called `list_comprehensions.py`:

```python
# Simple transformation
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]
print(f"Squared: {squared}")

# With filtering
evens = [n for n in range(1, 11) if n % 2 == 0]
print(f"Evens: {evens}")

# String transformation
words = ["apple", "banana", "cherry"]
upper = [w.upper() for w in words]
print(f"Uppercase: {upper}")

# Extract from list of dicts
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 92},
]
names = [s["name"] for s in students]
print(f"Names: {names}")

# Conditional transformation
values = [1, 2, 3, 4, 5]
result = ["even" if v % 2 == 0 else "odd" for v in values]
print(f"Even/odd: {result}")
```

Run it and observe how comprehensions work.

---

### Exercise 2: Set and Dictionary Comprehensions

Create a file called `set_dict_comprehensions.py`:

```python
# Set comprehension
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {n for n in numbers}
print(f"Unique: {unique}")

# Set comprehension with filter
evens = {n for n in range(1, 11) if n % 2 == 0}
print(f"Even set: {evens}")

# Dictionary comprehension
words = ["apple", "banana", "cherry"]
word_lengths = {w: len(w) for w in words}
print(f"Word lengths: {word_lengths}")

# Dict from list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = {k: v for k, v in pairs}
print(f"Dict from pairs: {d}")

# Dict with filtering
numbers = range(1, 6)
squares = {n: n ** 2 for n in numbers if n % 2 == 0}
print(f"Even squares: {squares}")

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")
```

Run it and observe set and dict comprehensions.

---

### Exercise 3: Generator Expressions

Create a file called `generator_expressions.py`:

```python
# Generator expression (lazy evaluation)
numbers = range(1, 6)
squared_gen = (n ** 2 for n in numbers)
print(f"Generator: {squared_gen}")
print(f"Type: {type(squared_gen)}")

# Consume the generator
print("Values:")
for value in squared_gen:
    print(f"  {value}")

# Generator with filter
numbers = range(1, 11)
evens_gen = (n for n in numbers if n % 2 == 0)
print(f"\nEven numbers: {list(evens_gen)}")

# Use with sum, max, min
numbers = range(1, 6)
total = sum(n ** 2 for n in numbers)
print(f"Sum of squares: {total}")

maximum = max(n ** 2 for n in numbers)
print(f"Max square: {maximum}")

# Generator vs list
import sys
list_comp = [n ** 2 for n in range(1000)]
gen_exp = (n ** 2 for n in range(1000))
print(f"\nList size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator size: {sys.getsizeof(gen_exp)} bytes")
```

Run it and observe generator efficiency.

---

### Exercise 4: Generator Functions

Create a file called `generator_functions.py`:

```python
# Simple generator function
def count_up(n):
    """Generate numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

print("Count up to 5:")
for num in count_up(5):
    print(f"  {num}")

# Generator with transformation
def squares(n):
    """Generate squares from 1 to n."""
    for i in range(1, n + 1):
        yield i ** 2

print("\nSquares up to 5:")
for sq in squares(5):
    print(f"  {sq}")

# Generator with filtering
def evens(n):
    """Generate even numbers up to n."""
    for i in range(2, n + 1, 2):
        yield i

print("\nEvens up to 10:")
print(list(evens(10)))

# Generator from iterable
def double_items(items):
    """Double each item."""
    for item in items:
        yield item * 2

numbers = [1, 2, 3, 4, 5]
print(f"\nDoubled: {list(double_items(numbers))}")
```

Run it and observe generator functions.

---

## Practice Exercises

### Exercise 5: Process Collections with Comprehensions

Create a file called `process_with_comprehensions.py`:

```python
# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened: {flat}")

# Combine two lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined = [(n, l) for n, l in zip(list1, list2)]
print(f"Combined: {combined}")

# Filter and transform
numbers = range(1, 11)
result = [n * 2 for n in numbers if n % 2 == 0]
print(f"Even numbers doubled: {result}")

# Group by property
words = ["apple", "apricot", "banana", "blueberry", "cherry"]
by_first = {}
for word in words:
    first = word[0]
    if first not in by_first:
        by_first[first] = []
    by_first[first].append(word)
print(f"Grouped: {by_first}")

# Count occurrences
items = ["a", "b", "a", "c", "b", "a"]
counts = {item: items.count(item) for item in set(items)}
print(f"Counts: {counts}")
```

Run it and observe practical comprehension patterns.

---

### Exercise 6: Use Built-in Functions with Iterables

Create a file called `builtin_functions.py`:

```python
# any() and all()
numbers = [2, 4, 6, 8]
print(f"All even: {all(n % 2 == 0 for n in numbers)}")

numbers = [2, 4, 5, 8]
print(f"Any odd: {any(n % 2 == 1 for n in numbers)}")

# sum(), min(), max()
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")

# enumerate()
words = ["apple", "banana", "cherry"]
for i, word in enumerate(words):
    print(f"  {i}: {word}")

# zip()
names = ["Alice", "Bob", "Carol"]
ages = [30, 25, 28]
for name, age in zip(names, ages):
    print(f"  {name}: {age}")

# map() and filter()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n ** 2, numbers))
print(f"Squared: {squared}")

evens = list(filter(lambda n: n % 2 == 0, numbers))
print(f"Evens: {evens}")
```

Run it and observe built-in functions.

---

### Exercise 7: Combine Comprehensions and Generators

Create a file called `combined_comprehensions.py`:

```python
# Use comprehension to build a generator
def process_data(data):
    """Process data and yield results."""
    for item in data:
        if item > 0:
            yield item ** 2

numbers = [-2, -1, 0, 1, 2, 3]
results = list(process_data(numbers))
print(f"Processed: {results}")

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(f"Flattened: {flattened}")

# Comprehension with multiple conditions
numbers = range(1, 21)
result = [n for n in numbers if n % 2 == 0 if n % 3 == 0]
print(f"Divisible by 2 and 3: {result}")

# Dictionary from comprehension
words = ["apple", "banana", "cherry", "date"]
word_dict = {w: len(w) for w in words if len(w) > 4}
print(f"Long words: {word_dict}")
```

Run it and observe combined patterns.

---

## Challenge Exercises

### Challenge 1: Build a Data Pipeline

Create a file called `data_pipeline.py`:

```python
def read_data():
    """Simulate reading data."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even(data):
    """Filter even numbers."""
    return (n for n in data if n % 2 == 0)

def square(data):
    """Square each number."""
    return (n ** 2 for n in data)

def sum_results(data):
    """Sum all values."""
    return sum(data)

# Build pipeline
data = read_data()
result = sum_results(square(filter_even(data)))
print(f"Pipeline result: {result}")

# Alternative with comprehension
result2 = sum(n ** 2 for n in data if n % 2 == 0)
print(f"Comprehension result: {result2}")
```

Run it and observe the pipeline pattern.

---

### Challenge 2: Analyze Text with Comprehensions

Create a file called `text_analysis.py`:

```python
text = "The quick brown fox jumps over the lazy dog"

# Word frequencies
words = text.lower().split()
word_counts = {w: words.count(w) for w in set(words)}
print(f"Word counts: {word_counts}")

# Words by length
words_by_length = {}
for word in set(words):
    length = len(word)
    if length not in words_by_length:
        words_by_length[length] = []
    words_by_length[length].append(word)
print(f"By length: {words_by_length}")

# Character frequencies
chars = [c for c in text if c.isalpha()]
char_counts = {c: chars.count(c) for c in set(chars)}
print(f"Character counts: {char_counts}")

# Vowels and consonants
vowels = [c for c in text.lower() if c in "aeiou"]
consonants = [c for c in text.lower() if c.isalpha() and c not in "aeiou"]
print(f"Vowels: {len(vowels)}, Consonants: {len(consonants)}")
```

Run it and observe text analysis.

---

### Challenge 3: Generate Sequences

Create a file called `generate_sequences.py`:

```python
def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci (10):")
print(list(fibonacci(10)))

def primes(limit):
    """Generate prime numbers up to limit."""
    for num in range(2, limit):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

print("\nPrimes up to 30:")
print(list(primes(30)))

def countdown(n):
    """Generate countdown from n to 1."""
    while n > 0:
        yield n
        n -= 1

print("\nCountdown from 5:")
print(list(countdown(5)))
```

Run it and observe sequence generation.

---

## Hints

**Generator exhausted** → Generators can only be iterated once. Convert to a list if you need to iterate multiple times.

**Comprehension too complex** → If your comprehension has multiple nested loops or conditions, use a regular loop instead for clarity.

**Memory issues with large lists** → Use a generator expression instead of a list comprehension for large datasets.

**Unexpected comprehension result** → Check variable scope and the order of `for` and `if` clauses.

---

## What to Review If You Get Stuck

- **List comprehensions** → Handbook section 2.1
- **Set and dict comprehensions** → Handbook section 2.2
- **Generator expressions** → Handbook section 2.3
- **Generator functions** → Handbook section 2.4
- **Built-in functions** → Handbook section 2.5
- **When to use comprehensions** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Write list, set, and dictionary comprehensions
- Use generator expressions for memory efficiency
- Create generator functions with `yield`
- Use built-in functions like `any()`, `all()`, `sum()`, `enumerate()`, `zip()`
- Choose between comprehensions, generators, and loops
- Process and transform sequences efficiently
- Build data pipelines with generators

