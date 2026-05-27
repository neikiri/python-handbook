"""
Input and Output - Getting User Input and Displaying Output

This example demonstrates:
- Using input() to get user input
- Using print() to display output
- f-strings for formatted output
- Basic input validation
"""

print("=== Getting User Input ===")

# input() always returns a string
name = input("Enter your name: ")
print(f"Hello, {name}!")
print()

# Convert input to number
age_input = input("Enter your age: ")
age = int(age_input)  # Convert string to int
print(f"You are {age} years old.")
print()

# Example with float
height_input = input("Enter your height in feet: ")
height = float(height_input)
print(f"You are {height} feet tall.")
print()

print("=== print() Function ===")

# Basic print
print("Hello, world!")

# Print multiple values (separated by space by default)
print("Name:", name, "Age:", age)

# Custom separator
print("Name:", name, "Age:", age, sep=" | ")
print()

# Custom end character (default is newline)
print("This is on one line.", end=" ")
print("This is on the same line.")
print()

# Print to a file (for now, just show the concept)
# with open("output.txt", "w") as f:
#     print("Hello from file!", file=f)
print()

print("=== f-Strings (Formatted String Literals) ===")

# Basic f-string
print(f"My name is {name}")

# Expression inside f-string
print(f"In 10 years, you will be {age + 10}")

# Formatting numbers
pi = 3.14159265
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi to 4 decimal places: {pi:.4f}")
print()

# Aligning text
print(f"{'Left aligned':<20} | {'Center':^10} | {'Right aligned':>20}")
print(f"{'Name':<20} | {'Age':^10} | {'Height':>20}")
print(f"{name:<20} | {age:^10} | {height:>20.1f}")
print()

print("=== Input Validation Example ===")

def get_valid_number(prompt, type_=int):
    """Get a valid number from user input."""
    while True:
        try:
            value = type_(input(prompt))
            return value
        except ValueError:
            print(f"Please enter a valid {type_.__name__}.")

# Example usage
try:
    number = get_valid_number("Enter a number: ")
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

print()
print("=== Simple Interactive Program ===")

def simple_chat():
    """A very simple chat program."""
    print("\n--- Simple Chat ---")
    
    user_name = input("What's your name? ")
    user_age = get_valid_number("How old are you? ")
    
    print(f"\nNice to meet you, {user_name}!")
    print(f"In 5 years, you'll be {user_age + 5}.")
    print("Chat complete!")

# Uncomment to run the chat:
# simple_chat()
