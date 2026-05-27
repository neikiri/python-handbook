"""
String Slicing - Extracting Substrings

This example demonstrates:
- Basic slicing syntax: string[start:end]
- Negative indices in slicing
- Step/skip in slicing
- Omitting start/end indices
"""

text = "Python Programming"
print(f"Text: '{text}'")
print(f"Length: {len(text)}")
print()

print("=== Basic Slicing ===")

# string[start:end] - end is exclusive
print(f"text[0:6] = '{text[0:6]}'")    # 'Python'
print(f"text[7:18] = '{text[7:18]}'")  # 'Programming'
print(f"text[0:3] = '{text[0:3]}'")    # 'Pyt'
print()

print("=== Negative Indices ===")

# Negative indices count from the end
print(f"text[-11:-1] = '{text[-11:-1]}'")  # 'Programmin'
print(f"text[-11:] = '{text[-11:]}'")      # 'Programming'
print(f"text[:-11] = '{text[:-11]}'")      # 'Python'
print()

print("=== Omitting Start or End ===")

# Omit start = from beginning
print(f"text[:6] = '{text[:6]}'")    # 'Python'

# Omit end = to the end
print(f"text[7:] = '{text[7:]}'")    # 'Programming'

# Omit both = whole string
print(f"text[:] = '{text[:]}'")      # 'Python Programming'
print()

print("=== Step/Skip in Slicing ===")

# string[start:end:step]
numbers = "0123456789"
print(f"Numbers: '{numbers}'")
print(f"numbers[::2] = '{numbers[::2]}'")      # '02468' (every 2nd)
print(f"numbers[1::2] = '{numbers[1::2]}'")    # '13579' (every 2nd, starting at 1)
print(f"numbers[::3] = '{numbers[::3]}'")      # '0369' (every 3rd)
print()

# Reverse with negative step
print(f"numbers[::-1] = '{numbers[::-1]}'")    # '9876543210' (reversed)
print(f"text[::-1] = '{text[::-1]}'")          # 'gnimmargorP nohtyP'
print()

print("=== Slicing with Step > 1 ===")

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"Alphabet: '{alphabet}'")
print(f"alphabet[::5] = '{alphabet[::5]}'")    # 'afkpuz' (every 5th)
print(f"alphabet[1::5] = '{alphabet[1::5]}'")  # 'bgqv' (every 5th, starting at 1)
print()

print("=== Slicing with Negative Step ===")

# Reverse a string
print(f"Reverse 'hello': '{'hello'[::-1]}'")

# Reverse with step
print(f"alphabet[::-2] = '{alphabet[::-2]}'")  # 'zxvtrpnljhfdb' (reverse, every 2nd)
print()

print("=== Common Slicing Patterns ===")

# Get first n characters
n = 3
print(f"First {n} chars of '{text}': '{text[:n]}'")

# Get last n characters
print(f"Last {n} chars of '{text}': '{text[-n:]}'")

# Get everything except first n
print(f"Except first {n} chars: '{text[n:]}'")

# Get everything except last n
print(f"Except last {n} chars: '{text[:-n]}'")

# Get middle section (skip first and last)
print(f"Middle (skip first 3, last 3): '{text[3:-3]}'")
