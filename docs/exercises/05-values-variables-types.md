# Chapter 05: Values, Variables, and Types — Exercises

## Overview

These exercises help you understand how Python stores and manages data: values, variables, types, and the difference between mutable and immutable objects. By the end, you will confidently work with Python's type system and avoid common pitfalls.

---

## How to Use These Exercises

- Create a folder called `chapter-05` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Explore Types with `type()`

Create a file called `explore_types.py`:

```python
# Test the type() function with different values
print(type(42))
print(type(3.14))
print(type("hello"))
print(type(True))
print(type(None))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"name": "Alice"}))
```

Run it and write down the output for each. Notice the pattern: each value has a type.

---

### Exercise 2: Understand Dynamic Typing

Create a file called `dynamic_typing.py`:

```python
x = 10
print(f"x = {x}, type = {type(x)}")

x = "hello"
print(f"x = {x}, type = {type(x)}")

x = [1, 2, 3]
print(f"x = {x}, type = {type(x)}")

x = None
print(f"x = {x}, type = {type(x)}")
```

Run it. Notice how `x` can hold different types at different times. This is dynamic typing.

---

### Exercise 3: Convert Between Types

Create a file called `type_conversion.py`:

```python
# String to integer
num_str = "42"
num_int = int(num_str)
print(f"'{num_str}' as int: {num_int}")

# Integer to string
num = 42
num_str = str(num)
print(f"{num} as string: '{num_str}'")

# String to float
price_str = "19.99"
price_float = float(price_str)
print(f"'{price_str}' as float: {price_float}")

# Float to integer (truncates, does not round)
value = 3.9
truncated = int(value)
print(f"{value} as int (truncated): {truncated}")

# Integer to boolean
print(f"int(0) as bool: {bool(0)}")
print(f"int(1) as bool: {bool(1)}")
print(f"int(42) as bool: {bool(42)}")

# String to list
text = "hello"
chars = list(text)
print(f"'{text}' as list: {chars}")
```

Run it and observe the conversions.

---

## Practice Exercises

### Exercise 4: Understand Mutability

Create a file called `mutability.py`:

```python
# Immutable: strings
s1 = "hello"
s2 = s1
s2 = s2.upper()  # creates a new string
print(f"s1: {s1}")  # still "hello"
print(f"s2: {s2}")  # "HELLO"
print(f"s1 is s2: {s1 is s2}")  # False — different objects

# Mutable: lists
list1 = [1, 2, 3]
list2 = list1
list2.append(4)  # modifies the existing list
print(f"list1: {list1}")  # [1, 2, 3, 4] — affected!
print(f"list2: {list2}")  # [1, 2, 3, 4]
print(f"list1 is list2: {list1 is list2}")  # True — same object

# Fix: make a copy
list3 = [1, 2, 3]
list4 = list3.copy()  # independent copy
list4.append(4)
print(f"list3: {list3}")  # [1, 2, 3] — not affected
print(f"list4: {list4}")  # [1, 2, 3, 4]
```

Run it and observe the difference between mutable and immutable types.

---

### Exercise 5: Use `is` vs `==`

Create a file called `is_vs_equals.py`:

```python
# Value equality with ==
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b: {a == b}")  # True — same values
print(f"a is b: {a is b}")  # False — different objects

# Identity with is
c = a
print(f"a is c: {a is c}")  # True — same object

# With None (always use is)
x = None
print(f"x is None: {x is None}")  # True
print(f"x == None: {x == None}")  # True (works, but not idiomatic)

# With small integers (CPython caches them)
n1 = 100
n2 = 100
print(f"n1 is n2: {n1 is n2}")  # True (implementation detail)

m1 = 1000
m2 = 1000
print(f"m1 is m2: {m1 is m2}")  # False (not cached)

# Rule: use == for values, is for None/True/False
```

Run it and observe the difference between `is` and `==`.

---

### Exercise 6: Multiple Assignment and Unpacking

Create a file called `unpacking.py`:

```python
# Assign the same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# Unpack a tuple
a, b = 10, 20
print(f"a={a}, b={b}")

# Swap without a temporary variable
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Unpack from a list
first, second, third = [1, 2, 3]
print(f"first={first}, second={second}, third={third}")

# Extended unpacking with *
numbers = [1, 2, 3, 4, 5]
head, *middle, tail = numbers
print(f"head={head}, middle={middle}, tail={tail}")

# Ignore values with _
x, _, z = (1, 2, 3)
print(f"x={x}, z={z}")
```

Run it and experiment with different unpacking patterns.

---

### Exercise 7: Understand Variable Scope

Create a file called `scope.py`:

```python
# Global variable
global_var = "I am global"

def my_function():
    # Local variable
    local_var = "I am local"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")

my_function()

print(f"Outside function: {global_var}")
# print(f"Outside function: {local_var}")  # This would cause NameError
```

Run it. Notice that `local_var` is not accessible outside the function, but `global_var` is.

---

## Challenge Exercises

### Challenge 1: Safe Type Conversion from User Input

Create a file called `safe_input.py`:

```python
def get_integer(prompt):
    """Ask for an integer, return it or None if invalid."""
    raw = input(prompt)
    try:
        return int(raw)
    except ValueError:
        print(f"Error: '{raw}' is not a valid integer.")
        return None

def get_float(prompt):
    """Ask for a float, return it or None if invalid."""
    raw = input(prompt)
    try:
        return float(raw)
    except ValueError:
        print(f"Error: '{raw}' is not a valid number.")
        return None

if __name__ == "__main__":
    age = get_integer("Enter your age: ")
    if age is not None:
        print(f"In 10 years you will be {age + 10}.")
    
    price = get_float("Enter a price: ")
    if price is not None:
        tax = price * 0.08
        print(f"Price: ${price:.2f}, Tax: ${tax:.2f}")
```

Run it and test with valid and invalid inputs.

---

### Challenge 2: Explore Truthiness

Create a file called `truthiness.py`:

```python
def check_truthiness(value):
    """Print whether a value is truthy or falsy."""
    if value:
        print(f"{value!r} is truthy")
    else:
        print(f"{value!r} is falsy")

# Test various values
check_truthiness(True)
check_truthiness(False)
check_truthiness(0)
check_truthiness(1)
check_truthiness(42)
check_truthiness("")
check_truthiness("hello")
check_truthiness([])
check_truthiness([1, 2, 3])
check_truthiness(())
check_truthiness((1,))
check_truthiness({})
check_truthiness({"key": "value"})
check_truthiness(None)
```

Run it and observe which values are truthy and which are falsy.

---

### Challenge 3: Demonstrate Mutable vs Immutable

Create a file called `mutable_demo.py`:

```python
def modify_immutable(value):
    """Try to modify an immutable value."""
    value = value + " modified"
    return value

def modify_mutable(items):
    """Modify a mutable list."""
    items.append("new item")

# Test with immutable
original_str = "hello"
result = modify_immutable(original_str)
print(f"Original string: {original_str}")
print(f"Returned value: {result}")

# Test with mutable
original_list = [1, 2, 3]
modify_mutable(original_list)
print(f"Original list: {original_list}")
```

Run it and observe how immutable and mutable types behave differently.

---

### Challenge 4: Use `isinstance()` for Type Checking

Create a file called `type_checking.py`:

```python
def process_value(value):
    """Process a value based on its type."""
    if isinstance(value, int):
        print(f"{value} is an integer. Doubled: {value * 2}")
    elif isinstance(value, float):
        print(f"{value} is a float. Rounded: {round(value)}")
    elif isinstance(value, str):
        print(f"'{value}' is a string. Uppercase: {value.upper()}")
    elif isinstance(value, list):
        print(f"{value} is a list. Length: {len(value)}")
    elif isinstance(value, bool):
        print(f"{value} is a boolean.")
    elif value is None:
        print("Value is None.")
    else:
        print(f"Unknown type: {type(value)}")

# Test with different types
process_value(42)
process_value(3.14)
process_value("hello")
process_value([1, 2, 3])
process_value(True)
process_value(None)
```

Run it and observe how `isinstance()` handles different types.

---

### Challenge 5: Create a Type Converter Function

Create a file called `converter.py`:

```python
def convert_to_type(value, target_type):
    """
    Convert a value to a target type.
    
    Args:
        value: The value to convert
        target_type: The target type ('int', 'float', 'str', 'bool', 'list')
    
    Returns:
        The converted value, or None if conversion fails
    """
    try:
        if target_type == 'int':
            return int(value)
        elif target_type == 'float':
            return float(value)
        elif target_type == 'str':
            return str(value)
        elif target_type == 'bool':
            return bool(value)
        elif target_type == 'list':
            return list(value)
        else:
            print(f"Unknown type: {target_type}")
            return None
    except (ValueError, TypeError) as e:
        print(f"Conversion failed: {e}")
        return None

# Test conversions
print(convert_to_type("42", 'int'))
print(convert_to_type("3.14", 'float'))
print(convert_to_type(42, 'str'))
print(convert_to_type("hello", 'list'))
print(convert_to_type("not a number", 'int'))
```

Run it and test various conversions.

---

## Hints

**ValueError when converting** → The string cannot be converted to that type. Check the format.

**NameError for a variable** → The variable is out of scope or not defined. Check where it was created.

**Unexpected mutation** → You assigned a mutable object to another variable. Use `.copy()` to make an independent copy.

**`is` returning unexpected results** → Remember that `is` checks object identity, not value equality. Use `==` for values.

---

## What to Review If You Get Stuck

- **Values and variables** → Handbook section 3.1
- **Dynamic typing** → Handbook section 3.2
- **The `type()` function** → Handbook section 3.3
- **Built-in types** → Handbook section 3.4
- **Type conversion** → Handbook section 3.6
- **`isinstance()` vs `type()`** → Handbook section 3.7
- **Variables are references** → Handbook section 3.8
- **Mutability** → Handbook section 3.8
- **Multiple assignment** → Handbook section 3.9
- **Variable scope** → Handbook section 3.12

---

## Key Takeaways

After completing these exercises, you should be able to:

- Understand Python's type system and dynamic typing
- Convert between types safely
- Distinguish between mutable and immutable types
- Use `is` and `==` correctly
- Unpack values from sequences
- Understand variable scope
- Handle type conversion errors gracefully
