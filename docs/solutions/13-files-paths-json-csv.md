# Solutions 13: Files, Paths, JSON, and CSV

## Overview

Chapter 13 exercises cover working with file paths using `pathlib`, reading and writing text files, parsing and creating JSON data, reading and writing CSV files, and converting between formats. This guide explains the reasoning behind each solution and highlights portable, idiomatic file handling.

---

## Notes Before Checking Solutions

File handling is one of the most common sources of bugs in Python programs. The two most important habits are: always use `with` statements so files are closed automatically, and always use `pathlib.Path` instead of string concatenation for paths.

---

## Warm-up Exercise Solutions

### Exercise 1: Work with Paths

```python
from pathlib import Path

current = Path(".")
home = Path.home()
file_path = Path("data") / "file.txt"

print(file_path.name)    # file.txt
print(file_path.stem)    # file
print(file_path.suffix)  # .txt
print(file_path.parent)  # data

# Check existence
file_path.exists()   # False (doesn't exist yet)
file_path.is_file()  # False
file_path.is_dir()   # False

# Create directory safely
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)  # no error if already exists

# List files
for item in Path(".").iterdir():
    if item.is_file():
        print(item.name)
```

**Use `/` to join paths.** `Path("data") / "file.txt"` is portable — it works on Windows, macOS, and Linux. String concatenation like `"data" + "/" + "file.txt"` breaks on Windows.

**`exist_ok=True`** prevents an error if the directory already exists. Without it, `mkdir()` raises `FileExistsError` on the second call.

**`Path.home()`** returns the user's home directory in a portable way. On Windows it returns `C:\Users\username`, on macOS/Linux it returns `/home/username` or `/Users/username`.

---

### Exercise 2: Read and Write Text Files

```python
from pathlib import Path

content = "Hello, World!\nThis is a test file.\nPython is great!"

file_path = Path("test.txt")

# Write
file_path.write_text(content)

# Read entire file
text = file_path.read_text()

# Read line by line
for line in file_path.read_text().splitlines():
    print(line)

# Using context manager (more control)
with open(file_path, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.rstrip()}")

# Delete
file_path.unlink()
```

**`Path.write_text()` and `Path.read_text()`** are convenient for small files. For large files or when you need to process line by line without loading everything into memory, use `open()` with a `with` statement.

**`line.rstrip()`** removes the trailing newline that `readline()` and iteration include. `splitlines()` handles this automatically.

**`file_path.unlink()`** deletes the file. Use `unlink(missing_ok=True)` (Python 3.8+) to avoid an error if the file does not exist.

---

### Exercise 3: Work with JSON

```python
import json
from pathlib import Path

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding", "hiking"],
    "address": {"street": "123 Main St", "zip": "10001"},
}

# Write JSON
json_file = Path("data.json")
json_file.write_text(json.dumps(data, indent=2))

# Read JSON
loaded = json.loads(json_file.read_text())
print(loaded["name"])     # Alice
print(loaded["hobbies"])  # ['reading', 'coding', 'hiking']

# Pretty print
print(json.dumps(loaded, indent=2))

# Clean up
json_file.unlink()
```

**`json.dumps()` vs. `json.dump()`:** `dumps()` returns a string; `dump()` writes directly to a file object. Both are useful — `dumps()` pairs well with `Path.write_text()`, while `dump()` pairs with `open()`.

**`indent=2`** makes the JSON human-readable. Omit it for compact output (smaller files, faster to write).

**JSON supports:** strings, numbers, booleans, `null`, arrays, and objects. Python types map as: `dict` → object, `list`/`tuple` → array, `str` → string, `int`/`float` → number, `True`/`False` → `true`/`false`, `None` → `null`.

---

### Exercise 4: Work with CSV

```python
import csv
from pathlib import Path

# Write CSV
csv_file = Path("data.csv")
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
]

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read as dictionaries (uses first row as keys)
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']}: {row['Age']} years old")

# Write dictionaries
dict_data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
]

dict_file = Path("people.csv")
with open(dict_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(dict_data)

# Clean up
csv_file.unlink()
dict_file.unlink()
```

**`newline=""`** is required when opening CSV files on Windows. Without it, the `csv` module's own newline handling conflicts with the OS newline translation, producing extra blank lines.

**`DictReader`** is usually more convenient than `reader` because you access fields by name instead of index. It is also more robust when columns are reordered.

**CSV values are always strings.** When you read a CSV, numbers come back as strings. Convert them explicitly: `int(row["age"])` or `float(row["price"])`.

---

## Practice Exercise Solutions

### Exercise 5: Process Multiple Files

```python
from pathlib import Path
import shutil

data_dir = Path("sample_data")
data_dir.mkdir(exist_ok=True)

for i in range(3):
    file_path = data_dir / f"file_{i}.txt"
    file_path.write_text(f"Content of file {i}\nLine 2\nLine 3")

# Process all .txt files
for file_path in data_dir.glob("*.txt"):
    lines = file_path.read_text().splitlines()
    print(f"{file_path.name}: {len(lines)} lines")

# Count total lines
total_lines = sum(
    len(fp.read_text().splitlines())
    for fp in data_dir.glob("*.txt")
)
print(f"Total lines: {total_lines}")

# Clean up
shutil.rmtree(data_dir)
```

**`Path.glob("*.txt")`** returns a generator of matching paths. Use `"**/*.txt"` to search recursively through subdirectories.

**`shutil.rmtree()`** removes a directory and all its contents. Use with care — it is not reversible.

---

### Exercise 6: Convert Between Formats

```python
import json
import csv
from pathlib import Path

people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
]

# Save as JSON
json_file = Path("people.json")
json_file.write_text(json.dumps(people, indent=2))

# Convert JSON to CSV
csv_file = Path("people.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(people)

# Read CSV and convert back to JSON
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    csv_data = list(reader)

# Restore numeric types
for person in csv_data:
    person["age"] = int(person["age"])

json_file2 = Path("people_from_csv.json")
json_file2.write_text(json.dumps(csv_data, indent=2))

# Clean up
for f in [json_file, csv_file, json_file2]:
    f.unlink()
```

**Type restoration after CSV round-trip** is necessary because CSV stores everything as text. Always convert numeric fields back to `int` or `float` after reading from CSV.

---

### Exercise 7: Parse Configuration Files

```python
import json
from pathlib import Path

config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "database": {"host": "localhost", "port": 5432, "name": "mydb"},
    "features": ["auth", "logging", "caching"],
}

config_file = Path("config.json")
config_file.write_text(json.dumps(config, indent=2))

# Load and use
loaded = json.loads(config_file.read_text())
print(f"App: {loaded['app_name']} v{loaded['version']}")
print(f"DB: {loaded['database']['host']}:{loaded['database']['port']}")

# Update and save
loaded["debug"] = False
loaded["features"].append("api")
config_file.write_text(json.dumps(loaded, indent=2))

config_file.unlink()
```

**JSON is a good format for configuration files** because it is human-readable, widely supported, and maps directly to Python dicts. For more complex configs, consider `tomllib` (Python 3.11+) or `configparser` from the standard library.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Data Aggregator

```python
import json
import csv
from pathlib import Path
import shutil

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Create source files
json_data = [{"id": 1, "value": 100}, {"id": 2, "value": 200}]
(data_dir / "data.json").write_text(json.dumps(json_data))

csv_data = [["id", "value"], ["3", "300"], ["4", "400"]]
with open(data_dir / "data.csv", "w", newline="") as f:
    csv.writer(f).writerows(csv_data)

# Aggregate
all_data = []

all_data.extend(json.loads((data_dir / "data.json").read_text()))

with open(data_dir / "data.csv", "r") as f:
    for row in csv.DictReader(f):
        all_data.append({"id": int(row["id"]), "value": int(row["value"])})

total = sum(item["value"] for item in all_data)
average = total / len(all_data)

print(f"Total items: {len(all_data)}")
print(f"Total value: {total}")
print(f"Average value: {average:.2f}")

(data_dir / "aggregated.json").write_text(json.dumps(all_data, indent=2))

shutil.rmtree(data_dir)
```

---

### Challenge 2: Implement a Simple Database

```python
import json
from pathlib import Path

class SimpleDB:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.data = self._load()

    def _load(self):
        if self.filename.exists():
            return json.loads(self.filename.read_text())
        return []

    def _save(self):
        self.filename.write_text(json.dumps(self.data, indent=2))

    def add(self, record):
        self.data.append(record)
        self._save()

    def get_all(self):
        return self.data

    def find(self, key, value):
        return [r for r in self.data if r.get(key) == value]

    def delete(self, key, value):
        self.data = [r for r in self.data if r.get(key) != value]
        self._save()

db = SimpleDB("users.json")
db.add({"id": 1, "name": "Alice", "age": 30})
db.add({"id": 2, "name": "Bob", "age": 25})

print(db.find("name", "Alice"))  # [{'id': 1, 'name': 'Alice', 'age': 30}]

Path("users.json").unlink()
```

**`_save()` after every mutation** keeps the file in sync with the in-memory state. For high-frequency writes, consider batching saves or using a proper database like SQLite.

**`r.get(key)`** is safer than `r[key]` — it returns `None` instead of raising `KeyError` if the key is missing.

---

## Common Mistakes

**Forgetting `newline=""` for CSV files.** On Windows, this causes extra blank lines between rows. Always include `newline=""` when opening CSV files.

**Not converting CSV values from strings.** CSV stores everything as text. `row["age"]` is `"30"`, not `30`. Convert explicitly.

**Using string concatenation for paths.** `"data/" + filename` breaks on Windows. Use `Path("data") / filename` instead.

**Not handling `FileNotFoundError`.** Always check `path.exists()` or wrap reads in `try-except FileNotFoundError` when the file might not exist.

**Leaving files open.** Always use `with open(...)` to ensure files are closed even if an exception occurs.

---

## What to Review Next

- Chapter 12: Errors, Exceptions, and Debugging — handling file errors gracefully
- Chapter 14: Modules, Packages, and Imports — organizing file-handling code into modules
- Chapter 21: Working with Data — applying file I/O to real data processing tasks
