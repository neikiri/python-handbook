"""
Sets - Creating and Working with Sets

This example demonstrates:
- Creating sets
- Set operations (union, intersection, difference)
- Adding and removing items
- Set membership testing
"""

print("=== Creating Sets ===")

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with values
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# Set from list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])
print(f"Numbers from list: {numbers}")  # {1, 2, 3}

# Set with mixed types
mixed_set = {1, "hello", 3.14}
print(f"Mixed: {mixed_set}")
print()

print("=== Set Properties ===")

# Sets are unordered
numbers = {3, 1, 4, 1, 5}
print(f"Numbers: {numbers}")  # Order may vary

# Sets only contain unique values
duplicates = {1, 1, 1, 2, 2, 3}
print(f"Duplicates removed: {duplicates}")  # {1, 2, 3}
print()

print("=== Adding and Removing Items ===")

colors = {"red", "green", "blue"}
print(f"Colors: {colors}")

# Add single item
colors.add("yellow")
print(f"After add('yellow'): {colors}")

# Add multiple items
colors.update(["orange", "purple"])
print(f"After update: {colors}")

# Remove item (raises KeyError if not found)
colors.remove("green")
print(f"After remove('green'): {colors}")

# Discard item (no error if not found)
colors.discard("pink")  # No error even though 'pink' not in set
print(f"After discard('pink'): {colors}")

# Pop item (removes and returns arbitrary item)
removed = colors.pop()
print(f"Pop '{removed}': {colors}")

# Clear all items
colors.clear()
print(f"After clear(): {colors}")
print()

print("=== Set Membership ===")

fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")
print()

print(f"'apple' in fruits: {'apple' in fruits}")     # True
print(f"'orange' in fruits: {'orange' in fruits}")   # False
print()

print("=== Set Operations ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print()

# Union (all items from both sets)
union = set_a | set_b
print(f"Union (A | B): {union}")

# Intersection (items in both sets)
intersection = set_a & set_b
print(f"Intersection (A & B): {intersection}")

# Difference (items in A but not in B)
difference = set_a - set_b
print(f"Difference (A - B): {difference}")

# Symmetric difference (items in A or B but not both)
sym_diff = set_a ^ set_b
print(f"Symmetric difference (A ^ B): {sym_diff}")
print()

print("=== Set Methods ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2, 3}
print()

print(f"A: {set_a}, B: {set_b}, C: {set_c}")
print()

print(f"A.issubset(C): {set_a.issubset(set_c)}")    # False
print(f"C.issubset(A): {set_c.issubset(set_a)}")    # True
print(f"A.issuperset(C): {set_a.issuperset(set_c)}")  # True
print(f"A.isdisjoint(B): {set_a.isdisjoint(set_b)}")  # False (share 4, 5)
print(f"A.isdisjoint({10, 11}): {set_a.isdisjoint({10, 11})}")  # True
print()

print("=== Set Comprehensions ===")

# Basic set comprehension
squares = {x**2 for x in range(5)}
print(f"Squares: {squares}")

# With condition
evens = {x for x in range(10) if x % 2 == 0}
print(f"Evens: {evens}")

# Transform and filter
words = ["apple", "banana", "cherry", "date"]
long_lengths = {len(w) for w in words if len(w) > 5}
print(f"Long word lengths: {long_lengths}")
print()

print("=== Removing Duplicates from List ===")

# Convert list to set, then back to list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
unique_numbers = list(set(numbers))
print(f"Original: {numbers}")
print(f"Unique: {unique_numbers}")  # Order may vary

# To preserve order, use dict.fromkeys()
unique_ordered = list(dict.fromkeys(numbers))
print(f"Unique (ordered): {unique_ordered}")
