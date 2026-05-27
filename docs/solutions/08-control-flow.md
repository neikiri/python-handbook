# Solutions 08: Control Flow

## Overview

Chapter 08 exercises cover conditionals, truthiness, `while` and `for` loops, `break` and `continue`, `enumerate()` and `zip()`, the loop `else` clause, and building interactive programs. This solution guide explains the reasoning behind each exercise.

---

## Notes Before Checking Solutions

Control flow is where programs start to feel alive — they make decisions and repeat actions. The most important habit to build here is writing loops that always terminate. An infinite loop that you did not intend is one of the most frustrating bugs to debug.

---

## Warm-up Exercise Solutions

### Exercise 1: Write Simple Conditionals

```python
age = 18
if age >= 18:
    print("You are an adult.")

score = 75
if score >= 70:
    print("You passed!")
else:
    print("You failed.")

grade_points = 85
if grade_points >= 90:
    grade = "A"
elif grade_points >= 80:
    grade = "B"
elif grade_points >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")  # B
```

**How `if/elif/else` works:** Python checks each condition from top to bottom and executes the first block whose condition is `True`. Once a match is found, the remaining conditions are skipped. The `else` block runs only if no condition matched.

**Nested conditionals:**

```python
temperature = 25
if temperature > 20:
    if temperature > 30:
        print("It is hot!")
    else:
        print("It is warm.")  # This runs
else:
    print("It is cold.")
```

Nested conditionals work, but they can become hard to read. When possible, flatten them using `and`:

```python
if temperature > 20 and temperature <= 30:
    print("It is warm.")
```

---

### Exercise 2: Understand Truthiness

**Falsy values:** `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`, `False`

**Everything else is truthy.**

```python
# These all print the "falsy" branch
if 0: ...
if "": ...
if []: ...
if None: ...

# These all print the "truthy" branch
if 1: ...
if "hello": ...
if [1, 2, 3]: ...
```

**Using truthiness directly:**

```python
name = input("Enter your name (or press Enter to skip): ")
if name:
    print(f"Hello, {name}!")
else:
    print("You did not enter a name.")
```

`if name:` is equivalent to `if name != "":` but more Pythonic. An empty string is falsy, so the `else` branch runs when the user presses Enter without typing anything.

---

### Exercise 3: Use `while` Loops

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

**The loop condition is checked before each iteration.** When `count` reaches `5`, the condition `count < 5` is `False` and the loop stops.

**`while True` with `break`:**

```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print(f"You entered: {user_input}")
```

`while True` creates an infinite loop. `break` exits it immediately. This pattern is useful when the exit condition is in the middle of the loop body, not at the top.

**`continue`:**

```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # skip even numbers
    print(f"Odd number: {count}")
```

`continue` skips the rest of the current iteration and jumps back to the loop condition. Here it skips the `print` for even numbers.

---

### Exercise 4: Use `for` Loops

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")

# Loop over a string
for letter in "Python":
    print(letter)

# range()
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):    # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(i)
```

**`range()` is exclusive of the stop value.** `range(5)` gives `0, 1, 2, 3, 4` — not `5`. `range(2, 8)` gives `2, 3, 4, 5, 6, 7` — not `8`.

**Nested loops:**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
```

The inner loop runs completely for each iteration of the outer loop. For a 3×3 table, the inner loop runs 9 times total.

---

## Practice Exercise Solutions

### Exercise 5: Use `enumerate()` and `zip()`

```python
fruits = ["apple", "banana", "cherry"]

# enumerate() — get index and value together
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

**Why `enumerate()` instead of `range(len(fruits))`?** Both work, but `enumerate()` is more readable and Pythonic. It avoids the awkward `fruits[i]` indexing.

```python
names = ["Alice", "Bob", "Carol"]
ages = [30, 25, 28]

# zip() — iterate over two lists in parallel
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```

**`zip()` stops at the shortest iterable.** If the lists have different lengths, `zip()` stops when the shorter one is exhausted. Use `itertools.zip_longest()` if you need to handle unequal lengths.

---

### Exercise 6: Use Loop `else` Clause

```python
# else runs if the loop completes without break
for i in range(1, 4):
    if i == 5:
        print("Found 5!")
        break
else:
    print("5 not found in range 1-3.")  # This runs
```

The `else` clause on a loop runs when the loop finishes normally (without hitting `break`). It does not run if `break` was used to exit.

**Practical use — searching:**

```python
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found: {target}")
            break
    else:
        print(f"{target} not found.")

find_item([1, 2, 3], 2)  # Found: 2
find_item([1, 2, 3], 5)  # 5 not found.
```

This is cleaner than using a flag variable (`found = False`).

---

### Exercise 7: Build a Menu-Driven Program

```python
def show_menu():
    print("\n=== Menu ===")
    print("1. Say hello")
    print("2. Add two numbers")
    print("3. Check if number is even")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("What is your name? ")
            print(f"Hello, {name}!")

        elif choice == "2":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            print(f"{a} + {b} = {a + b}")

        elif choice == "3":
            n = int(input("Enter a number: "))
            if n % 2 == 0:
                print(f"{n} is even.")
            else:
                print(f"{n} is odd.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
```

**Why compare `choice` to strings like `"1"` instead of integers?** `input()` always returns a string. Comparing to `"1"` avoids a conversion step and a potential `ValueError`.

**Why `while True` with `break`?** The menu should keep showing until the user chooses to exit. The exit condition is inside the loop, not at the top.

---

## Challenge Exercise Solutions

### Challenge 1: Validate Input in a Loop

```python
def get_positive_integer(prompt):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("That is not a valid integer.")
```

This function combines three techniques:
1. `while True` to keep asking until valid input is received
2. `try/except` to handle non-integer input
3. A range check to ensure the value is positive

`return value` exits both the loop and the function at once. This is cleaner than setting a flag and breaking.

---

### Challenge 2: Find Patterns in Numbers

```python
# Find all prime numbers in a range
for n in range(2, 31):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
```

**Why check up to `sqrt(n)`?** If `n` has a factor larger than its square root, it must also have a factor smaller than its square root. So checking up to `sqrt(n)` is sufficient. This makes the algorithm much faster for large numbers.

**Why `break` after finding a factor?** Once we know `n` is not prime, there is no need to check more factors. `break` exits the inner loop immediately.

**Fibonacci sequence:**

```python
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
```

The simultaneous assignment `a, b = b, a + b` updates both variables at once. Python evaluates the right side completely before assigning, so `a + b` uses the old value of `a`.

---

### Challenge 3: Build a Guessing Game with Hints

```python
import random

def play_game():
    secret = random.randint(1, 100)
    guesses = 0
    max_guesses = 7

    print("I am thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} guesses.")

    while guesses < max_guesses:
        try:
            guess = int(input(f"\nGuess #{guesses + 1}: "))
            guesses += 1

            if guess < secret:
                difference = secret - guess
                if difference > 50:
                    print("Way too low!")
                else:
                    print("Too low.")
            elif guess > secret:
                difference = guess - secret
                if difference > 50:
                    print("Way too high!")
                else:
                    print("Too high.")
            else:
                print(f"Correct! You guessed it in {guesses} tries.")
                return True

        except ValueError:
            print("Please enter a valid integer.")
            guesses -= 1  # Don't count invalid input as a guess

    print(f"Game over! The number was {secret}.")
    return False
```

**Why `guesses -= 1` after a `ValueError`?** We increment `guesses` before checking the value. If the input is invalid, we undo the increment so the user does not lose a guess for a typo.

**Why return `True`/`False`?** Returning a value lets the caller know whether the player won. This makes the function reusable — you could call it in a loop to play multiple rounds and track wins.

---

### Challenge 4: Multiplication Table Generator

```python
def print_multiplication_table(size):
    """Print a multiplication table."""
    # Header row
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()

    # Separator line
    print("   " + "-" * (size * 4))

    # Data rows
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()  # newline at end of each row

size = int(input("Enter table size (1-12): "))
if 1 <= size <= 12:
    print_multiplication_table(size)
else:
    print("Size must be between 1 and 12.")
```

**Format specifier `{i:4}`:** This right-aligns the number in a field 4 characters wide. All numbers in the same column will be aligned regardless of how many digits they have.

**`print(..., end="")`:** By default, `print()` adds a newline at the end. `end=""` suppresses the newline so the next `print()` continues on the same line.

---

## Common Mistakes

**Infinite loop because the loop variable is never updated.** Always make sure the condition will eventually become `False`, or use `break` to exit.

**Off-by-one with `range()`.** `range(n)` gives `0` to `n-1`. `range(1, n+1)` gives `1` to `n`. Think carefully about which you need.

**`break` only exits the innermost loop.** If you have nested loops and need to exit both, use a flag variable or restructure the code.

**Forgetting `continue` skips the rest of the current iteration.** Code after `continue` in the same loop body does not run for that iteration.

**Using `=` instead of `==` in a condition.** `if x = 5:` is a syntax error in Python. Use `if x == 5:`.

---

## What to Review Next

- Chapter 09: Collections — lists, tuples, sets, and dictionaries
- Chapter 10: Functions — organizing code into reusable pieces
- Chapter 11: Comprehensions and Generators — a concise way to build collections with loops
