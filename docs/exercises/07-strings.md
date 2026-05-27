# Chapter 07: Strings — Exercises

## Overview

These exercises help you master Python's string handling: creating strings, formatting them, searching and replacing, slicing, and using string methods. By the end, you will confidently work with text in Python.

---

## How to Use These Exercises

- Create a folder called `chapter-07` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Create and Inspect Strings

Create a file called `string_basics.py`:

```python
# Different ways to create strings
single = 'hello'
double = "world"
triple = """This is a
multi-line string."""

print(f"Single quotes: {single}")
print(f"Double quotes: {double}")
print(f"Triple quotes:\n{triple}")

# String length
text = "Python"
print(f"\nLength of '{text}': {len(text)}")

# Indexing
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Second character: {text[1]}")

# Slicing
print(f"First 3 characters: {text[:3]}")
print(f"Last 3 characters: {text[-3:]}")
print(f"Middle characters: {text[1:4]}")
```

Run it and observe how strings work.

---

### Exercise 2: Use String Methods

Create a file called `string_methods.py`:

```python
text = "Hello, World!"

# Case conversion
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")

# Searching
print(f"\nFind 'World': {text.find('World')}")
print(f"Count 'l': {text.count('l')}")
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with '!': {text.endswith('!')}")

# Replacing
print(f"\nReplace 'World' with 'Python': {text.replace('World', 'Python')}")

# Stripping whitespace
messy = "  hello world  "
print(f"\nOriginal: '{messy}'")
print(f"Strip: '{messy.strip()}'")
print(f"Lstrip: '{messy.lstrip()}'")
print(f"Rstrip: '{messy.rstrip()}'")

# Splitting and joining
sentence = "The quick brown fox"
words = sentence.split()
print(f"\nSplit: {words}")
print(f"Join: {' - '.join(words)}")
```

Run it and observe the output.

---

### Exercise 3: Format Strings with f-strings

Create a file called `formatting.py`:

```python
name = "Alice"
age = 30
price = 19.99

# Basic f-string
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price: {price}")

# Expressions inside f-strings
print(f"\nNext year: {age + 1}")
print(f"Doubled price: {price * 2}")
print(f"Name length: {len(name)}")

# Format specifiers
print(f"\nPrice with 2 decimals: ${price:.2f}")
print(f"Price with 4 decimals: ${price:.4f}")
print(f"Number with leading zeros: {age:03d}")
print(f"Percentage: {0.75:.1%}")

# Alignment
print(f"\nLeft align: '{name:<10}'")
print(f"Right align: '{name:>10}'")
print(f"Center: '{name:^10}'")
```

Run it and observe the formatting options.

---

## Practice Exercises

### Exercise 4: Work with Escape Sequences

Create a file called `escape_sequences.py`:

```python
# Newline
print("Line 1\nLine 2\nLine 3")

# Tab
print("Name\tAge\tCity")
print("Alice\t30\tNew York")
print("Bob\t25\tLos Angeles")

# Backslash
print("Path: C:\\Users\\Alice\\Documents")

# Quote inside string
print("She said \"Hello!\"")
print('It\'s a beautiful day.')

# Raw string (no escape sequences)
raw = r"C:\Users\Alice\Documents"
print(f"Raw string: {raw}")

# Unicode
print("Emoji: 🐍")
print("Greek: α β γ δ")
```

Run it and observe the escape sequences.

---

### Exercise 5: Check String Content

Create a file called `string_checks.py`:

```python
# Check character types
text = "Hello123"

print(f"'{text}':")
print(f"  isalpha: {text.isalpha()}")
print(f"  isdigit: {text.isdigit()}")
print(f"  isalnum: {text.isalnum()}")
print(f"  isupper: {text.isupper()}")
print(f"  islower: {text.islower()}")

# Test individual strings
print(f"\n'123':")
print(f"  isdigit: {'123'.isdigit()}")

print(f"\n'HELLO':")
print(f"  isupper: {'HELLO'.isupper()}")

print(f"\n'hello':")
print(f"  islower: {'hello'.islower()}")

print(f"\n'   ':")
print(f"  isspace: {'   '.isspace()}")
```

Run it and observe the string checking methods.

---

### Exercise 6: Slice and Manipulate Strings

Create a file called `string_slicing.py`:

```python
text = "Python Programming"

# Basic slicing
print(f"Original: {text}")
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[-11:]}")
print(f"Middle: {text[7:18]}")

# Slicing with step
print(f"\nEvery 2nd character: {text[::2]}")
print(f"Every 3rd character: {text[::3]}")
print(f"Reversed: {text[::-1]}")

# Practical examples
word = "hello"
print(f"\nWord: {word}")
print(f"Capitalized: {word[0].upper() + word[1:]}")
print(f"Reversed: {word[::-1]}")

# Extract parts
email = "alice@example.com"
at_index = email.find("@")
username = email[:at_index]
domain = email[at_index + 1:]
print(f"\nEmail: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}")
```

Run it and observe slicing patterns.

---

### Exercise 7: Build Strings Dynamically

Create a file called `string_building.py`:

```python
# Concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)

# Repetition
print("=" * 40)
print("Welcome to Python")
print("=" * 40)

# Join (preferred for multiple strings)
words = ["The", "quick", "brown", "fox"]
sentence = " ".join(words)
print(f"\nJoined: {sentence}")

# Build a formatted table
print("\nTable:")
print("Name".ljust(10) + "Age".ljust(5) + "City")
print("-" * 25)
print("Alice".ljust(10) + "30".ljust(5) + "New York")
print("Bob".ljust(10) + "25".ljust(5) + "Los Angeles")
print("Carol".ljust(10) + "28".ljust(5) + "Chicago")
```

Run it and observe string building techniques.

---

## Challenge Exercises

### Challenge 1: Analyze Text

Create a file called `text_analysis.py`:

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

# Test with different texts
analyze_text("Hello, World!")
print()
analyze_text("Python 3.10 is great!")
```

Run it and observe the analysis.

---

### Challenge 2: Create a Text Formatter

Create a file called `text_formatter.py`:

```python
def format_title(text, width=40):
    """Format text as a centered title."""
    return text.center(width, "=")

def format_paragraph(text, width=40):
    """Format text as a paragraph (simple version)."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(" ".join(current_line + [word])) <= width:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(" ".join(current_line))
    
    return "\n".join(lines)

# Use the formatters
print(format_title("Python Programming"))
print()
print(format_paragraph(
    "Python is a powerful and flexible programming language that is easy to learn and use.",
    width=30
))
```

Run it and observe the formatting.

---

### Challenge 3: Build a Simple Text Processor

Create a file called `text_processor.py`:

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
    
    # Replace common words
    replaced = text.replace("Python", "🐍")
    print(f"With emoji: {replaced}")

# Interactive processor
print("Text Processor")
user_text = input("Enter some text: ")
process_text(user_text)
```

Run it and test with different inputs.

---

### Challenge 4: Validate and Clean Input

Create a file called `input_cleaner.py`:

```python
def clean_name(name):
    """Clean and validate a name."""
    name = name.strip()
    if not name:
        return None
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
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) != 10:
        return None
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

# Test the cleaners
print("Name:", clean_name("  alice smith  "))
print("Email:", clean_email("  ALICE@EXAMPLE.COM  "))
print("Phone:", clean_phone("555-123-4567"))
print("Invalid name:", clean_name("alice123"))
print("Invalid email:", clean_email("alice@example"))
```

Run it and test with various inputs.

---

## Hints

**String is immutable** → You cannot change a character in place. Use slicing and concatenation to create new strings.

**Index out of range** → Strings have indices from 0 to len(string)-1. Use negative indices to count from the end.

**Unexpected slicing result** → Remember that slicing is exclusive of the end index: `text[0:3]` includes indices 0, 1, 2 but not 3.

**Method returns None** → Some string methods like `replace()` return a new string; they do not modify the original.

---

## What to Review If You Get Stuck

- **String literals** → Handbook section 3.2
- **String immutability** → Handbook section 3.1
- **Indexing and slicing** → Handbook section 3.3
- **String methods** → Handbook section 3.4
- **String formatting** → Handbook section 3.5
- **Escape sequences** → Handbook section 3.6
- **Raw strings** → Handbook section 3.7
- **String concatenation** → Handbook section 3.8
- **Checking string content** → Handbook section 3.9

---

## Key Takeaways

After completing these exercises, you should be able to:

- Create and manipulate strings
- Use string methods effectively
- Format strings with f-strings
- Slice and search strings
- Validate and clean text input
- Build strings dynamically
- Understand string immutability
