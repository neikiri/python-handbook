# Chapter 07: Strings

## 1. Overview

Text is everywhere in programming. Every time you display a message, read a
file, parse user input, or build a URL, you are working with strings. Python
treats text as a first-class citizen: it has a rich set of built-in methods,
powerful formatting syntax, and full Unicode support out of the box.

This chapter covers everything you need to work confidently with strings in
Python â€” from the basics of creating them to formatting, searching, slicing,
and understanding why they behave the way they do.

---

## 2. What You Will Learn

- The different ways to write string literals: single quotes, double quotes,
  and triple quotes
- What string immutability means and why it matters
- Escape sequences and raw strings
- Indexing and slicing with positive and negative indices
- The most useful string methods: `upper()`, `lower()`, `strip()`, `lstrip()`,
  `rstrip()`, `replace()`, `split()`, `join()`, `startswith()`, `endswith()`,
  `find()`, `count()`, `zfill()`, `center()`, `ljust()`, `rjust()`
- String formatting: f-strings (preferred), `.format()`, and `%` formatting
- Multiline strings
- Raw strings (`r"..."`)
- String concatenation and repetition
- Checking string content: `isdigit()`, `isalpha()`, `isalnum()`, `isspace()`,
  `isupper()`, `islower()`
- `len()` with strings
- Iterating over strings
- The `in` membership operator
- Converting other types to strings with `str()`

---

## 3. Core Concepts

### 3.1 What Is a String?

A **string** is an immutable sequence of Unicode characters. "Immutable" means
that once a string is created, its contents cannot be changed. "Sequence" means
that each character has a position (an index) and you can iterate over it.

```python
greeting = "Hello, world!"
print(type(greeting))  # <class 'str'>
print(len(greeting))   # 13
```

Every character in a Python string is a Unicode code point. This means Python
strings can hold text in any language, emoji, and mathematical symbols without
any extra setup.

```python
message = "HĂ©llo"
emoji   = "Python đźŤ"

print(len(message))  # 5
print(len(emoji))    # 8
```

---

### 3.2 String Literals

Python gives you four ways to write a string literal.

**Single quotes**

```python
name = 'Alice'
```

**Double quotes**

```python
name = "Alice"
```

Single and double quotes are interchangeable. The only practical difference is
that using one style lets you include the other inside the string without
escaping it.

```python
message = "It's a great day."   # single quote inside double-quoted string
reply   = 'She said "hello".'   # double quote inside single-quoted string
```

**Triple-quoted strings**

Triple quotes (`"""..."""` or `'''...'''`) let a string span multiple lines.
The newlines are part of the string.

```python
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

print(poem)
# Roses are red,
# Violets are blue,
# Python is great,
# And so are you.
```

Triple-quoted strings are also used for **docstrings** â€” the documentation
strings placed at the top of functions, classes, and modules.

```python
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"
```

---

### 3.3 String Immutability

Strings in Python are **immutable**: you cannot change a character in place.

```python
s = "hello"
s[0] = "H"   # TypeError: 'str' object does not support item assignment
```

To "modify" a string, you create a new one.

```python
s = "hello"

# Replace the first character using slicing
s = "H" + s[1:]
print(s)  # Hello

# Or use replace()
s = "hello"
s = s.replace("h", "H", 1)
print(s)  # Hello
```

Immutability has practical benefits:

- Strings can be used as dictionary keys and set members because they are
  hashable.
- Python can safely reuse identical string objects in memory.
- You never have to worry about a function secretly modifying a string you
  passed to it.

```python
# Strings are hashable â€” can be used as dict keys
person = {"name": "Alice", "city": "Paris"}

# Strings in sets
words = {"apple", "banana", "cherry"}
print("apple" in words)  # True
```

---

### 3.4 Escape Sequences

An **escape sequence** is a backslash followed by a character that together
represent something you cannot type directly in a string literal.

| Sequence | Meaning                  |
|----------|--------------------------|
| `\n`     | Newline                  |
| `\t`     | Horizontal tab           |
| `\\`     | Literal backslash        |
| `\'`     | Literal single quote     |
| `\"`     | Literal double quote     |
| `\r`     | Carriage return          |

```python
print("Line one\nLine two")
# Line one
# Line two

print("Name:\tAlice")
# Name:   Alice

print("C:\\Users\\Alice")
# C:\Users\Alice

print("She said \"hello\".")
# She said "hello".

print('It\'s fine.')
# It's fine.
```

---

### 3.5 Raw Strings

A **raw string** is prefixed with `r` (or `R`). In a raw string, backslashes
are treated as literal characters â€” no escape sequences are processed.

```python
path    = r"C:\Users\Alice\Documents"
pattern = r"\d{3}-\d{4}"   # regex pattern

print(path)     # C:\Users\Alice\Documents
print(pattern)  # \d{3}-\d{4}
```

Raw strings are especially useful for:

- Windows file paths (so you don't have to double every backslash)
- Regular expressions (which use `\d`, `\w`, `\s`, etc.)

One limitation: a raw string cannot end with an odd number of backslashes,
because the final backslash would escape the closing quote.

```python
# SyntaxError:
# bad = r"C:\Users\"

# Workaround: concatenate
good = r"C:\Users" + "\\"
print(good)  # C:\Users\
```

---

### 3.6 Multiline Strings

Triple-quoted strings are the standard way to write multiline strings. The
string includes every newline and leading space inside the quotes.

```python
address = """
123 Main Street
Springfield, IL 62701
USA
"""
print(address)
```

If you want a long string that does not contain literal newlines, use implicit
concatenation inside parentheses instead.

```python
message = (
    "This is a very long message that "
    "spans multiple lines in the source "
    "but is a single string at runtime."
)
print(message)
# This is a very long message that spans multiple lines in the source but is a single string at runtime.
```

Python joins adjacent string literals automatically â€” no `+` needed.

---

### 3.7 String Concatenation and Repetition

Use `+` to join two strings and `*` to repeat a string.

```python
first = "Hello"
last  = "World"

full = first + ", " + last + "!"
print(full)  # Hello, World!

line = "-" * 40
print(line)  # ----------------------------------------
```

> **Note:** Use `+` sparingly when building strings in a loop. It creates a
> new string object on every iteration. For joining many pieces, use
> `"".join()` instead (covered in section 3.13).

---

### 3.8 String Indexing

Strings are sequences, so each character has a numeric **index** starting at
0. Python also supports **negative indexing**: `-1` is the last character,
`-2` is the second-to-last, and so on.

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5   (positive indices)
#   -6 -5 -4 -3 -2 -1   (negative indices)

print(s[0])   # P
print(s[1])   # y
print(s[-1])  # n
print(s[-2])  # o
```

Accessing an index that does not exist raises an `IndexError`.

```python
print(s[10])  # IndexError: string index out of range
```

---

### 3.9 String Slicing

A **slice** extracts a portion of a string. The syntax is:

```text
s[start:stop:step]
```

- `start` â€” index to begin at (inclusive, default 0)
- `stop`  â€” index to stop before (exclusive, default end of string)
- `step`  â€” how many characters to advance each time (default 1)

```python
s = "Hello, World!"

print(s[0:5])    # Hello
print(s[7:12])   # World
print(s[:5])     # Hello   (start defaults to 0)
print(s[7:])     # World!  (stop defaults to end)
print(s[:])      # Hello, World!  (full copy)
print(s[::2])    # Hlo ol!  (every other character)
print(s[::-1])   # !dlroW ,olleH  (reversed)
```

Slices never raise an `IndexError` â€” if the indices are out of range, Python
returns as much as it can.

```python
s = "Hi"
print(s[0:100])  # Hi  (no error)
```

**Common slicing patterns**

```python
s = "abcdefgh"

print(s[2:5])    # cde   â€” characters at index 2, 3, 4
print(s[-3:])    # fgh   â€” last three characters
print(s[:-3])    # abcde â€” everything except the last three
print(s[1:-1])   # bcdefg â€” strip first and last character
print(s[::3])    # adg   â€” every third character
```

---

### 3.10 String Length

Use the built-in `len()` function to get the number of characters in a string.

```python
s = "Hello"
print(len(s))   # 5

empty = ""
print(len(empty))  # 0
```

`len()` counts Unicode code points, not bytes. A single emoji or accented
character counts as 1.

```python
print(len("cafĂ©"))   # 4
print(len("đźŤ"))     # 1
```

---

### 3.11 Converting Other Types to Strings

Use `str()` to convert any Python value to its string representation.

```python
print(str(42))          # "42"
print(str(3.14))        # "3.14"
print(str(True))        # "True"
print(str(False))       # "False"
print(str(None))        # "None"
print(str([1, 2, 3]))   # "[1, 2, 3]"
```

`str()` never raises an error â€” every Python object has a string
representation. This makes it safe to use when building output from mixed
types.

```python
score = 98
label = "Score: " + str(score)
print(label)  # Score: 98
```

The preferred alternative for most formatting tasks is an f-string, which
calls `str()` on the value automatically:

```python
score = 98
print(f"Score: {score}")  # Score: 98
```

Use `str()` explicitly when you need the string value itself â€” for example,
when joining a list of mixed types.

```python
values = [1, 3.14, True, None]
result = ", ".join(str(v) for v in values)
print(result)  # 1, 3.14, True, None
```

---

### 3.12 String Methods â€” Case

String methods are called with dot notation: `string.method()`. They always
return a **new** string; the original is unchanged.

```python
s = "hello, world"

print(s.upper())       # HELLO, WORLD
print(s.lower())       # hello, world
print(s.title())       # Hello, World
print(s.capitalize())  # Hello, world
print(s.swapcase())    # HELLO, WORLD
```

`title()` capitalizes the first letter of every word. `capitalize()` only
capitalizes the very first character of the whole string.

```python
print("the quick brown fox".title())      # The Quick Brown Fox
print("the quick brown fox".capitalize()) # The quick brown fox
```

---

### 3.13 String Methods â€” Whitespace and Splitting

**`strip()`, `lstrip()`, `rstrip()`**

These remove whitespace (or specified characters) from the ends of a string.

```python
s = "   hello, world   "

print(s.strip())    # "hello, world"    â€” both ends
print(s.lstrip())   # "hello, world   " â€” left end only
print(s.rstrip())   # "   hello, world" â€” right end only
```

You can pass a string of characters to strip. Python removes any combination
of those characters from the ends (not just the exact string).

```python
s = "***hello***"
print(s.strip("*"))   # hello

s = "xxhelloxx"
print(s.strip("x"))   # hello
```

**`split()`**

Splits a string into a list of substrings.

```python
s = "one two three"
print(s.split())         # ['one', 'two', 'three']  â€” splits on whitespace

csv = "a,b,c,d"
print(csv.split(","))    # ['a', 'b', 'c', 'd']

# Limit the number of splits
print(csv.split(",", 2)) # ['a', 'b', 'c,d']
```

When called with no argument, `split()` splits on any whitespace and discards
empty strings â€” useful for cleaning messy input.

```python
messy = "  one   two    three  "
print(messy.split())   # ['one', 'two', 'three']
```

**`splitlines()`**

Splits on line endings (`\n`, `\r\n`, `\r`).

```python
text = "line one\nline two\nline three"
print(text.splitlines())
# ['line one', 'line two', 'line three']
```

---

### 3.14 String Methods â€” Join

`join()` is the inverse of `split()`. It takes an iterable of strings and
joins them with the string it is called on as the separator.

```python
words = ["one", "two", "three"]

print(", ".join(words))   # one, two, three
print(" | ".join(words))  # one | two | three
print("".join(words))     # onetwothree
```

This is the preferred way to build a string from many pieces:

```python
parts = []
for i in range(5):
    parts.append(str(i))

result = "-".join(parts)
print(result)  # 0-1-2-3-4
```

---

### 3.15 String Methods â€” Search

**`find()` and `rfind()`**

`find()` returns the index of the first occurrence of a substring, or `-1` if
not found. `rfind()` searches from the right (finds the last occurrence).

```python
s = "banana"

print(s.find("a"))    # 1   â€” first 'a'
print(s.rfind("a"))   # 5   â€” last 'a'
print(s.find("z"))    # -1  â€” not found

# Optional start and stop arguments
print(s.find("a", 2))     # 3   â€” search from index 2
print(s.find("a", 2, 4))  # 3   â€” search between index 2 and 4
```

**`count()`**

Returns the number of non-overlapping occurrences of a substring.

```python
s = "banana"
print(s.count("a"))   # 3
print(s.count("an"))  # 2
print(s.count("z"))   # 0
```

**`startswith()` and `endswith()`**

```python
filename = "report_2024.pdf"

print(filename.startswith("report"))  # True
print(filename.endswith(".pdf"))      # True
print(filename.endswith(".txt"))      # False
```

Both methods accept a tuple of strings to check against multiple options at
once.

```python
filename = "image.png"
print(filename.endswith((".png", ".jpg", ".gif")))  # True
```

---

### 3.16 String Methods â€” Replace

**`replace()`**

Returns a new string with all occurrences of a substring replaced.

```python
s = "I like cats. Cats are great."

print(s.replace("cats", "dogs"))
# I like dogs. Cats are great.   (case-sensitive)

# Limit the number of replacements
print(s.replace("a", "X", 2))
# I like cXts. CXts are great.
```

Remember: `replace()` returns a new string. The original is unchanged.

```python
s = "hello"
s.replace("h", "H")   # return value discarded â€” s is still "hello"
s = s.replace("h", "H")   # correct â€” assign the result
print(s)  # Hello
```

---

### 3.17 String Methods â€” Padding and Alignment

These methods are useful for formatting tabular output.

**`center()`, `ljust()`, `rjust()`**

```python
s = "hello"

print(s.center(11))        # "   hello   "
print(s.center(11, "-"))   # "---hello---"

print(s.ljust(10))         # "hello     "
print(s.ljust(10, "."))    # "hello....."

print(s.rjust(10))         # "     hello"
print(s.rjust(10, "."))    # ".....hello"
```

If the string is already as long as or longer than the specified width, the
original string is returned unchanged.

**`zfill()`**

Pads a numeric string with leading zeros.

```python
print("42".zfill(5))    # 00042
print("3.14".zfill(7))  # 0003.14
print("-7".zfill(5))    # -0007  (sign is preserved)
```

`zfill()` is handy for formatting IDs, order numbers, or timestamps where
fixed-width zero-padded numbers are expected.

---

### 3.18 String Methods â€” Content Checks

These methods return `True` or `False` and are useful for validating input.

```python
print("123".isdigit())    # True  â€” all characters are digits
print("abc".isdigit())    # False

print("abc".isalpha())    # True  â€” all characters are letters
print("abc1".isalpha())   # False

print("abc1".isalnum())   # True  â€” all characters are letters or digits
print("abc!".isalnum())   # False

print("   ".isspace())    # True  â€” all characters are whitespace
print("  a".isspace())    # False

print("HELLO".isupper())  # True
print("Hello".isupper())  # False

print("hello".islower())  # True
print("Hello".islower())  # False
```

A few things to keep in mind:

- `isdigit()` returns `True` for Unicode digit characters too (e.g. `Â˛`).
  Use `s.isdecimal()` if you only want standard 0â€“9 digits.
- An empty string returns `False` for all of these methods.

```python
print("".isdigit())   # False
print("".isalpha())   # False
print("".isspace())   # False
```

---

### 3.19 Iterating Over Strings

Because strings are sequences, you can loop over them character by character.

```python
for char in "Python":
    print(char)
# P
# y
# t
# h
# o
# n
```

Use `enumerate()` when you need both the index and the character.

```python
for index, char in enumerate("Python"):
    print(f"{index}: {char}")
# 0: P
# 1: y
# 2: t
# 3: h
# 4: o
# 5: n
```

You can also use a `while` loop with an index counter, but the `for` loop is
cleaner and more idiomatic.

---

### 3.20 The `in` Operator

The `in` operator tests whether a substring exists inside a string. It returns
`True` or `False`.

```python
s = "Hello, World!"

print("World" in s)    # True
print("world" in s)    # False  (case-sensitive)
print("xyz" in s)      # False
print("Hello" not in s)  # False
```

`in` checks for substrings, not just single characters.

```python
email = "alice@example.com"
print("@" in email)          # True
print(".com" in email)       # True
print("example" in email)    # True
```

For case-insensitive membership checks, normalize both sides first.

```python
text = "The Quick Brown Fox"
print("quick" in text.lower())   # True
```

---

### 3.21 String Formatting

Python has three ways to format strings. The modern, preferred approach is
**f-strings**.

---

#### 3.21.1 `%` Formatting (Legacy)

This style comes from C and is still valid Python, but it is not recommended
for new code. You may encounter it in older codebases.

```python
name = "Alice"
age  = 30

print("Hello, %s. You are %d years old." % (name, age))
# Hello, Alice. You are 30 years old.
```

Common format codes: `%s` (string), `%d` (integer), `%f` (float).

---

#### 3.21.2 `str.format()`

`str.format()` uses `{}` placeholders and is more readable than `%`
formatting.

```python
# Positional
print("Hello, {}. You are {} years old.".format("Alice", 30))
# Hello, Alice. You are 30 years old.

# Keyword arguments
print("Hello, {name}. You are {age} years old.".format(name="Alice", age=30))
# Hello, Alice. You are 30 years old.

# Format specifications
pi = 3.14159265
print("Pi is approximately {:.2f}".format(pi))   # Pi is approximately 3.14
print("{:>10}".format("right"))                   #      right
print("{:<10}".format("left"))                    # left
print("{:^10}".format("center"))                  #   center
print("{:,}".format(1_000_000))                   # 1,000,000
```

---

#### 3.21.3 f-Strings (Python 3.6+)

**f-strings** are the preferred way to format strings in modern Python. Prefix
the string with `f` and put any Python expression inside `{}`.

```python
name = "Alice"
age  = 30

print(f"Hello, {name}. You are {age} years old.")
# Hello, Alice. You are 30 years old.
```

Any valid Python expression works inside the braces.

```python
x = 10
y = 3

print(f"{x} + {y} = {x + y}")          # 10 + 3 = 13
print(f"{x} / {y} = {x / y:.2f}")      # 10 / 3 = 3.33
print(f"{'hello'.upper()}")             # HELLO
print(f"{2 ** 8}")                      # 256
```

**Debugging with `=`** (Python 3.8+)

Adding `=` after the expression prints both the expression and its value.

```python
x = 42
print(f"{x = }")        # x = 42
print(f"{x * 2 = }")    # x * 2 = 84
```

---

#### 3.21.4 Format Specification Mini-Language

Both f-strings and `str.format()` support a **format spec** after a colon
inside the braces: `{value:spec}`.

**Number formatting**

```python
pi = 3.14159265

print(f"{pi:.2f}")    # 3.14       â€” 2 decimal places, fixed-point
print(f"{pi:.4f}")    # 3.1416     â€” 4 decimal places
print(f"{pi:e}")      # 3.141593e+00  â€” scientific notation

n = 1_000_000
print(f"{n:,}")       # 1,000,000  â€” thousands separator
print(f"{n:_}")       # 1_000_000  â€” underscore separator

x = 255
print(f"{x:b}")       # 11111111   â€” binary
print(f"{x:o}")       # 377        â€” octal
print(f"{x:x}")       # ff         â€” hex (lowercase)
print(f"{x:X}")       # FF         â€” hex (uppercase)
print(f"{x:#x}")      # 0xff       â€” hex with prefix
```

**Alignment and width**

```python
s = "hello"

print(f"{s:>10}")    #      hello  â€” right-align in 10 chars
print(f"{s:<10}")    # hello       â€” left-align in 10 chars
print(f"{s:^10}")    #   hello     â€” center in 10 chars
print(f"{s:*^10}")   # **hello***  â€” center, fill with '*'
print(f"{s:->10}")   # -----hello  â€” right-align, fill with '-'
```

**Percentage**

```python
ratio = 0.753
print(f"{ratio:.1%}")   # 75.3%
```

**Multi-line f-strings**

f-strings work inside triple quotes.

```python
name  = "Alice"
score = 98.5
grade = "A"

report = f"""
Student Report
--------------
Name:  {name}
Score: {score:.1f}
Grade: {grade}
"""
print(report)
```

You can also break an f-string across lines using parentheses.

```python
base_url = "https://api.example.com"
username = "alice"
page     = 2

url = (
    f"{base_url}"
    f"/users/{username}"
    f"?page={page}"
)
print(url)
# https://api.example.com/users/alice?page=2
```

---

## 4. Practical Examples

### 4.1 Cleaning User Input

A common task is normalizing text that comes from a user or an external source.

```python
def clean_name(raw: str) -> str:
    """Normalize a person's name: strip whitespace and title-case it."""
    return raw.strip().title()


print(clean_name("  alice smith  "))  # Alice Smith
print(clean_name("BOB JONES"))        # Bob Jones
print(clean_name("  charlie  "))      # Charlie
```

---

### 4.2 Validating a Username

```python
def is_valid_username(username: str) -> bool:
    """
    A valid username:
    - is 3 to 20 characters long
    - contains only letters, digits, and underscores
    - does not start with a digit
    """
    if not (3 <= len(username) <= 20):
        return False
    if not (username[0].isalpha() or username[0] == "_"):
        return False
    return all(c.isalnum() or c == "_" for c in username)


print(is_valid_username("alice_99"))   # True
print(is_valid_username("1alice"))     # False  â€” starts with digit
print(is_valid_username("ab"))         # False  â€” too short
print(is_valid_username("a" * 21))     # False  â€” too long
```

---

### 4.3 Parsing a CSV Line

```python
def parse_csv_line(line: str) -> list[str]:
    """Split a comma-separated line and strip whitespace from each field."""
    return [field.strip() for field in line.split(",")]


line = "Alice, 30, engineer, Paris"
fields = parse_csv_line(line)
print(fields)  # ['Alice', '30', 'engineer', 'Paris']
```

---

### 4.4 Building a Simple Report

```python
def format_report(title: str, data: list[tuple[str, int]]) -> str:
    """Format a simple two-column report."""
    width = 40
    lines = [
        title.center(width),
        "=" * width,
    ]
    for name, value in data:
        lines.append(f"  {name:<20} {value:>10,}")
    lines.append("=" * width)
    return "\n".join(lines)


scores = [
    ("Alice", 98_500),
    ("Bob", 72_300),
    ("Charlie", 115_000),
]

print(format_report("Annual Scores", scores))
```

Output:

```text
           Annual Scores           
========================================
  Alice                    98,500
  Bob                      72,300
  Charlie                 115,000
========================================
```

---

### 4.5 Counting Words and Characters

```python
def text_stats(text: str) -> dict[str, int]:
    """Return basic statistics about a block of text."""
    words = text.split()
    return {
        "characters":           len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "words":                len(words),
        "lines":                len(text.splitlines()),
    }


sample = """Python is a high-level programming language.
It emphasizes code readability.
Many beginners start with Python."""

stats = text_stats(sample)
for key, value in stats.items():
    print(f"{key:<25} {value}")
# characters                 97
# characters_no_spaces       80
# words                      15
# lines                       3
```

---

### 4.6 Palindrome Check

```python
def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards (ignoring case
    and spaces)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("racecar"))                       # True
print(is_palindrome("A man a plan a canal Panama"))   # True
print(is_palindrome("hello"))                         # False
```

---

### 4.7 Formatting a Table with f-Strings

```python
headers = ["Name", "Age", "City"]
rows = [
    ("Alice",   30, "New York"),
    ("Bob",     25, "London"),
    ("Charlie", 35, "Tokyo"),
]

# Print header
print(f"{'Name':<12} {'Age':>5} {'City':<12}")
print("-" * 32)

# Print rows
for name, age, city in rows:
    print(f"{name:<12} {age:>5} {city:<12}")
```

Output:

```text
Name          Age City        
--------------------------------
Alice          30 New York    
Bob            25 London      
Charlie        35 Tokyo       
```

---

### 4.8 Checking File Extensions

```python
def is_image(filename: str) -> bool:
    """Return True if the filename has a common image extension."""
    return filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))


print(is_image("photo.JPG"))     # True
print(is_image("report.pdf"))    # False
print(is_image("banner.webp"))   # True
```

---

### 4.9 Generating Zero-Padded IDs

```python
def make_order_id(number: int) -> str:
    """Return a zero-padded order ID like ORD-00042."""
    return f"ORD-{str(number).zfill(5)}"


print(make_order_id(1))      # ORD-00001
print(make_order_id(42))     # ORD-00042
print(make_order_id(99999))  # ORD-99999
```

---

### 4.10 Normalizing Whitespace

```python
def normalize_whitespace(text: str) -> str:
    """Collapse multiple spaces and strip each line."""
    lines = text.splitlines()
    cleaned = [" ".join(line.split()) for line in lines]
    return "\n".join(cleaned)


messy = """  Hello,   world!  
  This   has   extra   spaces.  
  And   another   line.  """

print(normalize_whitespace(messy))
# Hello, world!
# This has extra spaces.
# And another line.
```

---

### 4.11 Counting Specific Characters

```python
sentence = "The quick brown fox jumps over the lazy dog."

vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in sentence if c in vowels)
print(f"Vowels: {vowel_count}")   # Vowels: 11

# Using count() for a specific character
print(f"'o' appears {sentence.count('o')} times")   # 'o' appears 4 times
```

---

### 4.12 Building a Slug from a Title

```python
def slugify(title: str) -> str:
    """Convert a title to a URL-friendly slug."""
    return title.lower().strip().replace(" ", "-")


print(slugify("Hello World"))          # hello-world
print(slugify("  Python Tutorial  "))  # python-tutorial
print(slugify("My First Blog Post"))   # my-first-blog-post
```

---

## 5. Common Mistakes

### 5.1 Trying to Modify a String In Place

```python
s = "hello"
s[0] = "H"   # TypeError: 'str' object does not support item assignment
```

**Fix:** Create a new string.

```python
s = "H" + s[1:]   # Hello
```

---

### 5.2 Discarding the Return Value of a Method

String methods return a new string â€” they do not modify the original.

```python
s = "  hello  "
s.strip()          # return value discarded â€” s is still "  hello  "
print(s)           # "  hello  "

# Fix: assign the result
s = s.strip()
print(s)           # "hello"
```

This applies to every string method: `upper()`, `replace()`, `title()`, etc.

---

### 5.3 Confusing `find()` Return Value

`find()` returns `-1` when the substring is not found. The value `-1` is
truthy in Python, so a naive `if pos:` check will behave incorrectly.

```python
s = "hello"

pos = s.find("z")
if pos:           # BUG: -1 is truthy!
    print(f"Found at {pos}")   # This prints even though "z" was not found

# Correct check
if pos != -1:
    print(f"Found at {pos}")
else:
    print("Not found")
```

---

### 5.4 Using `+` in a Loop

```python
# Slow â€” creates a new string object on every iteration
result = ""
for i in range(1000):
    result += str(i)

# Fast â€” collect parts and join once
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)
```

For small loops this does not matter, but it becomes significant with thousands
of iterations.

---

### 5.5 Case-Sensitive Comparisons

```python
user_input = "Yes"

if user_input == "yes":   # False â€” "Yes" != "yes"
    print("Confirmed")

# Fix: normalize before comparing
if user_input.lower() == "yes":
    print("Confirmed")
```

The same applies to `in` checks and `startswith()` / `endswith()`.

---

### 5.6 Off-by-One in Slices

The `stop` index in a slice is **exclusive** â€” the character at that index is
not included.

```python
s = "Hello"

print(s[0:5])   # Hello  â€” indices 0, 1, 2, 3, 4
print(s[0:4])   # Hell   â€” indices 0, 1, 2, 3 (not 4)
print(s[1:4])   # ell    â€” indices 1, 2, 3
```

A common mistake is writing `s[0:len(s)-1]` when you want everything except
the last character. The correct idiom is `s[:-1]`.

```python
s = "Hello!"
print(s[:-1])   # Hello  â€” everything except the last character
```

---

### 5.7 Splitting on the Wrong Separator

```python
s = "one  two  three"   # double spaces

print(s.split(" "))
# ['one', '', 'two', '', 'three']  â€” empty strings from double spaces

# Fix: split() with no argument handles any whitespace
print(s.split())
# ['one', 'two', 'three']
```

---

### 5.8 Forgetting That `in` Is Case-Sensitive

```python
text = "Hello, World!"

print("world" in text)          # False â€” case mismatch
print("world" in text.lower())  # True  â€” normalize first
```

---

### 5.9 Passing a Non-String to `join()`

`join()` requires all items in the iterable to be strings. Passing integers
or other types raises a `TypeError`.

```python
numbers = [1, 2, 3]

# Wrong
", ".join(numbers)   # TypeError: sequence item 0: expected str instance, int found

# Fix: convert each item to str first
", ".join(str(n) for n in numbers)   # "1, 2, 3"
```

---

### 5.10 Using `%` Formatting with a Single Non-Tuple Value

```python
name = "Alice"

# Works â€” single value, no tuple needed
print("Hello, %s!" % name)

# Common mistake with a tuple value
coords = (10, 20)
print("Point: %s" % coords)   # TypeError: not all arguments converted

# Fix: wrap the tuple in another tuple
print("Point: %s" % (coords,))   # Point: (10, 20)

# Better: just use an f-string
print(f"Point: {coords}")   # Point: (10, 20)
```

This is one of many reasons to prefer f-strings over `%` formatting.

---

## 6. Practice Tasks

Work through these tasks on your own. Solutions are in
`docs/solutions/07-strings.md`.

---

### Task 1 â€” Reverse a String

Write a function `reverse_string(s: str) -> str` that returns the string
reversed.

```python
print(reverse_string("hello"))    # olleh
print(reverse_string("Python"))   # nohtyP
print(reverse_string(""))         # ""
```

---

### Task 2 â€” Count Vowels

Write a function `count_vowels(s: str) -> int` that counts the number of
vowels (a, e, i, o, u â€” case-insensitive) in a string.

```python
print(count_vowels("Hello, World!"))   # 3
print(count_vowels("Python"))          # 1
print(count_vowels("rhythm"))          # 0
```

---

### Task 3 â€” Title Case Without `title()`

Write a function `manual_title(s: str) -> str` that capitalizes the first
letter of each word without using the built-in `title()` method. Use
`split()`, `capitalize()`, and `join()`.

```python
print(manual_title("the quick brown fox"))   # The Quick Brown Fox
print(manual_title("hello world"))           # Hello World
```

---

### Task 4 â€” Caesar Cipher

Write a function `caesar(text: str, shift: int) -> str` that shifts every
letter in `text` by `shift` positions in the alphabet. Non-letter characters
should be left unchanged. The shift should wrap around (z + 1 = a).

```python
print(caesar("hello", 3))    # khoor
print(caesar("khoor", -3))   # hello
print(caesar("Hello, World!", 13))  # Uryyb, Jbeyq!
```

*Hint:* Use `ord()`, `chr()`, and the modulo operator.

---

### Task 5 â€” Word Frequency

Write a function `word_frequency(text: str) -> dict[str, int]` that returns
a dictionary mapping each word (lowercased) to the number of times it appears
in the text.

```python
result = word_frequency("the cat sat on the mat the cat")
print(result)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
```

---

### Task 6 â€” Truncate with Ellipsis

Write a function `truncate(s: str, max_length: int) -> str` that returns the
string truncated to `max_length` characters. If the string was truncated, add
`"..."` at the end (the `"..."` counts toward `max_length`).

```python
print(truncate("Hello, World!", 10))   # "Hello, ..."
print(truncate("Hi", 10))             # "Hi"
print(truncate("Hello, World!", 13))  # "Hello, World!"
```

---

### Task 7 â€” Initials

Write a function `initials(full_name: str) -> str` that returns the initials
of a full name, each followed by a period.

```python
print(initials("Alice Marie Smith"))   # A.M.S.
print(initials("Bob Jones"))           # B.J.
```

---

### Task 8 â€” Wrap Text

Write a function `wrap_text(text: str, width: int) -> str` that wraps a
string to a given line width. Words should not be split across lines.

```python
print(wrap_text("The quick brown fox jumps over the lazy dog.", 15))
# The quick brown
# fox jumps over
# the lazy dog.
```

*Hint:* Use `split()` to get words, then build lines by adding words until
the line would exceed `width`.

---

### Task 9 â€” Remove Duplicate Words

Write a function `remove_duplicates(text: str) -> str` that removes duplicate
words from a sentence while preserving the original order of first occurrences.

```python
print(remove_duplicates("the cat sat on the mat the cat"))
# the cat sat on mat
```

---

### Task 10 â€” Format a Phone Number

Write a function `format_phone(digits: str) -> str` that takes a 10-digit
string of digits and formats it as `(XXX) XXX-XXXX`.

```python
print(format_phone("8005551234"))   # (800) 555-1234
print(format_phone("2125559876"))   # (212) 555-9876
```

*Hint:* Use slicing to extract the three parts.

---

## 7. Key Takeaways

- A **string** is an immutable sequence of Unicode characters. You cannot
  change it in place â€” every "modification" creates a new string.

- Python has four string literal forms: single quotes, double quotes, triple
  single quotes, and triple double quotes. Single and double quotes are
  interchangeable; triple quotes allow multiline strings and docstrings.

- **Escape sequences** let you embed special characters (`\n`, `\t`, `\\`,
  `\'`, `\"`). **Raw strings** (`r"..."`) treat backslashes as literal
  characters â€” useful for regex patterns and Windows paths.

- **Indexing** is zero-based. Negative indices count from the end (`-1` is
  the last character). **Slicing** (`s[start:stop:step]`) extracts a
  substring and never raises an `IndexError`.

- `len()` returns the number of Unicode code points in a string.

- Use `str()` to convert any Python value to a string. Every object has a
  string representation, so `str()` never raises an error.

- Python has a large set of built-in string methods. The most important ones
  are: `strip()` / `lstrip()` / `rstrip()`, `split()`, `join()`, `replace()`,
  `find()`, `count()`, `startswith()`, `endswith()`, `upper()`, `lower()`,
  `center()`, `ljust()`, `rjust()`, `zfill()`, and the predicate methods
  (`isdigit()`, `isalpha()`, `isalnum()`, `isspace()`, `isupper()`,
  `islower()`).

- String methods always return a **new** string. Assign the result or the
  change is lost.

- **f-strings** (Python 3.6+) are the preferred way to format strings. They
  support any Python expression inside `{}` and a powerful format
  specification mini-language for controlling alignment, precision, and
  number bases. Use `.format()` when you need reusable templates; avoid `%`
  formatting in new code.

- Because strings are sequences, you can iterate over them with `for`, check
  membership with `in`, and use `enumerate()` to get index-value pairs.

- Use `"separator".join(list_of_strings)` instead of `+` in a loop when
  building strings from many pieces.

---

## Further Reading

- [Python docs â€” Text Sequence Type `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python docs â€” `string` module](https://docs.python.org/3/library/string.html)
- [Python docs â€” Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
- [PEP 498 â€” Literal String Interpolation (f-strings)](https://peps.python.org/pep-0498/)
- [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)

---

*Next chapter: [Chapter 08 â€” Control Flow](08-control-flow.md)*

---

