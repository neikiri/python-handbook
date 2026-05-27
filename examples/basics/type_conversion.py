"""
Type Conversion - Converting Between Python Types

This example demonstrates:
- Converting strings to numbers
- Converting numbers to strings
- Common conversion pitfalls
"""

# String to integer
age_string = "25"
age = int(age_string)
print(f"String '{age_string}' converted to int: {age} (type: {type(age).__name__})")

# String to float
price_string = "19.99"
price = float(price_string)
print(f"String '{price_string}' converted to float: {price} (type: {type(price).__name__})")
print()

# Integer to string
count = 42
count_string = str(count)
print(f"Int {count} converted to string: '{count_string}' (type: {type(count_string).__name__})")

# Float to integer (truncates, doesn't round)
pi = 3.14159
pi_int = int(pi)
print(f"Float {pi} converted to int: {pi_int} (truncates toward zero)")

# Integer to float
num = 10
num_float = float(num)
print(f"Int {num} converted to float: {num_float}")
print()

# Boolean conversions
print("=== Boolean Conversions ===")
print(f"bool(0) = {bool(0)}")           # False
print(f"bool(1) = {bool(1)}")           # True
print(f"bool('') = {bool('')}")         # False (empty string)
print(f"bool('hello') = {bool('hello')}")  # True (non-empty string)
print(f"bool([]) = {bool([])}")         # False (empty list)
print(f"bool([1]) = {bool([1])}")       # True (non-empty list)
print()

# Common conversion errors and how to handle them
print("=== Error Handling ===")

# This would raise a ValueError:
# invalid_int = int("not a number")

# Safer approach with try/except:
def safe_int_conversion(value, default=None):
    """Convert value to int, returning default if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f"safe_int_conversion('123') = {safe_int_conversion('123')}")
print(f"safe_int_conversion('abc') = {safe_int_conversion('abc', default=0)}")
print(f"safe_int_conversion(None) = {safe_int_conversion(None, default=-1)}")
print()

# Converting between lists and sets (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
numbers_set = set(numbers_list)
numbers_unique = list(numbers_set)
print(f"Original list: {numbers_list}")
print(f"As set (unique): {numbers_set}")
print(f"Back to list (unique): {numbers_unique}")
