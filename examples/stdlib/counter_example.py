"""
Counter Example - Using collections.Counter

This example demonstrates:
- Creating Counter objects
- Counting items
- Most common items
- Counter arithmetic
- Counter with dictionaries
"""

from collections import Counter

print("=== Creating Counters ===")

# From a list
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
fruit_counter = Counter(fruits)
print(f"Fruits: {fruits}")
print(f"Counter: {fruit_counter}")
print()

# From a string
text = "hello world"
char_counter = Counter(text)
print(f"Text: '{text}'")
print(f"Character counter: {char_counter}")
print()

# From a dictionary
counts = {"apple": 3, "banana": 2, "cherry": 1}
counter_from_dict = Counter(counts)
print(f"Dictionary: {counts}")
print(f"Counter: {counter_from_dict}")
print()

# Empty counter
empty_counter = Counter()
print(f"Empty counter: {empty_counter}")
print()

print("=== Accessing Counts ===")

counter = Counter(["apple", "banana", "apple", "cherry"])
print(f"Counter: {counter}")
print()

# Access count for a key
print(f"counter['apple']: {counter['apple']}")
print(f"counter['orange']: {counter['orange']}")  # Returns 0 for missing keys

# Get all elements
print(f"list(counter.elements()): {list(counter.elements())}")
print()

print("=== Most Common Items ===")

counter = Counter("abracadabra")
print(f"Counter: {counter}")
print()

# Get most common items
print(f"counter.most_common(): {counter.most_common()}")
print(f"counter.most_common(3): {counter.most_common(3)}")
print(f"counter.most_common(1): {counter.most_common(1)}")
print()

print("=== Counter Arithmetic ===")

counter1 = Counter("aabbcc")
counter2 = Counter("bcdd")

print(f"Counter 1: {counter1}")
print(f"Counter 2: {counter2}")
print()

# Addition (combine counts)
print(f"counter1 + counter2: {counter1 + counter2}")

# Subtraction (subtract counts, keep only positive)
print(f"counter1 - counter2: {counter1 - counter2}")

# Intersection (minimum of counts)
print(f"counter1 & counter2: {counter1 & counter2}")

# Union (maximum of counts)
print(f"counter1 | counter2: {counter1 | counter2}")
print()

print("=== Updating Counters ===")

counter = Counter(["apple", "banana"])
print(f"Initial: {counter}")

# Update with list
counter.update(["apple", "cherry"])
print(f"After update with list: {counter}")

# Update with dict
counter.update({"apple": 5, "date": 2})
print(f"After update with dict: {counter}")

# Subtract
counter.subtract(["apple", "banana"])
print(f"After subtract: {counter}")
print()

print("=== Counter Methods ===")

counter = Counter(["apple", "banana", "apple", "cherry"])
print(f"Counter: {counter}")
print()

# most_common() - get most frequent items
print(f"most_common(): {counter.most_common()}")

# elements() - iterate over elements
print(f"elements(): {list(counter.elements())}")

# total() - sum of all counts
print(f"total(): {counter.total()}")

# most_common(n) with n > len(counter)
print(f"most_common(10): {counter.most_common(10)}")
print()

print("=== Counter vs Dict ===")

# Counter has useful methods that dict doesn't
text = "the quick brown fox jumps over the lazy dog"
words = text.split()

word_counter = Counter(words)
print(f"Word counter: {word_counter}")
print()

# Get top 3 most common words
print(f"Top 3 words: {word_counter.most_common(3)}")

# Get total word count
print(f"Total words: {word_counter.total()}")

# Get unique word count
print(f"Unique words: {len(word_counter)}")
print()

print("=== Practical Examples ===")

# Find most common letters in a text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
letter_counts = Counter(text.lower())
print(f"Letter counts (top 5): {letter_counts.most_common(5)}")

# Count word frequencies
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
word_counts = Counter(words)
print(f"\nWord frequencies:")
for word, count in word_counts.most_common():
    print(f"  {word}: {count}")

# Check if two strings are anagrams
def are_anagrams(s1, s2):
    """Check if two strings are anagrams."""
    return Counter(s1.lower()) == Counter(s2.lower())


print(f"\n'listen' and 'silent' are anagrams: {are_anagrams('listen', 'silent')}")
print(f"'hello' and 'world' are anagrams: {are_anagrams('hello', 'world')}")

# Find duplicate items in a list
def find_duplicates(items):
    """Find items that appear more than once."""
    counter = Counter(items)
    return [item for item, count in counter.items() if count > 1]


items = ["apple", "banana", "apple", "cherry", "banana", "date"]
duplicates = find_duplicates(items)
print(f"\nItems: {items}")
print(f"Duplicates: {duplicates}")
