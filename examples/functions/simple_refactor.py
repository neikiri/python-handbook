"""
Simple Refactor - Turning Repeated Code into Functions

This example demonstrates:
- Identifying repeated code patterns
- Creating functions to eliminate duplication
- Making code more maintainable
"""

print("=== Before Refactoring (Repeated Code) ===")

# We have repeated code for calculating discounts
# This is hard to maintain - if discount logic changes, we must update everywhere

# Customer 1
customer1_name = "Alice"
customer1_total = 150
customer1_discount = customer1_total * 0.10  # 10% discount
customer1_final = customer1_total - customer1_discount
print(f"{customer1_name}: ${customer1_final:.2f}")

# Customer 2
customer2_name = "Bob"
customer2_total = 200
customer2_discount = customer2_total * 0.10  # 10% discount
customer2_final = customer2_total - customer2_discount
print(f"{customer2_name}: ${customer2_final:.2f}")

# Customer 3
customer3_name = "Charlie"
customer3_total = 75
customer3_discount = customer3_total * 0.10  # 10% discount
customer3_final = customer3_total - customer3_discount
print(f"{customer3_name}: ${customer3_final:.2f}")
print()

print("=== After Refactoring (Using Function) ===")


def calculate_final_price(name: str, total: float, discount_rate: float = 0.10) -> None:
    """Calculate and print the final price for a customer."""
    discount = total * discount_rate
    final = total - discount
    print(f"{name}: ${final:.2f}")


# Now we can call the function for each customer
calculate_final_price("Alice", 150)
calculate_final_price("Bob", 200)
calculate_final_price("Charlie", 75)
print()

print("=== More Complex Example: Data Processing ===")

print("=== Before: Repeated data cleaning code ===")

# Process user 1
user1_name = "  ALICE  "
user1_email = "alice@EXAMPLE.com"
user1_age = "30"

# Clean user 1
user1_name = user1_name.strip().title()
user1_email = user1_email.lower()
user1_age = int(user1_age)

print(f"User 1: {user1_name}, {user1_email}, {user1_age}")

# Process user 2
user2_name = "  bob  "
user2_email = "BOB@Example.com"
user2_age = "25"

# Clean user 2
user2_name = user2_name.strip().title()
user2_email = user2_email.lower()
user2_age = int(user2_age)

print(f"User 2: {user2_name}, {user2_email}, {user2_age}")
print()

print("=== After: Using functions for each cleaning task ===")


def clean_name(name: str) -> str:
    """Strip whitespace and title-case a name."""
    return name.strip().title()


def clean_email(email: str) -> str:
    """Convert email to lowercase."""
    return email.lower()


def clean_age(age: str) -> int:
    """Convert age string to integer."""
    return int(age)


def process_user(name: str, email: str, age: str) -> dict:
    """Process a user and return cleaned data."""
    return {
        "name": clean_name(name),
        "email": clean_email(email),
        "age": clean_age(age),
    }


# Process users with the function
user1 = process_user("  ALICE  ", "alice@EXAMPLE.com", "30")
user2 = process_user("  bob  ", "BOB@Example.com", "25")

print(f"User 1: {user1}")
print(f"User 2: {user2}")
print()

print("=== Example: Multiple File Operations ===")

print("=== Before: Repeated file reading code ===")

# Read file 1
with open("notes1.txt", "w") as f:
    f.write("First file content")

with open("notes1.txt", "r") as f:
    content1 = f.read().strip().upper()
print(f"File 1 content: {content1}")

# Read file 2
with open("notes2.txt", "w") as f:
    f.write("Second file content")

with open("notes2.txt", "r") as f:
    content2 = f.read().strip().upper()
print(f"File 2 content: {content2}")
print()

print("=== After: Using a function for file reading ===")


def read_file_upper(filename: str) -> str:
    """Read a file and return its content in uppercase."""
    with open(filename, "r") as f:
        return f.read().strip().upper()


# Read files with the function
content1 = read_file_upper("notes1.txt")
content2 = read_file_upper("notes2.txt")

print(f"File 1 content: {content1}")
print(f"File 2 content: {content2}")
print()

print("=== Example: Validation Logic ===")

print("=== Before: Repeated validation code ===")

# Validate user 1
user1_name = "Alice"
user1_age = 25

if not user1_name:
    print("Error: Name is required")
elif len(user1_name) < 2:
    print("Error: Name must be at least 2 characters")
elif not isinstance(user1_age, int):
    print("Error: Age must be an integer")
elif user1_age < 0:
    print("Error: Age cannot be negative")
else:
    print(f"User 1 is valid: {user1_name}, {user1_age}")

# Validate user 2
user2_name = "Bob"
user2_age = -5

if not user2_name:
    print("Error: Name is required")
elif len(user2_name) < 2:
    print("Error: Name must be at least 2 characters")
elif not isinstance(user2_age, int):
    print("Error: Age must be an integer")
elif user2_age < 0:
    print("Error: Age cannot be negative")
else:
    print(f"User 2 is valid: {user2_name}, {user2_age}")
print()

print("=== After: Using a validation function ===")


def validate_user(name: str, age: int) -> tuple[bool, str]:
    """Validate user data. Returns (is_valid, error_message)."""
    if not name:
        return False, "Name is required"
    if len(name) < 2:
        return False, "Name must be at least 2 characters"
    if not isinstance(age, int):
        return False, "Age must be an integer"
    if age < 0:
        return False, "Age cannot be negative"
    return True, "Valid"


def process_user_validation(name: str, age: int) -> None:
    """Process and validate a user."""
    is_valid, message = validate_user(name, age)
    if is_valid:
        print(f"User is valid: {name}, {age}")
    else:
        print(f"Error: {message}")


process_user_validation("Alice", 25)
process_user_validation("Bob", -5)
process_user_validation("", 30)
print()

print("=== Benefits of Refactoring ===")

print("1. DRY (Don't Repeat Yourself): Code is written once")
print("2. Maintainability: Changes only need to be made in one place")
print("3. Readability: Function names describe what the code does")
print("4. Testability: Functions can be tested independently")
print("5. Reusability: Functions can be used in multiple places")
