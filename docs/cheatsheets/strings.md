# String Methods Cheatsheet

Quick reference for working with strings in Python.

## String Literals

```python
s = "double quotes"
s = 'single quotes'
s = """multi-line
string"""
s = r"raw string \n not escaped"  # Raw string (backslashes literal)
s = f"formatted {variable}"       # f-string (Python 3.6+)
```

## Indexing and Slicing

```python
s = "Hello"
s[0]      # 'H' (first character)
s[-1]     # 'o' (last character)
s[1:4]    # 'ell' (characters 1 to 3)
s[:3]     # 'Hel' (first 3 characters)
s[2:]     # 'llo' (from character 2 to end)
s[::2]    # 'Hlo' (every 2nd character)
s[::-1]   # 'olleH' (reversed)
```

## F-Strings (Preferred)

```python
name = "Alice"
age = 30

# Basic
f"{name} is {age}"  # Alice is 30

# Expressions
f"{2 + 2}"  # 4
f"{name.upper()}"  # ALICE

# Formatting
f"{3.14159:.2f}"  # 3.14 (2 decimal places)
f"{1000:,}"  # 1,000 (with thousands separator)
f"{value:>10}"  # Right-aligned in 10 characters
```

## Common String Methods

| Method | Example | Result |
|--------|---------|--------|
| `lower()` | `"HELLO".lower()` | `"hello"` |
| `upper()` | `"hello".upper()` | `"HELLO"` |
| `capitalize()` | `"hello".capitalize()` | `"Hello"` |
| `title()` | `"hello world".title()` | `"Hello World"` |
| `strip()` | `"  hello  ".strip()` | `"hello"` |
| `lstrip()` | `"  hello  ".lstrip()` | `"hello  "` |
| `rstrip()` | `"  hello  ".rstrip()` | `"  hello"` |
| `replace(old, new)` | `"hello".replace("l", "L")` | `"heLLo"` |
| `split(sep)` | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| `join(iterable)` | `",".join(["a", "b"])` | `"a,b"` |
| `startswith(prefix)` | `"hello".startswith("he")` | `True` |
| `endswith(suffix)` | `"hello".endswith("lo")` | `True` |
| `find(sub)` | `"hello".find("ll")` | `2` |
| `count(sub)` | `"hello".count("l")` | `2` |
| `isdigit()` | `"123".isdigit()` | `True` |
| `isalpha()` | `"abc".isalpha()` | `True` |
| `isalnum()` | `"abc123".isalnum()` | `True` |
| `isspace()` | `"   ".isspace()` | `True` |

## Escape Sequences

```python
"\n"    # Newline
"\t"    # Tab
"\\"    # Backslash
"\""    # Double quote
"\'"    # Single quote
"\r"    # Carriage return
"\b"    # Backspace
```

## String Operations

```python
# Concatenation
s = "Hello" + " " + "World"  # "Hello World"

# Repetition
s = "ab" * 3  # "ababab"

# Membership
"ell" in "hello"  # True
"xyz" not in "hello"  # True

# Length
len("hello")  # 5
```

## Useful Patterns

```python
# Split and process
words = "apple,banana,cherry".split(",")
# ["apple", "banana", "cherry"]

# Join with separator
result = " - ".join(["a", "b", "c"])
# "a - b - c"

# Strip whitespace
user_input = input().strip()

# Case-insensitive comparison
if user_input.lower() == "yes":
    print("User said yes")

# Check if string contains substring
if "error" in message:
    print("Error found")

# Replace multiple occurrences
text = "foo bar foo".replace("foo", "baz")
# "baz bar baz"

# Format with multiple values
template = "Name: {}, Age: {}"
result = template.format("Alice", 30)
```

## Common String Mistakes

- **Strings are immutable**: `s[0] = 'x'` raises TypeError. Create a new string instead.
- **Indexing out of bounds**: `"hello"[10]` raises IndexError. Use slicing instead: `"hello"[10:]` returns `""`.
- **Forgetting `.strip()` on input**: `input()` includes the newline. Use `input().strip()`.
- **Mixing string types**: `"hello" + 5` raises TypeError. Convert first: `"hello" + str(5)`.
- **Forgetting `.join()` for lists**: `", ".join(["a", "b"])` not `", " + ["a", "b"]`.
- **Case sensitivity**: `"Hello" != "hello"`. Use `.lower()` for case-insensitive comparison.