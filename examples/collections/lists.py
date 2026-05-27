"""
Lists - Creating and Working with Lists

This example demonstrates:
- Creating lists
- Accessing list items
- Modifying lists (append, insert, remove, pop)
- List slicing
- List comprehensions
"""

print("=== Creating Lists ===")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with values
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# List with mixed types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed: {mixed_list}")

# Using list() constructor
numbers = list(range(5))
print(f"Numbers from range: {numbers}")
print()

print("=== Accessing List Items ===")

letters = ["a", "b", "c", "d", "e"]
print(f"Letters: {letters}")
print()

# Positive indexing
print(f"letters[0] = '{letters[0]}'")  # 'a'
print(f"letters[2] = '{letters[2]}'")  # 'c'

# Negative indexing
print(f"letters[-1] = '{letters[-1]}'")  # 'e'
print(f"letters[-2] = '{letters[-2]}'")  # 'd'
print()

print("=== Modifying Lists ===")

# Change item by index
letters[1] = "B"
print(f"Change letters[1] to 'B': {letters}")

# Append item to end
letters.append("f")
print(f"Append 'f': {letters}")

# Insert item at position
letters.insert(2, "C")
print(f"Insert 'C' at index 2: {letters}")
print()

print("=== Removing Items ===")

# Remove by value
letters.remove("C")
print(f"Remove 'C': {letters}")

# Remove by index with pop()
removed = letters.pop(1)
print(f"Pop index 1 ('{removed}'): {letters}")

# Remove last item
letters.pop()
print(f"Pop last item: {letters}")

# Clear all items
letters.clear()
print(f"Clear list: {letters}")
print()

print("=== List Slicing ===")

numbers = list(range(10))
print(f"Numbers: {numbers}")
print()

print(f"numbers[2:5] = {numbers[2:5]}")    # [2, 3, 4]
print(f"numbers[:3] = {numbers[:3]}")      # [0, 1, 2]
print(f"numbers[7:] = {numbers[7:]}")      # [7, 8, 9]
print(f"numbers[::2] = {numbers[::2]}")    # [0, 2, 4, 6, 8] (every 2nd)
print(f"numbers[::-1] = {numbers[::-1]}")  # reversed
print()

print("=== List Length ===")

print(f"len([1, 2, 3]) = {len([1, 2, 3])}")
print(f"len([]) = {len([])}")
print()

print("=== List Operations ===")

# Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"[1, 2, 3] + [4, 5, 6] = {combined}")

# Repeat list
repeated = [1, 2] * 3
print(f"[1, 2] * 3 = {repeated}")

# Check membership
print(f"2 in [1, 2, 3]: {2 in [1, 2, 3]}")
print(f"5 in [1, 2, 3]: {5 in [1, 2, 3]}")
print()

print("=== List Methods ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Numbers: {numbers}")
print()

print(f"count(1): {numbers.count(1)}")     # 2
print(f"index(4): {numbers.index(4)}")     # 2
print(f"min: {min(numbers)}")              # 1
print(f"max: {max(numbers)}")              # 9
print(f"sum: {sum(numbers)}")              # 31
print()

# Sort in place
numbers.sort()
print(f"After sort(): {numbers}")

# Reverse in place
numbers.reverse()
print(f"After reverse(): {numbers}")
print()

print("=== List Comprehensions ===")

# Basic list comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Transform and filter
words = ["apple", "banana", "cherry", "date"]
long_words = [w.upper() for w in words if len(w) > 5]
print(f"Long words (uppercase): {long_words}")
print()

print("=== Nested Lists ===")

# List of lists (2D grid)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(f"Grid: {grid}")
print(f"grid[0][1] = {grid[0][1]}")  # 2
print(f"grid[2][2] = {grid[2][2]}")  # 9

# Flatten a nested list
flat = [item for row in grid for item in row]
print(f"Flattened: {flat}")
