"""
CSV Read/Write - Reading and Writing CSV Files

This example demonstrates:
- Reading CSV files with csv.reader()
- Writing CSV files with csv.writer()
- Using DictReader and DictWriter
- Handling different delimiters
"""

import csv
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

print("=== Reading CSV Files ===")

# Read the sample_people.csv file
csv_file = SCRIPT_DIR / "sample_people.csv"

if csv_file.exists():
    print(f"Reading {csv_file.name}:")
    print()
    
    # Method 1: Using csv.reader()
    with open(csv_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        
        # Read header
        header = next(reader)
        print(f"Header: {header}")
        
        # Read rows
        for row_num, row in enumerate(reader, 2):
            print(f"Row {row_num}: {row}")
    print()

print("=== Reading CSV with DictReader ===")

# DictReader automatically uses the first row as field names
if csv_file.exists():
    print("Using DictReader:")
    with open(csv_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}, City: {row['city']}")
    print()

print("=== Writing CSV Files ===")

# Data to write
people = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Boston"],
    ["Charlie", "35", "Chicago"],
]

output_file = SCRIPT_DIR / "output.csv"

# Method 1: Using csv.writer()
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(people)

print(f"Written to {output_file}")
print()

# Verify the output
print("Content of output.csv:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())
print()

print("=== Writing CSV with DictWriter ===")

# Data as list of dicts
people_dicts = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Boston"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]

output_file2 = SCRIPT_DIR / "output_dict.csv"

fieldnames = ["name", "age", "city"]

with open(output_file2, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write rows
    writer.writerows(people_dicts)

print(f"Written to {output_file2}")

# Verify
print("Content of output_dict.csv:")
with open(output_file2, "r", encoding="utf-8") as f:
    print(f.read())
print()

print("=== Custom Delimiters ===")

# Tab-separated values (TSV)
tsv_file = SCRIPT_DIR / "output.tsv"

with open(tsv_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", "30", "New York"])
    writer.writerow(["Bob", "25", "Boston"])

print(f"Created TSV file: {tsv_file}")
print("Content:")
with open(tsv_file, "r", encoding="utf-8") as f:
    print(f.read())
print()

print("=== Handling Different Quote Styles ===")

# Quote all fields
output_file3 = SCRIPT_DIR / "output_quoted.csv"

with open(output_file3, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", "30", "New York"])
    writer.writerow(["Bob", "25", "Boston"])

print(f"Created quoted CSV: {output_file3}")
print("Content (all fields quoted):")
with open(output_file3, "r", encoding="utf-8") as f:
    print(f.read())
print()

print("=== Reading CSV with Custom Delimiter ===")

# Create a pipe-separated file
pipe_file = SCRIPT_DIR / "output_pipe.txt"
with open(pipe_file, "w", encoding="utf-8", newline="") as f:
    f.write("Name|Age|City\n")
    f.write("Alice|30|New York\n")
    f.write("Bob|25|Boston\n")

# Read it with custom delimiter
print(f"Reading pipe-separated file: {pipe_file.name}")
with open(pipe_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        print(f"  {row}")
print()

print("=== Error Handling ===")

# Handle missing file
missing_file = SCRIPT_DIR / "missing.csv"
try:
    with open(missing_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"File not found: {missing_file.name}")
print()

# Handle empty file
empty_file = SCRIPT_DIR / "empty.csv"
empty_file.touch()  # Create empty file

try:
    with open(empty_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except StopIteration:
    print(f"File is empty: {empty_file.name}")
print()

print("=== Practical Example: Processing CSV Data ===")

# Read people data, modify it, and write it back
if csv_file.exists():
    print("Processing CSV data:")
    
    # Read data
    people = []
    with open(csv_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert age to int
            row["age"] = int(row["age"])
            # Add a new field
            row["category"] = "Senior" if int(row["age"]) >= 30 else "Junior"
            people.append(row)
    
    # Write modified data
    output_file4 = SCRIPT_DIR / "output_processed.csv"
    fieldnames = ["name", "age", "city", "category"]
    
    with open(output_file4, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)
    
    print(f"Processed data written to {output_file4}")
    
    # Show result
    print("\nProcessed data:")
    with open(output_file4, "r", encoding="utf-8") as f:
        print(f.read())
