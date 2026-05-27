# Chapter 08: Control Flow — Exercises

## Overview

These exercises help you master Python's control flow: conditionals, loops, and flow control statements. By the end, you will confidently write programs that make decisions and repeat actions.

---

## How to Use These Exercises

- Create a folder called `chapter-08` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and test with different inputs.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Write Simple Conditionals

Create a file called `conditionals.py`:

```python
# Simple if
age = 18
if age >= 18:
    print("You are an adult.")

# if/else
score = 75
if score >= 70:
    print("You passed!")
else:
    print("You failed.")

# if/elif/else
grade_points = 85
if grade_points >= 90:
    grade = "A"
elif grade_points >= 80:
    grade = "B"
elif grade_points >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# Nested conditionals
temperature = 25
if temperature > 20:
    if temperature > 30:
        print("It is hot!")
    else:
        print("It is warm.")
else:
    print("It is cold.")
```

Run it and observe the output.

---

### Exercise 2: Understand Truthiness

Create a file called `truthiness.py`:

```python
# Falsy values
if 0:
    print("0 is truthy")
else:
    print("0 is falsy")

if "":
    print("Empty string is truthy")
else:
    print("Empty string is falsy")

if []:
    print("Empty list is truthy")
else:
    print("Empty list is falsy")

if None:
    print("None is truthy")
else:
    print("None is falsy")

# Truthy values
if 1:
    print("1 is truthy")

if "hello":
    print("Non-empty string is truthy")

if [1, 2, 3]:
    print("Non-empty list is truthy")

# Using truthiness directly
name = input("Enter your name (or press Enter to skip): ")
if name:
    print(f"Hello, {name}!")
else:
    print("You did not enter a name.")
```

Run it and test with different inputs.

---

### Exercise 3: Use `while` Loops

Create a file called `while_loops.py`:

```python
# Simple while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Loop with user input
print("\nGuessing game:")
secret = 42
guess = None
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")

# Loop with break
print("\nLoop with break:")
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print(f"You entered: {user_input}")

# Loop with continue
print("\nLoop with continue:")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(f"Odd number: {count}")
```

Run it and test the different loop patterns.

---

### Exercise 4: Use `for` Loops

Create a file called `for_loops.py`:

```python
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")

# Loop over a string
word = "Python"
for letter in word:
    print(letter)

# Loop with range
print("\nCounting:")
for i in range(5):
    print(i)

# Range with start and stop
print("\nRange 2 to 7:")
for i in range(2, 8):
    print(i)

# Range with step
print("\nEvens from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# Nested loops
print("\nMultiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
```

Run it and observe the output.

---

## Practice Exercises

### Exercise 5: Use `enumerate()` and `zip()`

Create a file called `enumerate_zip.py`:

```python
# enumerate() — get index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate() with start parameter
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# zip() — combine two lists
names = ["Alice", "Bob", "Carol"]
ages = [30, 25, 28]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# zip() with three lists
cities = ["New York", "Los Angeles", "Chicago"]
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")
```

Run it and observe the output.

---

### Exercise 6: Use Loop `else` Clause

Create a file called `loop_else.py`:

```python
# for/else — else runs if loop completes normally
print("Searching for 5:")
for i in range(1, 4):
    if i == 5:
        print("Found 5!")
        break
else:
    print("5 not found in range 1-3.")

# for/else — else does not run if break is used
print("\nSearching for 2:")
for i in range(1, 4):
    if i == 2:
        print("Found 2!")
        break
else:
    print("2 not found.")

# while/else
print("\nCounting down:")
count = 3
while count > 0:
    print(count)
    count -= 1
else:
    print("Blast off!")
```

Run it and observe when the `else` clause runs.

---

### Exercise 7: Build a Menu-Driven Program

Create a file called `menu.py`:

```python
def show_menu():
    """Display the menu."""
    print("\n=== Menu ===")
    print("1. Say hello")
    print("2. Add two numbers")
    print("3. Check if number is even")
    print("4. Exit")

def main():
    """Main program loop."""
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

Run it and test the menu.

---

## Challenge Exercises

### Challenge 1: Validate Input in a Loop

Create a file called `input_validation.py`:

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

def get_choice(prompt, valid_choices):
    """Get a valid choice from the user."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print(f"Please enter one of: {', '.join(valid_choices)}")

# Use the validators
age = get_positive_integer("Enter your age: ")
print(f"You are {age} years old.")

choice = get_choice("Do you like Python? (yes/no): ", ['yes', 'no'])
print(f"You answered: {choice}")
```

Run it and test with invalid inputs.

---

### Challenge 2: Find Patterns in Numbers

Create a file called `number_patterns.py`:

```python
# Find all even numbers in a range
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Find all prime numbers in a range
print("\nPrime numbers from 1 to 30:")
for n in range(2, 31):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
print()

# Find factors of a number
number = 24
print(f"\nFactors of {number}:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print()

# Fibonacci sequence
print("\nFibonacci sequence (first 10):")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
```

Run it and observe the patterns.

---

### Challenge 3: Build a Guessing Game with Hints

Create a file called `guessing_game.py`:

```python
import random

def play_game():
    """Play a number guessing game with hints."""
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
            guesses -= 1
    
    print(f"Game over! The number was {secret}.")
    return False

if __name__ == "__main__":
    play_game()
```

Run it and play the game.

---

### Challenge 4: Create a Multiplication Table Generator

Create a file called `multiplication_table.py`:

```python
def print_multiplication_table(size):
    """Print a multiplication table."""
    # Header
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    
    # Separator
    print("   " + "-" * (size * 4))
    
    # Rows
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()

# Get size from user
size = int(input("Enter table size (1-12): "))
if 1 <= size <= 12:
    print_multiplication_table(size)
else:
    print("Size must be between 1 and 12.")
```

Run it and generate tables of different sizes.

---

## Hints

**Infinite loop** → Make sure your loop condition will eventually become False, or use `break` to exit.

**Off-by-one error** → Remember that `range(n)` goes from 0 to n-1, not 0 to n.

**Unexpected indentation** → Make sure the loop body is indented. Python uses indentation to define the loop body.

**`break` not working** → `break` only exits the innermost loop. Use a flag variable or restructure the code if you need to exit an outer loop.

---

## What to Review If You Get Stuck

- **Truthiness** → Handbook section 3.2
- **if/elif/else statements** → Handbook section 3.3
- **Nested conditionals** → Handbook section 3.4
- **Ternary expressions** → Handbook section 3.5
- **while loops** → Handbook section 3.6
- **for loops** → Handbook section 3.7
- **range()** → Handbook section 3.8
- **break and continue** → Handbook section 3.9
- **Loop else clause** → Handbook section 3.10
- **enumerate() and zip()** → Handbook section 3.11

---

## Key Takeaways

After completing these exercises, you should be able to:

- Write conditional statements with if/elif/else
- Understand truthiness and falsy values
- Use while and for loops effectively
- Use break and continue to control loops
- Use enumerate() and zip() for common patterns
- Build interactive, menu-driven programs
- Validate user input in loops
- Solve problems using loops and conditionals
