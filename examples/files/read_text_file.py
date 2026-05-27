"""
Read Text File - Reading Text Files in Python

This example demonstrates:
- Reading entire file content
- Reading line by line
- Reading into a list
- Using context managers (with statement)
"""

from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent


print("=== Reading Entire File ===")

# Read the sample_notes.txt file
notes_file = SCRIPT_DIR / "sample_notes.txt"

# Method 1: Using read_text() (Python 3.10+)
if notes_file.exists():
    content = notes_file.read_text()
    print("Content of sample_notes.txt:")
    print(content)
else:
    print("sample_notes.txt not found")
print()

# Method 2: Using open() and read()
if notes_file.exists():
    with open(notes_file, "r", encoding="utf-8") as f:
        content = f.read()
    print("Content (using open):")
    print(content)
print()

print("=== Reading Line by Line ===")

if notes_file.exists():
    print("Reading line by line:")
    with open(notes_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            # rstrip() removes trailing whitespace including newline
            print(f"Line {line_num}: {line.rstrip()}")
print()

print("=== Reading into a List ===")

if notes_file.exists():
    # Method 1: Using readlines()
    with open(notes_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print(f"File has {len(lines)} lines")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.rstrip()}")
    print()
    
    # Method 2: Using list(f)
    with open(notes_file, "r", encoding="utf-8") as f:
        lines = list(f)
    
    print(f"Same result with list(f): {len(lines)} lines")
print()

print("=== Using pathlib Path.read_text() ===")

if notes_file.exists():
    # read_text() is cleaner for simple cases
    content = notes_file.read_text(encoding="utf-8")
    print(f"File size: {len(content)} characters")
    print(f"First 50 chars: {content[:50]}...")
print()

print("=== Handling File Not Found ===")

# Try to read a file that doesn't exist
missing_file = SCRIPT_DIR / "missing.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"File not found: {missing_file}")

# Better: Check if file exists first
if missing_file.exists():
    content = missing_file.read_text()
else:
    print(f"File doesn't exist: {missing_file}")
print()

print("=== Reading with Different Encodings ===")

# Most text files use UTF-8
# But some might use other encodings

# UTF-8 (default in Python 3)
with open(notes_file, "r", encoding="utf-8") as f:
    content = f.read()
print(f"UTF-8 content length: {len(content)}")

# Other encodings (if needed):
# with open(file, "r", encoding="latin-1") as f:
# with open(file, "r", encoding="cp1252") as f:
print()

print("=== Reading Large Files ===")

# For large files, read in chunks
def read_in_chunks(file_path, chunk_size=1024):
    """Read file in chunks (memory efficient)."""
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


if notes_file.exists():
    print("Reading in chunks:")
    for i, chunk in enumerate(read_in_chunks(notes_file, chunk_size=20), 1):
        print(f"Chunk {i}: {repr(chunk[:50])}")
        if i >= 3:  # Only show first 3 chunks
            print("...")
            break
