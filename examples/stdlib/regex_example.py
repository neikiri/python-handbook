"""
Regex Example - Using Regular Expressions

This example demonstrates:
- Creating regex patterns
- Matching and searching
- Finding all matches
- Replacing text
- Common regex patterns
"""

import re

print("=== Creating Regex Patterns ===")

# Basic pattern
pattern = r"hello"  # r prefix for raw string
text = "hello world"

# Compile pattern (optional but recommended for reuse)
regex = re.compile(pattern)

# Check if pattern matches
match = regex.match(text)
print(f"Pattern: {pattern}")
print(f"Text: {text}")
print(f"Match found: {match is not None}")
print()

print("=== Matching vs Searching ===")

# match() - matches from the beginning of the string
text1 = "hello world"
text2 = "say hello"

pattern = r"hello"

print(f"Pattern: '{pattern}'")
print(f"Text 1: '{text1}'")
print(f"  match(): {re.match(pattern, text1)}")  # Match found
print(f"Text 2: '{text2}'")
print(f"  match(): {re.match(pattern, text2)}")  # No match (not at start)
print()

# search() - searches anywhere in the string
print(f"search() on text1: {re.search(pattern, text1)}")
print(f"search() on text2: {re.search(pattern, text2)}")  # Match found
print()

print("=== Finding All Matches ===")

text = "hello hello world hello again"
pattern = r"hello"

# Find all matches
matches = re.findall(pattern, text)
print(f"Text: '{text}'")
print(f"Pattern: '{pattern}'")
print(f"findall(): {matches}")
print(f"Number of matches: {len(matches)}")
print()

print("=== Match Objects ===")

text = "The price is $25.99"
pattern = r"\$(\d+\.\d+)"  # Match dollar amount

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")  # $25.99
    print(f"First group: {match.group(1)}")  # 25.99
    print(f"Match span: {match.span()}")  # (13, 20)
    print(f"Start: {match.start()}, End: {match.end()}")
print()

print("=== Common Pattern Examples ===")

# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = ["alice@example.com", "bob@test.org", "invalid-email"]

print("Email validation:")
for email in emails:
    is_valid = bool(re.match(email_pattern, email))
    print(f"  {email}: {is_valid}")
print()

# Phone number validation (US format)
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
phones = ["123-456-7890", "555-1234", "999-888-7777"]

print("Phone number validation:")
for phone in phones:
    is_valid = bool(re.match(phone_pattern, phone))
    print(f"  {phone}: {is_valid}")
print()

# URL pattern
url_pattern = r"https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?"
urls = [
    "https://example.com",
    "http://www.test.org/path",
    "not a url",
]

print("URL pattern:")
for url in urls:
    matches = re.findall(url_pattern, url)
    print(f"  {url}: {matches}")
print()

print("=== Grouping and Capturing ===")

text = "John Doe, Age: 30, City: New York"
pattern = r"(\w+) (\w+), Age: (\d+), City: (.+)"

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"First name: {match.group(1)}")
    print(f"Last name: {match.group(2)}")
    print(f"Age: {match.group(3)}")
    print(f"City: {match.group(4)}")
print()

print("=== Named Groups ===")

text = "Name: Alice, Age: 30"
pattern = r"Name: (?P<name>\w+), Age: (?P<age>\d+)"

match = re.search(pattern, text)
if match:
    print(f"Name (by name): {match.group('name')}")
    print(f"Age (by name): {match.group('age')}")
    print(f"All groups: {match.groupdict()}")
print()

print("=== Replacing Text ===")

# sub() - replace all matches
text = "Hello world, hello universe"
pattern = r"hello"

result = re.sub(pattern, "hi", text, flags=re.IGNORECASE)
print(f"Original: '{text}'")
print(f"Pattern: '{pattern}'")
print(f"Result: '{result}'")
print()

# sub() with function
def capitalize_match(match):
    """Capitalize the matched text."""
    return match.group(0).upper()


text = "hello world"
result = re.sub(r"\b\w+\b", capitalize_match, text)
print(f"Original: '{text}'")
print(f"Result (capitalize words): '{result}'")
print()

print("=== Splitting with Regex ===")

text = "apple,banana;cherry|date"
pattern = r"[,;|]"  # Split on comma, semicolon, or pipe

parts = re.split(pattern, text)
print(f"Original: '{text}'")
print(f"Pattern: '{pattern}'")
print(f"Parts: {parts}")
print()

print("=== Flags ===")

# re.IGNORECASE (i)
text = "Hello HELLO hello"
pattern = r"hello"

matches = re.findall(pattern, text, re.IGNORECASE)
print(f"Text: '{text}'")
print(f"Pattern: '{pattern}' (with IGNORECASE)")
print(f"Matches: {matches}")
print()

# re.MULTILINE (m)
text = "line 1\nline 2\nline 3"
pattern = r"^line"

# Without MULTILINE
print(f"Without MULTILINE: {re.findall(pattern, text)}")

# With MULTILINE
print(f"With MULTILINE: {re.findall(pattern, text, re.MULTILINE)}")
print()

# re.DOTALL (s)
text = "line 1\nline 2"
pattern = r"line.2"

# Without DOTALL (dot doesn't match newline)
print(f"Without DOTALL: {re.findall(pattern, text)}")

# With DOTALL (dot matches newline)
print(f"With DOTALL: {re.findall(pattern, text, re.DOTALL)}")
print()

print("=== Practical Examples ===")

# Extract all numbers from text
text = "Order #12345, Item: Widget, Price: $25.99, Qty: 3"
pattern = r"\d+"

numbers = re.findall(pattern, text)
print(f"Text: '{text}'")
print(f"Numbers found: {numbers}")

# Extract all words starting with capital letter
text = "Alice and Bob went to New York City"
pattern = r"\b[A-Z]\w*\b"

capitalized = re.findall(pattern, text)
print(f"\nText: '{text}'")
print(f"Capitalized words: {capitalized}")

# Remove extra whitespace
text = "This   is   a   test   string"
pattern = r"\s+"

cleaned = re.sub(pattern, " ", text).strip()
print(f"\nOriginal: '{text}'")
print(f"Cleaned: '{cleaned}'")
