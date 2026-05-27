# Solutions 05: Values, Variables, and Types

## Overview

Chapter 05 exercises explore Python's type system: how values are stored, how types work, the difference between mutable and immutable objects, and how to convert between types safely. This solution guide explains the reasoning behind each exercise.

---

## Notes Before Checking Solutions

The concepts in this chapter — especially mutability and identity vs. equality — trip up many beginners. Take time to understand the explanations, not just the code. These ideas come up constantly in real Python programs.

---

## Warm-up Exercise Solutions

### Exercise 1: Explore Types with `type()`

```python
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type(None))        # <class 'NoneType'>
print(type([1, 2, 3]))   # <class 'list'>
print(type((1, 2, 3)))   # <class 'tuple'>
print(type({1, 2, 3}))   # <class 'set'>
print(type({"name": "Alice"}))  # <class 'dict'>
```

Every value in Python has a type. The `type()` function returns the type as a class object. Notice that `True` is a `bool`, not an `int` — though `bool` is actually a subclass of `int` in Python, so `True == 1` and `False == 0`.

`None` has its own type, `NoneType`. There is only one `None` object in Python.

---

### Exercise 2: Understand Dynamic Typing

```python
x = 10
print(f"x = {x}, type = {type(x)}")   # int

x = "hello"
print(f"x = {x}, type = {type(x)}")   # str

x = [1, 2, 3]
print(f"x = {x}, type = {type(x)}")   # list

x = None
print(f"x = {x}, type = {type(x)}")   # NoneType
```

In Python, variables are labels that point to objects. When you write `x = "hello"`, you are not changing the type of `x` — you are making `x` point to a new string object. The integer `10` still exists in memory (until garbage collected); `x` just no longer points to it.

This is called *dynamic typing*: the type is associated with the value, not the variable.

---

### Exercise 3: Convert Between Types

```python
# String to integer
num_str = "42"
num_int = int(num_str)
print(f"'{num_str}' as int: {num_int}")   # 42

# Integer to string
num = 42
num_str = str(num)
print(f"{num} as string: '{num_str}'")    # '42'

# String to float
price_str = "19.99"
price_float = float(price_str)
print(f"'{price_str}' as float: {price_float}")  # 19.99

# Float to integer (truncates, does not round)
value = 3.9
truncated = int(value)
print(f"{value} as int (truncated): {truncated}")  # 3

# Integer to boolean
print(f"bool(0): {bool(0)}")    # False
print(f"bool(1): {bool(1)}")    # True
print(f"bool(42): {bool(42)}")  # True

# String to list
text = "hello"
chars = list(text)
print(f"'{text}' as list: {chars}")  # ['h', 'e', 'l', 'l', 'o']
```

**Key point about `int(3.9)`:** It truncates toward zero, it does not round. `int(3.9)` is `3`, and `int(-3.9)` is `-3`. Use `round()` if you want rounding.

**Key point about `bool()`:** Zero, empty strings, empty collections, and `None` are all falsy (convert to `False`). Everything else is truthy.

---

## Practice Exercise Solutions

### Exercise 4: Understand Mutability

```python
# Immutable: strings
s1 = "hello"
s2 = s1
s2 = s2.upper()   # creates a NEW string object
print(f"s1: {s1}")          # hello — unchanged
print(f"s2: {s2}")          # HELLO
print(f"s1 is s2: {s1 is s2}")  # False — different objects
```

When you call `s2.upper()`, Python creates a brand-new string `"HELLO"` and makes `s2` point to it. The original `"hello"` is untouched. Strings are immutable — you cannot change a character in place.

```python
# Mutable: lists
list1 = [1, 2, 3]
list2 = list1       # both point to the SAME list object
list2.append(4)     # modifies the object in place
print(f"list1: {list1}")  # [1, 2, 3, 4] — affected!
print(f"list2: {list2}")  # [1, 2, 3, 4]
print(f"list1 is list2: {list1 is list2}")  # True — same object
```

`list2 = list1` does not copy the list. It makes `list2` point to the same list object. When you call `list2.append(4)`, you are modifying the shared object, so `list1` sees the change too.

```python
# Fix: make a copy
list3 = [1, 2, 3]
list4 = list3.copy()   # independent copy
list4.append(4)
print(f"list3: {list3}")  # [1, 2, 3] — not affected
print(f"list4: {list4}")  # [1, 2, 3, 4]
```

`.copy()` creates a shallow copy — a new list object with the same elements. For nested lists, use `copy.deepcopy()` from the standard library.

---

### Exercise 5: Use `is` vs `==`

```python
# Value equality with ==
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b: {a == b}")  # True — same values
print(f"a is b: {a is b}")  # False — different objects
```

`==` compares values. `is` compares identity (whether two variables point to the exact same object in memory).

```python
# Identity with is
c = a
print(f"a is c: {a is c}")  # True — same object
```

```python
# With None — always use is
x = None
print(f"x is None: {x is None}")   # True — correct idiom
print(f"x == None: {x == None}")   # True — works, but not idiomatic
```

Use `is None` and `is not None` for None checks. The `==` operator can be overridden by a class's `__eq__` method, which could produce unexpected results. `is` always checks identity and cannot be overridden.

```python
# Small integer caching (CPython implementation detail)
n1 = 100
n2 = 100
print(f"n1 is n2: {n1 is n2}")  # True (CPython caches -5 to 256)

m1 = 1000
m2 = 1000
print(f"m1 is m2: {m1 is m2}")  # False (not cached)
```

CPython caches small integers (-5 to 256) for performance. Do not rely on this behavior — it is an implementation detail that could change. Always use `==` to compare values.

---

### Exercise 6: Multiple Assignment and Unpacking

```python
# Assign the same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")  # 0, 0, 0

# Unpack a tuple
a, b = 10, 20
print(f"a={a}, b={b}")  # 10, 20

# Swap without a temporary variable
a, b = b, a
print(f"After swap: a={a}, b={b}")  # 20, 10
```

The swap `a, b = b, a` works because Python evaluates the right side completely before assigning. It creates a tuple `(b, a)` = `(20, 10)`, then unpacks it into `a` and `b`.

```python
# Extended unpacking with *
numbers = [1, 2, 3, 4, 5]
head, *middle, tail = numbers
print(f"head={head}, middle={middle}, tail={tail}")
# head=1, middle=[2, 3, 4], tail=5
```

The `*` in unpacking collects all remaining elements into a list. It can appear anywhere in the unpacking pattern, but only once.

```python
# Ignore values with _
x, _, z = (1, 2, 3)
print(f"x={x}, z={z}")  # x=1, z=3
```

`_` is a valid variable name that conventionally means "I do not care about this value." It is not special to Python, but it is a widely understood convention.

---

### Exercise 7: Variable Scope

```python
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")  # can read global

my_function()

print(f"Outside function: {global_var}")
# print(local_var)  # NameError — local_var does not exist here
```

Variables created inside a function are local to that function. They are created when the function is called and destroyed when it returns. Code outside the function cannot access them.

Functions can *read* global variables, but they cannot *modify* them without the `global` keyword. Modifying globals from inside functions is generally a bad practice — it makes code harder to understand and test.

---

## Challenge Exercise Solutions

### Challenge 1: Safe Type Conversion from User Input

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

**Why return `None` instead of raising an exception?** For a simple interactive program, returning `None` and checking it with `if age is not None:` is clean and readable. The caller decides what to do with an invalid input. In a larger program, you might raise a custom exception instead.

---

### Challenge 2: Explore Truthiness

```python
def check_truthiness(value):
    if value:
        print(f"{value!r} is truthy")
    else:
        print(f"{value!r} is falsy")
```

**Falsy values in Python:**
- `False`
- `0` (integer zero)
- `0.0` (float zero)
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dict)
- `set()` (empty set)
- `None`

Everything else is truthy. This is why you can write `if items:` instead of `if len(items) > 0:` — both work, but the first is more Pythonic.

The `!r` format specifier in `{value!r}` uses `repr()` to format the value, which adds quotes around strings and makes `None` visible as `None` rather than an empty string.

---

### Challenge 3: Mutable vs Immutable

```python
def modify_immutable(value):
    value = value + " modified"  # creates a new string
    return value

def modify_mutable(items):
    items.append("new item")  # modifies the list in place

original_str = "hello"
result = modify_immutable(original_str)
print(f"Original string: {original_str}")  # hello — unchanged
print(f"Returned value: {result}")          # hello modified

original_list = [1, 2, 3]
modify_mutable(original_list)
print(f"Original list: {original_list}")   # [1, 2, 3, 'new item']
```

When you pass a string to a function and reassign the parameter inside the function, the original variable is unaffected — strings are immutable, and reassignment just makes the local parameter point to a new object.

When you pass a list and call `.append()`, you are modifying the same object that the caller holds a reference to. The change is visible outside the function.

This is why functions that modify mutable arguments should document that behavior clearly, or return a new object instead of modifying in place.

---

### Challenge 4: Use `isinstance()` for Type Checking

```python
def process_value(value):
    if isinstance(value, bool):
        # Check bool BEFORE int — bool is a subclass of int
        print(f"{value} is a boolean.")
    elif isinstance(value, int):
        print(f"{value} is an integer. Doubled: {value * 2}")
    elif isinstance(value, float):
        print(f"{value} is a float. Rounded: {round(value)}")
    elif isinstance(value, str):
        print(f"'{value}' is a string. Uppercase: {value.upper()}")
    elif isinstance(value, list):
        print(f"{value} is a list. Length: {len(value)}")
    elif value is None:
        print("Value is None.")
    else:
        print(f"Unknown type: {type(value)}")
```

**Why check `bool` before `int`?** `bool` is a subclass of `int`. `isinstance(True, int)` returns `True`. If you check `int` first, `True` and `False` will be caught by the `int` branch. Check the more specific type first.

`isinstance()` is preferred over `type(value) == int` because it handles inheritance correctly. `isinstance(True, int)` is `True`; `type(True) == int` is `False`.

---

### Challenge 5: Type Converter Function

```python
def convert_to_type(value, target_type):
    """Convert a value to a target type. Returns None on failure."""
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
```

**Why catch both `ValueError` and `TypeError`?**
- `ValueError` is raised when the value has the right type but the wrong content: `int("hello")`.
- `TypeError` is raised when the value has the wrong type entirely: `int(None)`.

Catching both covers the common failure cases.

---

## Common Mistakes

**Assigning a list to another variable and expecting a copy.** `b = a` makes `b` point to the same list. Use `b = a.copy()` or `b = list(a)` for a copy.

**Using `is` to compare values.** `is` checks identity, not equality. `"hello" is "hello"` may be `True` due to string interning, but you should not rely on it. Use `==` for value comparisons.

**Forgetting that `int()` truncates, not rounds.** `int(2.9)` is `2`, not `3`. Use `round(2.9)` to get `3`.

**Checking `if x == None:` instead of `if x is None:`.** Both work, but `is None` is the correct idiom and avoids potential issues with custom `__eq__` methods.

---

## What to Review Next

- Chapter 06: Operators, Expressions, and Input — arithmetic, comparisons, and user input
- Chapter 07: Strings — string methods, formatting, and manipulation
- Chapter 09: Collections — lists, tuples, sets, and dictionaries in depth
