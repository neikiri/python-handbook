# File I/O Cheatsheet

Quick reference for reading, writing, and working with files in Python.

## Pathlib Basics

```python
from pathlib import Path

# Create path objects
p = Path("file.txt")
p = Path("folder/file.txt")
p = Path.cwd()  # Current working directory
p = Path.home()  # Home directory

# Path operations
p.exists()  # Check if path exists
p.is_file()  # Check if it's a file
p.is_dir()  # Check if it's a directory
p.parent  # Parent directory
p.name  # Filename
p.stem  # Filename without extension
p.suffix  # File extension
p.with_name("new.txt")  # Change filename
p.with_suffix(".py")  # Change extension

# Create directories
p.mkdir(parents=True, exist_ok=True)

# List files
for file in Path("folder").glob("*.txt"):
    print(file)
```

## Reading Text Files

```python
from pathlib import Path

# Read entire file
content = Path("file.txt").read_text(encoding="utf-8")

# Read line by line
with open("file.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Read all lines as list
with open("file.txt", encoding="utf-8") as f:
    lines = f.readlines()

# Using pathlib
lines = Path("file.txt").read_text(encoding="utf-8").splitlines()
```

## Writing Text Files

```python
from pathlib import Path

# Write (overwrites if exists)
Path("file.txt").write_text("Hello, World!", encoding="utf-8")

# Write with open
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")
    f.write("\nSecond line")
```

## Appending Text

```python
# Append to file
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("\nNew line")

# Using pathlib
content = Path("file.txt").read_text(encoding="utf-8")
content += "\nNew line"
Path("file.txt").write_text(content, encoding="utf-8")
```

## File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites) |
| `"a"` | Append |
| `"x"` | Create (fails if exists) |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`) |
| `"+"` | Read and write (e.g., `"r+"`) |

## JSON

```python
import json
from pathlib import Path

# Read JSON
data = json.loads(json_string)
data = json.load(open("file.json"))

# Using pathlib
data = json.loads(Path("file.json").read_text())

# Write JSON
json_string = json.dumps(data, indent=2)
Path("file.json").write_text(json.dumps(data, indent=2))

# Write with open
with open("file.json", "w") as f:
    json.dump(data, f, indent=2)

# Example
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)  # '{"name": "Alice", "age": 30}'
parsed = json.loads(json_str)  # {"name": "Alice", "age": 30}
```

## CSV

```python
import csv
from pathlib import Path

# Read CSV
with open("file.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Each row is a list

# Read CSV as dictionaries
with open("file.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # Each row is a dict

# Write CSV
with open("file.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])

# Write CSV from dictionaries
with open("file.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 30})
```

## Common Patterns

```python
# Read and process lines
with open("file.txt") as f:
    for line in f:
        line = line.strip()
        if line:  # Skip empty lines
            print(line)

# Count lines
with open("file.txt") as f:
    line_count = sum(1 for _ in f)

# Read file into list
with open("file.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

# Process CSV and write results
import csv
with open("input.csv") as infile, open("output.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        row["processed"] = row["value"].upper()
        writer.writerow(row)

# Safe file operations with pathlib
p = Path("file.txt")
if p.exists():
    content = p.read_text()
else:
    print("File not found")
```

## Encoding

Always specify `encoding="utf-8"` for text files:

```python
# Good
with open("file.txt", encoding="utf-8") as f:
    content = f.read()

# Also good
Path("file.txt").read_text(encoding="utf-8")

# Avoid (uses system default, may cause issues)
with open("file.txt") as f:
    content = f.read()
```

## Common File Mistakes

- **Not closing files**: Use `with` statement to ensure files are closed
- **Forgetting `newline=""` in CSV**: Required when writing CSV files
- **Not specifying encoding**: Always use `encoding="utf-8"`
- **Mixing pathlib and os.path**: Pick one and stick with it (prefer pathlib)
- **Assuming file exists**: Check with `Path.exists()` before reading
- **Modifying while reading**: Read entire file first, then modify
- **Relative paths**: Be aware of current working directory; use `Path.cwd()` to check
- **Binary vs text mode**: Use `"rb"` for binary, `"r"` for text