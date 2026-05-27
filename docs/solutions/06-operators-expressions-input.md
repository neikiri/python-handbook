# Solutions 06: Operators, Expressions, and Input

## Overview

Chapter 06 exercises cover arithmetic, comparison, and logical operators, operator precedence, the modulo operator, and reading user input safely. This solution guide explains the reasoning behind each exercise and highlights common pitfalls.

---

## Notes Before Checking Solutions

Operators are the building blocks of almost every Python expression. Understanding how they work — especially precedence and short-circuit evaluation — will save you from subtle bugs. The input-handling exercises are also important: real programs always need to deal with invalid user input.

---

## Warm-up Exercise Solutions

### Exercise 1: Explore Arithmetic Operators

```python
a = 10
b = 3

print(f"{a} + {b} = {a + b}")    # 13
print(f"{a} - {b} = {a - b}")    # 7
print(f"{a} * {b} = {a * b}")    # 30
print(f"{a} / {b} = {a / b}")    # 3.3333...
print(f"{a} // {b} = {a // b}")  # 3
print(f"{a} % {b} = {a % b}")    # 1
print(f"{a} ** {b} = {a ** b}")  # 1000
```

Key distinctions:
- `/` always returns a `float`, even when the result is a whole number: `10 / 2` gives `5.0`.
- `//` is floor division — it rounds down to the nearest integer: `10 // 3` gives `3`.
- `%` is the modulo operator — it returns the remainder: `10 % 3` gives `1`.
- `**` is exponentiation: `10 ** 3` gives `1000`.

**Negative numbers and floor division:**

```python
print(f"-{a} // {b} = {-a // b}")  # -4 (not -3!)
print(f"-{a} % {b} = {-a % b}")    # 2 (not -1!)
```

Python's `//` always rounds toward negative infinity, not toward zero. So `-10 // 3` is `-4` (not `-3`). The modulo result always has the same sign as the divisor. This is mathematically consistent but can surprise programmers coming from C or Java.

---

### Exercise 2: Understand Operator Precedence

```python
result1 = 2 + 3 * 4      # 14 (multiplication first)
result2 = (2 + 3) * 4    # 20 (parentheses first)
result3 = 10 - 2 * 3 + 4 # 8  (2*3=6, then 10-6+4=8)
result4 = 2 ** 3 ** 2    # 512 (right-associative: 3**2=9, then 2**9=512)
result5 = (2 ** 3) ** 2  # 64  (left-to-right: 2**3=8, then 8**2=64)
```

**Precedence order (highest to lowest, simplified):**
1. `()` — parentheses
2. `**` — exponentiation (right-associative)
3. `+x`, `-x` — unary plus/minus
4. `*`, `/`, `//`, `%` — multiplication and division
5. `+`, `-` — addition and subtraction
6. `==`, `!=`, `<`, `<=`, `>`, `>=` — comparisons
7. `not` — logical not
8. `and` — logical and
9. `or` — logical or

**Practical advice:** Do not memorize the full precedence table. Use parentheses to make the intended order explicit whenever there is any doubt. `(2 + 3) * 4` is clearer than relying on the reader knowing that `*` binds tighter than `+`.

---

### Exercise 3: Use Comparison Operators

```python
x = 10
y = 20

print(f"{x} == {y}: {x == y}")   # False
print(f"{x} != {y}: {x != y}")   # True
print(f"{x} < {y}: {x < y}")     # True
print(f"{x} <= {y}: {x <= y}")   # True
print(f"{x} > {y}: {x > y}")     # False
print(f"{x} >= {y}: {x >= y}")   # False

# Chained comparisons
a = 5
print(f"1 < {a} < 10: {1 < a < 10}")  # True
print(f"1 < {a} < 3: {1 < a < 3}")    # False
```

Python supports chained comparisons like `1 < a < 10`. This is equivalent to `1 < a and a < 10` but more readable. Most other languages do not support this syntax.

**String comparisons** use lexicographic (dictionary) order based on Unicode code points:

```python
s1 = "apple"
s2 = "banana"
print(f"'{s1}' < '{s2}': {s1 < s2}")  # True ('a' < 'b')
```

---

## Practice Exercise Solutions

### Exercise 4: Use Logical Operators

```python
x = 10
y = 20

print(f"x > 5 and y > 15: {x > 5 and y > 15}")   # True
print(f"x > 15 and y > 15: {x > 15 and y > 15}") # False
print(f"x > 15 or y > 15: {x > 15 or y > 15}")   # True
print(f"not (x > 15): {not (x > 15)}")             # True
```

**Short-circuit evaluation:**

`and` stops evaluating as soon as it finds a `False` value. `or` stops as soon as it finds a `True` value.

```python
def always_true():
    print("  always_true() called")
    return True

# False and ... — the second operand is never evaluated
result = False and always_true()
# "always_true() called" is NOT printed

# True or ... — the second operand is never evaluated
result = True or always_false()
# "always_false() called" is NOT printed
```

This matters in practice. You can write:

```python
if items and items[0] == "target":
    ...
```

If `items` is empty (falsy), Python never evaluates `items[0]`, so there is no `IndexError`. The short-circuit prevents the error.

---

### Exercise 5: Work with the Modulo Operator

```python
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0
```

The modulo operator has many practical uses:

**Check divisibility:** `n % k == 0` means `n` is divisible by `k`.

**Get the last digit:** `12345 % 10` gives `5`.

**Wrap around (like a clock):**

```python
hours = 25
wrapped = hours % 24  # 1 (25 o'clock wraps to 1 o'clock)
```

This pattern is useful for circular data structures, game boards, and any situation where values need to wrap around a fixed range.

**Alternate between two states:**

```python
for i in range(10):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
```

---

### Exercise 6: Use `input()` for Interactive Programs

```python
name = input("What is your name? ")
print(f"Hello, {name}!")

age_str = input("How old are you? ")
age = int(age_str)
print(f"In 10 years you will be {age + 10}.")
```

**Key points:**
- `input()` always returns a string, regardless of what the user types.
- You must convert the string to the appropriate type before doing arithmetic.
- If the user types something that cannot be converted (e.g., "hello" when you call `int()`), Python raises a `ValueError`.

**Combining input and conversion on one line:**

```python
age = int(input("How old are you? "))
```

This is fine for simple cases, but it makes error handling harder. For robust programs, keep the `input()` and conversion separate so you can catch the `ValueError`.

---

### Exercise 7: Handle Input Errors

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
            print("That is not a valid integer. Try again.")
```

**Why a `while True` loop?** The loop keeps asking until the user provides valid input. `return value` exits the loop and the function when valid input is received.

**Why `try/except`?** `int()` raises `ValueError` if the string cannot be converted. Catching it lets you print a helpful message and try again instead of crashing.

This pattern — a loop with `try/except` that keeps asking until valid input is received — is the standard way to validate user input in Python.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Simple Calculator

```python
def calculate(a, b, operation):
    """Perform a calculation based on the operation."""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    elif operation == '//':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a // b
    elif operation == '%':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a % b
    elif operation == '**':
        return a ** b
    else:
        return "Error: Unknown operation"
```

**Why check for zero before dividing?** Division by zero raises `ZeroDivisionError`. Checking explicitly lets you return a meaningful error message instead of crashing.

**Why use a function?** Separating the calculation logic from the input/output logic makes the code easier to test and reuse. You can call `calculate(10, 3, '+')` directly in tests without simulating user input.

---

### Challenge 2: Check Number Properties

```python
def analyze_number(n):
    """Analyze properties of a number."""
    print(f"\nAnalyzing {n}:")
    print(f"  Even: {n % 2 == 0}")
    print(f"  Odd: {n % 2 != 0}")
    print(f"  Positive: {n > 0}")
    print(f"  Negative: {n < 0}")
    print(f"  Zero: {n == 0}")

    if n > 0:
        # A perfect square has an integer square root
        root = int(n ** 0.5)
        print(f"  Perfect square: {root * root == n}")
        print(f"  Square root: {n ** 0.5:.2f}")
```

**Why `int(n ** 0.5) ** 2 == n` for perfect square check?** `n ** 0.5` computes the square root as a float. Taking `int()` truncates it to the nearest integer. If squaring that integer gives back `n`, then `n` is a perfect square. This avoids floating-point precision issues that can arise with `round()`.

---

### Challenge 3: Build a Guessing Game

```python
import random

def play_guessing_game():
    """Play a number guessing game."""
    secret = random.randint(1, 100)
    guesses = 0

    print("I am thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Guess the number: "))
            guesses += 1

            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {guesses} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    play_guessing_game()
```

**Why `random.randint(1, 100)`?** Unlike `range()`, `randint` is inclusive on both ends — it can return `1` or `100`.

**Why `guesses += 1` before the comparison?** We count the guess regardless of whether it is correct. If we only counted wrong guesses, the final message would be off by one.

**Why `break` instead of a condition in the `while`?** The loop needs to run at least once, and the exit condition (correct guess) is in the middle of the loop body. `while True` with `break` is the clearest way to express this.

---

### Challenge 4: Validate User Input

```python
def is_valid_email(email):
    """Check if an email looks valid (simple check)."""
    return "@" in email and "." in email

def is_valid_phone(phone):
    """Check if a phone number is valid (simple check)."""
    digits = phone.replace("-", "").replace(" ", "")
    return len(digits) == 10 and digits.isdigit()

def is_valid_password(password):
    """Check if a password is strong."""
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
    )
```

**Why `any(c.isupper() for c in password)`?** `any()` returns `True` if at least one element in the iterable is truthy. The generator expression `c.isupper() for c in password` produces `True` for each uppercase character. This is more readable than a loop with a flag variable.

**Note on email validation:** This is a simplified check. Real email validation is surprisingly complex — the full RFC 5321 specification covers many edge cases. For production code, use a library or a proper regex. For learning purposes, the simple check is fine.

---

## Common Mistakes

**Forgetting that `/` always returns a float.** `10 / 2` gives `5.0`, not `5`. Use `//` if you need an integer result.

**Confusing `=` (assignment) with `==` (comparison).** `if x = 5:` is a syntax error in Python (unlike C). Use `if x == 5:`.

**Not handling `ValueError` when converting input.** `int(input(...))` crashes if the user types anything that is not an integer. Always wrap input conversion in `try/except`.

**Relying on operator precedence instead of using parentheses.** `2 + 3 * 4` is `14`, not `20`. When in doubt, add parentheses.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 07 - Strings](../handbook/07-strings.md)
