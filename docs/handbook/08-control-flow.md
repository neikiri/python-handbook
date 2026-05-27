# Chapter 08: Control Flow

## 1. Overview

Every program you write needs to make decisions and repeat actions. Without that
ability, code would run the same way every time, ignoring input, context, and
changing data. Control flow is the mechanism that lets your program choose
different paths and repeat work efficiently.

Python gives you a clean, readable set of tools for this:

- **Conditional statements** — run a block only when a condition is true.
- **`while` loops** — repeat a block as long as a condition holds.
- **`for` loops** — iterate over a sequence of values.

These three building blocks, combined with `break`, `continue`, `pass`, and a
handful of supporting builtins, cover the vast majority of real-world
programming needs.

---

## 2. What You Will Learn

- How to write `if`, `if/else`, and `if/elif/else` statements
- What truthiness means and which values Python treats as false
- How to nest conditionals and when to flatten them
- How to use the ternary expression for concise two-way choices
- How to use `match/case` for structural pattern matching (Python 3.10+)
- How to write `while` loops and avoid infinite loops
- How to write `for` loops over lists, strings, ranges, and other sequences
- How `range()` works in all three forms
- How `break` and `continue` control loop execution
- How the `else` clause on loops works — and when it is useful
- What `pass` does and where to use it
- How nested loops work
- How `enumerate()` and `zip()` simplify common loop patterns

---

## 3. Core Concepts

### 3.1 What Is Control Flow?

By default, Python executes statements from top to bottom, one line at a time.
Control flow changes that order. It lets you:

- **Branch**: run one block of code or another depending on a condition.
- **Loop**: run the same block multiple times.
- **Skip or exit early**: jump past code or leave a loop before it finishes.

Think of it like a flowchart: your program reaches a decision point, evaluates
a condition, and takes one path or another.

---

### 3.2 Truthiness and Falsy Values

Before writing conditionals, you need to understand how Python evaluates
conditions. Every value in Python is either **truthy** or **falsy** — Python
can treat any value as a boolean without an explicit comparison.

**Values that evaluate to `False`:**

| Value | Type |
|-------|------|
| `False` | bool |
| `0` | int |
| `0.0` | float |
| `0j` | complex |
| `""` | str (empty string) |
| `[]` | list (empty list) |
| `()` | tuple (empty tuple) |
| `{}` | dict (empty dict) |
| `set()` | set (empty set) |
| `None` | NoneType |

Everything else evaluates to `True`.

```python
# All of these evaluate as False
if 0:
    print("won't run")

if "":
    print("won't run")

if []:
    print("won't run")

if None:
    print("won't run")

# All of these evaluate as True
if 1:
    print("runs")        # runs

if "hello":
    print("runs")        # runs

if [0]:
    print("runs")        # runs — non-empty list, even if it contains 0
```

This lets you write cleaner conditions:

```python
name = input("Enter your name: ")

# Instead of: if len(name) > 0:
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")
```

---

### 3.3 The `if` Statement

The `if` statement runs a block of code only when a condition is `True`.

```python
if condition:
    # body — runs only if condition is True
```

The colon (`:`) at the end of the `if` line is required. The body must be
indented — Python uses indentation to define blocks, not curly braces.

```python
temperature = 35

if temperature > 30:
    print("It's hot outside.")
    print("Stay hydrated.")
```

Output:
```text
It's hot outside.
Stay hydrated.
```

If `temperature` were `25`, neither line would print.

---

### 3.4 `if/else`: Two-Way Branching

Add an `else` clause to handle the case when the condition is `False`.

```python
temperature = 18

if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not that hot today.")
```

Exactly one of the two blocks will always run.

---

### 3.5 `if/elif/else`: Multi-Way Branching

Use `elif` (short for "else if") to check multiple conditions in sequence.
Python evaluates them top to bottom and runs the first block whose condition
is `True`. The `else` block is optional and runs if none of the conditions match.

```python
score = 74

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")    # Grade: C
```

You can have as many `elif` branches as you need. Only the first matching
branch runs — the rest are skipped entirely.

---

### 3.6 Nested Conditionals

You can place an `if` statement inside another `if` block. This is called
nesting.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("Must be 18 or older.")
```

Nesting is fine for one or two levels, but deep nesting quickly becomes hard
to read. When you find yourself three or four levels deep, consider:

- Combining conditions with `and` / `or`
- Returning early from a function (the "guard clause" pattern)
- Extracting logic into a separate function

**Flattening with `and`:**

```python
# Nested version
if age >= 18:
    if has_id:
        print("Entry allowed.")

# Flat version — easier to read
if age >= 18 and has_id:
    print("Entry allowed.")
```

**Guard clause pattern** — return early instead of nesting:

```python
# Hard to read — three levels deep
def process_order(user, order):
    if user:
        if user.is_active:
            if order and order.is_valid:
                return order.total
    return 0

# Easier to read — early returns flatten the logic
def process_order(user, order):
    if not user:
        return 0
    if not user.is_active:
        return 0
    if not order or not order.is_valid:
        return 0
    return order.total
```

---

### 3.7 The Ternary Expression

Python has a one-line conditional expression for simple two-way choices:

```python
value_if_true if condition else value_if_false
```

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)    # adult
```

Use it when the logic is simple and the result fits naturally on one line.
Avoid it for complex conditions — a regular `if/else` is clearer.

```python
# Good use: simple, readable
label = "even" if number % 2 == 0 else "odd"

# Bad use: too complex for one line — split into if/else
result = "pass" if score >= 60 and attendance >= 0.8 and not cheated else "fail"
```

---

### 3.8 `match/case`: Structural Pattern Matching (Python 3.10+)

Python 3.10 introduced `match/case`, which lets you match a value against a
series of patterns. It is more powerful than a chain of `if/elif` because it
can match structure — not just equality.

```python
match subject:
    case pattern1:
        # runs if subject matches pattern1
    case pattern2:
        # runs if subject matches pattern2
    case _:
        # wildcard — runs if nothing else matched
```

#### Matching literals

```python
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Unknown day")
```

The `|` operator inside a case means "or".

#### Matching sequences

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On the x-axis at {x}")
    case (0, y):
        print(f"On the y-axis at {y}")    # prints: On the y-axis at 5
    case (x, y):
        print(f"Point at ({x}, {y})")
```

When a pattern contains a name like `x` or `y`, Python binds the matched
value to that name so you can use it in the case body.

#### Matching mappings (dicts)

```python
response = {"status": 200, "body": "OK"}

match response:
    case {"status": 200}:
        print("Success")
    case {"status": 404}:
        print("Not found")
    case {"status": 500}:
        print("Server error")
    case _:
        print("Unknown response")
```

Mapping patterns only require the listed keys to be present — extra keys are
ignored.

#### Guard clauses with `if`

Add a guard to a case to impose an extra condition:

```python
number = 42

match number:
    case n if n < 0:
        print("Negative")
    case 0:
        print("Zero")
    case n if n % 2 == 0:
        print(f"{n} is a positive even number")    # prints this
    case n:
        print(f"{n} is a positive odd number")
```

#### The wildcard `_`

The `_` pattern matches anything and does not bind a name. Use it as the
final catch-all, similar to `else`.

```python
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print(f"Unknown command: {command}")
```

---

### 3.9 The `while` Loop

A `while` loop repeats a block of code as long as a condition is `True`.

```python
while condition:
    # body — repeats while condition is True
```

```python
count = 1

while count <= 5:
    print(count)
    count += 1

# Output: 1  2  3  4  5
```

Each time the loop body runs, `count` increases by 1. When `count` reaches 6,
the condition `count <= 5` becomes `False` and the loop stops.

#### Infinite loops and how to avoid them

If the condition never becomes `False`, the loop runs forever. This is usually
a bug.

```python
# BUG: count never changes — loop runs forever
count = 1
while count <= 5:
    print(count)
    # forgot: count += 1
```

To stop an accidentally infinite loop in the terminal, press `Ctrl+C`.

The fix is always to ensure the loop variable is updated inside the body, or
to use `break` to exit when a condition is met.

#### `break`: exit the loop early

`break` immediately exits the loop, regardless of the condition.

```python
count = 1

while True:          # condition is always True
    print(count)
    count += 1
    if count > 5:
        break        # exit when count exceeds 5

# Output: 1  2  3  4  5
```

#### `continue`: skip to the next iteration

`continue` skips the rest of the current iteration and jumps back to the
condition check.

```python
count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue     # skip even numbers
    print(count)

# Output: 1  3  5  7  9
```

#### `else` clause on `while`

A `while` loop can have an `else` block. It runs when the loop condition
becomes `False` — but **not** if the loop was exited with `break`.

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1
    if password == "secret":
        print("Access granted.")
        break
else:
    print("Too many failed attempts. Account locked.")
```

The `else` block only runs if the user never entered the correct password
within the allowed attempts.

---

### 3.10 The `for` Loop

A `for` loop iterates over a sequence — a list, string, range, tuple, or any
other iterable — running the body once for each item.

```python
for variable in iterable:
    # body — runs once per item
```

#### Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

#### Iterating over a string

Strings are sequences of characters, so you can loop over them directly.

```python
for char in "Python":
    print(char, end=" ")

# Output: P y t h o n
```

#### Iterating over a tuple

```python
coordinates = (10, 20, 30)

for value in coordinates:
    print(value)
```

#### `break` and `continue` in `for` loops

`break` and `continue` work the same way in `for` loops as in `while` loops.

```python
# break: stop as soon as we find what we need
numbers = [3, 7, 2, 9, 4, 1]

for n in numbers:
    if n > 8:
        print(f"Found a large number: {n}")
        break

# Output: Found a large number: 9
```

```python
# continue: skip items that don't meet a condition
for i in range(1, 11):
    if i % 3 == 0:
        continue    # skip multiples of 3
    print(i, end=" ")

# Output: 1 2 4 5 7 8 10
```

#### `else` clause on `for`

Like `while`, a `for` loop can have an `else` block. It runs after the loop
finishes normally — but not if the loop was exited with `break`.

```python
names = ["Alice", "Bob", "Charlie"]
target = "Dave"

for name in names:
    if name == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} is not in the list.")

# Output: Dave is not in the list.
```

This pattern is useful for search operations where you want to know whether
the loop completed without finding a match.

---

### 3.11 `range()`: Generating Number Sequences

`range()` generates a sequence of integers. It is the most common way to
repeat something a fixed number of times or to iterate over indices.

**Three forms:**

```python
range(stop)               # 0, 1, 2, ..., stop-1
range(start, stop)        # start, start+1, ..., stop-1
range(start, stop, step)  # start, start+step, ..., up to (not including) stop
```

```python
# range(5) → 0, 1, 2, 3, 4
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4

# range(2, 6) → 2, 3, 4, 5
for i in range(2, 6):
    print(i, end=" ")
# Output: 2 3 4 5

# range(0, 10, 2) → 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8

# Counting down: range(5, 0, -1) → 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i, end=" ")
# Output: 5 4 3 2 1
```

`range()` does not create a list in memory — it generates values on demand,
which makes it efficient even for very large ranges.

```python
# This is fine — no list of a billion integers is created
for i in range(1_000_000_000):
    if i > 5:
        break
    print(i)
```

---

### 3.12 Nested Loops

You can place a `for` loop inside another `for` loop. The inner loop runs
completely for each iteration of the outer loop.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()    # newline after each row

# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)
```

A practical use — multiplication table:

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")
    print()

# Output:
#   1  2  3  4  5
#   2  4  6  8 10
#   3  6  9 12 15
#   4  8 12 16 20
#   5 10 15 20 25
```

Keep nesting to two levels when possible. Three or more levels usually signals
that the inner logic should be extracted into a function.

`break` inside a nested loop only exits the **innermost** loop. To exit
multiple levels at once, use a flag variable or restructure into a function
and use `return`.

```python
# Using a flag to break out of two loops
found = False
for row in range(5):
    for col in range(5):
        if row * col > 10:
            found = True
            break
    if found:
        break

print(f"Stopped at row={row}, col={col}")
```

---

### 3.13 `enumerate()`: Index and Value Together

When you need both the index and the value while iterating, use `enumerate()`.
It returns pairs of `(index, value)`.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

You can start the index at a number other than 0:

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. cherry
```

Avoid using `range(len(sequence))` just to get an index — `enumerate()` is
cleaner and less error-prone.

```python
# Avoid this pattern
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Prefer this
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

---

### 3.14 `zip()`: Iterating Over Multiple Sequences

`zip()` pairs up items from two or more iterables, stopping when the shortest
one runs out.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 88
# Bob: 92
# Charlie: 75
```

Combining `zip()` with `enumerate()`:

```python
for rank, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{rank}. {name} scored {score}")

# Output:
# 1. Alice scored 88
# 2. Bob scored 92
# 3. Charlie scored 75
```

If the iterables have different lengths, `zip()` stops at the shortest one.
Use `itertools.zip_longest()` from the standard library if you need to
continue to the end of the longest iterable.

---

### 3.15 `pass`: A Do-Nothing Statement

`pass` is a placeholder that does nothing. Use it when Python requires a
statement syntactically but you have nothing to put there yet.

```python
# Placeholder while you figure out the logic
for item in items:
    pass    # TODO: process item

# Empty branch — acknowledge the case but do nothing
if condition:
    pass    # handle this case later
else:
    print("Condition was false.")
```

`pass` is also used in empty class and function definitions, which you will
see in later chapters.

```python
def my_function():
    pass    # implementation coming later
```

---

### 3.16 Common Loop Patterns

These patterns appear constantly in real code. Recognizing them helps you
write loops quickly and correctly.

#### Accumulator pattern

Collect or combine values across iterations.

```python
numbers = [4, 7, 2, 9, 1]

total = 0
for n in numbers:
    total += n

print(total)    # 23
```

Start the accumulator at a neutral value: `0` for addition, `1` for
multiplication, `[]` for building a list.

#### Search pattern

Find the first item that meets a condition.

```python
emails = ["alice@example.com", "bob@example.com", "admin@example.com"]

found = None
for email in emails:
    if email.startswith("admin"):
        found = email
        break

if found:
    print(f"Admin email: {found}")
else:
    print("No admin email found.")
```

#### Counting pattern

Count how many items meet a condition.

```python
words = ["apple", "ant", "banana", "avocado", "cherry"]

count = 0
for word in words:
    if word.startswith("a"):
        count += 1

print(f"Words starting with 'a': {count}")    # 3
```

#### Building a list in a loop

Collect results into a new list. (Chapter 11 covers list comprehensions, which
are a more concise way to do this.)

```python
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)    # [1, 4, 9, 16, 25]
```

---

---

## 4. Practical Examples

### 4.1 Grade Classifier

Classify a student's score into a letter grade and a descriptive message.

```python
def classify_grade(score: int) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A — Excellent"
    elif score >= 80:
        return "B — Good"
    elif score >= 70:
        return "C — Satisfactory"
    elif score >= 60:
        return "D — Needs improvement"
    else:
        return "F — Failing"


scores = [95, 83, 71, 58, 42, 101]

for score in scores:
    print(f"{score:>3}: {classify_grade(score)}")

# Output:
#  95: A — Excellent
#  83: B — Good
#  71: C — Satisfactory
#  58: D — Needs improvement
#  42: F — Failing
# 101: Invalid score
```

---

### 4.2 Input Validation Loop

Keep asking the user for a number until they enter a valid one.

```python
while True:
    raw = input("Enter a number between 1 and 10: ")

    if not raw.isdigit():
        print("That's not a number. Try again.")
        continue

    number = int(raw)

    if 1 <= number <= 10:
        print(f"You entered: {number}")
        break
    else:
        print("Out of range. Try again.")
```

This is the standard input validation loop pattern:

1. Loop forever with `while True`.
2. Read input.
3. Validate it — use `continue` to restart if invalid.
4. Use `break` once the input is acceptable.

---

### 4.3 FizzBuzz

A classic exercise: print numbers 1 to 30, but replace multiples of 3 with
"Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".

```python
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Check `% 15` first. If you check `% 3` first, multiples of 15 would print
"Fizz" instead of "FizzBuzz".

---

### 4.4 Number Guessing Game

Combine a `while` loop, conditionals, and user input into a small interactive
program.

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100.")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts:
    raw = input("Your guess: ")

    if not raw.isdigit():
        print("Please enter a whole number.")
        continue

    guess = int(raw)
    attempts += 1

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"Correct! You got it in {attempts} attempt(s).")
        break
else:
    print(f"Out of attempts. The number was {secret}.")
```

This example uses `while` with a counter, `continue` to skip invalid input
without counting it as an attempt, `break` on a correct guess, and `else` on
the `while` loop to detect running out of attempts.

---

### 4.5 Word Frequency Counter

Count how many times each word appears in a sentence.

```python
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()

frequency: dict[str, int] = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in sorted(frequency.items()):
    print(f"{word}: {count}")

# Output:
# brown: 1
# dog: 1
# fox: 2
# jumps: 1
# lazy: 1
# over: 1
# quick: 1
# the: 3
```

---

### 4.6 Command Dispatcher with `match/case`

A simple command-line menu using structural pattern matching.

```python
def handle_command(command: str) -> None:
    match command.strip().lower().split():
        case ["quit"] | ["exit"]:
            print("Goodbye!")
        case ["hello", name]:
            print(f"Hello, {name}!")
        case ["add", *numbers]:
            total = sum(int(n) for n in numbers)
            print(f"Sum: {total}")
        case ["help"]:
            print("Commands: hello <name>, add <numbers...>, quit")
        case _:
            print(f"Unknown command: {command!r}")


handle_command("hello Alice")       # Hello, Alice!
handle_command("add 3 5 7")         # Sum: 15
handle_command("quit")              # Goodbye!
handle_command("fly to the moon")   # Unknown command: 'fly to the moon'
```

The `*numbers` syntax in a sequence pattern captures zero or more remaining
items into a list.

---

### 4.7 Finding Prime Numbers

Use a `for` loop with `break` and `else` to test primality.

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


limit = 50
primes = [n for n in range(2, limit + 1) if is_prime(n)]
print(primes)

# Output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

The loop checks divisors only up to the square root of `n` — if no divisor
is found there, the number is prime.

---

### 4.8 Student Rankings with `enumerate()` and `zip()`

Pair student names with their scores and rank them.

```python
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 92, 75, 95, 83]

# Sort by score descending, keeping names paired
ranked = sorted(zip(students, scores), key=lambda pair: pair[1], reverse=True)

print("Ranking:")
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"  {rank}. {name}: {score}")

# Output:
# Ranking:
#   1. Diana: 95
#   2. Bob: 92
#   3. Alice: 88
#   4. Eve: 83
#   5. Charlie: 75
```

---

### 4.9 Skipping Missing Data with `continue`

Process a list that contains `None` values, skipping them cleanly.

```python
readings = [23.1, None, 19.8, None, 21.4, 20.0, None, 22.7]

valid = []
for reading in readings:
    if reading is None:
        continue    # skip missing readings
    valid.append(reading)

average = sum(valid) / len(valid)
print(f"Valid readings: {valid}")
print(f"Average: {average:.2f}")

# Output:
# Valid readings: [23.1, 19.8, 21.4, 20.0, 22.7]
# Average: 21.40
```

---

### 4.10 Countdown Timer

Use `range()` with a negative step to count down.

```python
import time

def countdown(seconds: int) -> None:
    print(f"Counting down from {seconds}...")
    for remaining in range(seconds, 0, -1):
        print(f"  {remaining}...")
        time.sleep(1)
    print("Go!")


countdown(5)

# Output (one line per second):
# Counting down from 5...
#   5...
#   4...
#   3...
#   2...
#   1...
# Go!
```

---

### 4.11 Flattening a Nested List

Use nested loops to flatten a list of lists into a single list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

flat = []
for row in matrix:
    for value in row:
        flat.append(value)

print(flat)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### 4.12 Formatted Times Table

Use nested loops and f-string formatting to print a clean multiplication table.

```python
size = 10

# Header row
print("    ", end="")
for j in range(1, size + 1):
    print(f"{j:4}", end="")
print()
print("    " + "-" * (size * 4))

# Table rows
for i in range(1, size + 1):
    print(f"{i:3} |", end="")
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print()
```

Output (first three rows):
```text
       1   2   3   4   5   6   7   8   9  10
    ----------------------------------------
  1 |   1   2   3   4   5   6   7   8   9  10
  2 |   2   4   6   8  10  12  14  16  18  20
  3 |   3   6   9  12  15  18  21  24  27  30
```

---

---

## 5. Common Mistakes

### 5.1 Forgetting the Colon

Every `if`, `elif`, `else`, `while`, and `for` line must end with a colon.

```python
# Wrong — SyntaxError
if x > 0
    print("positive")

# Correct
if x > 0:
    print("positive")
```

---

### 5.2 Wrong Indentation

Python uses indentation to define blocks. Inconsistent indentation causes
`IndentationError` or, worse, silent logic bugs.

```python
# Wrong — IndentationError
if x > 0:
print("positive")    # not indented

# Wrong — logic bug: print always runs regardless of the condition
if x > 0:
    x = x * 2
print("positive")    # outside the if block — always executes

# Correct
if x > 0:
    x = x * 2
    print("positive")
```

Use 4 spaces per indentation level. Do not mix tabs and spaces.

---

### 5.3 Using `=` Instead of `==` in Conditions

`=` is assignment. `==` is comparison. Using `=` in a condition is a
`SyntaxError` in Python.

```python
# Wrong — SyntaxError
if x = 10:
    print("ten")

# Correct
if x == 10:
    print("ten")
```

---

### 5.4 Off-by-One Errors with `range()`

`range(n)` generates `0` through `n-1`, not `0` through `n`. The stop value
is always excluded.

```python
# Prints 0 to 4, not 0 to 5
for i in range(5):
    print(i)

# To include 5:
for i in range(6):
    print(i)

# To print 1 through 5:
for i in range(1, 6):
    print(i)
```

---

### 5.5 Modifying a List While Iterating Over It

Changing a list's size while looping over it leads to skipped items or
unexpected behavior.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Wrong — skips items because the list shrinks as you iterate
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)    # [1, 3, 5] — looks right but 4 and 6 were skipped

# Correct — iterate over a copy
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

# Or build a new list (clearest approach)
numbers = [n for n in numbers if n % 2 != 0]
```

---

### 5.6 Infinite Loop Due to Missing Update

The most common `while` loop bug: forgetting to update the variable that the
condition depends on.

```python
# Wrong — infinite loop
i = 0
while i < 5:
    print(i)
    # forgot: i += 1

# Correct
i = 0
while i < 5:
    print(i)
    i += 1
```

---

### 5.7 Using `is` Instead of `==` for Value Comparisons

Use `==` to compare values. Use `is` only to check identity — whether two
variables point to the exact same object in memory.

```python
x = 1000

# Wrong — may fail for large integers (implementation detail)
if x is 1000:
    print("one thousand")

# Correct
if x == 1000:
    print("one thousand")

# Correct use of `is`: checking for None
if value is None:
    print("no value")
```

Python caches small integers (-5 to 256) and some strings, so `is` may
accidentally return `True` for them — but this is an implementation detail
you should never rely on.

---

### 5.8 Misunderstanding `for/else` and `while/else`

The `else` block on a loop runs when the loop finishes normally — **not** when
`break` exits it. Beginners sometimes expect the opposite.

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed")    # does NOT run — break was used

for i in range(5):
    pass
else:
    print("Loop completed")    # DOES run — no break
```

---

### 5.9 Shadowing Built-in Names in Loops

Avoid using names like `list`, `str`, `input`, or `type` as loop variables —
they shadow Python's built-in functions for the rest of the scope.

```python
# Wrong — shadows the built-in list() function
for list in data:
    print(list)

# Correct — use a descriptive name
for item in data:
    print(item)
```

---

### 5.10 Using `range(len(...))` When `enumerate()` Is Cleaner

A very common beginner pattern that works but is less readable:

```python
fruits = ["apple", "banana", "cherry"]

# Avoid this
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Prefer this
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

The `enumerate()` version is shorter, avoids the index-out-of-range risk, and
makes the intent clearer.

---

### 5.11 Deeply Nested Conditionals

Deep nesting is hard to read and maintain. Flatten it using early returns,
combined conditions, or helper functions.

```python
# Hard to read — three levels deep
def process(user, order):
    if user:
        if user.is_active:
            if order:
                if order.is_valid:
                    return order.total
    return 0

# Easier to read — early returns
def process(user, order):
    if not user:
        return 0
    if not user.is_active:
        return 0
    if not order or not order.is_valid:
        return 0
    return order.total
```

---

---

## 6. Practice Tasks

Work through these tasks to solidify your understanding. Try to solve each one
before looking at the solution.

---

### Task 1: Even or Odd

Write a program that asks the user for a number and prints whether it is even
or odd.

**Requirements:**
- Use `input()` to get the number.
- Convert it to an integer.
- Use an `if/else` statement.
- Print `"X is even"` or `"X is odd"` where X is the number.

**Example output:**
```text
Enter a number: 7
7 is odd
```

---

### Task 2: Season Detector

Write a function `get_season(month: int) -> str` that returns the season for a
given month number (1–12).

- December, January, February → `"Winter"`
- March, April, May → `"Spring"`
- June, July, August → `"Summer"`
- September, October, November → `"Autumn"`
- Any other value → `"Invalid month"`

```python
print(get_season(3))    # Spring
print(get_season(12))   # Winter
print(get_season(0))    # Invalid month
```

---

### Task 3: Multiplication Table

Write a program that prints the multiplication table for a number entered by
the user.

**Requirements:**
- Ask the user for a number.
- Print the table from 1 to 12.
- Format each line as: `3 x  4 = 12`

**Example output (for 3):**
```text
3 x  1 =  3
3 x  2 =  6
3 x  3 =  9
3 x 12 = 36
```

---

### Task 4: Sum of Digits

Write a function `sum_of_digits(n: int) -> int` that returns the sum of the
digits of a positive integer.

```python
print(sum_of_digits(1234))    # 10
print(sum_of_digits(9))       # 9
print(sum_of_digits(100))     # 1
```

Hint: convert the number to a string and iterate over its characters.

---

### Task 5: Collatz Sequence

The Collatz conjecture: starting from any positive integer `n`, repeatedly
apply this rule:

- If `n` is even: `n = n // 2`
- If `n` is odd: `n = n * 3 + 1`

The sequence always reaches 1 (as far as anyone knows).

Write a function `collatz(n: int) -> list[int]` that returns the full sequence
from `n` down to 1.

```python
print(collatz(6))
# [6, 3, 10, 5, 16, 8, 4, 2, 1]
```

---

### Task 6: Password Strength Checker

Write a function `check_password(password: str) -> str` that rates a password
as `"weak"`, `"medium"`, or `"strong"`:

- Weak: fewer than 8 characters
- Medium: 8 or more characters, but missing at least one digit or uppercase letter
- Strong: 8 or more characters, contains at least one digit AND one uppercase letter

```python
print(check_password("abc"))          # weak
print(check_password("abcdefgh"))     # medium
print(check_password("Abcdefg1"))     # strong
```

---

### Task 7: Number Pyramid

Write a function `print_pyramid(n: int) -> None` that prints a number pyramid
of height `n`. For `n = 5`:

```text
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
```

---

### Task 8: Find the Longest Word

Write a function `longest_word(sentence: str) -> str` that returns the longest
word in a sentence. If there is a tie, return the first one.

```python
print(longest_word("the quick brown fox"))    # quick
print(longest_word("I love Python"))          # Python
```

---

### Task 9: Caesar Cipher

Write a function `caesar_encrypt(text: str, shift: int) -> str` that encrypts
a string by shifting each letter by `shift` positions in the alphabet.
Non-letter characters should remain unchanged. The shift should wrap around
(so shifting `'z'` by 1 gives `'a'`).

```python
print(caesar_encrypt("Hello, World!", 3))    # Khoor, Zruog!
print(caesar_encrypt("abc", 1))              # bcd
print(caesar_encrypt("xyz", 2))              # zab
```

Hint: use `ord()` and `chr()` to work with character codes.

---

### Task 10: Match Command Parser

Using `match/case`, write a function `parse_command(command: str) -> str` that
handles these commands:

- `"go north"`, `"go south"`, `"go east"`, `"go west"` → `"Moving <direction>"`
- `"pick up <item>"` → `"Picked up <item>"`
- `"drop <item>"` → `"Dropped <item>"`
- `"look"` → `"You look around."`
- Anything else → `"Unknown command"`

```python
print(parse_command("go north"))       # Moving north
print(parse_command("pick up sword"))  # Picked up sword
print(parse_command("look"))           # You look around.
print(parse_command("fly"))            # Unknown command
```

---

---

## 7. Key Takeaways

- **Control flow** lets your program make decisions (`if/elif/else`) and repeat
  actions (`while`, `for`). Without it, every program would do the same thing
  every time.

- **Indentation defines blocks** in Python. Every statement in a block must be
  indented consistently — 4 spaces is the standard. Mixing tabs and spaces
  causes errors.

- **Truthiness**: Python treats `0`, `""`, `[]`, `{}`, `set()`, `None`, and
  `False` as falsy. Everything else is truthy. Use this to write cleaner
  conditions like `if name:` instead of `if len(name) > 0:`.

- **`if/elif/else`** evaluates conditions top to bottom and runs only the first
  matching branch. The `else` is optional.

- **The ternary expression** `value_if_true if condition else value_if_false`
  is useful for simple two-way choices on a single line. Avoid it for complex
  logic.

- **`match/case`** (Python 3.10+) matches a value against patterns — literals,
  sequences, mappings, and more. Use `|` for "or" inside a case, and `_` as a
  wildcard catch-all. Guard clauses (`case n if n > 0`) add extra conditions.

- **`while` loops** repeat while a condition is `True`. Always ensure the
  condition will eventually become `False`, or use `break` to exit. The
  `while True` / `break` pattern is standard for input validation loops.

- **`for` loops** iterate over any iterable. Use `range()` to generate number
  sequences. `range(stop)`, `range(start, stop)`, and `range(start, stop, step)`
  cover all common cases. The stop value is always excluded.

- **`break`** exits a loop immediately. **`continue`** skips the rest of the
  current iteration and moves to the next one. Both work in `while` and `for`
  loops.

- **`else` on loops** runs after the loop finishes normally — it does not run
  if `break` was used. This is most useful for search patterns where you want
  to know whether the loop completed without finding a match.

- **`pass`** is a no-op placeholder. Use it when a block is syntactically
  required but you have nothing to put there yet.

- **Nested loops**: the inner loop runs completely for each iteration of the
  outer loop. `break` only exits the innermost loop. Keep nesting to two
  levels when possible.

- **`enumerate()`** gives you both the index and the value while iterating.
  Prefer it over `range(len(sequence))`.

- **`zip()`** pairs items from two or more sequences together, stopping at the
  shortest one. Combine it with `enumerate()` for ranked or indexed pairs.

- **Common loop patterns** — accumulator, search, counting, building a list —
  appear constantly in real code. Recognizing them makes writing loops faster.

- **Avoid deep nesting**. Flatten conditionals using early returns, combined
  conditions (`and`/`or`), or helper functions.

---

### What's Next

Chapter 09 covers **collections** — lists, tuples, dictionaries, and sets.
These are the data structures you will use in almost every Python program, and
they work hand-in-hand with the loops and conditionals you learned here.

---

*See also:*
- [Exercises for Chapter 08](../exercises/08-control-flow.md)
- [Solutions for Chapter 08](../solutions/08-control-flow.md)
- [Cheatsheet: Syntax](../cheatsheets/syntax.md)
