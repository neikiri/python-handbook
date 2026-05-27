# Chapter 09: Collections

## 1. Overview

Most real programs work with groups of values, not just single ones. Python
provides four built-in collection types that cover the vast majority of
everyday needs:

- **Lists** — ordered, mutable sequences of any values.
- **Tuples** — ordered, immutable sequences, often used for fixed groups.
- **Sets** — unordered collections of unique values.
- **Dictionaries** — mappings from keys to values.

Each type has a distinct purpose. Choosing the right one makes your code
clearer, faster, and less error-prone.

---

## 2. What You Will Learn

- How to create, read, and modify lists
- Common list methods: `append`, `extend`, `insert`, `remove`, `pop`, `sort`,
  `reverse`, `index`, `count`, `copy`
- How list slicing works
- When to use tuples instead of lists
- Tuple packing and unpacking
- How sets work and when they are useful
- Set operations: union, intersection, difference, symmetric difference
- How dictionaries store and retrieve data
- Common dict methods: `get`, `keys`, `values`, `items`, `update`, `pop`,
  `setdefault`
- How to iterate over all four collection types
- Nesting collections inside each other
- How to choose the right collection for a task

---

## 3. Core Concepts

### 3.1 Lists

A **list** is an ordered, mutable sequence. You can store any mix of types,
change items in place, add new items, and remove existing ones.

```python
# Creating lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]
nested = [[1, 2], [3, 4], [5, 6]]
```

#### Indexing and slicing

Lists use the same indexing and slicing rules as strings.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])     # apple
print(fruits[-1])    # elderberry
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[::-1])  # reversed list
```

#### Modifying items

```python
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(colors)   # ['red', 'yellow', 'blue']
```

#### Common list methods

```python
items = [3, 1, 4, 1, 5, 9, 2, 6]

items.append(7)          # add one item to the end
items.extend([8, 0])     # add multiple items to the end
items.insert(0, 99)      # insert 99 at index 0
items.remove(1)          # remove the first occurrence of 1
popped = items.pop()     # remove and return the last item
popped_at = items.pop(0) # remove and return item at index 0

items.sort()             # sort in place (ascending)
items.sort(reverse=True) # sort in place (descending)
items.reverse()          # reverse in place

print(items.index(5))    # index of first occurrence of 5
print(items.count(1))    # how many times 1 appears
copy = items.copy()      # shallow copy
items.clear()            # remove all items
```

#### `len()`, `min()`, `max()`, `sum()`

```python
numbers = [4, 7, 2, 9, 1, 5]

print(len(numbers))   # 6
print(min(numbers))   # 1
print(max(numbers))   # 9
print(sum(numbers))   # 28
```

#### Checking membership

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # True
print("mango" not in fruits)   # True
```

#### Sorting without modifying the original

`sorted()` returns a new sorted list; the original is unchanged.

```python
numbers = [4, 7, 2, 9, 1]
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print(numbers)    # [4, 7, 2, 9, 1]  — unchanged
print(ascending)  # [1, 2, 4, 7, 9]
```

You can sort by a custom key using the `key` parameter.

```python
words = ["banana", "apple", "fig", "cherry"]
by_length = sorted(words, key=len)
print(by_length)   # ['fig', 'apple', 'banana', 'cherry']
```

---

### 3.2 Tuples

A **tuple** is an ordered, immutable sequence. Once created, you cannot add,
remove, or change its items. Tuples are faster than lists for read-only data
and can be used as dictionary keys or set members because they are hashable.

```python
# Creating tuples
empty = ()
single = (42,)          # trailing comma required for a one-element tuple
point = (3, 7)
rgb = (255, 128, 0)
mixed = ("Alice", 30, True)
```

The parentheses are optional — Python recognizes a comma-separated sequence
as a tuple.

```python
point = 3, 7
print(type(point))   # <class 'tuple'>
```

#### Indexing and slicing

Tuples support the same indexing and slicing as lists.

```python
t = (10, 20, 30, 40, 50)

print(t[0])     # 10
print(t[-1])    # 50
print(t[1:3])   # (20, 30)
```

#### Tuple unpacking

You can assign the items of a tuple to individual variables in one step.

```python
point = (3, 7)
x, y = point
print(x)   # 3
print(y)   # 7

# Swap two variables without a temporary variable
a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10
```

Use `*` to capture multiple items into a list.

```python
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*head, last = (1, 2, 3, 4, 5)
print(head)    # [1, 2, 3, 4]
print(last)    # 5

a, *middle, z = (1, 2, 3, 4, 5)
print(middle)  # [2, 3, 4]
```

#### When to use a tuple vs. a list

| Use a tuple when... | Use a list when... |
|---|---|
| The data is fixed (coordinates, RGB values, a record) | The data will grow or change |
| You need a hashable collection (dict key, set member) | You need to sort, append, or remove |
| Returning multiple values from a function | Building a sequence incrementally |

```python
# Tuple as a dict key — works because tuples are hashable
distances = {
    ("New York", "London"): 5570,
    ("Paris", "Tokyo"): 9714,
}

# List as a dict key — TypeError: unhashable type: 'list'
# bad = {["a", "b"]: 1}
```

---

### 3.3 Sets

A **set** is an unordered collection of unique values. Duplicates are
automatically removed. Sets are useful for membership testing, deduplication,
and mathematical set operations.

```python
# Creating sets
empty = set()           # NOT {} — that creates an empty dict
numbers = {1, 2, 3, 4, 5}
letters = set("hello")  # {'h', 'e', 'l', 'o'} — duplicates removed
```

Sets are unordered — you cannot index or slice them.

```python
s = {3, 1, 4, 1, 5, 9, 2, 6}
print(s)        # {1, 2, 3, 4, 5, 6, 9} — order not guaranteed, duplicates gone
print(len(s))   # 7
```

#### Adding and removing items

```python
s = {1, 2, 3}

s.add(4)          # add one item
s.update([5, 6])  # add multiple items

s.remove(2)       # remove — raises KeyError if not present
s.discard(99)     # remove — no error if not present
popped = s.pop()  # remove and return an arbitrary item
s.clear()         # remove all items
```

#### Membership testing

Sets have O(1) membership testing — much faster than lists for large
collections.

```python
valid_extensions = {".py", ".txt", ".md", ".json"}

filename = "script.py"
ext = filename[filename.rfind("."):]
print(ext in valid_extensions)   # True
```

#### Set operations

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)    # union: {1, 2, 3, 4, 5, 6, 7}
print(a & b)    # intersection: {3, 4, 5}
print(a - b)    # difference: {1, 2}  (in a but not b)
print(b - a)    # difference: {6, 7}  (in b but not a)
print(a ^ b)    # symmetric difference: {1, 2, 6, 7}
```

Method equivalents:

```python
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
```

#### Subset and superset checks

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))    # True  — all of a is in b
print(b.issuperset(a))  # True  — b contains all of a
print(a.isdisjoint({6, 7}))  # True  — no common elements
```

#### Frozensets

A **frozenset** is an immutable set. It can be used as a dictionary key or
stored inside another set.

```python
fs = frozenset([1, 2, 3])
print(fs)   # frozenset({1, 2, 3})
```

---

### 3.4 Dictionaries

A **dictionary** maps unique **keys** to **values**. Keys must be hashable
(strings, numbers, and tuples are common choices). Values can be anything.
Dictionaries preserve insertion order (Python 3.7+).

```python
# Creating dictionaries
empty = {}
person = {"name": "Alice", "age": 30, "city": "Paris"}
scores = dict(alice=88, bob=92, charlie=75)
```

#### Accessing values

```python
person = {"name": "Alice", "age": 30}

print(person["name"])          # Alice
print(person.get("age"))       # 30
print(person.get("email"))     # None  — no KeyError
print(person.get("email", "")) # ""    — default value
```

Use `get()` when the key might not exist. Using `[]` on a missing key raises
a `KeyError`.

#### Adding and updating items

```python
person = {"name": "Alice"}

person["age"] = 30          # add a new key
person["name"] = "Bob"      # update an existing key
person.update({"city": "London", "age": 25})  # update multiple at once
```

#### Removing items

```python
d = {"a": 1, "b": 2, "c": 3}

del d["a"]              # remove by key — KeyError if missing
val = d.pop("b")        # remove and return value — KeyError if missing
val = d.pop("z", None)  # remove and return — default if missing
d.clear()               # remove all items
```

#### Iterating over a dictionary

```python
person = {"name": "Alice", "age": 30, "city": "Paris"}

# Keys (default iteration)
for key in person:
    print(key)

# Values
for value in person.values():
    print(value)

# Key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

#### Checking membership

`in` tests keys, not values.

```python
person = {"name": "Alice", "age": 30}

print("name" in person)       # True
print("email" in person)      # False
print("Alice" in person)      # False — checks keys, not values
print("Alice" in person.values())  # True
```

#### `setdefault()`

Returns the value for a key if it exists; otherwise inserts the key with a
default value and returns it.

```python
counts = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

for word in words:
    counts.setdefault(word, 0)
    counts[word] += 1

print(counts)   # {'apple': 3, 'banana': 2, 'cherry': 1}
```

#### Dictionary comprehensions

A concise way to build a dictionary (covered in depth in Chapter 11).

```python
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Merging dictionaries (Python 3.9+)

```python
defaults = {"color": "blue", "size": "medium", "weight": 1.0}
overrides = {"color": "red", "weight": 2.5}

merged = defaults | overrides
print(merged)
# {'color': 'red', 'size': 'medium', 'weight': 2.5}
```

---

### 3.5 Nesting Collections

Collections can contain other collections. This is how you represent
structured data like tables, trees, and records.

```python
# List of dicts — a common pattern for tabular data
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 92},
    {"name": "Charlie", "grade": 75},
]

for student in students:
    print(f"{student['name']}: {student['grade']}")

# Dict of lists — group items by category
inventory = {
    "fruits":     ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli"],
    "grains":     ["rice", "oats", "wheat"],
}

for category, items in inventory.items():
    print(f"{category}: {', '.join(items)}")
```

Access nested values by chaining `[]` operators.

```python
data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Paris",
            "country": "France",
        },
    }
}

city = data["user"]["address"]["city"]
print(city)   # Paris
```

---

### 3.6 Choosing the Right Collection

| Need | Use |
|---|---|
| Ordered sequence that changes | `list` |
| Ordered sequence that is fixed | `tuple` |
| Fast membership testing, unique values | `set` |
| Key-to-value mapping | `dict` |
| Immutable set (hashable) | `frozenset` |

A few rules of thumb:

- If you are building a sequence incrementally, use a list.
- If you are returning multiple values from a function, use a tuple.
- If you need to deduplicate or test membership frequently, use a set.
- If you need to look things up by name or label, use a dict.

---

## 4. Practical Examples

### 4.1 Deduplicating a List

```python
def deduplicate(items: list) -> list:
    """Return a new list with duplicates removed, preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(deduplicate(data))   # [3, 1, 4, 5, 9, 2, 6]
```

Converting to a set and back is shorter but does not preserve order:

```python
print(list(set(data)))   # order not guaranteed
```

---

### 4.2 Word Frequency Counter

```python
def word_frequency(text: str) -> dict[str, int]:
    """Count how many times each word appears in text."""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


text = "the cat sat on the mat the cat"
freq = word_frequency(text)

for word, count in sorted(freq.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{word}: {count}")

# Output:
# the: 3
# cat: 2
# sat: 1
# on: 1
# mat: 1
```

---

### 4.3 Grouping Items by Category

```python
def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter."""
    groups: dict[str, list[str]] = {}
    for word in words:
        key = word[0].upper()
        groups.setdefault(key, []).append(word)
    return groups


animals = ["ant", "bear", "cat", "alligator", "bison", "crane", "ape"]
grouped = group_by_first_letter(animals)

for letter, group in sorted(grouped.items()):
    print(f"{letter}: {group}")

# Output:
# A: ['ant', 'alligator', 'ape']
# B: ['bear', 'bison']
# C: ['cat', 'crane']
```

---

### 4.4 Finding Common and Unique Elements

```python
team_a = {"Alice", "Bob", "Charlie", "Diana"}
team_b = {"Charlie", "Diana", "Eve", "Frank"}

both   = team_a & team_b
only_a = team_a - team_b
only_b = team_b - team_a
either = team_a | team_b

print(f"On both teams:  {sorted(both)}")
print(f"Only in team A: {sorted(only_a)}")
print(f"Only in team B: {sorted(only_b)}")
print(f"On any team:    {sorted(either)}")

# Output:
# On both teams:  ['Charlie', 'Diana']
# Only in team A: ['Alice', 'Bob']
# Only in team B: ['Eve', 'Frank']
# On any team:    ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
```

---

### 4.5 Inverting a Dictionary

```python
def invert_dict(d: dict) -> dict:
    """Swap keys and values. Assumes values are unique and hashable."""
    return {v: k for k, v in d.items()}


country_codes = {"US": "United States", "FR": "France", "JP": "Japan"}
by_name = invert_dict(country_codes)
print(by_name)
# {'United States': 'US', 'France': 'FR', 'Japan': 'JP'}
```

---

### 4.6 Flattening a List of Lists

```python
def flatten(nested: list[list]) -> list:
    """Flatten one level of nesting."""
    result = []
    for sublist in nested:
        result.extend(sublist)
    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(matrix))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### 4.7 Sorting a List of Dicts

```python
students = [
    {"name": "Charlie", "grade": 75},
    {"name": "Alice",   "grade": 88},
    {"name": "Bob",     "grade": 92},
    {"name": "Diana",   "grade": 88},
]

# Sort by grade descending, then name ascending
ranked = sorted(students, key=lambda s: (-s["grade"], s["name"]))

for i, s in enumerate(ranked, start=1):
    print(f"{i}. {s['name']}: {s['grade']}")

# Output:
# 1. Bob: 92
# 2. Alice: 88
# 3. Diana: 88
# 4. Charlie: 75
```

---

### 4.8 Building a Simple Phone Book

```python
def make_phone_book(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build a phone book that supports multiple numbers per name."""
    book: dict[str, list[str]] = {}
    for name, number in entries:
        book.setdefault(name, []).append(number)
    return book


entries = [
    ("Alice", "555-1234"),
    ("Bob",   "555-5678"),
    ("Alice", "555-9999"),
]

book = make_phone_book(entries)
for name, numbers in sorted(book.items()):
    print(f"{name}: {', '.join(numbers)}")

# Output:
# Alice: 555-1234, 555-9999
# Bob: 555-5678
```

---

### 4.9 Checking for Anagrams

```python
def are_anagrams(a: str, b: str) -> bool:
    """Return True if a and b are anagrams of each other."""
    return sorted(a.lower()) == sorted(b.lower())


print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("hello", "world"))     # False
print(are_anagrams("Astronomer", "Moon starer"))  # False (spaces differ)
```

A set-based approach works when you only care about unique characters:

```python
def share_same_letters(a: str, b: str) -> bool:
    return set(a.lower()) == set(b.lower())
```

---

### 4.10 Counting with `collections.Counter`

The standard library's `Counter` is a dict subclass designed for counting.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts)                    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts["apple"])           # 3
print(counts["mango"])           # 0  — no KeyError for missing keys
print(counts.most_common(2))     # [('apple', 3), ('banana', 2)]
```

---

## 5. Common Mistakes

### 5.1 Using a Mutable Default Argument

Never use a list or dict as a default parameter value. Python creates the
default object once when the function is defined, not each time it is called.

```python
# Wrong — all calls share the same list
def add_item(item, container=[]):
    container.append(item)
    return container

print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b']  — unexpected!

# Correct — use None and create a new list inside the function
def add_item(item, container=None):
    if container is None:
        container = []
    container.append(item)
    return container
```

---

### 5.2 Confusing `{}` for an Empty Set

`{}` creates an empty **dict**, not an empty set.

```python
empty_dict = {}
print(type(empty_dict))   # <class 'dict'>

empty_set = set()
print(type(empty_set))    # <class 'set'>
```

---

### 5.3 Modifying a List While Iterating Over It

Removing items from a list while looping over it skips elements.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Wrong — skips items
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)   # [1, 3, 5] — looks right but 4 was skipped

# Correct — iterate over a copy or build a new list
numbers = [1, 2, 3, 4, 5, 6]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)   # [1, 3, 5]
```

---

### 5.4 Shallow vs. Deep Copy

`list.copy()` and `list[:]` create a **shallow copy** — the outer list is
new, but nested objects are still shared.

```python
original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0].append(99)
print(original)   # [[1, 2, 99], [3, 4]]  — original was affected!

# For a true deep copy, use the copy module
import copy
deep = copy.deepcopy(original)
deep[0].append(0)
print(original)   # [[1, 2, 99], [3, 4]]  — original unchanged
```

---

### 5.5 Forgetting That `dict.keys()`, `dict.values()`, and `dict.items()` Are Views

These methods return **view objects** that reflect the current state of the
dict. If you need a static snapshot, convert to a list first.

```python
d = {"a": 1, "b": 2}
keys = d.keys()

d["c"] = 3
print(keys)   # dict_keys(['a', 'b', 'c'])  — view updated automatically

# Snapshot
keys_snapshot = list(d.keys())
d["d"] = 4
print(keys_snapshot)   # ['a', 'b', 'c']  — unchanged
```

---

### 5.6 Assuming Sets Are Ordered

Sets do not preserve insertion order. Do not rely on the order of items when
iterating over a set.

```python
s = {3, 1, 4, 1, 5, 9}
print(list(s))   # order is not guaranteed
```

If you need unique items in a predictable order, use `sorted()`:

```python
print(sorted(s))   # [1, 3, 4, 5, 9]
```

---

### 5.7 Using a List When a Set Would Be Faster

Membership testing with `in` is O(n) for lists and O(1) for sets. For large
collections, this difference is significant.

```python
# Slow for large data
valid_ids = [1001, 1002, 1003, ...]   # list
if user_id in valid_ids:              # O(n) scan
    ...

# Fast
valid_ids = {1001, 1002, 1003, ...}   # set
if user_id in valid_ids:              # O(1) lookup
    ...
```

---

## 6. Practice Tasks

1. Write a function `top_n(items: list[int], n: int) -> list[int]` that
   returns the `n` largest values from a list, sorted descending.

2. Write a function `merge_dicts(dicts: list[dict]) -> dict` that merges a
   list of dictionaries. Later keys overwrite earlier ones.

3. Given a list of strings, write a function that returns a dict mapping each
   unique string to the number of times it appears.

4. Write a function `common_elements(a: list, b: list) -> list` that returns
   the elements present in both lists, without duplicates, in sorted order.

5. Write a function `rotate(items: list, n: int) -> list` that rotates a list
   `n` positions to the right. For example, `rotate([1,2,3,4,5], 2)` returns
   `[4, 5, 1, 2, 3]`.

6. Given a list of student dicts with `"name"` and `"score"` keys, write a
   function that returns the name of the student with the highest score.

7. Write a function that takes a sentence and returns a dict of letter
   frequencies (lowercase, ignoring spaces and punctuation).

8. Write a function `is_subset(a: list, b: list) -> bool` that returns `True`
   if every element of `a` appears in `b`.

---

## 7. Key Takeaways

- **Lists** are ordered and mutable. Use them when you need to build, sort, or
  modify a sequence.
- **Tuples** are ordered and immutable. Use them for fixed groups of values,
  multiple return values, and as dict keys.
- **Sets** are unordered collections of unique values. Use them for
  deduplication, fast membership testing, and set algebra.
- **Dictionaries** map keys to values. Use them whenever you need to look
  something up by name or label.
- `get()` is safer than `[]` for dict access when a key might be missing.
- `setdefault()` is the clean way to build dicts of lists or dicts of counts.
- Avoid modifying a list while iterating over it — build a new list instead.
- `{}` is an empty dict, not an empty set. Use `set()` for an empty set.
- For large membership tests, prefer sets over lists.
- The `collections` module (especially `Counter` and `defaultdict`) extends
  these built-in types with useful extras.

---

### Further Reading

- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

### What's Next

Ready to continue? Head to the next chapter: **Functions**.

→ [Chapter 10 — Functions](10-functions.md)

*See also:*
- [Exercise](../exercises/09-collections.md)
- [Solution](../solutions/09-collections.md)
- [Cheatsheet](../cheatsheets/collections.md)
