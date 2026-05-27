# Built-in Types Reference

Comprehensive reference for Python's built-in data types.

## Numeric Types

### int — Integer

```python
x = 10
x = -5
x = 0
x = 0xFF  # Hexadecimal
x = 0b1010  # Binary
x = 0o12  # Octal

# Operations
10 + 5  # 15
10 - 5  # 5
10 * 5  # 50
10 / 5  # 2.0 (always float)
10 // 5  # 2 (floor division)
10 % 3  # 1 (modulo)
2 ** 10  # 1024 (exponentiation)

# Methods
abs(-5)  # 5
int("10")  # 10
int(3.14)  # 3
```

### float — Floating-Point Number

```python
x = 3.14
x = -2.5
x = 1.0
x = 1e-3  # 0.001 (scientific notation)
x = float("inf")  # Infinity
x = float("-inf")  # Negative infinity
x = float("nan")  # Not a number

# Operations (same as int)
3.14 + 2.86  # 6.0
10.0 / 3  # 3.3333...

# Methods
round(3.14159, 2)  # 3.14
float("3.14")  # 3.14
```

### bool — Boolean

```python
x = True
x = False

# Conversion
bool(1)  # True
bool(0)  # False
bool("")  # False
bool("hello")  # True
bool([])  # False
bool([1, 2])  # True

# Operations
True and False  # False
True or False  # True
not True  # False
```

## Text Type

### str — String

```python
s = "hello"
s = 'hello'
s = """multi-line
string"""

# Indexing
s[0]  # 'h'
s[-1]  # 'o'

# Slicing
s[1:4]  # 'ell'
s[:3]  # 'hel'
s[2:]  # 'llo'

# Methods
s.upper()  # 'HELLO'
s.lower()  # 'hello'
s.replace("l", "L")  # 'heLLo'
s.split()  # ['hello']
",".join(["a", "b"])  # 'a,b'

# Formatting
f"Hello {name}"  # f-string
"Hello {}".format(name)  # .format()
"Hello %s" % name  # % formatting
```

## Sequence Types

### list — Mutable Sequence

```python
lst = [1, 2, 3]
lst = []
lst = list()

# Indexing and slicing
lst[0]  # First element
lst[-1]  # Last element
lst[1:3]  # Slice

# Modification
lst.append(4)
lst.insert(0, 0)
lst.remove(2)
lst.pop()
lst.extend([5, 6])
lst.clear()

# Query
len(lst)
2 in lst
lst.index(2)
lst.count(2)

# Sorting
lst.sort()
lst.reverse()
```

### tuple — Immutable Sequence

```python
tup = (1, 2, 3)
tup = 1, 2, 3
tup = (1,)  # Single element
tup = ()  # Empty

# Indexing and slicing (same as list)
tup[0]
tup[1:3]

# Immutable (no modification methods)
# tup[0] = 10  # TypeError

# Query
len(tup)
2 in tup
tup.index(2)
tup.count(2)

# Unpacking
a, b, c = (1, 2, 3)
```

### range — Immutable Sequence of Numbers

```python
r = range(5)  # 0, 1, 2, 3, 4
r = range(2, 5)  # 2, 3, 4
r = range(0, 10, 2)  # 0, 2, 4, 6, 8

# Indexing
r[0]  # 0
r[-1]  # Last element

# Query
len(r)
2 in r

# Convert to list
list(r)  # [0, 1, 2, 3, 4]
```

## Mapping Type

### dict — Dictionary

```python
d = {"name": "Alice", "age": 30}
d = dict(name="Alice", age=30)
d = {}

# Access
d["name"]  # "Alice"
d.get("name")  # "Alice"
d.get("missing", "default")  # "default"

# Modification
d["name"] = "Bob"
d["city"] = "NYC"
d.update({"age": 31})
del d["age"]
d.pop("age")
d.clear()

# Query
len(d)
"name" in d
d.keys()
d.values()
d.items()

# Iteration
for key in d:
    print(key)
for key, value in d.items():
    print(key, value)
```

## Set Types

### set — Mutable Set

```python
s = {1, 2, 3}
s = set()
s = set([1, 2, 3])

# Modification
s.add(4)
s.remove(2)  # Raises KeyError if not found
s.discard(2)  # No error if not found
s.pop()
s.clear()

# Query
len(s)
2 in s

# Set operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2  # Union: {1, 2, 3, 4}
s1 & s2  # Intersection: {2, 3}
s1 - s2  # Difference: {1}
s1 ^ s2  # Symmetric difference: {1, 4}
```

### frozenset — Immutable Set

```python
fs = frozenset([1, 2, 3])
fs = frozenset()

# Query (same as set)
len(fs)
2 in fs

# Set operations (same as set)
fs1 | fs2
fs1 & fs2

# Immutable (no modification methods)
# fs.add(4)  # AttributeError
```

## Special Type

### None — Null Value

```python
x = None

# Check for None
if x is None:
    print("x is None")

# Default values
def func(x=None):
    if x is None:
        x = []
    return x
```

## bytes — Byte Sequence

```python
b = b"hello"
b = bytes([72, 101, 108, 108, 111])
b = "hello".encode("utf-8")

# Indexing
b[0]  # 72

# Decoding
b.decode("utf-8")  # "hello"
```

## Type Conversion

```python
int("10")  # 10
int(3.14)  # 3
float("3.14")  # 3.14
float(3)  # 3.0
str(42)  # "42"
bool(1)  # True
list((1, 2, 3))  # [1, 2, 3]
tuple([1, 2, 3])  # (1, 2, 3)
set([1, 1, 2, 3])  # {1, 2, 3}
dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}
```

## Mutability Overview

| Type | Mutable | Notes |
|------|---------|-------|
| int | No | Immutable |
| float | No | Immutable |
| bool | No | Immutable |
| str | No | Immutable |
| bytes | No | Immutable |
| list | Yes | Can be modified |
| tuple | No | Immutable |
| dict | Yes | Can be modified |
| set | Yes | Can be modified |
| frozenset | No | Immutable |

## Truthiness Overview

Values that evaluate to `False`:
- `False`
- `None`
- `0`, `0.0`
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dict)
- `set()` (empty set)

All other values evaluate to `True`.