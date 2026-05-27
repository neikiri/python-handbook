"""
Dictionaries - Creating and Working with Dictionaries

This example demonstrates:
- Creating dictionaries
- Accessing and modifying values
- Dictionary methods
- Looping over dictionaries
"""

print("=== Creating Dictionaries ===")

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary with values
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# Using dict() constructor
person2 = dict(name="Bob", age=25, city="Boston")
print(f"Person2: {person2}")

# Dictionary from list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(f"From pairs: {dict_from_pairs}")
print()

print("=== Accessing Values ===")

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person: {person}")
print()

# Using square brackets
print(f"person['name']: {person['name']}")

# Using get() (returns None if key doesn't exist)
print(f"person.get('age'): {person.get('age')}")
print(f"person.get('job'): {person.get('job')}")  # None
print(f"person.get('job', 'Unknown'): {person.get('job', 'Unknown')}")  # 'Unknown'
print()

print("=== Modifying Dictionaries ===")

person = {"name": "Alice", "age": 30}
print(f"Original: {person}")

# Add new key-value pair
person["city"] = "New York"
print(f"After adding city: {person}")

# Update existing value
person["age"] = 31
print(f"After updating age: {person}")

# Update with another dictionary
person.update({"job": "Engineer", "country": "USA"})
print(f"After update(): {person}")
print()

print("=== Removing Items ===")

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}
print(f"Original: {person}")
print()

# Remove with pop() (returns value, removes key)
age = person.pop("age")
print(f"Pop 'age' ({age}): {person}")

# Remove with popitem() (removes last inserted item)
last_item = person.popitem()
print(f"Popitem: {last_item}, Result: {person}")

# Remove with del
del person["city"]
print(f"After del person['city']: {person}")

# Clear all items
person.clear()
print(f"After clear(): {person}")
print()

print("=== Dictionary Keys and Values ===")

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person: {person}")
print()

# Get all keys
keys = person.keys()
print(f"Keys: {list(keys)}")

# Get all values
values = person.values()
print(f"Values: {list(values)}")

# Get all key-value pairs
items = person.items()
print(f"Items: {list(items)}")
print()

print("=== Looping Over Dictionaries ===")

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person: {person}")
print()

# Loop over keys (default)
print("Keys:")
for key in person:
    print(f"  {key}: {person[key]}")

# Loop over keys explicitly
print("\nKeys (explicit):")
for key in person.keys():
    print(f"  {key}: {person[key]}")

# Loop over values
print("\nValues:")
for value in person.values():
    print(f"  {value}")

# Loop over key-value pairs
print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")
print()

print("=== Dictionary Comprehensions ===")

# Basic dict comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transform values
words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
print(f"Word lengths: {lengths}")
print()

print("=== Checking Key Existence ===")

person = {"name": "Alice", "age": 30}
print(f"Person: {person}")
print()

print(f"'name' in person: {'name' in person}")     # True
print(f"'job' in person: {'job' in person}")       # False
print()

print("=== Dictionary Methods ===")

person = {"name": "Alice", "age": 30}
print(f"Person: {person}")
print()

# copy() - create a shallow copy
person_copy = person.copy()
print(f"Copy: {person_copy}")

# fromkeys() - create dict from iterable
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(f"From keys: {new_dict}")

# setdefault() - get value or set default
print(f"person.setdefault('city', 'Unknown'): {person.setdefault('city', 'Unknown')}")
print(f"After setdefault: {person}")
print()

print("=== Nested Dictionaries ===")

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 22, "grade": "B"},
}
print(f"Students: {students}")
print(f"alice's grade: {students['alice']['grade']}")

# Using dict() constructor for nested
students2 = {
    "alice": dict(age=20, grade="A"),
    "bob": dict(age=22, grade="B"),
}
print(f"Students2: {students2}")
