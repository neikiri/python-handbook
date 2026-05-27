# Collections Cheatsheet

Quick reference for Python's main collection types: lists, tuples, sets, and dictionaries.

## Lists

```python
# Create
lst = [1, 2, 3]
lst = list()  # Empty list
lst = [1] * 3  # [1, 1, 1]

# Access
lst[0]      # First element
lst[-1]     # Last element
lst[1:3]    # Slice: elements 1 and 2

# Modify
lst[0] = 10  # Change element
lst.append(4)  # Add to end
lst.insert(0, 0)  # Insert at index
lst.extend([5, 6])  # Add multiple items
lst.remove(2)  # Remove first occurrence
lst.pop()  # Remove and return last item
lst.pop(0)  # Remove and return item at index
lst.clear()  # Remove all items

# Query
len(lst)  # Length
2 in lst  # Check membership
lst.index(2)  # Find index of value
lst.count(2)  # Count occurrences

# Sort and reverse
lst.sort()  # Sort in place
lst.sort(reverse=True)  # Sort descending
lst.reverse()  # Reverse in place
sorted(lst)  # Return new sorted list
```

## Tuples

```python
# Create
tup = (1, 2, 3)
tup = 1, 2, 3  # Parentheses optional
tup = (1,)  # Single element (comma required)
tup = tuple()  # Empty tuple

# Access (same as lists)
tup[0]  # First element
tup[-1]  # Last element
tup[1:3]  # Slice

# Tuples are immutable
# tup[0] = 10  # TypeError

# Query
len(tup)  # Length
2 in tup  # Check membership
tup.index(2)  # Find index
tup.count(2)  # Count occurrences

# Unpacking
a, b, c = (1, 2, 3)
a, *rest = (1, 2, 3, 4)  # rest = [2, 3, 4]
```

## Sets

```python
# Create
s = {1, 2, 3}
s = set()  # Empty set (not {})
s = set([1, 2, 3])  # From list

# Add and remove
s.add(4)  # Add single item
s.update([5, 6])  # Add multiple items
s.remove(2)  # Remove (raises KeyError if not found)
s.discard(2)  # Remove (no error if not found)
s.pop()  # Remove and return arbitrary item
s.clear()  # Remove all items

# Query
len(s)  # Number of items
2 in s  # Check membership

# Set operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2  # Union: {1, 2, 3, 4}
s1 & s2  # Intersection: {2, 3}
s1 - s2  # Difference: {1}
s1 ^ s2  # Symmetric difference: {1, 4}
```

## Dictionaries

```python
# Create
d = {"name": "Alice", "age": 30}
d = dict(name="Alice", age=30)
d = {}  # Empty dictionary

# Access
d["name"]  # "Alice"
d.get("name")  # "Alice"
d.get("missing", "default")  # "default" (no KeyError)

# Modify
d["name"] = "Bob"  # Change value
d["city"] = "NYC"  # Add new key
d.update({"age": 31, "city": "NYC"})  # Update multiple
del d["age"]  # Delete key
d.pop("age")  # Remove and return value
d.pop("missing", "default")  # With default
d.clear()  # Remove all items

# Query
len(d)  # Number of key-value pairs
"name" in d  # Check if key exists
d.keys()  # All keys
d.values()  # All values
d.items()  # All key-value pairs

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)
```

## Looping Patterns

```python
# Lists
for item in [1, 2, 3]:
    print(item)

# With index
for i, item in enumerate([1, 2, 3]):
    print(i, item)

# Dictionaries
for key, value in {"a": 1, "b": 2}.items():
    print(key, value)

# Multiple iterables
for x, y in zip([1, 2], ["a", "b"]):
    print(x, y)

# Range
for i in range(5):
    print(i)
```

## Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, ...}

# Set comprehension
unique = {x % 3 for x in range(10)}  # {0, 1, 2}

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
```

## Sorting and Filtering

```python
# Sort list
numbers = [3, 1, 4, 1, 5]
sorted(numbers)  # [1, 1, 3, 4, 5]
sorted(numbers, reverse=True)  # [5, 4, 3, 1, 1]

# Sort by key
words = ["apple", "pie", "a"]
sorted(words, key=len)  # ["a", "pie", "apple"]

# Sort dictionaries by value
d = {"a": 3, "b": 1, "c": 2}
sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]

# Filter
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]  # [2, 4]
```

## Counting Items

```python
from collections import Counter

items = ["a", "b", "a", "c", "a", "b"]
counts = Counter(items)  # Counter({'a': 3, 'b': 2, 'c': 1})
counts["a"]  # 3
counts.most_common(2)  # [('a', 3), ('b', 2)]
```

## Choosing the Right Collection

| Type | Ordered | Mutable | Duplicates | Use Case |
|------|---------|---------|-----------|----------|
| List | Yes | Yes | Yes | General purpose, when order matters |
| Tuple | Yes | No | Yes | Immutable sequences, dictionary keys |
| Set | No | Yes | No | Unique items, membership testing |
| Dictionary | Yes* | Yes | Keys unique | Key-value associations |

*Dictionaries maintain insertion order in Python 3.7+

## Common Mistakes

- **Empty set syntax**: Use `set()` not `{}` (which creates an empty dict)
- **Modifying while iterating**: Don't add/remove items from a list while looping over it
- **List vs tuple**: Tuples are immutable and can be dictionary keys; lists cannot
- **Dictionary key errors**: Use `.get()` with a default to avoid KeyError
- **Set operations**: Sets are unordered; don't rely on order
- **Shallow copy**: `new_list = old_list` creates a reference, not a copy. Use `new_list = old_list.copy()` or `new_list = old_list[:]`