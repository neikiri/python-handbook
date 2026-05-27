"""
Counting Items - Counting with dict and Counter

This example demonstrates:
- Counting items with a regular dictionary
- Using collections.Counter
- Most common items
- Updating counts
"""

from collections import Counter

print("=== Counting with Regular Dictionary ===")

# List of items to count
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(f"Fruits: {fruits}")
print()

# Manual counting with dict
fruit_counts = {}
for fruit in fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

print("Manual count:")
for fruit, count in fruit_counts.items():
    print(f"  {fruit}: {count}")
print()

print("=== Using dict.get() ===")

# More concise with get()
fruit_counts = {}
for fruit in fruits:
    fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

print("Using get():")
for fruit, count in fruit_counts.items():
    print(f"  {fruit}: {count}")
print()

print("=== Using collections.Counter ===")

# Counter is designed for counting
fruit_counts = Counter(fruits)
print(f"Counter result: {fruit_counts}")
print()

# Access counts
print(f"apple count: {fruit_counts['apple']}")
print(f"cherry count: {fruit_counts['cherry']}")
print(f"orange count (not present): {fruit_counts['orange']}")  # 0
print()

print("=== Counter Methods ===")

text = "hello world"
char_counts = Counter(text)
print(f"Text: '{text}'")
print(f"Character counts: {char_counts}")
print()

# most_common() - get most frequent items
print("Most common characters:")
for char, count in char_counts.most_common(3):
    print(f"  '{char}': {count}")

# most_common() with no argument returns all
print("\nAll characters (most common first):")
for char, count in char_counts.most_common():
    print(f"  '{char}': {count}")
print()

# elements() - iterate over elements (repeated by count)
print("Elements (repeated by count):")
print(f"  {list(char_counts.elements())}")
print()

print("=== Updating Counts ===")

# Create counter
counts = Counter(["a", "b", "c", "a"])
print(f"Initial: {counts}")

# Update with list
counts.update(["a", "b", "d"])
print(f"After update with list: {counts}")

# Update with dict
counts.update({"a": 5, "e": 2})
print(f"After update with dict: {counts}")
print()

print("=== Counter Arithmetic ===")

counts1 = Counter(["a", "a", "b", "c"])
counts2 = Counter(["a", "b", "b", "d"])
print(f"Counts1: {counts1}")
print(f"Counts2: {counts2}")
print()

# Addition (combine counts)
print(f"Counts1 + Counts2: {counts1 + counts2}")

# Subtraction (subtract counts, keep only positive)
print(f"Counts1 - Counts2: {counts1 - counts2}")

# Intersection (minimum of counts)
print(f"Counts1 & Counts2: {counts1 & counts2}")

# Union (maximum of counts)
print(f"Counts1 | Counts2: {counts1 | counts2}")
print()

print("=== Counting Words in Text ===")

text = """
Python is great. Python is easy to learn.
Python is popular for data science.
"""

# Clean and split text
words = text.lower().split()
# Remove punctuation
words = [word.strip(".,!?") for word in words]

# Count words
word_counts = Counter(words)
print("Word counts:")
for word, count in word_counts.most_common():
    print(f"  {word}: {count}")
print()

print("=== Counting with DefaultDict ===")

from collections import defaultdict

# DefaultDict with int (default value is 0)
fruit_counts = defaultdict(int)
for fruit in fruits:
    fruit_counts[fruit] += 1

print("Using defaultdict:")
for fruit, count in fruit_counts.items():
    print(f"  {fruit}: {count}")
