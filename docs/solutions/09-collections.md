# Solutions 09: Collections

## Overview

Chapter 09 exercises cover Python's four built-in collection types: lists, tuples, sets, and dictionaries. This solution guide explains the reasoning behind each exercise and when to choose each collection type.

---

## Notes Before Checking Solutions

The most important skill in this chapter is not memorizing methods — it is knowing which collection to reach for. Lists for ordered, mutable sequences. Tuples for fixed data. Sets for unique values and membership tests. Dictionaries for key-value lookups. When you internalize that, the rest follows naturally.

---

## Warm-up Exercise Solutions

### Exercise 1: Work with Lists

```python
numbers = [1, 2, 3, 4, 5]

# Access
print(numbers[0])    # 1 (first)
print(numbers[-1])   # 5 (last)
print(numbers[1:4])  # [2, 3, 4]

# Modify
numbers.append(6)          # [1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])     # [1, 2, 3, 4, 5, 6, 7, 8]
numbers.insert(0, 0)       # [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers.remove(0)          # [1, 2, 3, 4, 5, 6, 7, 8]
popped = numbers.pop()     # removes and returns 8
```

**`append()` vs `extend()`:**
- `append(x)` adds `x` as a single element: `[1, 2].append([3, 4])` → `[1, 2, [3, 4]]`
- `extend(iterable)` adds each element of the iterable: `[1, 2].extend([3, 4])` → `[1, 2, 3, 4]`

**`remove()` vs `pop()`:**
- `remove(x)` removes the first occurrence of value `x`. Raises `ValueError` if not found.
- `pop(i)` removes and returns the element at index `i`. Defaults to the last element.

```python
items = [3, 1, 4, 1, 5, 9, 2, 6]
items.sort()     # sorts in place: [1, 1, 2, 3, 4, 5, 6, 9]
items.reverse()  # reverses in place: [9, 6, 5, 4, 3, 2, 1, 1]
copy = items.copy()  # independent copy
```

**`sort()` vs `sorted()`:** `sort()` modifies the list in place and returns `None`. `sorted()` returns a new sorted list and leaves the original unchanged. Use `sorted()` when you need to keep the original order.

---

### Exercise 2: Work with Tuples

```python
point = (10, 20)
colors = ("red", "green", "blue")
single = (42,)   # the comma is required for a single-element tuple
empty = ()

# Access — same as lists
print(colors[0])    # red
print(colors[-1])   # blue
print(colors[0:2])  # ('red', 'green')

# Tuple unpacking
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

r, g, b = colors
print(f"r={r}, g={g}, b={b}")
```

**Why the comma for single-element tuples?** Without the comma, `(42)` is just `42` in parentheses — Python treats it as a grouped expression, not a tuple. The comma is what makes it a tuple: `(42,)`.

**Tuples as dictionary keys:**

```python
locations = {
    (0, 0): "origin",
    (1, 1): "diagonal",
}
print(locations[(0, 0)])  # origin
```

Lists cannot be dictionary keys because they are mutable (and therefore not hashable). Tuples can be keys because they are immutable.

---

### Exercise 3: Work with Sets

```python
numbers = {1, 2, 3, 4, 5}
empty = set()  # {} creates an empty dict, not a set

numbers.add(6)      # {1, 2, 3, 4, 5, 6}
numbers.remove(1)   # {2, 3, 4, 5, 6}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}  — union
print(a & b)   # {3, 4}              — intersection
print(a - b)   # {1, 2}              — difference (in a but not b)
print(a ^ b)   # {1, 2, 5, 6}        — symmetric difference
```

**Set operations are fast.** Checking `x in some_set` is O(1) — it does not matter how large the set is. Checking `x in some_list` is O(n) — it scans the list from the beginning. Use sets when you need fast membership tests.

**Remove duplicates:**

```python
items = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(items))  # [1, 2, 3, 4] (order not guaranteed)
```

Note: converting to a set and back to a list removes duplicates but does not preserve order. If order matters, use `dict.fromkeys()` (Python 3.7+):

```python
unique_ordered = list(dict.fromkeys(items))  # preserves order
```

---

### Exercise 4: Work with Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access
print(person["name"])   # Alice
print(person["age"])    # 30

# Add and modify
person["job"] = "Engineer"
person["age"] = 31

# Methods
print(person.keys())    # dict_keys(['name', 'age', 'city', 'job'])
print(person.values())  # dict_values(['Alice', 31, 'New York', 'Engineer'])
print(person.items())   # dict_items([...])

# Safe access
print(person.get("salary", "Not specified"))  # Not specified

# Iterate
for key, value in person.items():
    print(f"  {key}: {value}")

# Remove
del person["job"]

# Update from another dict
person.update({"age": 32, "city": "Boston"})
```

**`get()` vs direct access:** `person["salary"]` raises `KeyError` if the key does not exist. `person.get("salary", "Not specified")` returns the default value instead. Use `get()` when the key might not be present.

**Dictionary order:** Since Python 3.7, dictionaries maintain insertion order. Iterating over a dict gives keys in the order they were added.

---

## Practice Exercise Solutions

### Exercise 5: Combine Collections

```python
# List of dictionaries — common pattern for tabular data
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 92},
]

for student in students:
    print(f"  {student['name']}: {student['grade']}")

# Dictionary with lists — group related values
inventory = {
    "apples": [10, 5, 8],
    "bananas": [15, 12, 20],
}

for fruit, quantities in inventory.items():
    total = sum(quantities)
    print(f"  {fruit}: {total} total")
```

Nested collections are very common in real programs. JSON data, API responses, and database results often come back as lists of dictionaries. Getting comfortable with `data["key"]` and `data[0]["key"]` patterns is essential.

---

### Exercise 6: Process Collections

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter
evens = [n for n in numbers if n % 2 == 0]
# [2, 4, 6, 8, 10]

# Transform
squared = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Count occurrences
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
# {"apple": 3, "banana": 2, "cherry": 1}
```

**`counts.get(item, 0) + 1`:** If `item` is not yet in `counts`, `get()` returns `0`. Adding `1` gives the first count. On subsequent iterations, `get()` returns the current count and we add `1` again.

**Group by first letter:**

```python
words = ["apple", "apricot", "banana", "blueberry", "cherry"]
by_first_letter = {}
for word in words:
    first = word[0]
    if first not in by_first_letter:
        by_first_letter[first] = []
    by_first_letter[first].append(word)
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
```

A cleaner version using `setdefault()`:

```python
for word in words:
    by_first_letter.setdefault(word[0], []).append(word)
```

`setdefault(key, default)` returns the value for `key` if it exists, otherwise inserts `key` with `default` and returns `default`.

---

### Exercise 7: Choose the Right Collection

| Use case | Collection | Reason |
|---|---|---|
| Ordered, changeable sequence | `list` | Supports indexing, appending, sorting |
| Fixed, unchangeable data | `tuple` | Immutable, can be a dict key |
| Unique values, fast membership test | `set` | No duplicates, O(1) lookup |
| Key-value pairs | `dict` | Fast lookup by key |

```python
# List — shopping list (order matters, items can be added/removed)
shopping_list = ["milk", "eggs", "bread"]
shopping_list.append("butter")

# Tuple — RGB color (fixed, three values, can be a dict key)
rgb_color = (255, 128, 0)

# Set — visited cities (unique values, order does not matter)
visited_cities = {"New York", "Boston", "Chicago"}
visited_cities.add("Denver")

# Dict — phone book (look up by name)
phone_book = {"Alice": "555-1234", "Bob": "555-5678"}
```

---

## Challenge Exercise Solutions

### Challenge 1: Analyze Text with Collections

```python
def analyze_text(text):
    """Analyze text and return statistics."""
    words = text.lower().split()

    # Count word frequencies using a dict
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Unique words using a set
    unique_words = set(words)

    # Sort by frequency (descending)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return {
        "total_words": len(words),
        "unique_words": len(unique_words),
        "word_counts": word_counts,
        "most_common": sorted_words[:5],
    }
```

**`sorted(word_counts.items(), key=lambda x: x[1], reverse=True)`:**
- `word_counts.items()` gives `(word, count)` pairs.
- `key=lambda x: x[1]` sorts by the count (second element of each pair).
- `reverse=True` sorts in descending order (highest count first).

---

### Challenge 2: Build a Contact Manager

```python
def add_contact(contacts, name, phone, email):
    """Add a contact."""
    contacts[name] = {"phone": phone, "email": email}

def remove_contact(contacts, name):
    """Remove a contact."""
    if name in contacts:
        del contacts[name]
    else:
        print(f"Contact '{name}' not found.")

def list_contacts(contacts):
    """List all contacts."""
    if not contacts:
        print("No contacts.")
        return
    for name, info in contacts.items():
        print(f"{name}: {info['phone']}, {info['email']}")

def search_contact(contacts, name):
    """Search for a contact."""
    info = contacts.get(name)
    if info:
        print(f"{name}: {info['phone']}, {info['email']}")
    else:
        print(f"Contact '{name}' not found.")
```

**Why use `contacts.get(name)` instead of `contacts[name]`?** `contacts[name]` raises `KeyError` if the name is not in the dictionary. `contacts.get(name)` returns `None` instead, which we can check with `if info:`.

---

### Challenge 3: Implement a Simple Inventory System

```python
class Inventory:
    """Simple inventory system."""

    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        """Add an item to inventory."""
        if name in self.items:
            # Item already exists — just increase quantity
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price}

    def remove_item(self, name, quantity):
        """Remove items from inventory."""
        if name not in self.items:
            print(f"Item '{name}' not found.")
            return
        self.items[name]["quantity"] -= quantity
        if self.items[name]["quantity"] <= 0:
            del self.items[name]

    def get_total_value(self):
        """Calculate total inventory value."""
        total = 0
        for item in self.items.values():
            total += item["quantity"] * item["price"]
        return total

    def list_items(self):
        """List all items."""
        for name, info in self.items.items():
            value = info["quantity"] * info["price"]
            print(f"{name}: {info['quantity']} @ ${info['price']:.2f} = ${value:.2f}")
```

**Why delete the item when quantity reaches zero?** An item with zero quantity is not in stock. Keeping it in the dictionary with `quantity: 0` would clutter the inventory and require extra checks everywhere. Deleting it keeps the data clean.

---

### Challenge 4: Find Patterns in Collections

```python
# Find duplicates
items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
duplicates = [x for x in set(items) if items.count(x) > 1]
print(f"Duplicates: {duplicates}")  # [2, 3, 4]

# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1) & set(list2))
print(f"Common: {common}")  # [3, 4, 5]

# Find missing elements
all_numbers = set(range(1, 6))
present = {1, 2, 4, 5}
missing = all_numbers - present
print(f"Missing: {missing}")  # {3}

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened: {flat}")  # [1, 2, 3, 4, 5, 6]
```

**Flattening with a nested comprehension:** `[item for sublist in nested for item in sublist]` reads as "for each sublist in nested, for each item in sublist, yield item." The outer loop comes first, the inner loop second.

**Group consecutive numbers:**

```python
numbers = [1, 2, 3, 5, 6, 7, 9, 10]
groups = []
current_group = [numbers[0]]

for n in numbers[1:]:
    if n == current_group[-1] + 1:
        current_group.append(n)
    else:
        groups.append(current_group)
        current_group = [n]

groups.append(current_group)  # don't forget the last group
print(f"Groups: {groups}")  # [[1, 2, 3], [5, 6, 7], [9, 10]]
```

The key insight: we check if the current number is exactly one more than the last number in the current group. If yes, it belongs to the same group. If no, we start a new group.

---

## Common Mistakes

**Using `{}` to create an empty set.** `{}` creates an empty dictionary. Use `set()` for an empty set.

**Modifying a list while iterating over it.** This can skip elements or cause unexpected behavior. Iterate over a copy: `for item in items.copy():`.

**Forgetting that `sort()` returns `None`.** `sorted_list = my_list.sort()` gives you `None`. Use `sorted_list = sorted(my_list)` instead.

**Using a list when a set would be faster.** If you are checking membership frequently (`if x in items`), use a set. List membership checks scan the entire list; set checks are nearly instant.

**Accessing a dict key that might not exist.** Use `.get()` with a default value, or check with `if key in dict:` first.

---

## What to Review Next

- Chapter 10: Functions — organizing code into reusable pieces
- Chapter 11: Comprehensions and Generators — concise ways to build and process collections
- Chapter 12: Errors, Exceptions, and Debugging — handling `KeyError`, `IndexError`, and other collection errors
