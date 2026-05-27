"""
Tuples - Creating and Working with Tuples

This example demonstrates:
- Creating tuples
- Accessing tuple items
- Tuple unpacking
- When to use tuples vs lists
"""

print("=== Creating Tuples ===")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with values
fruits = ("apple", "banana", "cherry")
print(f"Fruits: {fruits}")

# Tuple with mixed types
mixed_tuple = (1, "hello", 3.14, True)
print(f"Mixed: {mixed_tuple}")

# Single element tuple (note the comma!)
single = (42,)
print(f"Single element: {single}")

# Without comma, it's just parentheses around a value
not_a_tuple = (42)
print(f"Not a tuple: {not_a_tuple} (type: {type(not_a_tuple).__name__})")

# Using tuple() constructor
numbers = tuple(range(5))
print(f"Numbers from range: {numbers}")
print()

print("=== Accessing Tuple Items ===")

letters = ("a", "b", "c", "d", "e")
print(f"Letters: {letters}")
print()

# Positive indexing
print(f"letters[0] = '{letters[0]}'")  # 'a'
print(f"letters[2] = '{letters[2]}'")  # 'c'

# Negative indexing
print(f"letters[-1] = '{letters[-1]}'")  # 'e'
print(f"letters[-2] = '{letters[-2]}'")  # 'd'
print()

print("=== Tuple Unpacking ===")

# Unpack tuple into variables
person = ("Alice", 30, "Engineer")
name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# Using _ for unused values
coordinates = (10, 20, 30)
x, y, _ = coordinates
print(f"x: {x}, y: {y}")

# Unpack with * (collects remaining items)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")
print()

print("=== Tuple Immutability ===")

# Tuples cannot be modified after creation
fruits = ("apple", "banana", "cherry")
print(f"Fruits: {fruits}")

# This would raise an error:
# fruits[0] = "orange"  # TypeError

# To "modify" a tuple, create a new one
new_fruits = ("orange",) + fruits[1:]
print(f"New fruits: {new_fruits}")
print()

print("=== Tuple Operations ===")

# Concatenate tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"(1, 2, 3) + (4, 5, 6) = {combined}")

# Repeat tuple
repeated = (1, 2) * 3
print(f"(1, 2) * 3 = {repeated}")

# Check membership
print(f"2 in (1, 2, 3): {2 in (1, 2, 3)}")
print(f"5 in (1, 2, 3): {5 in (1, 2, 3)}")
print()

print("=== Tuple Methods ===")

numbers = (3, 1, 4, 1, 5, 9, 2, 6)
print(f"Numbers: {numbers}")
print()

print(f"count(1): {numbers.count(1)}")  # 2
print(f"index(4): {numbers.index(4)}")  # 2
print()

print("=== Tuples vs Lists ===")

print("Tuples:")
print("  - Immutable (cannot be changed)")
print("  - Used for fixed collections")
print("  - Can be used as dictionary keys")
print("  - Slightly more memory efficient")
print()

print("Lists:")
print("  - Mutable (can be changed)")
print("  - Used for collections that may change")
print("  - Cannot be dictionary keys")
print("  - More flexible for modifications")
print()

print("=== When to Use Tuples ===")

# 1. Return multiple values from a function
def get_point():
    """Return a 2D point as a tuple."""
    return (10, 20)

point = get_point()
print(f"Point: {point}")

# 2. Use as dictionary keys (because tuples are hashable)
locations = {
    ("New York", "NY"): "USA",
    ("London", "UK"): "UK",
}
print(f"Locations: {locations}")

# 3. Unpack in loops
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(f"Pair: {a}, {b}")
