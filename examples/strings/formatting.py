"""
String Formatting - f-Strings and Other Methods

This example demonstrates:
- f-strings (modern Python formatting)
- format() method
- Old-style % formatting
- Number formatting options
"""

print("=== f-Strings (Recommended) ===")

name = "Alice"
age = 30
height = 5.75

# Basic f-string
print(f"Name: {name}, Age: {age}")

# Expression inside f-string
print(f"In 5 years, {name} will be {age + 5}")

# Call function inside f-string
print(f"Name in uppercase: {name.upper()}")

# Format number
print(f"Height: {height:.1f} feet")  # 1 decimal place
print(f"Height: {height:.2f} feet")  # 2 decimal places
print()

print("=== Number Formatting ===")

pi = 3.14159265
large_num = 1234567.89

print(f"Pi: {pi}")
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")
print()

# Thousands separator
print(f"Large number: {large_num:,}")      # 1,234,567.89
print(f"Large number with 2 decimals: {large_num:,.2f}")  # 1,234,567.89
print()

# Percentage
score = 0.85
print(f"Score: {score:.0%}")  # 85%
print(f"Score: {score:.1%}")  # 85.0%
print()

# Alignment
print(f"Left aligned:  |{name:<10}|")
print(f"Right aligned: |{name:>10}|")
print(f"Center aligned:|{name:^10}|")
print()

print("=== format() Method ===")

# Positional arguments
print("Name: {}, Age: {}".format(name, age))

# Named arguments
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Indexing
print("Name: {0}, Age: {1}, Name again: {0}".format(name, age))

# Number formatting
print("Pi: {:.2f}".format(pi))
print("Large: {:,.2f}".format(large_num))
print()

print("=== Old-Style % Formatting ===")

# Not recommended for new code, but you'll see it
print("Name: %s, Age: %d" % (name, age))
print("Pi: %.2f" % pi)
print()

print("=== Complex Formatting ===")

# Multi-line f-string
output = f"""
Name: {name}
Age: {age}
Height: {height:.1f} feet
In 10 years: {age + 10}
"""

print(output)

# Dictionary unpacking
person = {"name": "Bob", "age": 25, "city": "New York"}
print(f"{person['name']} is {person['age']} years old and lives in {person['city']}")
print()

# List formatting
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Numbers joined: {', '.join(str(n) for n in numbers)}")
print()

print("=== Width and Precision ===")

# Width (minimum characters)
print(f"'{name:10}'")  # Width 10
print(f"'{name:>10}'") # Right-aligned width 10

# Precision (decimal places for floats)
print(f"Pi: {pi:.2f}")  # 2 decimal places
print(f"Pi: {pi:8.2f}") # Width 8, 2 decimal places
print(f"Pi: {pi:08.2f}") # Width 8, pad with zeros
print()

print("=== Special Characters ===")

# Escape characters in f-strings
print(f"Quote: \"Hello\"")
print(f"Backslash: \\")
print(f"Newline:\nLine 1\nLine 2")
print()

# Raw strings with f-strings (r before f)
path = r"C:\Users\Name"
print(f"Path (raw): {path}")
