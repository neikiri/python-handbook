"""
Simple Data Cleaning - Cleaning Data from Files

This example demonstrates:
- Reading data from CSV
- Cleaning and validating data
- Writing cleaned data back
- Handling common data issues
"""

import csv
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

print("=== Sample Data Issues ===")

# Create a sample dirty CSV file
dirty_data = [
    ["name", "age", "email", "score"],
    ["  Alice  ", "30", "alice@example.com", "85"],
    ["Bob", "  25  ", "bob@example.com", "92"],
    ["Charlie", "35", "  charlie@example.com  ", "78"],
    ["", "40", "david@example.com", "88"],
    ["Eve", "invalid", "eve@example.com", "95"],
    ["Frank", "28", "", "72"],
    ["Grace", "32", "grace@example.com", "invalid"],
]

dirty_file = SCRIPT_DIR / "dirty_data.csv"
with open(dirty_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dirty_data)

print(f"Created dirty data file: {dirty_file.name}")
print("Content:")
with open(dirty_file, "r", encoding="utf-8") as f:
    print(f.read())
print()

print("=== Cleaning Data ===")


def clean_string(value):
    """Strip whitespace from a string."""
    if value is None:
        return ""
    return str(value).strip()


def clean_age(value):
    """Clean and validate age."""
    value = clean_string(value)
    if not value:
        return None
    try:
        age = int(value)
        if 0 <= age <= 150:
            return age
        return None
    except ValueError:
        return None


def clean_email(value):
    """Clean and validate email."""
    value = clean_string(value)
    if not value:
        return None
    # Simple email validation (not comprehensive)
    if "@" in value and "." in value:
        return value.lower()
    return None


def clean_score(value):
    """Clean and validate score."""
    value = clean_string(value)
    if not value:
        return None
    try:
        score = float(value)
        if 0 <= score <= 100:
            return score
        return None
    except ValueError:
        return None


def clean_row(row):
    """Clean a single row of data."""
    return {
        "name": clean_string(row.get("name", "")),
        "age": clean_age(row.get("age")),
        "email": clean_email(row.get("email")),
        "score": clean_score(row.get("score")),
    }


def is_valid_row(row):
    """Check if a row has valid data."""
    # Must have a name and valid email
    if not row["name"]:
        return False
    if not row["email"]:
        return False
    return True


# Clean the data
cleaned_data = []
invalid_rows = []

with open(dirty_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    
    for row_num, row in enumerate(reader, 2):  # Start at 2 (header is row 1)
        cleaned = clean_row(row)
        
        if is_valid_row(cleaned):
            cleaned_data.append(cleaned)
        else:
            invalid_rows.append((row_num, row, cleaned))

print(f"Cleaned {len(cleaned_data)} valid rows")
print(f"Found {len(invalid_rows)} invalid rows")
print()

print("=== Cleaned Data ===")

for person in cleaned_data:
    print(f"Name: {person['name']}, Age: {person['age']}, "
          f"Email: {person['email']}, Score: {person['score']}")

print()

print("=== Invalid Rows ===")

for row_num, original, cleaned in invalid_rows:
    print(f"Row {row_num}:")
    print(f"  Original: {original}")
    print(f"  Cleaned: {cleaned}")
    print()

print("=== Writing Cleaned Data ===")

output_file = SCRIPT_DIR / "cleaned_data.csv"

with open(output_file, "w", encoding="utf-8", newline="") as f:
    fieldnames = ["name", "age", "email", "score"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(cleaned_data)

print(f"Written cleaned data to {output_file.name}")
print("Content:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())

print("=== Additional Cleaning Examples ===")

print("=== Example 1: Remove Duplicates ===")

# Create data with duplicates
data_with_duplicates = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
    {"name": "Alice", "age": 30, "email": "alice@example.com"},  # Duplicate
    {"name": "Charlie", "age": 35, "email": "charlie@example.com"},
    {"name": "Alice", "age": 31, "email": "alice2@example.com"},  # Different age
]

# Remove exact duplicates
seen = set()
unique_data = []
for item in data_with_duplicates:
    # Create a tuple of values to check for duplicates
    key = (item["name"], item["age"], item["email"])
    if key not in seen:
        seen.add(key)
        unique_data.append(item)

print(f"Original: {len(data_with_duplicates)} items")
print(f"Unique: {len(unique_data)} items")
print()

print("=== Example 2: Normalize Data ===")

# Normalize names to title case
for person in cleaned_data:
    person["name"] = person["name"].title()

print("Normalized names:")
for person in cleaned_data:
    print(f"  {person['name']}")

print()

print("=== Example 3: Filter Data ===")

# Filter people by age
adults = [p for p in cleaned_data if p["age"] and p["age"] >= 30]
print(f"Adults (age >= 30): {len(adults)}")
for person in adults:
    print(f"  {person['name']}: {person['age']}")

# Filter by score
high_scorers = [p for p in cleaned_data if p["score"] and p["score"] >= 85]
print(f"\nHigh scorers (score >= 85): {len(high_scorers)}")
for person in high_scorers:
    print(f"  {person['name']}: {person['score']}")

print()

print("=== Example 4: Calculate Statistics ===")

# Calculate average score
scores = [p["score"] for p in cleaned_data if p["score"]]
if scores:
    avg_score = sum(scores) / len(scores)
    min_score = min(scores)
    max_score = max(scores)
    
    print(f"Score statistics:")
    print(f"  Average: {avg_score:.1f}")
    print(f"  Min: {min_score}")
    print(f"  Max: {max_score}")
