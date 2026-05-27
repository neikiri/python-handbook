"""
Itertools Example - Efficient Iteration with itertools

This example demonstrates:
- Infinite iterators (count, cycle, repeat)
- Accumulating values (accumulate)
- Combinatoric generators (permutations, combinations, product)
- Chaining and grouping
"""

import itertools
import operator

print("=== Infinite Iterators ===")

print("count() - count from start, stepping by step:")
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(f"  {i}")

print()

print("cycle() - cycle through an iterable:")
count = 0
for item in itertools.cycle(["A", "B", "C"]):
    if count >= 6:
        break
    print(f"  {item}")
    count += 1

print()

print("repeat() - repeat an item:")
for item in itertools.repeat("Hello", 3):
    print(f"  {item}")
print()

print("=== Accumulate ===")

# accumulate() - accumulate values
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"accumulate(numbers): {list(itertools.accumulate(numbers))}")

# With custom function (multiply)
print(f"accumulate(numbers, operator.mul): {list(itertools.accumulate(numbers, operator.mul))}")

# With max function
print(f"accumulate(numbers, max): {list(itertools.accumulate(numbers, max))}")
print()

print("=== Combinatoric Generators ===")

# permutations() - all possible orderings
items = ["A", "B", "C"]
print(f"Items: {items}")
print(f"permutations(items):")
for perm in itertools.permutations(items):
    print(f"  {perm}")

print()

# permutations with length
print(f"permutations(items, 2):")
for perm in itertools.permutations(items, 2):
    print(f"  {perm}")

print()

# combinations() - all possible combinations (order doesn't matter)
print(f"combinations(items, 2):")
for combo in itertools.combinations(items, 2):
    print(f"  {combo}")

print()

# combinations_with_replacement()
print(f"combinations_with_replacement(items, 2):")
for combo in itertools.combinations_with_replacement(items, 2):
    print(f"  {combo}")

print()

# product() - Cartesian product
print(f"product([1, 2], ['A', 'B']):")
for prod in itertools.product([1, 2], ["A", "B"]):
    print(f"  {prod}")

print()

print("=== Chaining and Grouping ===")

# chain() - chain multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"chain(list1, list2, list3): {list(itertools.chain(list1, list2, list3))}")

print()

# chain.from_iterable() - chain from iterable of iterables
iterables = [[1, 2], [3, 4], [5, 6]]
print(f"iterables: {iterables}")
print(f"chain.from_iterable(iterables): {list(itertools.chain.from_iterable(iterables))}")

print()

# groupby() - group consecutive items
data = [("apple", 1), ("apple", 2), ("banana", 3), ("banana", 4), ("cherry", 5)]
print(f"Data: {data}")

# Group by first element
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

print()

print("=== Slice Iterators ===")

# islice() - slice an iterator
numbers = itertools.count(0)
print(f"First 5 numbers from count(): {list(itertools.islice(numbers, 5))}")

# Slice with start, stop, step
numbers = itertools.count(0)
print(f"Numbers[5:10:2]: {list(itertools.islice(numbers, 5, 10, 2))}")
print()

print("=== Tee - Create Independent Iterators ===")

# tee() - create independent copies of an iterator
original = [1, 2, 3, 4, 5]
iter1, iter2 = itertools.tee(original, 2)

print(f"Original: {original}")
print(f"Iterator 1: {list(iter1)}")
print(f"Iterator 2: {list(iter2)}")
print()

print("=== Practical Examples ===")

# Generate all possible 3-digit binary numbers
binary_digits = [0, 1]
binary_numbers = list(itertools.product(binary_digits, repeat=3))
print("All 3-digit binary numbers:")
for num in binary_numbers:
    print(f"  {num}")

print()

# Generate all 2-card combinations from a deck
suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5"]
deck = list(itertools.product(ranks, suits))

print(f"Deck size: {len(deck)}")
print(f"2-card combinations: {len(list(itertools.combinations(deck, 2)))}")

# Generate all possible passwords (simple example)
chars = "abc123"
passwords = itertools.product(chars, repeat=3)
print(f"\nAll 3-character passwords from '{chars}':")
for i, pwd in enumerate(passwords):
    if i >= 10:  # Show first 10
        print(f"  ... and {len(chars)**3 - 10} more")
        break
    print(f"  {''.join(pwd)}")

print()

# Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain.from_iterable(nested))
print(f"\nNested: {nested}")
print(f"Flattened: {flat}")

# Group items by category
items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("date", "fruit"),
]

# Sort by category first (required for groupby)
items.sort(key=lambda x: x[1])

print(f"\nItems grouped by category:")
for category, group in itertools.groupby(items, key=lambda x: x[1]):
    print(f"  {category}: {[item[0] for item in group]}")
