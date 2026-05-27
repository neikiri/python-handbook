# Chapter 13: Files, Paths, JSON, and CSV — Exercises

## Overview

These exercises help you work with files and directories, parse and create JSON and CSV data, and handle paths portably. By the end, you will confidently read, write, and process data files.

---

## How to Use These Exercises

- Create a folder called `chapter-13` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Work with Paths

Create a file called `paths.py`:

```python
from pathlib import Path

# Create path objects
current = Path(".")
home = Path.home()
file_path = Path("data") / "file.txt"

print(f"Current: {current}")
print(f"Home: {home}")
print(f"File path: {file_path}")

# Path properties
print(f"\nAbsolute: {file_path.absolute()}")
print(f"Name: {file_path.name}")
print(f"Stem: {file_path.stem}")
print(f"Suffix: {file_path.suffix}")
print(f"Parent: {file_path.parent}")

# Check path properties
print(f"\nExists: {file_path.exists()}")
print(f"Is file: {file_path.is_file()}")
print(f"Is dir: {file_path.is_dir()}")

# Create directories
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
print(f"\nCreated directory: {data_dir}")

# List files
for item in Path(".").iterdir():
    if item.is_file():
        print(f"File: {item.name}")
```

Run it and observe path operations.

---

### Exercise 2: Read and Write Text Files

Create a file called `text_files.py`:

```python
from pathlib import Path

# Write to a file
content = """Hello, World!
This is a test file.
Python is great!"""

file_path = Path("test.txt")
file_path.write_text(content)
print(f"Wrote to {file_path}")

# Read entire file
text = file_path.read_text()
print(f"Content:\n{text}")

# Read line by line
print("\nLine by line:")
for line in file_path.read_text().splitlines():
    print(f"  {line}")

# Append to file
file_path.write_text(file_path.read_text() + "\nAppended line")
print(f"\nAppended to {file_path}")

# Read with context manager
print("\nUsing context manager:")
with open(file_path, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  {i}: {line.rstrip()}")

# Clean up
file_path.unlink()
print(f"\nDeleted {file_path}")
```

Run it and observe file operations.

---

### Exercise 3: Work with JSON

Create a file called `json_files.py`:

```python
import json
from pathlib import Path

# Create data
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}

# Write JSON
json_file = Path("data.json")
json_file.write_text(json.dumps(data, indent=2))
print(f"Wrote JSON to {json_file}")

# Read JSON
loaded = json.loads(json_file.read_text())
print(f"\nLoaded data:")
print(f"  Name: {loaded['name']}")
print(f"  Age: {loaded['age']}")
print(f"  Hobbies: {loaded['hobbies']}")

# Pretty print
print(f"\nPretty JSON:")
print(json.dumps(loaded, indent=2))

# List of objects
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 28},
]

people_file = Path("people.json")
people_file.write_text(json.dumps(people, indent=2))

loaded_people = json.loads(people_file.read_text())
print(f"\nLoaded {len(loaded_people)} people")
for person in loaded_people:
    print(f"  {person['name']}: {person['age']}")

# Clean up
json_file.unlink()
people_file.unlink()
```

Run it and observe JSON operations.

---

### Exercise 4: Work with CSV

Create a file called `csv_files.py`:

```python
import csv
from pathlib import Path

# Write CSV
csv_file = Path("data.csv")
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Carol", "28", "Chicago"],
]

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print(f"Wrote CSV to {csv_file}")

# Read CSV
print("\nRead CSV:")
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# Read as dictionaries
print("\nRead as dictionaries:")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']}: {row['Age']} years old")

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
print(f"\nWrote dictionaries to {dict_file}")

# Clean up
csv_file.unlink()
dict_file.unlink()
```

Run it and observe CSV operations.

---

## Practice Exercises

### Exercise 5: Process Multiple Files

Create a file called `process_files.py`:

```python
from pathlib import Path
import json

# Create sample files
data_dir = Path("sample_data")
data_dir.mkdir(exist_ok=True)

for i in range(3):
    file_path = data_dir / f"file_{i}.txt"
    file_path.write_text(f"Content of file {i}\nLine 2\nLine 3")

# Process all files
print("Processing files:")
for file_path in data_dir.glob("*.txt"):
    content = file_path.read_text()
    lines = content.splitlines()
    print(f"  {file_path.name}: {len(lines)} lines")

# Count total lines
total_lines = sum(
    len(file_path.read_text().splitlines())
    for file_path in data_dir.glob("*.txt")
)
print(f"\nTotal lines: {total_lines}")

# Clean up
import shutil
shutil.rmtree(data_dir)
```

Run it and observe file processing.

---

### Exercise 6: Convert Between Formats

Create a file called `format_conversion.py`:

```python
import json
import csv
from pathlib import Path

# Create sample data
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Carol", "age": 28, "city": "Chicago"},
]

# Save as JSON
json_file = Path("people.json")
json_file.write_text(json.dumps(people, indent=2))
print(f"Saved as JSON: {json_file}")

# Convert JSON to CSV
csv_file = Path("people.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(people)
print(f"Converted to CSV: {csv_file}")

# Read CSV and convert back to JSON
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    csv_data = list(reader)

# Convert age back to int
for person in csv_data:
    person["age"] = int(person["age"])

json_file2 = Path("people_from_csv.json")
json_file2.write_text(json.dumps(csv_data, indent=2))
print(f"Converted back to JSON: {json_file2}")

# Clean up
json_file.unlink()
csv_file.unlink()
json_file2.unlink()
```

Run it and observe format conversion.

---

### Exercise 7: Parse Configuration Files

Create a file called `config_files.py`:

```python
import json
from pathlib import Path

# Create a config file
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "features": ["auth", "logging", "caching"]
}

config_file = Path("config.json")
config_file.write_text(json.dumps(config, indent=2))
print(f"Created config file: {config_file}")

# Load and use config
loaded_config = json.loads(config_file.read_text())

print(f"\nApp: {loaded_config['app_name']} v{loaded_config['version']}")
print(f"Debug: {loaded_config['debug']}")
print(f"Database: {loaded_config['database']['host']}:{loaded_config['database']['port']}")
print(f"Features: {', '.join(loaded_config['features'])}")

# Update config
loaded_config["debug"] = False
loaded_config["features"].append("api")
config_file.write_text(json.dumps(loaded_config, indent=2))
print(f"\nUpdated config file")

# Clean up
config_file.unlink()
```

Run it and observe config file handling.

---

## Challenge Exercises

### Challenge 1: Build a Data Aggregator

Create a file called `data_aggregator.py`:

```python
import json
import csv
from pathlib import Path

# Create sample data files
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Create JSON file
json_data = [
    {"id": 1, "value": 100},
    {"id": 2, "value": 200},
]
(data_dir / "data.json").write_text(json.dumps(json_data))

# Create CSV file
csv_data = [["id", "value"], ["3", "300"], ["4", "400"]]
with open(data_dir / "data.csv", "w", newline="") as f:
    csv.writer(f).writerows(csv_data)

# Aggregate data
all_data = []

# Load JSON
json_file = data_dir / "data.json"
all_data.extend(json.loads(json_file.read_text()))

# Load CSV
csv_file = data_dir / "data.csv"
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        all_data.append({"id": int(row["id"]), "value": int(row["value"])})

# Process aggregated data
total = sum(item["value"] for item in all_data)
average = total / len(all_data)

print(f"Total items: {len(all_data)}")
print(f"Total value: {total}")
print(f"Average value: {average:.2f}")

# Save aggregated data
output_file = data_dir / "aggregated.json"
output_file.write_text(json.dumps(all_data, indent=2))
print(f"Saved to {output_file}")

# Clean up
import shutil
shutil.rmtree(data_dir)
```

Run it and observe data aggregation.

---

### Challenge 2: Implement a Simple Database

Create a file called `simple_database.py`:

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

# Use the database
db = SimpleDB("users.json")

# Add records
db.add({"id": 1, "name": "Alice", "age": 30})
db.add({"id": 2, "name": "Bob", "age": 25})

# Query
print("All users:")
for user in db.get_all():
    print(f"  {user}")

# Find
print("\nFind Alice:")
results = db.find("name", "Alice")
print(f"  {results}")

# Clean up
Path("users.json").unlink()
```

Run it and observe the simple database.

---

## Hints

**Path not found** → Use `Path.exists()` to check before reading. Use `Path.mkdir(exist_ok=True)` to create directories safely.

**JSON decode error** → Ensure the file contains valid JSON. Use `json.dumps()` to create valid JSON strings.

**CSV encoding issues** → Use `newline=""` when opening CSV files to avoid extra blank lines.

**File not closed** → Always use `with` statements or call `.close()` to ensure files are properly closed.

---

## What to Review If You Get Stuck

- **Path objects** → Handbook section 2.1
- **Reading and writing files** → Handbook section 2.2
- **JSON format** → Handbook section 2.3
- **CSV format** → Handbook section 2.4
- **Working with directories** → Handbook section 2.5
- **Error handling for files** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Use `pathlib.Path` for portable file paths
- Read and write text files
- Parse and create JSON data
- Read and write CSV files
- Process multiple files
- Convert between data formats
- Handle file errors gracefully
- Build simple file-based applications

