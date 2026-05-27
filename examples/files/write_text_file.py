"""
Write Text File - Writing Text Files in Python

This example demonstrates:
- Writing to new files
- Appending to existing files
- Using context managers (with statement)
- Writing multiple lines
"""

from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

print("=== Writing to a New File ===")

# Create a new file
output_file = SCRIPT_DIR / "output.txt"

# Method 1: Using write_text() (Python 3.10+)
content = "Hello, World!\nThis is a test file."
output_file.write_text(content, encoding="utf-8")
print(f"Written to {output_file}")
print(f"File exists: {output_file.exists()}")
print()

# Method 2: Using open() with "w" mode
with open(output_file, "w", encoding="utf-8") as f:
    f.write("This overwrites the previous content.\n")
print(f"Overwritten {output_file}")
print()

print("=== Appending to a File ===")

# Append to the file
with open(output_file, "a", encoding="utf-8") as f:
    f.write("This line is appended.\n")
    f.write("Another appended line.\n")
print("Appended two lines to output.txt")
print()

print("=== Reading Back the File ===")

if output_file.exists():
    print("Content of output.txt:")
    with open(output_file, "r", encoding="utf-8") as f:
        print(f.read())
print()

print("=== Writing Multiple Lines ===")

# Method 1: Using writelines() with a list
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n",
]

output_file2 = SCRIPT_DIR / "output2.txt"
with open(output_file2, "w", encoding="utf-8") as f:
    f.writelines(lines)
print(f"Written {len(lines)} lines to {output_file2}")

# Method 2: Using a generator expression
output_file3 = SCRIPT_DIR / "output3.txt"
with open(output_file3, "w", encoding="utf-8") as f:
    f.writelines(f"Number {i}\n" for i in range(1, 6))
print(f"Written numbers 1-5 to {output_file3}")
print()

print("=== Writing with f-strings ===")

name = "Alice"
age = 30
city = "New York"

output_file4 = SCRIPT_DIR / "output4.txt"
with open(output_file4, "w", encoding="utf-8") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"City: {city}\n")
print(f"Written person info to {output_file4}")

# Read it back
print("Content of output4.txt:")
with open(output_file4, "r", encoding="utf-8") as f:
    print(f.read())
print()

print("=== Writing Large Files ===")

# For large files, write in chunks
def write_large_file(file_path, num_lines=10000):
    """Write a large file in chunks."""
    with open(file_path, "w", encoding="utf-8") as f:
        for i in range(num_lines):
            f.write(f"This is line {i + 1}\n")
    print(f"Written {num_lines} lines to {file_path}")


large_file = SCRIPT_DIR / "large_output.txt"
write_large_file(large_file, num_lines=100)
print(f"First 3 lines of large_output.txt:")
with open(large_file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(f"  {line.rstrip()}")
        if i >= 2:
            break
print()

print("=== Writing Binary Files ===")

# For non-text files (images, etc.), use binary mode
binary_file = SCRIPT_DIR / "output.bin"
with open(binary_file, "wb") as f:
    f.write(b"Hello, Binary!\n")
    f.write(bytes([65, 66, 67]))  # Writes "ABC"
print(f"Written binary data to {binary_file}")

# Read it back
with open(binary_file, "rb") as f:
    content = f.read()
print(f"Binary content: {content}")
print()

print("=== Error Handling ===")

# Handle permission errors
try:
    # Try to write to a read-only location (might fail)
    # This is just an example - adjust path as needed
    readonly_file = Path("/tmp/readonly_test.txt")
    with open(readonly_file, "w") as f:
        f.write("test")
except PermissionError:
    print("Permission denied - cannot write to this location")
except OSError as e:
    print(f"OS error: {e}")
print()

print("=== Using pathlib for Writing ===")

# pathlib has write_text() and write_bytes()
output_path = SCRIPT_DIR / "pathlib_output.txt"
output_path.write_text("Written with pathlib!\n", encoding="utf-8")
print(f"Written with pathlib: {output_path}")

# Append with pathlib
output_path.write_text("Appended content\n", encoding="utf-8", append=True)
print("Appended content")
