# Chapter 09: Collections — Exercises

## Overview

These exercises help you master Python's four built-in collection types: lists, tuples, sets, and dictionaries. By the end, you will confidently choose and use the right collection for each task.

---

## How to Use These Exercises

- Create a folder called `chapter-09` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Work with Lists

Create a file called `lists.py`:

```python
# Create lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# Access elements
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"Slice: {numbers[1:4]}")

# Modify lists
numbers.append(6)
print(f"After append: {numbers}")

numbers.extend([7, 8])
print(f"After extend: {numbers}")

numbers.insert(0, 0)
print(f"After insert: {numbers}")

numbers.remove(0)
print(f"After remove: {numbers}")

popped = numbers.pop()
print(f"After pop: {numbers}, popped: {popped}")

# List methods
items = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {items}")
print(f"Index of 5: {items.index(5)}")
print(f"Count of 1: {items.count(1)}")

items.sort()
print(f"Sorted: {items}")

items.reverse()
print(f"Reversed: {items}")

copy = items.copy()
print(f"Copy: {copy}")
```

Run it and observe list operations.

---

### Exercise 2: Work with Tuples

Create a file called `tuples.py`:

```python
# Create tuples
point = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # note the comma
empty = ()

print(f"Point: {point}")
print(f"Colors: {colors}")
print(f"Single: {single}")
print(f"Empty: {empty}")

# Access elements
print(f"\nFirst color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Slice: {colors[0:2]}")

# Tuples are immutable
# colors[0] = "yellow"  # This would cause TypeError

# Tuple unpacking
x, y = point
print(f"\nUnpacked: x={x}, y={y}")

r, g, b = colors
print(f"Unpacked: r={r}, g={g}, b={b}")

# Tuple methods
items = (1, 2, 3, 2, 1)
print(f"\nIndex of 2: {items.index(2)}")
print(f"Count of 1: {items.count(1)}")

# Tuples as dictionary keys (lists cannot be)
locations = {
    (0, 0): "origin",
    (1, 1): "diagonal",
    (0, 1): "up",
}
print(f"\nLocation at (0, 0): {locations[(0, 0)]}")
```

Run it and observe tuple operations.

---

### Exercise 3: Work with Sets

Create a file called `sets.py`:

```python
# Create sets
numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}
empty = set()  # note: {} creates an empty dict, not a set

print(f"Numbers: {numbers}")
print(f"Colors: {colors}")

# Add and remove
numbers.add(6)
print(f"After add: {numbers}")

numbers.remove(1)
print(f"After remove: {numbers}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nSet a: {a}")
print(f"Set b: {b}")
print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")
print(f"Symmetric difference: {a ^ b}")

# Check membership
print(f"\n2 in a: {2 in a}")
print(f"5 in a: {5 in a}")

# Remove duplicates
items = [1, 2, 2, 3, 3, 3, 4]
unique = set(items)
print(f"\nOriginal: {items}")
print(f"Unique: {unique}")
```

Run it and observe set operations.

---

### Exercise 4: Work with Dictionaries

Create a file called `dicts.py`:

```python
# Create dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}

print(f"Person: {person}")

# Access values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Add and modify
person["job"] = "Engineer"
print(f"After adding job: {person}")

person["age"] = 31
print(f"After updating age: {person}")

# Dictionary methods
print(f"\nKeys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Safe access with get()
print(f"\nJob: {person.get('job')}")
print(f"Salary: {person.get('salary', 'Not specified')}")

# Iterate over dictionary
print("\nIterating:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Remove items
del person["job"]
print(f"\nAfter deleting job: {person}")

# Update from another dict
updates = {"age": 32, "city": "Boston"}
person.update(updates)
print(f"After update: {person}")
```

Run it and observe dictionary operations.

---

## Practice Exercises

### Exercise 5: Combine Collections

Create a file called `combined.py`:

```python
# List of dictionaries
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 92},
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

# Dictionary with lists
inventory = {
    "apples": [10, 5, 8],
    "bananas": [15, 12, 20],
    "oranges": [7, 9, 6],
}

print("\nInventory:")
for fruit, quantities in inventory.items():
    total = sum(quantities)
    print(f"  {fruit}: {total} total")

# Set of tuples
coordinates = {(0, 0), (1, 1), (2, 2), (0, 1)}
print(f"\nCoordinates: {coordinates}")

# Nested structures
data = {
    "users": [
        {"id": 1, "name": "Alice", "tags": {"admin", "user"}},
        {"id": 2, "name": "Bob", "tags": {"user"}},
    ]
}

print("\nUsers:")
for user in data["users"]:
    print(f"  {user['name']}: {user['tags']}")
```

Run it and observe nested collections.

---

### Exercise 6: Process Collections

Create a file called `process_collections.py`:

```python
# Filter a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")

# Transform a list
squared = [n ** 2 for n in numbers]
print(f"Squared: {squared}")

# Count occurrences
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print(f"\nCounts: {counts}")

# Group by property
words = ["apple", "apricot", "banana", "blueberry", "cherry"]
by_first_letter = {}
for word in words:
    first = word[0]
    if first not in by_first_letter:
        by_first_letter[first] = []
    by_first_letter[first].append(word)
print(f"\nGrouped: {by_first_letter}")

# Find unique elements
items = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(items))
print(f"\nUnique: {unique}")
```

Run it and observe collection processing.

---

### Exercise 7: Choose the Right Collection

Create a file called `choose_collection.py`:

```python
# Use a list for ordered, mutable data
shopping_list = ["milk", "eggs", "bread"]
shopping_list.append("butter")
print(f"Shopping list: {shopping_list}")

# Use a tuple for fixed, immutable data
rgb_color = (255, 128, 0)
print(f"RGB color: {rgb_color}")

# Use a set for unique values
visited_cities = {"New York", "Boston", "Chicago"}
visited_cities.add("Denver")
print(f"Visited: {visited_cities}")

# Use a dict for key-value pairs
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Carol": "555-9012",
}
print(f"Alice's number: {phone_book['Alice']}")

# Combine them
database = {
    "users": [
        {"id": 1, "name": "Alice", "tags": ("admin", "user")},
        {"id": 2, "name": "Bob", "tags": ("user",)},
    ],
    "locations": {(0, 0), (1, 1), (2, 2)},
}
print(f"\nDatabase: {database}")
```

Run it and observe when to use each collection type.

---

## Challenge Exercises

### Challenge 1: Analyze Text with Collections

Create a file called `text_analysis.py`:

```python
def analyze_text(text):
    """Analyze text and return statistics."""
    words = text.lower().split()
    
    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find unique words
    unique_words = set(words)
    
    # Sort by frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return {
        "total_words": len(words),
        "unique_words": len(unique_words),
        "word_counts": word_counts,
        "most_common": sorted_words[:5],
    }

# Test
text = "Python is great. Python is powerful. Python is fun."
result = analyze_text(text)

print(f"Total words: {result['total_words']}")
print(f"Unique words: {result['unique_words']}")
print(f"Most common: {result['most_common']}")
```

Run it and observe the analysis.

---

### Challenge 2: Build a Contact Manager

Create a file called `contact_manager.py`:

```python
def add_contact(contacts, name, phone, email):
    """Add a contact."""
    contacts[name] = {"phone": phone, "email": email}

def remove_contact(contacts, name):
    """Remove a contact."""
    if name in contacts:
        del contacts[name]

def list_contacts(contacts):
    """List all contacts."""
    for name, info in contacts.items():
        print(f"{name}: {info['phone']}, {info['email']}")

def search_contact(contacts, name):
    """Search for a contact."""
    if name in contacts:
        info = contacts[name]
        print(f"{name}: {info['phone']}, {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

# Use the manager
contacts = {}
add_contact(contacts, "Alice", "555-1234", "alice@example.com")
add_contact(contacts, "Bob", "555-5678", "bob@example.com")

print("All contacts:")
list_contacts(contacts)

print("\nSearch for Alice:")
search_contact(contacts, "Alice")

print("\nAfter removing Bob:")
remove_contact(contacts, "Bob")
list_contacts(contacts)
```

Run it and test the contact manager.

---

### Challenge 3: Implement a Simple Inventory System

Create a file called `inventory.py`:

```python
class Inventory:
    """Simple inventory system."""
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, price):
        """Add an item to inventory."""
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price}
    
    def remove_item(self, name, quantity):
        """Remove items from inventory."""
        if name in self.items:
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

# Use the inventory
inv = Inventory()
inv.add_item("Apple", 10, 0.50)
inv.add_item("Banana", 15, 0.30)
inv.add_item("Orange", 8, 0.60)

print("Inventory:")
inv.list_items()
print(f"Total value: ${inv.get_total_value():.2f}")

inv.remove_item("Apple", 3)
print("\nAfter selling 3 apples:")
inv.list_items()
print(f"Total value: ${inv.get_total_value():.2f}")
```

Run it and test the inventory system.

---

### Challenge 4: Find Patterns in Collections

Create a file called `patterns.py`:

```python
# Find duplicates
items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
duplicates = [x for x in set(items) if items.count(x) > 1]
print(f"Duplicates: {duplicates}")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1) & set(list2))
print(f"Common: {common}")

# Find missing elements
all_numbers = set(range(1, 6))
present = {1, 2, 4, 5}
missing = all_numbers - present
print(f"Missing: {missing}")

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened: {flat}")

# Group consecutive numbers
numbers = [1, 2, 3, 5, 6, 7, 9, 10]
groups = []
current_group = [numbers[0]]
for n in numbers[1:]:
    if n == current_group[-1] + 1:
        current_group.append(n)
    else:
        groups.append(current_group)
        current_group = [n]
groups.append(current_group)
print(f"Groups: {groups}")
```

Run it and observe the patterns.

---

## Hints

**KeyError when accessing dict** → The key does not exist. Use `.get()` with a default value instead.

**TypeError when modifying tuple** → Tuples are immutable. Convert to a list, modify, and convert back if needed.

**Set operations confusing** → Remember: `|` is union, `&` is intersection, `-` is difference, `^` is symmetric difference.

**List comprehension syntax** → The pattern is `[expression for item in iterable if condition]`.

---

## What to Review If You Get Stuck

- **Lists** → Handbook section 3.1
- **Tuples** → Handbook section 3.2
- **Sets** → Handbook section 3.3
- **Dictionaries** → Handbook section 3.4
- **Iterating over collections** → Handbook section 3.5
- **Nesting collections** → Handbook section 3.6
- **Choosing the right collection** → Handbook section 3.7

---

## Key Takeaways

After completing these exercises, you should be able to:

- Create and manipulate lists, tuples, sets, and dictionaries
- Choose the right collection type for each task
- Use collection methods effectively
- Iterate over collections
- Combine collections in nested structures
- Process and analyze collections
- Solve real-world problems with collections
