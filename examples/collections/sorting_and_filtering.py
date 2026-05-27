"""
Sorting and Filtering - Sorting and Filtering Collections

This example demonstrates:
- Sorting lists with sorted() and sort()
- Sorting dictionaries
- Filtering with list comprehensions and filter()
- Custom sort keys
"""

print("=== Sorting Lists ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Numbers: {numbers}")
print()

# sorted() returns a new sorted list
sorted_numbers = sorted(numbers)
print(f"sorted(numbers): {sorted_numbers}")

# sort() sorts in place
numbers.sort()
print(f"After sort(): {numbers}")

# Reverse sort
reverse_sorted = sorted(numbers, reverse=True)
print(f"sorted(numbers, reverse=True): {reverse_sorted}")
print()

print("=== Sorting Strings ===")

words = ["banana", "apple", "cherry", "date"]
print(f"Words: {words}")

# Sort alphabetically
sorted_words = sorted(words)
print(f"sorted(words): {sorted_words}")

# Sort by length
sorted_by_length = sorted(words, key=len)
print(f"sorted(words, key=len): {sorted_by_length}")
print()

print("=== Custom Sort Keys ===")

# Sort by last character
words = ["apple", "banana", "cherry", "date"]
sorted_by_last = sorted(words, key=lambda x: x[-1])
print(f"Sorted by last character: {sorted_by_last}")

# Sort by multiple criteria
students = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 30),
    ("Diana", 25),
]
print(f"\nStudents: {students}")

# Sort by age, then by name
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
print(f"Sorted by age, then name: {sorted_students}")
print()

print("=== Sorting Dictionaries ===")

# Sort dictionary keys
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person: {person}")

sorted_keys = sorted(person.keys())
print(f"Sorted keys: {sorted_keys}")

sorted_items = sorted(person.items())
print(f"Sorted items: {sorted_items}")
print()

# Sort dictionary by value
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(f"Scores: {scores}")

# Get sorted items by value
sorted_by_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(f"Sorted by score (descending): {sorted_by_score}")
print()

print("=== Filtering Lists ===")

numbers = list(range(1, 11))
print(f"Numbers: {numbers}")
print()

# List comprehension
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")

# Using filter()
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers (filter): {odds}")

# Filter with condition
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [w for w in words if len(w) > 5]
print(f"Long words (>5 chars): {long_words}")
print()

print("=== Filtering Dictionaries ===")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 78}
print(f"Scores: {scores}")
print()

# Filter by value (scores >= 90)
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"High scores (>= 90): {high_scores}")

# Filter keys by condition
vowel_names = {name: score for name, score in scores.items() if name[0].lower() in "aeiou"}
print(f"Names starting with vowel: {vowel_names}")
print()

print("=== Complex Filtering Example ===")

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 20, "grade": "A"},
    {"name": "Diana", "age": 21, "grade": "B"},
]

print(f"Students: {students}")
print()

# Filter students with grade "A" and age <= 21
top_students = [
    s for s in students
    if s["grade"] == "A" and s["age"] <= 21
]
print(f"Top students (A grade, age <= 21): {top_students}")

# Sort by name
sorted_top = sorted(top_students, key=lambda x: x["name"])
print(f"Sorted top students: {sorted_top}")
print()

print("=== Removing Duplicates and Sorting ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Numbers: {numbers}")

# Remove duplicates and sort
unique_sorted = sorted(set(numbers))
print(f"Unique sorted: {unique_sorted}")

# Or: sort first, then remove adjacent duplicates
numbers.sort()
unique_sorted2 = []
for n in numbers:
    if not unique_sorted2 or n != unique_sorted2[-1]:
        unique_sorted2.append(n)
print(f"Unique sorted (manual): {unique_sorted2}")
