# Chapter 13: Files, Paths, JSON, and CSV

## 1. Overview

Most real programs need to read data from somewhere and write results
somewhere. That somewhere is usually the filesystem. Python makes file I/O
straightforward, and its standard library includes everything you need to work
with the two most common data formats: JSON and CSV.

This chapter covers reading and writing text and binary files, navigating the
filesystem with `pathlib`, and processing structured data with the `json` and
`csv` modules.

---

## 2. What You Will Learn

- Opening, reading, and writing text files
- The `with` statement and why it matters
- Reading files line by line
- Writing and appending to files
- Working with binary files
- Navigating the filesystem with `pathlib`
- Common path operations: joining, checking existence, listing directories
- Reading and writing JSON with the `json` module
- Reading and writing CSV with the `csv` module
- Handling encoding issues

---

## 3. Core Concepts

### 3.1 Opening Files

Use the built-in `open()` function to open a file. It returns a file object.

```python
f = open("notes.txt", "r", encoding="utf-8")
content = f.read()
f.close()
```

The second argument is the **mode**:

| Mode | Meaning |
|---|---|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates the file or truncates it if it exists. |
| `"a"` | Append. Creates the file if it does not exist. |
| `"x"` | Exclusive creation. Fails if the file already exists. |
| `"b"` | Binary mode (combine with others: `"rb"`, `"wb"`). |
| `"t"` | Text mode (default, combine with others: `"rt"`, `"wt"`). |
| `"+"` | Read and write (combine with others: `"r+"`, `"w+"`). |

Always specify `encoding="utf-8"` for text files. If you omit it, Python uses
the platform default, which varies between operating systems and can cause
subtle bugs.

---

### 3.2 The `with` Statement

Always open files with a `with` statement. It automatically closes the file
when the block exits — even if an exception occurs.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
# f is closed here automatically
```

Without `with`, you must call `f.close()` manually. If an exception occurs
before `close()`, the file stays open. The `with` statement eliminates this
risk.

---

### 3.3 Reading Files

#### Read the entire file at once

```python
with open("notes.txt", encoding="utf-8") as f:
    content = f.read()   # returns a single string
print(content)
```

#### Read all lines into a list

```python
with open("notes.txt", encoding="utf-8") as f:
    lines = f.readlines()   # returns a list of strings, each ending with '\n'

for line in lines:
    print(line.rstrip())   # strip the trailing newline
```

#### Read line by line (memory-efficient)

For large files, iterate over the file object directly. Python reads one line
at a time without loading the whole file into memory.

```python
with open("large_file.txt", encoding="utf-8") as f:
    for line in f:
        process(line.rstrip())
```

#### Read a single line

```python
with open("notes.txt", encoding="utf-8") as f:
    first_line = f.readline()   # reads up to and including '\n'
```

---

### 3.4 Writing Files

#### Write mode (`"w"`) — creates or overwrites

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")
    f.write("Second line.\n")
```

`write()` does not add a newline automatically. You must include `\n` where
you want line breaks.

#### Write multiple lines at once

```python
lines = ["line one", "line two", "line three"]

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(line + "\n" for line in lines)
```

`writelines()` accepts any iterable of strings. It does not add newlines
between items.

#### Append mode (`"a"`) — adds to the end

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry.\n")
```

---

### 3.5 Binary Files

Use binary mode (`"rb"`, `"wb"`) when working with non-text files: images,
audio, executables, or any file where you need exact byte control.

```python
# Copy a binary file
with open("photo.jpg", "rb") as src:
    data = src.read()

with open("photo_copy.jpg", "wb") as dst:
    dst.write(data)
```

In binary mode, `read()` returns `bytes`, not `str`. You cannot use
`encoding` with binary mode.

---

### 3.6 Working with Paths Using `pathlib`

The `pathlib` module provides `Path` objects that represent filesystem paths.
They are cleaner and more powerful than string-based path manipulation.

```python
from pathlib import Path
```

#### Creating a Path

```python
p = Path("docs/handbook/01-introduction.md")
p = Path("/home/user/projects")
p = Path.home()          # user's home directory
p = Path.cwd()           # current working directory
```

#### Joining paths

Use `/` to join path components — it works on all platforms.

```python
base = Path("data")
file = base / "2024" / "report.csv"
print(file)   # data/2024/report.csv
```

#### Inspecting a path

```python
p = Path("docs/handbook/01-introduction.md")

print(p.name)       # 01-introduction.md
print(p.stem)       # 01-introduction
print(p.suffix)     # .md
print(p.parent)     # docs/handbook
print(p.parts)      # ('docs', 'handbook', '01-introduction.md')
print(p.is_absolute())  # False
print(p.resolve())  # absolute path
```

#### Checking existence

```python
p = Path("config.json")

print(p.exists())    # True or False
print(p.is_file())   # True if it exists and is a file
print(p.is_dir())    # True if it exists and is a directory
```

#### Reading and writing with Path

`Path` objects have `read_text()` and `write_text()` methods that open, read
or write, and close the file in one call.

```python
# Read
content = Path("notes.txt").read_text(encoding="utf-8")

# Write (creates or overwrites)
Path("output.txt").write_text("Hello, world!\n", encoding="utf-8")

# Binary
data = Path("photo.jpg").read_bytes()
Path("copy.jpg").write_bytes(data)
```

These are convenient for simple cases. Use `open()` with `with` when you need
more control (appending, reading line by line, etc.).

#### Listing directory contents

```python
p = Path("docs")

# All items in the directory
for item in p.iterdir():
    print(item)

# Only files
for item in p.iterdir():
    if item.is_file():
        print(item.name)

# Recursive glob — all Markdown files
for md_file in p.rglob("*.md"):
    print(md_file)

# Non-recursive glob — Markdown files in docs/ only
for md_file in p.glob("*.md"):
    print(md_file)
```

#### Creating and removing

```python
# Create a directory (and any missing parents)
Path("output/reports/2024").mkdir(parents=True, exist_ok=True)

# Create an empty file
Path("placeholder.txt").touch()

# Remove a file
Path("temp.txt").unlink(missing_ok=True)

# Remove an empty directory
Path("empty_dir").rmdir()
```

#### Renaming and moving

```python
old = Path("draft.txt")
new = old.rename("final.txt")          # rename in place
moved = old.rename("archive/draft.txt")  # move to another directory
```

---

### 3.7 JSON

JSON (JavaScript Object Notation) is a text format for structured data. It
maps naturally to Python dicts, lists, strings, numbers, booleans, and `None`.

| JSON | Python |
|---|---|
| `object` `{}` | `dict` |
| `array` `[]` | `list` |
| `string` `""` | `str` |
| `number` | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

#### Reading JSON from a file

```python
import json

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

print(config["host"])
print(config["port"])
```

#### Writing JSON to a file

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "languages": ["Python", "JavaScript"],
    "active": True,
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

The `indent` parameter makes the output human-readable. Omit it for compact
output.

#### JSON from and to strings

Use `json.loads()` to parse a JSON string, and `json.dumps()` to serialize
Python data to a JSON string.

```python
import json

# Parse a JSON string
raw = '{"name": "Bob", "score": 95}'
parsed = json.loads(raw)
print(parsed["name"])   # Bob

# Serialize to a JSON string
data = {"x": 1, "y": 2}
text = json.dumps(data)
print(text)   # {"x": 1, "y": 2}

text_pretty = json.dumps(data, indent=2)
print(text_pretty)
# {
#   "x": 1,
#   "y": 2
# }
```

#### What JSON cannot represent

JSON does not support Python-specific types like `datetime`, `set`, `tuple`,
or custom objects. Trying to serialize them raises a `TypeError`.

```python
import json
from datetime import date

data = {"today": date.today()}
json.dumps(data)   # TypeError: Object of type date is not JSON serializable
```

Convert unsupported types to strings or numbers before serializing:

```python
data = {"today": date.today().isoformat()}
print(json.dumps(data))   # {"today": "2024-03-15"}
```

---

### 3.8 CSV

CSV (Comma-Separated Values) is a plain-text format for tabular data. Each
line is a row; fields within a row are separated by commas (or another
delimiter).

Python's `csv` module handles quoting, escaping, and different delimiters
correctly. Do not try to parse CSV by splitting on commas — edge cases will
break your code.

#### Reading CSV

```python
import csv

with open("students.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # each row is a list of strings
```

Always pass `newline=""` when opening CSV files. This lets the `csv` module
handle line endings correctly across platforms.

#### Reading CSV with a header row

```python
import csv

with open("students.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)   # read the first row as the header
    print(f"Columns: {header}")
    for row in reader:
        print(row)
```

#### Reading CSV as dicts

`csv.DictReader` maps each row to a dict using the header row as keys.

```python
import csv

with open("students.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['grade']}")
```

This is usually more readable than indexing by column number.

#### Writing CSV

```python
import csv

rows = [
    ["name", "age", "city"],
    ["Alice", "30", "Paris"],
    ["Bob", "25", "London"],
    ["Charlie", "35", "Berlin"],
]

with open("people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

#### Writing CSV from dicts

```python
import csv

people = [
    {"name": "Alice", "age": 30, "city": "Paris"},
    {"name": "Bob",   "age": 25, "city": "London"},
]

fieldnames = ["name", "age", "city"]

with open("people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)
```

#### Custom delimiters

Some CSV files use semicolons or tabs instead of commas.

```python
import csv

# Tab-separated values
with open("data.tsv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)
```

---

### 3.9 Encoding

Text files store bytes, not characters. An **encoding** defines how characters
map to bytes. The most common encoding is UTF-8, which handles virtually all
characters in all languages.

Always specify `encoding="utf-8"` when opening text files. If you open a file
with the wrong encoding, you will get garbled text or a `UnicodeDecodeError`.

```python
# Safe — explicit UTF-8
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

# Risky — uses platform default (may not be UTF-8 on Windows)
with open("data.txt") as f:
    content = f.read()
```

If you receive a file with an unknown encoding, try `"utf-8"` first. If that
fails, try `"latin-1"` (also called `"iso-8859-1"`), which accepts any byte
sequence without error (though it may misinterpret some characters).

---

## 4. Practical Examples

### 4.1 Word Frequency Counter

```python
from pathlib import Path
from collections import Counter


def word_frequency(path: str | Path) -> Counter:
    """Count word frequencies in a text file."""
    text = Path(path).read_text(encoding="utf-8").lower()
    words = text.split()
    # Strip punctuation from each word
    cleaned = [word.strip(".,!?;:\"'()[]{}") for word in words]
    return Counter(w for w in cleaned if w)


# Usage:
# freq = word_frequency("chapter.txt")
# for word, count in freq.most_common(10):
#     print(f"{word:20} {count}")
```

---

### 4.2 Config File with JSON

```python
import json
from pathlib import Path


DEFAULT_CONFIG = {
    "theme": "light",
    "font_size": 14,
    "autosave": True,
    "recent_files": [],
}


def load_config(path: str | Path) -> dict:
    """Load config from JSON, falling back to defaults."""
    p = Path(path)
    if not p.exists():
        return DEFAULT_CONFIG.copy()
    try:
        with p.open(encoding="utf-8") as f:
            loaded = json.load(f)
        # Merge with defaults so new keys are always present
        return {**DEFAULT_CONFIG, **loaded}
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not load config ({e}). Using defaults.")
        return DEFAULT_CONFIG.copy()


def save_config(config: dict, path: str | Path) -> None:
    """Save config to a JSON file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {p}.")


# Usage:
# config = load_config("~/.myapp/config.json")
# config["theme"] = "dark"
# save_config(config, "~/.myapp/config.json")
```

---

### 4.3 CSV Report Generator

```python
import csv
from pathlib import Path


def generate_sales_report(records: list[dict], output_path: str | Path) -> None:
    """Write a sales report CSV from a list of record dicts."""
    if not records:
        print("No records to write.")
        return

    fieldnames = list(records[0].keys())
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Wrote {len(records)} records to {output}.")


sales = [
    {"product": "Widget A", "units": 120, "revenue": 2400.00},
    {"product": "Widget B", "units": 85,  "revenue": 3400.00},
    {"product": "Gadget X", "units": 42,  "revenue": 8400.00},
]

generate_sales_report(sales, "reports/sales.csv")
```

---

### 4.4 Reading a CSV and Computing Statistics

```python
import csv
from pathlib import Path


def summarize_grades(path: str | Path) -> None:
    """Print grade statistics from a CSV file with 'name' and 'grade' columns."""
    grades = []

    with Path(path).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                grades.append(float(row["grade"]))
            except (KeyError, ValueError):
                print(f"Skipping invalid row: {row}")

    if not grades:
        print("No valid grades found.")
        return

    print(f"Count:   {len(grades)}")
    print(f"Average: {sum(grades) / len(grades):.1f}")
    print(f"Highest: {max(grades):.1f}")
    print(f"Lowest:  {min(grades):.1f}")
    passing = sum(1 for g in grades if g >= 60)
    print(f"Passing: {passing}/{len(grades)}")
```

---

### 4.5 Recursive Directory Scanner

```python
from pathlib import Path


def scan_directory(root: str | Path, extension: str = ".py") -> list[Path]:
    """Return all files with the given extension under root."""
    return sorted(Path(root).rglob(f"*{extension}"))


def print_tree(root: str | Path, extension: str = ".py") -> None:
    """Print a simple tree of matching files."""
    files = scan_directory(root, extension)
    print(f"Found {len(files)} {extension} files under {root}:\n")
    for f in files:
        rel = f.relative_to(root)
        depth = len(rel.parts) - 1
        indent = "  " * depth
        print(f"{indent}{f.name}")


# Usage:
# print_tree(".", ".md")
```

---

### 4.6 JSON Lines Format

JSON Lines (`.jsonl`) stores one JSON object per line. It is useful for
streaming large datasets because you can process one record at a time.

```python
import json
from pathlib import Path


def write_jsonl(records: list[dict], path: str | Path) -> None:
    """Write records to a JSON Lines file."""
    with Path(path).open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")


def read_jsonl(path: str | Path):
    """Yield records from a JSON Lines file."""
    with Path(path).open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


events = [
    {"event": "login",  "user": "alice", "ts": "2024-01-15T09:00:00"},
    {"event": "view",   "user": "alice", "ts": "2024-01-15T09:01:30"},
    {"event": "logout", "user": "alice", "ts": "2024-01-15T09:45:00"},
]

write_jsonl(events, "events.jsonl")

for record in read_jsonl("events.jsonl"):
    print(record["event"], record["user"])
```

---

### 4.7 Safe Atomic File Write

Writing to a file directly risks leaving it in a partial state if the program
crashes mid-write. Write to a temporary file first, then rename it.

```python
import json
import os
from pathlib import Path


def atomic_write_json(data: dict, path: str | Path) -> None:
    """Write JSON to a file atomically using a temporary file."""
    p = Path(path)
    tmp = p.with_suffix(".tmp")
    try:
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        tmp.replace(p)   # atomic on most platforms
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


# Usage:
# atomic_write_json({"key": "value"}, "config.json")
```

---

## 5. Common Mistakes

### 5.1 Forgetting to Close Files

Without `with`, you must call `f.close()` manually. If an exception occurs
first, the file stays open.

```python
# Risky
f = open("data.txt")
content = f.read()   # what if this raises?
f.close()            # may never run

# Safe
with open("data.txt") as f:
    content = f.read()
```

---

### 5.2 Omitting `encoding`

Omitting `encoding` uses the platform default, which is not always UTF-8.
This causes `UnicodeDecodeError` or garbled text on some systems.

```python
# Risky — platform-dependent encoding
with open("data.txt") as f:
    content = f.read()

# Safe
with open("data.txt", encoding="utf-8") as f:
    content = f.read()
```

---

### 5.3 Forgetting `newline=""` for CSV

Without `newline=""`, the `csv` module may mishandle line endings, especially
on Windows, producing extra blank rows.

```python
# Wrong
with open("data.csv", "w") as f:
    writer = csv.writer(f)

# Correct
with open("data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
```

---

### 5.4 Parsing CSV by Splitting on Commas

Fields in CSV can contain commas if they are quoted. Splitting on `","` breaks
for these cases.

```python
# Wrong — breaks on: "Smith, John",30,Paris
line = '"Smith, John",30,Paris'
parts = line.split(",")   # ['\"Smith', ' John\"', '30', 'Paris'] — wrong

# Correct — use the csv module
import csv, io
reader = csv.reader(io.StringIO(line))
parts = next(reader)   # ['Smith, John', '30', 'Paris'] — correct
```

---

### 5.5 Overwriting a File When You Meant to Append

Opening a file in `"w"` mode truncates it immediately, even before you write
anything.

```python
# Destroys existing content
with open("log.txt", "w") as f:
    f.write("New entry.\n")

# Adds to existing content
with open("log.txt", "a") as f:
    f.write("New entry.\n")
```

---

### 5.6 Using String Concatenation for Paths

String concatenation for paths breaks on different operating systems because
of different path separators.

```python
# Fragile — uses "/" which breaks on Windows
path = "data" + "/" + "2024" + "/" + "report.csv"

# Correct — pathlib handles separators automatically
from pathlib import Path
path = Path("data") / "2024" / "report.csv"
```

---

### 5.7 Assuming JSON Preserves Key Order or Types

JSON does not have a `tuple` type — tuples become lists when serialized.
Integer dict keys become strings.

```python
import json

data = {1: "one", 2: "two"}
text = json.dumps(data)
print(text)   # {"1": "one", "2": "two"}  — keys became strings

restored = json.loads(text)
print(restored)   # {'1': 'one', '2': 'two'}  — still strings
```

---

## 6. Practice Tasks

1. Write a function `count_lines(path: str) -> int` that returns the number
   of lines in a text file.

2. Write a function `copy_file(src: str, dst: str) -> None` that copies a
   text file from `src` to `dst` using `pathlib` and `read_text`/`write_text`.

3. Write a function `find_files(root: str, extension: str) -> list[str]` that
   returns the paths of all files with the given extension under `root`,
   sorted alphabetically.

4. Write a function `save_scores(scores: dict[str, int], path: str) -> None`
   that saves a dict of name-to-score pairs as a JSON file, and a matching
   `load_scores(path: str) -> dict[str, int]` that reads it back.

5. Write a function `csv_to_dicts(path: str) -> list[dict]` that reads a CSV
   file with a header row and returns a list of dicts, one per data row.

6. Write a function `append_log(message: str, path: str) -> None` that
   appends a timestamped log line to a file. Use `datetime.now().isoformat()`
   for the timestamp.

7. Write a function `merge_json_files(paths: list[str], output: str) -> None`
   that reads multiple JSON files (each containing a list), merges all the
   lists, and writes the combined list to `output`.

8. Write a function `largest_file(directory: str) -> Path | None` that
   returns the `Path` of the largest file in a directory (non-recursive), or
   `None` if the directory is empty.

---

## 7. Key Takeaways

- Always open files with `with open(...) as f:` — it closes the file
  automatically, even if an exception occurs.
- Always specify `encoding="utf-8"` for text files to avoid platform-specific
  encoding issues.
- Use `pathlib.Path` for all path operations. The `/` operator joins path
  components portably.
- `Path.read_text()` and `Path.write_text()` are convenient for simple
  reads and writes. Use `open()` for appending, line-by-line reading, or
  binary files.
- `json.load()` reads JSON from a file; `json.loads()` parses a JSON string.
  `json.dump()` writes to a file; `json.dumps()` serializes to a string.
- JSON supports only strings, numbers, booleans, `null`, lists, and objects.
  Tuples become lists; custom objects need manual conversion.
- Use `csv.reader` and `csv.writer` for simple CSV. Use `csv.DictReader` and
  `csv.DictWriter` when working with named columns.
- Always pass `newline=""` when opening CSV files.
- Never parse CSV by splitting on commas — quoted fields containing commas
  will break your code.

---

### What's Next

Chapter 14 covers **modules and packages** — how Python's import system works,
how to organize your code into reusable modules, and how to structure a
package with multiple files.

---

*See also:*
- [Exercises for Chapter 13](../exercises/13-files-paths-json-csv.md)
- [Solutions for Chapter 13](../solutions/13-files-paths-json-csv.md)
- [Cheatsheet: File I/O](../cheatsheets/file-io.md)
