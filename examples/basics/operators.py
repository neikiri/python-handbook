"""
Operators - Python Arithmetic, Comparison, and Logical Operators

This example demonstrates:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Operator precedence
"""

print("=== Arithmetic Operators ===")

# Addition, subtraction, multiplication
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # 13
print(f"a - b = {a - b}")   # 7
print(f"a * b = {a * b}")   # 30

# Division (always returns float)
print(f"a / b = {a / b}")   # 3.333...

# Floor division (returns integer, truncates toward negative infinity)
print(f"a // b = {a // b}") # 3

# Modulo (remainder)
print(f"a % b = {a % b}")   # 1

# Exponentiation
print(f"a ** b = {a ** b}") # 1000
print()

print("=== Comparison Operators ===")

x = 5
y = 10
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # False
print(f"x != y: {x != y}")  # True
print(f"x < y: {x < y}")    # True
print(f"x > y: {x > y}")    # False
print(f"x <= 5: {x <= 5}")  # True
print(f"y >= 10: {y >= 10}")  # True
print()

print("=== Logical Operators ===")

is_raining = True
is_cold = False
has_umbrella = True

# and: both must be True
print(f"is_raining and is_cold: {is_raining and is_cold}")  # False

# or: at least one must be True
print(f"is_raining or is_cold: {is_raining or is_cold}")    # True

# not: negates the value
print(f"not is_raining: {not is_raining}")                  # False

# Combined example
stay_inside = is_cold and not has_umbrella
print(f"stay_inside (is_cold and not has_umbrella): {stay_inside}")

go_outside = is_raining and has_umbrella or not is_cold
print(f"go_outside (is_raining and has_umbrella or not is_cold): {go_outside}")
print()

print("=== Operator Precedence ===")

# Precedence (highest to lowest):
# 1. ** (exponent)
# 2. *, /, //, % (multiplication, division, etc.)
# 3. +, - (addition, subtraction)
# 4. <, <=, >, >=, ==, != (comparison)
# 5. not (logical not)
# 6. and (logical and)
# 7. or (logical or)

result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")  # 14 (not 20), * has higher precedence

result_with_parens = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result_with_parens}")  # 20, parens override precedence

# For clarity, use parentheses even when not needed
clear_result = (2 + 3) * 4  # Easier to read
print()

print("=== Short-circuit Evaluation ===")

# and: if first condition is False, second is not evaluated
def check_a():
    print("check_a() called")
    return False

def check_b():
    print("check_b() called")
    return True

print("Evaluating: check_a() and check_b()")
result = check_a() and check_b()  # Only check_a() runs
print(f"Result: {result}")
print()

print("Evaluating: check_a() or check_b()")
result = check_a() or check_b()  # Both run
print(f"Result: {result}")
