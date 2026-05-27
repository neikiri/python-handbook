# Built-in Functions Cheatsheet

Quick reference for Python's most commonly used built-in functions.

## Output and Input

```python
print(*objects, sep=' ', end='\n')
# Print objects to console
print("Hello", "World")  # Hello World
print("a", "b", sep="-")  # a-b

input(prompt='')
# Read a line from user input (returns string)
name = input("Enter your name: ")
```

## Type Conversion

```python
int(x, base=10)      # Convert to integer
float(x)             # Convert to float
str(x)               # Convert to string
bool(x)              # Convert to boolean
list(x)              # Convert to list
tuple(x)             # Convert to tuple
dict(x)              # Convert to dictionary
set(x)               # Convert to set
```

## Type Information

```python
type(object)         # Return the type of an object
isinstance(obj, classinfo)  # Check if object is instance of class
```

## Sequences and Iteration

```python
len(s)               # Return length of sequence
range(start, stop, step)  # Create sequence of numbers
enumerate(iterable, start=0)  # Get index and value pairs
zip(*iterables)      # Combine multiple iterables
sorted(iterable, key=None, reverse=False)  # Return sorted list
reversed(seq)        # Return reversed iterator
```

## Examples

```python
# range
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)
for i in range(2, 5):        # 2, 3, 4
    print(i)
for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
    print(i)

# enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)  # 0 a, 1 b, 2 c

# zip
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)  # Alice 25, Bob 30

# sorted
numbers = [3, 1, 4, 1, 5]
sorted(numbers)  # [1, 1, 3, 4, 5]
sorted(numbers, reverse=True)  # [5, 4, 3, 1, 1]
```

## Aggregation Functions

```python
min(iterable, *args, key=None, default=...)
# Return smallest item
min([3, 1, 4])  # 1

max(iterable, *args, key=None, default=...)
# Return largest item
max([3, 1, 4])  # 4

sum(iterable, start=0)
# Return sum of items
sum([1, 2, 3])  # 6

any(iterable)
# Return True if any element is true
any([False, False, True])  # True

all(iterable)
# Return True if all elements are true
all([True, True, True])  # True
```

## Object Inspection

```python
help(object)         # Display help for object
dir(object)          # List attributes and methods
id(object)           # Return unique identifier
callable(object)     # Check if object is callable
hasattr(obj, name)   # Check if object has attribute
getattr(obj, name, default=None)  # Get attribute value
setattr(obj, name, value)  # Set attribute value
```

## File Operations

```python
open(file, mode='r', encoding=None)
# Open file and return file object
# Modes: 'r' (read), 'w' (write), 'a' (append), 'b' (binary)
with open("file.txt") as f:
    content = f.read()
```

## Other Useful Functions

```python
abs(x)               # Return absolute value
round(number, ndigits=None)  # Round to nearest integer
pow(base, exp, mod=None)  # Return base to power exp
divmod(a, b)         # Return (quotient, remainder)
hex(x)               # Convert to hexadecimal string
bin(x)               # Convert to binary string
oct(x)               # Convert to octal string
ord(c)               # Return Unicode code point of character
chr(i)               # Return character from Unicode code point
```

## Common Beginner Notes

- `print()` always adds a newline at the end by default
- `input()` always returns a string, even if user enters a number
- Use `int(input())` to get a number from user
- `len()` works on any sequence: strings, lists, tuples, etc.
- `range()` does not include the stop value
- `enumerate()` is useful when you need both index and value
- `zip()` stops at the shortest iterable
- `sorted()` returns a new list; it doesn't modify the original
- `any()` and `all()` short-circuit: `any()` stops at first True, `all()` stops at first False