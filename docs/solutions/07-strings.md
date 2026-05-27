# Solutions 07: Strings and Text Processing

## Overview

Chapter 07 exercises cover creating and inspecting strings, using string methods, formatting with f-strings, escape sequences, slicing, and building strings dynamically. This solution guide explains the reasoning behind each exercise and highlights common pitfalls.

---

## Notes Before Checking Solutions

Strings are one of the most-used types in Python. The key insight to internalize early is that strings are *immutable* — every string method returns a new string rather than modifying the original. Once that clicks, the rest of the chapter falls into place.

---

## Warm-up Exercise Solutions

### Exercise 1: Create and Inspect Strings

```python
single = 'hello'
double = "world"
triple = """This is a
multi-line string."""

text = "Python"
print(f"Length of '{text}': {len(text)}")  # 6

# Indexing
print(f"First character: {text[0]}")   # P
print(f"Last character: {text[-1]}")   # n
print(f"Second character: {text[1]}")  # y

# Slicing
print(f"First 3 characters: {text[:3]}")   # Pyt
print(f"Last 3 characters: {text[-3:]}")   # hon
print(f"Middle characters: {text[1:4]}")   # yth
```

**Indexing rules:**
- Indices start at `0`. The first character is `text[0]`.
- Negative indices count from the end. `text[-1]` is the last character.
- `text[1:4]` is a slice from index 1 up to (but not including) index 4.

**Why use triple quotes?** Triple-quoted strings can span multiple lines without escape sequences. They are commonly used for docstrings and for strings that contain both single and double quotes.

---

### Exercise 2: Use String Methods

```python
text = "Hello, World!"

print(text.upper())    # HELLO, WORLD!
print(text.lower())    # hello, world!
print(text.title())    # Hello, World!

print(text.find('World'))       # 7 (index of first match)
print(text.count('l'))          # 3
print(text.startswith('Hello')) # True
print(text.endswith('!'))       # True

print(text.replace('World', 'Python'))  # Hello, Python!

messy = "  hello world  "
print(messy.strip())   # 'hello world'
print(messy.lstrip())  # 'hello world  '
print(messy.rstrip())  # '  hello world'

sentence = "The quick brown fox"
words = sentence.split()          # ['The', 'quick', 'brown', 'fox']
print(' - '.join(words))          # The - quick - brown - fox
```

**Important:** String methods return new strings. They do not modify the original. `text.upper()` does not change `text` — it returns a new uppercase string. You must assign the result if you want to keep it:

```python
text = text.upper()  # now text is uppercase
```

**`find()` vs `index()`:** Both find the position of a substring. `find()` returns `-1` if not found; `index()` raises a `ValueError`. Use `find()` when "not found" is a normal case, and `index()` when you expect the substring to always be present.

---

### Exercise 3: Format Strings with f-strings

```python
name = "Alice"
age = 30
price = 19.99

# Basic
print(f"Name: {name}")
print(f"Next year: {age + 1}")  # expressions work inside {}

# Format specifiers
print(f"Price: ${price:.2f}")        # $19.99 (2 decimal places)
print(f"Number: {age:03d}")          # 030 (zero-padded, 3 digits wide)
print(f"Percentage: {0.75:.1%}")     # 75.0%

# Alignment
print(f"Left:   '{name:<10}'")   # 'Alice     '
print(f"Right:  '{name:>10}'")   # '     Alice'
print(f"Center: '{name:^10}'")   # '  Alice   '
```

**Format specifier syntax:** `{value:format_spec}` where the format spec follows the pattern `[[fill]align][width][.precision][type]`.

Common format types:
- `d` — integer
- `f` — float (use `.2f` for 2 decimal places)
- `%` — percentage (multiplies by 100 and adds `%`)
- `s` — string (default for strings)
- `e` — scientific notation

f-strings are the preferred way to format strings in Python 3.6+. They are faster than `%` formatting and `.format()`, and more readable.

---

## Practice Exercise Solutions

### Exercise 4: Work with Escape Sequences

```python
print("Line 1\nLine 2\nLine 3")
print("Name\tAge\tCity")
print("Path: C:\\Users\\Alice\\Documents")
print('She said "Hello!"')
print("It's a beautiful day.")

# Raw string — backslashes are literal
raw = r"C:\Users\Alice\Documents"
print(f"Raw string: {raw}")
```

**Common escape sequences:**
- `\n` — newline
- `\t` — tab
- `\\` — literal backslash
- `\"` — double quote inside a double-quoted string
- `\'` — single quote inside a single-quoted string
- `\r` — carriage return (Windows line endings use `\r\n`)

**Raw strings (`r"..."`):** The `r` prefix tells Python to treat backslashes as literal characters. This is useful for Windows file paths and regular expressions, where backslashes are common and you do not want them interpreted as escape sequences.

---

### Exercise 5: Check String Content

```python
text = "Hello123"

print(text.isalpha())   # False (contains digits)
print(text.isdigit())   # False (contains letters)
print(text.isalnum())   # True (letters and digits only)
print(text.isupper())   # False (has lowercase letters)
print(text.islower())   # False (has uppercase letters)

print('123'.isdigit())  # True
print('HELLO'.isupper()) # True
print('hello'.islower()) # True
print('   '.isspace())   # True
```

These methods are useful for input validation. For example, to check if a username contains only letters and digits:

```python
def is_valid_username(username):
    return username.isalnum() and len(username) >= 3
```

**Note:** `isdigit()` returns `True` for Unicode digit characters too (like `²`). If you need to check for ASCII digits only, use `all(c in '0123456789' for c in s)` or a regex.

---

### Exercise 6: Slice and Manipulate Strings

```python
text = "Python Programming"

print(text[:6])     # Python
print(text[-11:])   # Programming
print(text[7:18])   # Programming

# Slicing with step
print(text[::2])    # Pto rgamn (every 2nd character)
print(text[::-1])   # gnimmargorP nohtyP (reversed)

# Capitalize first letter
word = "hello"
capitalized = word[0].upper() + word[1:]
print(capitalized)  # Hello

# Extract email parts
email = "alice@example.com"
at_index = email.find("@")
username = email[:at_index]    # alice
domain = email[at_index + 1:]  # example.com
```

**Slice syntax:** `text[start:stop:step]`
- `start` defaults to `0`
- `stop` defaults to `len(text)`
- `step` defaults to `1`
- Negative step reverses direction

**Why `text[::-1]` reverses a string:** With `step=-1`, Python reads from the end to the beginning. `start` defaults to the last index, `stop` defaults to before the first index.

---

### Exercise 7: Build Strings Dynamically

```python
# Concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Hello, Alice!

# Repetition
print("=" * 40)
print("Welcome to Python")
print("=" * 40)

# Join (preferred for multiple strings)
words = ["The", "quick", "brown", "fox"]
sentence = " ".join(words)
print(sentence)  # The quick brown fox

# Formatted table
print("Name".ljust(10) + "Age".ljust(5) + "City")
print("-" * 25)
print("Alice".ljust(10) + "30".ljust(5) + "New York")
```

**Why use `join()` instead of `+` in a loop?** String concatenation with `+` creates a new string object each time. In a loop with many iterations, this is slow because Python has to copy the growing string repeatedly. `join()` is more efficient — it calculates the total length first and allocates memory once.

```python
# Slow (avoid in loops)
result = ""
for word in words:
    result += word + " "

# Fast (preferred)
result = " ".join(words)
```

---

## Challenge Exercise Solutions

### Challenge 1: Analyze Text

```python
def analyze_text(text):
    """Analyze various properties of a text."""
    print(f"Text: {text}")
    print(f"Length: {len(text)}")
    print(f"Words: {len(text.split())}")
    print(f"Uppercase letters: {sum(1 for c in text if c.isupper())}")
    print(f"Lowercase letters: {sum(1 for c in text if c.islower())}")
    print(f"Digits: {sum(1 for c in text if c.isdigit())}")
    print(f"Spaces: {text.count(' ')}")
    print(f"Vowels: {sum(1 for c in text.lower() if c in 'aeiou')}")
```

**How `sum(1 for c in text if c.isupper())` works:** This is a generator expression. For each character `c` in `text`, if `c.isupper()` is `True`, it contributes `1` to the sum. It is equivalent to:

```python
count = 0
for c in text:
    if c.isupper():
        count += 1
```

The generator expression is more concise and slightly more efficient.

---

### Challenge 2: Create a Text Formatter

```python
def format_title(text, width=40):
    """Format text as a centered title."""
    return text.center(width, "=")

def format_paragraph(text, width=40):
    """Format text as a paragraph with word wrapping."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        # Check if adding this word would exceed the width
        test_line = " ".join(current_line + [word])
        if len(test_line) <= width:
            current_line.append(word)
        else:
            # Save the current line and start a new one
            lines.append(" ".join(current_line))
            current_line = [word]

    # Add the last line
    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)
```

**How the word-wrapping works:**
1. Split the text into words.
2. For each word, check if adding it to the current line would exceed the width.
3. If yes, save the current line and start a new one with the current word.
4. After the loop, add the last line (which may not have triggered the "too long" condition).

This is a greedy algorithm — it fills each line as much as possible before starting a new one. The standard library's `textwrap` module does this more robustly.

---

### Challenge 3: Build a Simple Text Processor

```python
def process_text(text):
    """Process text with various transformations."""
    print(f"Original: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title case: {text.title()}")
    print(f"Reversed: {text[::-1]}")
    print(f"Capitalized: {text.capitalize()}")

    # Remove extra spaces
    cleaned = " ".join(text.split())
    print(f"Cleaned: {cleaned}")
```

**`capitalize()` vs `title()`:**
- `capitalize()` makes the first character uppercase and the rest lowercase.
- `title()` makes the first character of each word uppercase.

`"hello world".capitalize()` → `"Hello world"`
`"hello world".title()` → `"Hello World"`

**Removing extra spaces:** `" ".join(text.split())` is a common idiom. `split()` with no arguments splits on any whitespace and discards empty strings, so multiple spaces, tabs, and newlines all collapse to a single space.

---

### Challenge 4: Validate and Clean Input

```python
def clean_name(name):
    """Clean and validate a name."""
    name = name.strip()
    if not name:
        return None
    # Allow letters and spaces only
    if not name.replace(" ", "").isalpha():
        return None
    return name.title()

def clean_email(email):
    """Clean and validate an email."""
    email = email.strip().lower()
    if "@" not in email or "." not in email:
        return None
    return email

def clean_phone(phone):
    """Clean and validate a phone number."""
    # Extract only digits
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) != 10:
        return None
    # Format as (XXX) XXX-XXXX
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
```

**Why `name.replace(" ", "").isalpha()`?** `isalpha()` returns `False` if the string contains spaces. We want to allow spaces in names (like "Alice Smith"), so we remove spaces before checking. The `replace()` call does not modify `name` — it returns a new string used only for the check.

**Why `"".join(c for c in phone if c.isdigit())`?** This extracts only the digit characters from the phone string, discarding dashes, spaces, parentheses, and anything else. It is more flexible than `replace("-", "")` because it handles any non-digit character.

---

## Common Mistakes

**Trying to modify a string in place.** `text[0] = 'H'` raises a `TypeError`. Strings are immutable. Create a new string: `text = 'H' + text[1:]`.

**Forgetting that string methods return new strings.** `text.upper()` does not change `text`. You must write `text = text.upper()` to update the variable.

**Off-by-one in slicing.** `text[0:3]` includes indices 0, 1, 2 — not 3. The stop index is exclusive.

**Using `+` to build strings in a loop.** Use `join()` instead for better performance.

**Confusing `find()` and `index()`.** `find()` returns `-1` when not found; `index()` raises `ValueError`. Choose based on whether "not found" is an error or a normal case.

---

## What to Review Next

- Chapter 08: Control Flow — conditionals and loops
- Chapter 09: Collections — lists, tuples, sets, and dictionaries
- Chapter 11: Comprehensions and Generators — a more concise way to process strings and collections
