# Chapter 06: Operators, Expressions, and Input

## 1. Overview

Programs do useful work by computing things. To compute, you need operators — the
symbols that tell Python how to combine values. You also need a way to get data
from the person running your program, which is where the `input()` function comes
in. This chapter covers every operator category in Python, explains how Python
decides which operation to perform first (operator precedence), and shows you how
to build interactive programs that read and respond to user input.

---

## 2. What You Will Learn

- The difference between an expression and a statement
- All seven arithmetic operators and how integer division differs from float division
- How to use the modulo operator for practical tasks like checking even/odd numbers
- Comparison operators and how to chain them
- Logical operators (`and`, `or`, `not`) and short-circuit evaluation
- What "truthy" and "falsy" mean in Python
- Bitwise operators and when they appear in real code
- Assignment operators, including the walrus operator (`:=`)
- Identity operators (`is`, `is not`) and when to use them instead of `==`
- Membership operators (`in`, `not in`)
- Operator precedence — the rules Python uses to evaluate complex expressions
- The `input()` function and how to convert its output to numbers
- How to handle bad input gracefully with `try/except`
- Advanced `print()` parameters: `sep`, `end`, `file`, and `flush`

---

## 3. Core Concepts

### 3.1 Expressions vs. Statements

An **expression** is any piece of code that produces a value. Python evaluates it
and returns a result.

```python
3 + 4          # expression — evaluates to 7
len("hello")   # expression — evaluates to 5
x > 0          # expression — evaluates to True or False
```

A **statement** is an instruction that performs an action but does not itself
produce a value you can use directly.

```python
x = 10         # assignment statement
print("hi")    # expression statement (print returns None)
if x > 0:      # compound statement
    pass
```

The distinction matters because expressions can appear inside other expressions,
while statements cannot.

```python
# This works — expression inside a function call
print(3 + 4)

# This does not work — you cannot embed a statement inside an expression
# print(x = 10)   # SyntaxError
```

---

### 3.2 Arithmetic Operators

Python provides seven arithmetic operators.

| Operator | Name              | Example    | Result |
|----------|-------------------|------------|--------|
| `+`      | Addition          | `7 + 3`    | `10`   |
| `-`      | Subtraction       | `7 - 3`    | `4`    |
| `*`      | Multiplication    | `7 * 3`    | `21`   |
| `/`      | Float division    | `7 / 3`    | `2.333...` |
| `//`     | Integer division  | `7 // 3`   | `2`    |
| `%`      | Modulo (remainder)| `7 % 3`    | `1`    |
| `**`     | Exponentiation    | `2 ** 10`  | `1024` |


#### Float division vs. integer division

The `/` operator always returns a `float`, even when the result is a whole number.

```python
10 / 2    # 5.0  — float, not 5
7 / 2     # 3.5
```

The `//` operator performs **floor division**: it divides and then rounds down to
the nearest integer (toward negative infinity, not toward zero).

```python
7 // 2     # 3
-7 // 2    # -4  — rounds toward negative infinity, not toward zero
7.0 // 2   # 3.0 — result is float when either operand is float
```

Use `//` when you need a whole-number quotient — for example, converting a total
number of seconds into minutes.

```python
total_seconds = 137
minutes = total_seconds // 60   # 2
remaining = total_seconds % 60  # 17
print(f"{minutes}m {remaining}s")  # 2m 17s
```

#### Modulo operator

The `%` operator returns the **remainder** after division.

```python
10 % 3    # 1
15 % 5    # 0
7 % 2     # 1
```

Common use cases:

**Even/odd check:**

```python
number = 42
if number % 2 == 0:
    print("even")
else:
    print("odd")
```

**Wrapping a value within a range** (useful for cycling through a list):

```python
# Cycle through indices 0, 1, 2, 0, 1, 2, ...
index = 7
size = 3
wrapped = index % size   # 1
```

**Checking divisibility:**

```python
year = 2024
if year % 4 == 0:
    print("possibly a leap year")
```

#### Exponentiation

The `**` operator raises a number to a power.

```python
2 ** 8     # 256
3 ** 3     # 27
9 ** 0.5   # 3.0  — square root
2 ** -1    # 0.5  — negative exponent gives reciprocal
```

Python integers have arbitrary precision, so large exponents work without overflow.

```python
2 ** 100   # 1267650600228229401496703205376
```


#### Operator precedence (PEMDAS/BODMAS)

When an expression contains multiple operators, Python follows a specific order of
evaluation — the same rules you learned in math class, extended for programming.

From highest to lowest precedence:

| Priority | Operator(s)          | Description                        |
|----------|----------------------|------------------------------------|
| 1        | `()`                 | Parentheses (grouping)             |
| 2        | `**`                 | Exponentiation                     |
| 3        | `+x`, `-x`, `~x`    | Unary plus, minus, bitwise NOT     |
| 4        | `*`, `/`, `//`, `%`  | Multiplication, division, modulo   |
| 5        | `+`, `-`             | Addition, subtraction              |
| 6        | `<<`, `>>`           | Bitwise shifts                     |
| 7        | `&`                  | Bitwise AND                        |
| 8        | `^`                  | Bitwise XOR                        |
| 9        | `\|`                 | Bitwise OR                         |
| 10       | Comparisons          | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` |
| 11       | `not`                | Logical NOT                        |
| 12       | `and`                | Logical AND                        |
| 13       | `or`                 | Logical OR                         |

Operators at the same level are evaluated **left to right**, except `**` which is
evaluated **right to left**.

```python
2 + 3 * 4       # 14  — multiplication first
(2 + 3) * 4     # 20  — parentheses override
2 ** 3 ** 2     # 512 — right to left: 3**2=9, then 2**9=512
(2 ** 3) ** 2   # 64  — left to right with parentheses
```

When in doubt, use parentheses. They make intent clear and prevent bugs.

```python
# Ambiguous without parentheses
result = 10 - 2 * 3 + 1   # 5 (not 25)

# Clear with parentheses
result = (10 - 2) * (3 + 1)   # 32
```

---

### 3.3 Comparison Operators

Comparison operators compare two values and always return a `bool` (`True` or
`False`).

| Operator | Meaning                  | Example    | Result  |
|----------|--------------------------|------------|---------|
| `==`     | Equal to                 | `5 == 5`   | `True`  |
| `!=`     | Not equal to             | `5 != 3`   | `True`  |
| `<`      | Less than                | `3 < 5`    | `True`  |
| `>`      | Greater than             | `5 > 3`    | `True`  |
| `<=`     | Less than or equal to    | `5 <= 5`   | `True`  |
| `>=`     | Greater than or equal to | `6 >= 5`   | `True`  |

```python
age = 20
print(age >= 18)   # True
print(age == 21)   # False
print(age != 21)   # True
```

Comparisons work on strings too — Python compares them lexicographically
(alphabetical order based on Unicode code points).

```python
"apple" < "banana"   # True
"z" > "a"            # True
"abc" == "abc"        # True
```

#### Chained comparisons

Python allows you to chain comparisons in a natural, math-like way.

```python
x = 5
0 < x < 10       # True  — x is between 0 and 10 (exclusive)
1 <= x <= 10     # True
0 < x < 3        # False
```

This is equivalent to `0 < x and x < 10`, but more readable. Python evaluates
each pair in sequence and short-circuits if any pair is `False`.

```python
score = 75
if 60 <= score < 70:
    print("D")
elif 70 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
else:
    print("A or F")
```


---

### 3.4 Logical Operators

Logical operators combine boolean expressions.

| Operator | Description                              |
|----------|------------------------------------------|
| `and`    | `True` if both operands are truthy       |
| `or`     | `True` if at least one operand is truthy |
| `not`    | Inverts the boolean value                |

```python
True and True    # True
True and False   # False
False or True    # True
False or False   # False
not True         # False
not False        # True
```

In practice:

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

temperature = 35
if temperature < 0 or temperature > 40:
    print("Extreme temperature warning")

is_closed = False
if not is_closed:
    print("Store is open")
```

#### Short-circuit evaluation

Python does not evaluate the second operand if the first operand already
determines the result.

- `and`: if the left side is falsy, Python returns it immediately without
  evaluating the right side.
- `or`: if the left side is truthy, Python returns it immediately without
  evaluating the right side.

```python
# The division never happens because False short-circuits the and
result = False and (10 / 0)   # False — no ZeroDivisionError

# The division never happens because True short-circuits the or
result = True or (10 / 0)     # True — no ZeroDivisionError
```

This is useful for providing default values:

```python
name = ""
display_name = name or "Anonymous"   # "Anonymous" — name is falsy
print(display_name)

username = "alice"
display_name = username or "Anonymous"   # "alice" — username is truthy
print(display_name)
```

#### Truthiness and falsiness

Every Python value has a boolean interpretation. You can check it with `bool()`.

**Falsy values** — these evaluate to `False` in a boolean context:

```python
bool(0)       # False
bool(0.0)     # False
bool("")      # False  — empty string
bool([])      # False  — empty list
bool(())      # False  — empty tuple
bool({})      # False  — empty dict or set
bool(None)    # False
```

**Truthy values** — everything else evaluates to `True`:

```python
bool(1)          # True
bool(-1)         # True  — any non-zero number
bool("hello")    # True
bool([0])        # True  — non-empty list, even if it contains falsy items
bool(" ")        # True  — a space is not an empty string
```

You can use this directly in `if` statements without comparing to `True` or
`False` explicitly.

```python
items = []

# Verbose — works but unnecessary
if len(items) == 0:
    print("No items")

# Idiomatic Python
if not items:
    print("No items")
```

```python
user_input = input("Enter your name: ")

if user_input:
    print(f"Hello, {user_input}!")
else:
    print("You didn't enter a name.")
```


---

### 3.5 Bitwise Operators

Bitwise operators work on the individual binary bits of integers. They are less
common in everyday Python but appear in systems programming, networking, flags,
and performance-sensitive code.

| Operator | Name         | Example    | Result | Description                        |
|----------|--------------|------------|--------|------------------------------------|
| `&`      | AND          | `5 & 3`    | `1`    | Bit is 1 only if both bits are 1   |
| `\|`     | OR           | `5 \| 3`   | `7`    | Bit is 1 if either bit is 1        |
| `^`      | XOR          | `5 ^ 3`    | `6`    | Bit is 1 if bits differ            |
| `~`      | NOT          | `~5`       | `-6`   | Flips all bits                     |
| `<<`     | Left shift   | `1 << 3`   | `8`    | Shifts bits left (multiply by 2^n) |
| `>>`     | Right shift  | `8 >> 2`   | `2`    | Shifts bits right (divide by 2^n)  |

```python
# 5 in binary: 0101
# 3 in binary: 0011

5 & 3    # 0001 = 1
5 | 3    # 0111 = 7
5 ^ 3    # 0110 = 6
~5       # -(5+1) = -6
1 << 3   # 1000 = 8
8 >> 2   # 0010 = 2
```

**Common use cases:**

- **Permission flags**: combining read/write/execute bits in file systems
- **Checking if a number is even**: `n & 1 == 0` (faster than `n % 2 == 0` in
  some contexts, though Python optimizes both)
- **Fast powers of two**: `1 << n` gives `2 ** n`
- **Masking bits**: extracting specific bits from a value

```python
# Check if a number is even using bitwise AND
n = 42
if n & 1 == 0:
    print("even")

# Fast way to compute 2^10
print(1 << 10)   # 1024
```

You will not need bitwise operators for most beginner programs. They are included
here so you recognize them when you encounter them.

---

### 3.6 Assignment Operators

The basic assignment operator `=` binds a name to a value. Python also provides
**augmented assignment operators** that combine an operation with assignment.

| Operator | Equivalent to  | Example     | Result (if `x = 10`) |
|----------|----------------|-------------|----------------------|
| `=`      | —              | `x = 10`    | `x` is `10`          |
| `+=`     | `x = x + n`   | `x += 3`    | `x` is `13`          |
| `-=`     | `x = x - n`   | `x -= 3`    | `x` is `7`           |
| `*=`     | `x = x * n`   | `x *= 2`    | `x` is `20`          |
| `/=`     | `x = x / n`   | `x /= 4`    | `x` is `2.5`         |
| `//=`    | `x = x // n`  | `x //= 3`   | `x` is `3`           |
| `%=`     | `x = x % n`   | `x %= 3`    | `x` is `1`           |
| `**=`    | `x = x ** n`  | `x **= 2`   | `x` is `100`         |

```python
score = 0
score += 10    # player earns 10 points
score += 5     # earns 5 more
score -= 3     # loses 3
print(score)   # 12
```

Augmented assignment is not just shorthand — it can be more efficient for mutable
objects like lists because it may modify the object in place rather than creating
a new one.

#### The walrus operator `:=` (Python 3.8+)

The walrus operator (`:=`) is the **assignment expression** operator. It assigns a
value to a variable and returns that value, all in one expression. This lets you
assign and test a value in the same line.

```python
# Without walrus operator
line = input("Enter something: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter something: ")

# With walrus operator — cleaner, no repeated input() call
while (line := input("Enter something: ")) != "quit":
    print(f"You entered: {line}")
```

Another common use: avoid calling a function twice when you need both the result
and a check on it.

```python
import re

text = "Order number: 12345"

# Without walrus — calls re.search twice or uses a temp variable
match = re.search(r"\d+", text)
if match:
    print(match.group())

# With walrus — assigns and checks in one step
if match := re.search(r"\d+", text):
    print(match.group())   # 12345
```

The walrus operator is useful but not always necessary. Use it when it genuinely
reduces repetition and keeps the code readable. Avoid it when it makes the code
harder to follow.


---

### 3.7 Identity Operators

Identity operators test whether two variables refer to the **same object in
memory**, not just whether they have the same value.

| Operator  | Description                                  |
|-----------|----------------------------------------------|
| `is`      | `True` if both refer to the same object      |
| `is not`  | `True` if they refer to different objects    |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  — same value
print(a is b)    # False — different objects in memory
print(a is c)    # True  — c points to the same object as a
```

#### When to use `is` vs `==`

Use `is` only when you specifically want to check object identity:

- **Checking for `None`**: this is the standard Python idiom.

```python
result = None

# Correct — use is for None checks
if result is None:
    print("No result yet")

# Also correct
if result is not None:
    print(f"Result: {result}")

# Avoid — technically works but not idiomatic
if result == None:
    print("No result yet")
```

- **Checking for singleton objects** like `True` and `False` (though `if x:` is
  usually clearer).

Do not use `is` to compare integers, strings, or other values where you care
about equality, not identity. Python caches small integers (-5 to 256) and
interned strings, so `is` may return `True` for them — but this is an
implementation detail you should not rely on.

```python
x = 1000
y = 1000
print(x == y)   # True  — correct way to compare values
print(x is y)   # may be False — do not rely on this
```

---

### 3.8 Membership Operators

Membership operators test whether a value exists inside a sequence or collection.

| Operator   | Description                                  |
|------------|----------------------------------------------|
| `in`       | `True` if value is found in the sequence     |
| `not in`   | `True` if value is not found in the sequence |

**Strings:**

```python
"py" in "python"        # True
"java" in "python"      # False
"x" not in "python"     # True
```

**Lists:**

```python
fruits = ["apple", "banana", "cherry"]
"banana" in fruits      # True
"mango" in fruits       # False
"mango" not in fruits   # True
```

**Dictionaries** — `in` checks keys, not values:

```python
person = {"name": "Alice", "age": 30}
"name" in person        # True  — checks keys
"Alice" in person       # False — "Alice" is a value, not a key
"Alice" in person.values()   # True — explicitly check values
```

**Tuples and sets:**

```python
vowels = ("a", "e", "i", "o", "u")
"e" in vowels    # True

primes = {2, 3, 5, 7, 11}
4 in primes      # False
```

Membership testing on sets and dicts is O(1) (constant time), while on lists and
tuples it is O(n) (linear time). For large collections where you frequently check
membership, prefer sets or dicts.


---

### 3.9 The `input()` Function

`input()` pauses your program and waits for the user to type something and press
Enter. It always returns a **string**, regardless of what the user types.

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

When you run this, Python prints the prompt, waits, and stores whatever the user
typed as a string in `name`.

#### `input()` always returns a string

This is the most important thing to remember. Even if the user types `42`, you
get the string `"42"`, not the integer `42`.

```python
value = input("Enter a number: ")
print(type(value))   # <class 'str'>
print(value + 1)     # TypeError: can only concatenate str (not "int") to str
```

#### Converting input to numbers

Use `int()` or `float()` to convert the string to a number.

```python
age = int(input("Enter your age: "))
print(f"In 10 years you will be {age + 10}.")

price = float(input("Enter the price: "))
tax = price * 0.08
print(f"Total with tax: ${price + tax:.2f}")
```

You can nest the conversion directly inside the `input()` call, which is the
common pattern.

```python
# These two are equivalent
raw = input("Enter a number: ")
number = int(raw)

# Shorter — same result
number = int(input("Enter a number: "))
```

#### Handling bad input with `try/except`

If the user types something that cannot be converted — like `"hello"` when you
call `int()` — Python raises a `ValueError`. You can catch it with a
`try/except` block. (Error handling is covered in depth in Chapter 12; this is
just a preview.)

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("That doesn't look like a valid age.")
```

A more robust version that keeps asking until the user enters a valid number:

```python
while True:
    try:
        number = int(input("Enter a whole number: "))
        break   # exit the loop on success
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print(f"You entered: {number}")
```

#### The prompt string

The string you pass to `input()` is displayed before the cursor. It is optional,
but always include it so the user knows what to type.

```python
# With prompt — clear
name = input("Enter your name: ")

# Without prompt — confusing, cursor just blinks
name = input()
```

Convention: end your prompt with a space or `: ` so the user's input does not
run directly into the prompt text.

```python
# Good
city = input("Enter your city: ")

# Less readable — input runs into the colon
city = input("Enter your city:")
```


---

### 3.10 `print()` in Depth

You have been using `print()` since Chapter 1. It has several optional parameters
that give you more control over output formatting.

#### `sep` — separator between values

By default, `print()` separates multiple arguments with a single space. Use `sep`
to change this.

```python
print("Alice", "Bob", "Carol")              # Alice Bob Carol
print("Alice", "Bob", "Carol", sep=", ")    # Alice, Bob, Carol
print("Alice", "Bob", "Carol", sep=" | ")   # Alice | Bob | Carol
print("2024", "01", "15", sep="-")          # 2024-01-15
print("Alice", "Bob", "Carol", sep="")      # AliceBobCarol
```

#### `end` — what to print at the end

By default, `print()` adds a newline (`\n`) at the end. Use `end` to change this.

```python
print("Loading", end="")
print("...")                  # Loading...  (on the same line)

print("Step 1", end=" -> ")
print("Step 2", end=" -> ")
print("Step 3")               # Step 1 -> Step 2 -> Step 3
```

Combining `sep` and `end`:

```python
for i in range(1, 6):
    print(i, end=" ")
# Output: 1 2 3 4 5
```

#### `file` — redirect output

By default, `print()` writes to `sys.stdout` (the terminal). You can redirect it
to any file-like object, including actual files.

```python
import sys

# Print to stderr instead of stdout
print("Something went wrong", file=sys.stderr)

# Print to a file
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
    print("Second line", file=f)
```

#### `flush` — force immediate output

Python buffers output for performance. In most cases this is invisible, but when
you are printing progress updates in a loop, the output may not appear until the
buffer is flushed. Set `flush=True` to force immediate output.

```python
import time

for i in range(5):
    print(f"Processing step {i + 1}...", end="\r", flush=True)
    time.sleep(0.5)

print("Done!                  ")   # overwrite the last progress line
```

This is most useful in scripts that show real-time progress, or when writing to
files where you need data written immediately.

---

## 4. Practical Examples

### 4.1 Simple Calculator

```python
print("Simple Calculator")
print("------------------")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    print(f"\n{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")

    if b != 0:
        print(f"{a} / {b} = {a / b:.4f}")
        print(f"{a} // {b} = {a // b}")
        print(f"{a} % {b} = {a % b}")
    else:
        print("Division by zero is undefined.")

    print(f"{a} ** {b} = {a ** b}")
```

Sample output:

```text
Simple Calculator
------------------
Enter first number: 17
Enter second number: 5

17.0 + 5.0 = 22.0
17.0 - 5.0 = 12.0
17.0 * 5.0 = 85.0
17.0 / 5.0 = 3.4000
17.0 // 5.0 = 3.0
17.0 % 5.0 = 2.0
17.0 ** 5.0 = 1419857.0
```


### 4.2 Even/Odd Checker

```python
while True:
    try:
        n = int(input("Enter an integer (or 0 to quit): "))
    except ValueError:
        print("That's not an integer. Try again.")
        continue

    if n == 0:
        print("Goodbye!")
        break

    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")
```

### 4.3 Temperature Converter

```python
def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose (1 or 2): ").strip()

if choice == "1":
    try:
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.1f}°F")
    except ValueError:
        print("Invalid temperature.")
elif choice == "2":
    try:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.1f}°C")
    except ValueError:
        print("Invalid temperature.")
else:
    print("Invalid choice.")
```

### 4.4 Grade Classifier

```python
try:
    score = float(input("Enter your score (0–100): "))
except ValueError:
    print("Please enter a number.")
else:
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    if 0 <= score <= 100:
        print(f"Score: {score:.1f} — Grade: {grade}")
```

### 4.5 Walrus Operator in a Menu Loop

```python
menu = """
--- Menu ---
1. Say hello
2. Show date
3. Quit
"""

import datetime

while (choice := input(menu + "Choose: ").strip()) != "3":
    if choice == "1":
        name = input("Your name: ")
        print(f"Hello, {name}!")
    elif choice == "2":
        today = datetime.date.today()
        print(f"Today is {today}")
    else:
        print("Unknown option. Try 1, 2, or 3.")

print("Goodbye!")
```

### 4.6 Bitwise Flags Example

```python
# Permission flags — common pattern in systems programming
READ    = 0b001   # 1
WRITE   = 0b010   # 2
EXECUTE = 0b100   # 4

# Grant read and write permissions
permissions = READ | WRITE   # 0b011 = 3

# Check individual permissions
has_read    = bool(permissions & READ)     # True
has_write   = bool(permissions & WRITE)    # True
has_execute = bool(permissions & EXECUTE)  # False

print(f"Read: {has_read}, Write: {has_write}, Execute: {has_execute}")

# Add execute permission
permissions |= EXECUTE
print(f"After adding execute: {permissions:03b}")   # 111

# Remove write permission
permissions &= ~WRITE
print(f"After removing write: {permissions:03b}")   # 101
```


### 4.7 Interactive Tip Calculator

```python
print("=== Tip Calculator ===")

try:
    bill = float(input("Bill amount ($): "))
    tip_pct = float(input("Tip percentage (e.g. 18 for 18%): "))
    people = int(input("Number of people splitting the bill: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    if bill < 0 or tip_pct < 0 or people < 1:
        print("Invalid values. Bill and tip must be non-negative; people must be at least 1.")
    else:
        tip_amount = bill * (tip_pct / 100)
        total = bill + tip_amount
        per_person = total / people

        print(f"\nBill:        ${bill:.2f}")
        print(f"Tip ({tip_pct:.0f}%):   ${tip_amount:.2f}")
        print(f"Total:       ${total:.2f}")
        print(f"Per person:  ${per_person:.2f}")
```

Sample output:

```text
=== Tip Calculator ===
Bill amount ($): 85.50
Tip percentage (e.g. 18 for 18%): 20
Number of people splitting the bill: 3

Bill:        $85.50
Tip (20%):   $17.10
Total:       $102.60
Per person:  $34.20
```

### 4.8 Membership and Identity in Practice

```python
# Membership — checking allowed values
VALID_COLORS = {"red", "green", "blue", "yellow"}

color = input("Enter a color: ").lower().strip()
if color in VALID_COLORS:
    print(f"{color} is a valid color.")
else:
    print(f"{color} is not in the allowed list.")

# Identity — checking for None
def find_user(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob", 3: "Carol"}
    return users.get(user_id)   # returns None if not found

result = find_user(2)
if result is not None:
    print(f"Found user: {result}")
else:
    print("User not found.")
```

---

## 5. Common Mistakes

### 5.1 Using `=` instead of `==` in comparisons

```python
x = 5

# Wrong — this is assignment, not comparison
# if x = 5:   # SyntaxError in Python (unlike some other languages)

# Correct
if x == 5:
    print("x is 5")
```

Python raises a `SyntaxError` if you use `=` inside an `if` condition (unless
you use the walrus operator `:=`). This is a safety feature.

### 5.2 Forgetting that `input()` returns a string

```python
# Wrong — comparing a string to an integer
age = input("Enter your age: ")
if age > 18:   # TypeError: '>' not supported between instances of 'str' and 'int'
    print("Adult")

# Correct — convert first
age = int(input("Enter your age: "))
if age > 18:
    print("Adult")
```

### 5.3 Integer division surprises

```python
# Expecting 2.5, getting 2
result = 5 / 2    # 2.5  — this is fine with /
result = 5 // 2   # 2    — floor division truncates

# Negative floor division surprises
-7 // 2    # -4, not -3 — rounds toward negative infinity
```

### 5.4 Confusing `is` with `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]

# Wrong — checking identity when you want equality
if a is b:   # False — different objects
    print("same")

# Correct — checking value equality
if a == b:   # True — same contents
    print("same")
```

The only reliable use of `is` is with `None`, `True`, and `False`.

### 5.5 Operator precedence surprises

```python
# Intended: check if x is between 1 and 10
x = 5
result = 1 < x < 10    # True — chained comparison, works correctly

# Common mistake: mixing arithmetic and comparison without parentheses
result = 2 + 3 == 5    # True — but confusing to read
result = (2 + 3) == 5  # True — clearer

# Tricky precedence
result = not True == False   # True — parsed as not (True == False)
result = (not True) == False # True — same result here, but be explicit
```

### 5.6 Short-circuit side effects

```python
def check():
    print("check() was called")
    return True

# check() is never called because True short-circuits the or
result = True or check()   # check() not called

# check() is never called because False short-circuits the and
result = False and check()  # check() not called
```

This is usually what you want, but be aware that functions with side effects
(like printing or writing to a file) may not run if they are short-circuited.

### 5.7 Modulo with negative numbers

```python
# Python's modulo always returns a non-negative result when the divisor is positive
-7 % 3    # 2  — not -1 (Python follows mathematical modulo convention)
7 % -3    # -2 — sign follows the divisor
```

This differs from some other languages (like C or JavaScript) where `%` returns
a result with the sign of the dividend. Python's behavior is mathematically
consistent but can surprise programmers coming from other languages.


### 5.8 Mutable default and `or` for defaults

```python
# This works for strings and numbers
name = "" or "Anonymous"   # "Anonymous"

# But be careful with 0 — 0 is falsy
count = 0
display = count or 10   # 10 — probably not what you wanted if 0 is valid

# Better — use explicit None check
count = 0
display = count if count is not None else 10   # 0 — correct
```

### 5.9 Chained assignment vs. chained comparison

```python
# Chained assignment — assigns the same value to multiple variables
a = b = c = 0   # all three are 0

# Chained comparison — tests a range
x = 5
0 < x < 10   # True — this is a comparison, not assignment
```

These look similar but do completely different things.

---

## 6. Practice Tasks

These tasks are designed to be solved using only the concepts from this chapter.
Write your solutions in a Python file and run them from the terminal.

**Task 1 — Arithmetic practice**

Write a program that asks the user for two integers and prints:
- Their sum, difference, product
- The result of integer division and the remainder
- The first number raised to the power of the second

Handle the case where the user enters non-integer input.

**Task 2 — Even/odd and divisibility**

Ask the user for a number. Print:
- Whether it is even or odd
- Whether it is divisible by 3
- Whether it is divisible by both 2 and 3
- Whether it is divisible by 2 or 3 (but not necessarily both)

**Task 3 — Temperature range checker**

Ask the user for a temperature in Celsius. Use a chained comparison to classify
it as: freezing (below 0), cold (0–10), mild (10–20), warm (20–30), or hot
(above 30). Print the classification.

**Task 4 — Login simulator**

Define a correct username and password as variables. Ask the user to enter both.
Use `and` to check if both are correct. Print "Access granted" or "Access
denied". Do not use `==` more than twice.

**Task 5 — Truthiness explorer**

Write a program that asks the user for input and prints whether the value they
entered is truthy or falsy. Test it with: an empty string, a space, `0`, `1`,
and a word.

**Task 6 — Walrus operator loop**

Use the walrus operator to write a loop that keeps asking the user to enter a
positive number. The loop should stop when the user enters a number greater than
100. Print each number as it is entered, and print the total count at the end.

**Task 7 — Formatted output**

Ask the user for their first name, last name, and birth year. Print a formatted
summary using `print()` with `sep` and `end` parameters. The output should look
like:

```text
Name: Alice Smith | Birth year: 1995 | Age: 29
```

(Calculate the age from the current year using `datetime.date.today().year`.)

**Task 8 — Membership check**

Create a list of five cities. Ask the user to enter a city name. Use `in` to
check if it is in the list and print an appropriate message. Make the check
case-insensitive.

**Task 9 — Operator precedence puzzle**

Without running the code, predict the result of each expression. Then verify
your answers in the Python REPL.

```python
2 + 3 * 4
(2 + 3) * 4
2 ** 3 ** 2
10 - 4 - 2
not 5 > 3
True or False and False
```

**Task 10 — Interactive unit converter**

Build a program that converts between units. Support at least two conversions
(for example: kilometers to miles, kilograms to pounds). Show a menu, read the
user's choice, ask for the value, and print the result. Handle invalid input.

---

## 7. Key Takeaways

- An **expression** produces a value; a **statement** performs an action.
  Expressions can be nested inside other expressions.

- Python has seven arithmetic operators. `/` always returns a float; `//`
  performs floor division (rounds toward negative infinity). `%` returns the
  remainder. `**` raises to a power.

- **Operator precedence** follows PEMDAS/BODMAS rules. When in doubt, use
  parentheses to make your intent explicit.

- **Comparison operators** return `bool` values. Python supports chained
  comparisons like `0 < x < 10`, which are both readable and efficient.

- **Logical operators** (`and`, `or`, `not`) combine boolean expressions.
  Python uses **short-circuit evaluation**: it stops as soon as the result is
  determined. This can be used to provide default values with `or`.

- Every Python value is either **truthy** or **falsy**. Falsy values include
  `0`, `0.0`, `""`, `[]`, `{}`, `()`, and `None`. Everything else is truthy.
  Use this in `if` statements instead of comparing to `True` or `False`.

- **Bitwise operators** work on individual bits of integers. They appear in
  systems programming, flags, and performance-sensitive code.

- **Augmented assignment operators** (`+=`, `-=`, etc.) combine an operation
  with assignment. The **walrus operator** (`:=`) assigns and returns a value
  in a single expression, useful for avoiding repeated function calls.

- Use `is` and `is not` only for identity checks — primarily for `None`.
  Use `==` for value equality.

- **Membership operators** (`in`, `not in`) test whether a value exists in a
  sequence or collection. Checking membership in a set or dict is O(1);
  in a list or tuple it is O(n).

- `input()` **always returns a string**. Convert it with `int()` or `float()`
  before doing arithmetic. Wrap conversions in `try/except ValueError` to
  handle bad input gracefully.

- `print()` accepts `sep`, `end`, `file`, and `flush` parameters for fine-
  grained control over output formatting and destination.

---

### Further Reading

- [Expressions](https://docs.python.org/3/reference/expressions.html)
- [Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

### What's Next

Ready to continue? Head to the next chapter: **Strings**.

→ [Chapter 07 — Strings](07-strings.md)

*See also:*
- [Exercise](../exercises/06-operators-expressions-input.md)
- [Solution](../solutions/06-operators-expressions-input.md)
- [Cheatsheet](../cheatsheets/syntax.md)
