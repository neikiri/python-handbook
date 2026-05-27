"""
String Methods - Common String Operations

This example demonstrates:
- Case conversion (upper, lower, title, swapcase)
- Stripping whitespace (strip, lstrip, rstrip)
- Finding and replacing (find, index, replace)
- Checking string properties (startswith, endswith, isdigit, etc.)
"""

text = "  Hello, World!  "
print(f"Original: '{text}'")
print()

print("=== Case Conversion ===")

# upper() - all uppercase
print(f"upper(): '{text.upper().strip()}'")

# lower() - all lowercase
print(f"lower(): '{text.lower().strip()}'")

# title() - first letter of each word uppercase
sentence = "hello world, how are you?"
print(f"title(): '{sentence.title()}'")

# capitalize() - first letter of string uppercase
print(f"capitalize(): '{sentence.capitalize()}'")

# swapcase() - swap upper and lower
print(f"swapcase(): '{text.swapcase().strip()}'")
print()

print("=== Stripping Whitespace ===")

# strip() - remove whitespace from both ends
print(f"strip(): '{text.strip()}'")

# lstrip() - remove whitespace from left
print(f"lstrip(): '{text.lstrip()}'")

# rstrip() - remove whitespace from right
print(f"rstrip(): '{text.rstrip()}'")
print()

print("=== Finding Substrings ===")

text2 = "Python is fun, Python is powerful"
print(f"Text: '{text2}'")
print()

# find() - returns index or -1 if not found
print(f"find('Python'): {text2.find('Python')}")    # 0
print(f"find('Java'): {text2.find('Java')}")        # -1
print(f"find('Python', 10): {text2.find('Python', 10)}")  # 18

# rfind() - search from the right
print(f"rfind('Python'): {text2.rfind('Python')}")  # 18

# index() - like find(), but raises ValueError if not found
try:
    print(f"index('Python'): {text2.index('Python')}")
    print(f"index('Java'): {text2.index('Java')}")  # This will raise
except ValueError as e:
    print(f"index('Java') raised ValueError: {e}")
print()

print("=== Replacing Substrings ===")

# replace() - replace all occurrences
print(f"replace('Python', 'Java'): '{text2.replace('Python', 'Java')}'")

# replace with count (replace first n occurrences)
print(f"replace('Python', 'Java', 1): '{text2.replace('Python', 'Java', 1)}'")
print()

print("=== Checking String Properties ===")

test_strings = [
    "Hello",
    "123",
    "hello123",
    "   ",
    "HELLO",
    "hello",
    "12.34",
]

print("String | isalpha() | isdigit() | isalnum() | isspace() | islower() | isupper()")
print("-" * 90)

for s in test_strings:
    print(f"{s:8} | {str(s.isalpha()):9} | {str(s.isdigit()):9} | "
          f"{str(s.isalnum()):9} | {str(s.isspace()):9} | "
          f"{str(s.islower()):9} | {str(s.isupper()):9}")
print()

print("=== startswith() and endswith() ===")

filename = "document.txt"
url = "https://example.com"

print(f"filename: '{filename}'")
print(f"  startswith('doc'): {filename.startswith('doc')}")
print(f"  endswith('.txt'): {filename.endswith('.txt')}")

print(f"\nurl: '{url}'")
print(f"  startswith('https://'): {url.startswith('https://')}")
print(f"  endswith('.com'): {url.endswith('.com')}")
print()

print("=== count() ===")

text3 = "banana"
print(f"Text: '{text3}'")
print(f"count('a'): {text3.count('a')}")
print(f"count('na'): {text3.count('na')}")
print(f"count('a', 1, 3): {text3.count('a', 1, 3)}")  # count from index 1 to 3
