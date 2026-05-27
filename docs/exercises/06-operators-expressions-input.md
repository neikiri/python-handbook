# Chapter 06: Operators, Expressions, and Input — Exercises

## Overview

These exercises help you master Python's operators, understand how expressions are evaluated, and learn to build interactive programs that read user input. By the end, you will confidently use all operator types and handle user input safely.

---

## How to Use These Exercises

- Create a folder called `chapter-06` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and test with different inputs.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Explore Arithmetic Operators

Create a file called `arithmetic.py`:

```python
# Test all arithmetic operators
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Test with negative numbers
print(f"\n-{a} // {b} = {-a // b}")
print(f"-{a} % {b} = {-a % b}")
```

Run it and observe the difference between `/` and `//`, and how `%` works with negative numbers.

---

### Exercise 2: Understand Operator Precedence

Create a file called `precedence.py`:

```python
# Without parentheses — relies on precedence
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # 14, not 20

# With parentheses — explicit order
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # 20

# More complex
result3 = 10 - 2 * 3 + 4
print(f"10 - 2 * 3 + 4 = {result3}")  # 8

result4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result4}")  # 512 (right-associative)

result5 = (2 ** 3) ** 2
print(f"(2 ** 3) ** 2 = {result5}")  # 64
```

Run it and observe how precedence affects the result.

---

### Exercise 3: Use Comparison Operators

Create a file called `comparisons.py`:

```python
x = 10
y = 20

print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} <= {y}: {x <= y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} >= {y}: {x >= y}")

# Chained comparisons
a = 5
print(f"\n1 < {a} < 10: {1 < a < 10}")
print(f"1 < {a} < 3: {1 < a < 3}")

# Comparing strings
s1 = "apple"
s2 = "banana"
print(f"\n'{s1}' < '{s2}': {s1 < s2}")
```

Run it and observe how comparisons work with different types.

---

## Practice Exercises

### Exercise 4: Use Logical Operators

Create a file called `logical.py`:

```python
# and, or, not
x = 10
y = 20

print(f"x > 5 and y > 15: {x > 5 and y > 15}")
print(f"x > 15 and y > 15: {x > 15 and y > 15}")
print(f"x > 15 or y > 15: {x > 15 or y > 15}")
print(f"not (x > 15): {not (x > 15)}")

# Short-circuit evaluation
def always_true():
    print("  always_true() called")
    return True

def always_false():
    print("  always_false() called")
    return False

print("\nShort-circuit with and:")
print("True and always_true():")
result = True and always_true()

print("False and always_true():")
result = False and always_true()

print("\nShort-circuit with or:")
print("True or always_false():")
result = True or always_false()

print("False or always_false():")
result = False or always_false()
```

Run it and observe short-circuit evaluation in action.

---

### Exercise 5: Work with the Modulo Operator

Create a file called `modulo.py`:

```python
# Check if a number is even or odd
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

for i in range(1, 11):
    if is_even(i):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# Check divisibility
print("\nDivisibility:")
print(f"15 % 3 = {15 % 3} (15 is divisible by 3)")
print(f"16 % 3 = {16 % 3} (16 is not divisible by 3)")

# Get the last digit
number = 12345
last_digit = number % 10
print(f"\nLast digit of {number}: {last_digit}")

# Wrap around (like a clock)
hours = 25
wrapped = hours % 24
print(f"\n{hours} hours = {wrapped} hours (on a 24-hour clock)")
```

Run it and observe practical uses of the modulo operator.

---

### Exercise 6: Use `input()` for Interactive Programs

Create a file called `interactive.py`:

```python
# Simple input
name = input("What is your name? ")
print(f"Hello, {name}!")

# Input and conversion
age_str = input("How old are you? ")
age = int(age_str)
print(f"In 10 years you will be {age + 10}.")

# Multiple inputs
print("\nEnter two numbers:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"\nResults:")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
```

Run it and test with different inputs.

---

### Exercise 7: Handle Input Errors

Create a file called `safe_input.py`:

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

def get_choice(prompt, options):
    """Get a choice from the user."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        else:
            print(f"Please enter one of: {', '.join(options)}")

# Use the functions
age = get_positive_integer("Enter your age: ")
print(f"You are {age} years old.")

choice = get_choice("Do you like Python? (yes/no): ", ['yes', 'no'])
print(f"You answered: {choice}")
```

Run it and test with invalid inputs to see error handling.

---

## Challenge Exercises

### Challenge 1: Build a Simple Calculator

Create a file called `calculator.py`:

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

# Interactive calculator
print("Simple Calculator")
print("Operations: +, -, *, /, //, %, **")

num1 = float(input("Enter first number: "))
op = input("Enter operation: ")
num2 = float(input("Enter second number: "))

result = calculate(num1, num2, op)
print(f"\n{num1} {op} {num2} = {result}")
```

Run it and test various operations.

---

### Challenge 2: Check Number Properties

Create a file called `number_properties.py`:

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
        print(f"  Perfect square: {int(n ** 0.5) ** 2 == n}")
        print(f"  Square root: {n ** 0.5:.2f}")

# Test with different numbers
for num in [-5, 0, 1, 4, 9, 16, 25, 100]:
    analyze_number(num)
```

Run it and observe the properties of different numbers.

---

### Challenge 3: Build a Guessing Game

Create a file called `guessing_game.py`:

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

Run it and play the game.

---

### Challenge 4: Validate User Input

Create a file called `validator.py`:

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

# Test validators
print("Email validation:")
email = input("Enter an email: ")
print(f"Valid: {is_valid_email(email)}")

print("\nPhone validation:")
phone = input("Enter a phone number: ")
print(f"Valid: {is_valid_phone(phone)}")

print("\nPassword validation:")
password = input("Enter a password: ")
print(f"Valid: {is_valid_password(password)}")
```

Run it and test with various inputs.

---

## Hints

**ValueError when converting input** → The user entered something that cannot be converted to the target type. Use try/except to handle it.

**Unexpected operator precedence** → Use parentheses to make the order explicit. Do not rely on memorizing precedence.

**Short-circuit evaluation confusing** → Remember: `and` stops at the first False, `or` stops at the first True.

**Modulo with negative numbers** → Python's modulo always returns a result with the same sign as the divisor.

---

## What to Review If You Get Stuck

- **Arithmetic operators** → Handbook section 3.2
- **Comparison operators** → Handbook section 3.3 (in Chapter 06)
- **Logical operators** → Handbook section 3.4 (in Chapter 06)
- **Operator precedence** → Handbook section 3.8 (in Chapter 06)
- **The `input()` function** → Handbook section 3.9 (in Chapter 06)
- **Advanced `print()` parameters** → Handbook section 3.10 (in Chapter 06)

---

## Key Takeaways

After completing these exercises, you should be able to:

- Use all arithmetic, comparison, and logical operators
- Understand operator precedence and use parentheses when needed
- Build interactive programs with `input()`
- Convert and validate user input safely
- Handle errors gracefully
- Use operators to solve practical problems
