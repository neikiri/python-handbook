"""
String Basics - Creating and Working with Strings

This example demonstrates:
- Creating strings with single, double, and triple quotes
- String indexing and negative indexing
- String length with len()
- String immutability
"""

print("=== Creating Strings ===")

# Single quotes
single_quote = 'Hello'
print(f"Single quotes: '{single_quote}'")

# Double quotes
double_quote = "Hello"
print(f"Double quotes: '{double_quote}'")

# Triple quotes (for multi-line strings)
multi_line = """This is a
multi-line string
in Python."""
print(f"Triple quotes:\n{multi_line}")
print()

# Triple quotes for docstrings
def example_function():
    """This is a docstring."""
    pass

print(f"Docstring: {example_function.__doc__}")
print()

print("=== String Indexing ===")

text = "Python"
print(f"Text: '{text}'")
print(f"Length: {len(text)}")
print()

# Positive indexing (starts at 0)
print("Positive indexing:")
print(f"text[0] = '{text[0]}'")  # 'P'
print(f"text[1] = '{text[1]}'")  # 'y'
print(f"text[5] = '{text[5]}'")  # 'n'
print()

# Negative indexing (starts at -1)
print("Negative indexing:")
print(f"text[-1] = '{text[-1]}'")  # 'n'
print(f"text[-2] = '{text[-2]}'")  # 'o'
print(f"text[-6] = '{text[-6]}'")  # 'P'
print()

print("=== String Slicing (Preview) ===")

# Slicing: string[start:end] - end is exclusive
print(f"text[0:2] = '{text[0:2]}'")  # 'Py'
print(f"text[1:4] = '{text[1:4]}'")  # 'yth'
print(f"text[2:] = '{text[2:]}'")    # 'thon'
print(f"text[:4] = '{text[:4]}'")    # 'Pyth'
print()

print("=== String Immutability ===")

# Strings cannot be changed after creation
name = "Alice"
print(f"Original: '{name}'")

# This would raise an error:
# name[0] = "B"  # TypeError: 'str' object does not support item assignment

# Instead, create a new string
new_name = "B" + name[1:]
print(f"Modified: '{new_name}'")
print()

print("=== String Concatenation ===")

first = "Hello"
second = "World"

# Using +
result = first + " " + second
print(f"Using +: '{result}'")

# Using join() (better for many strings)
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(f"Using join(): '{sentence}'")
print()

print("=== String Repetition ===")

# Using *
print(f"'Hi' * 3 = {'Hi' * 3}")
print(f"'- ' * 10 = {'- ' * 10}")
