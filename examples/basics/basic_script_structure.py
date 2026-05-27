"""
Basic Script Structure - How to Organize Python Code

This example demonstrates:
- The if __name__ == "__main__" pattern
- Organizing code into functions
- Import statements at the top
- Module-level constants
"""

# Import statements (always at the top of the file)
import os
from pathlib import Path

# Module-level constants (uppercase by convention)
SCRIPT_DIR = Path(__file__).parent
APP_NAME = "Basic Script"
VERSION = "1.0.0"


def greet_user(name):
    """Greet the user by name."""
    return f"Hello, {name}!"


def calculate_square(number):
    """Return the square of a number."""
    return number * number


def get_user_info():
    """Get user information from input."""
    name = input("Enter your name: ")
    number = int(input("Enter a number: "))
    return name, number


def display_info(name, number):
    """Display user information."""
    square = calculate_square(number)
    print(greet_user(name))
    print(f"The square of {number} is {square}")


def main():
    """Main function - entry point for the script."""
    print(f"Welcome to {APP_NAME} v{VERSION}")
    print("-" * 40)
    
    # Get user input
    name, number = get_user_info()
    
    # Display information
    display_info(name, number)
    
    print("-" * 40)
    print("Script completed successfully!")


# This is the entry point of the script
# Code inside this block only runs when the file is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()

# Code outside the if block runs even when imported
# This is useful for initialization code
print(f"Script directory: {SCRIPT_DIR}")
print(f"Python version: {os.sys.version_info.major}.{os.sys.version_info.minor}")
