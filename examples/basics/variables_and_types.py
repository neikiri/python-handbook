"""
Variables and Types - Basic Python Examples

This example demonstrates:
- Creating variables with different built-in types
- Checking types with type() and isinstance()
- Variable naming conventions
"""

# Integer (whole number)
age = 25
year = 2024

# Float (decimal number)
height = 5.9
weight = 165.5

# String (text)
name = "Alice"
greeting = "Hello, world!"

# Boolean (True or False)
is_student = True
has_license = False

# NoneType (represents no value)
middle_name = None


def print_variable_info():
    """Print information about our variables."""
    print("=== Variables and Types ===")
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is student: {is_student} (type: {type(is_student).__name__})")
    print(f"Middle name: {middle_name} (type: {type(middle_name).__name__})")
    print()


def check_types():
    """Demonstrate type checking with isinstance()."""
    print("=== Type Checking ===")
    
    # isinstance() checks if a value is of a specific type
    print(f"Is 'name' a string? {isinstance(name, str)}")
    print(f"Is 'age' an integer? {isinstance(age, int)}")
    print(f"Is 'height' a float? {isinstance(height, float)}")
    print(f"Is 'is_student' a boolean? {isinstance(is_student, bool)}")
    print()
    
    # Type checking in conditionals
    if isinstance(age, int):
        print(f"Age is an integer: {age}")
    
    if not middle_name:
        print("No middle name provided")
    print()


def variable_naming():
    """Show valid variable naming conventions."""
    print("=== Variable Naming ===")
    
    # snake_case (recommended for variables)
    user_name = "Bob"
    total_count = 100
    
    # ALL_CAPS for constants
    MAX_SIZE = 1000
    PI_VALUE = 3.14159
    
    # Descriptive names are better than single letters
    # Bad: x = 5
    # Good: page_limit = 5
    
    print(f"User name: {user_name}")
    print(f"Max size: {MAX_SIZE}")
    print()


if __name__ == "__main__":
    print_variable_info()
    check_types()
    variable_naming()
