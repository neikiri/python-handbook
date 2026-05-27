# Chapter 22: Practical Projects

## 1. Overview

Reading about Python and writing Python are two different things. The gap
between understanding a concept and applying it in a real program is where
most learning actually happens. This chapter is about closing that gap.

You will work through the process of building a small project from scratch:
breaking down requirements, planning the structure, writing the code in
layers, and testing it. Along the way you will see how the skills from
earlier chapters — functions, file I/O, modules, type hints, testing — fit
together in a real program rather than isolated examples.

The repository includes eight mini projects in the `projects/` directory.
This chapter uses them as reference points and walks you through building
one from scratch so you can apply the same approach to the others.

---

## 2. What You Will Learn

- How to break a project requirement into smaller, concrete tasks
- How to plan a file structure before writing any code
- How to write a `main.py` entry point and keep it thin
- How to separate concerns: I/O, logic, and presentation in different
  functions or modules
- How to use `pathlib`, f-strings, and type hints in a real project
- How to test project behavior with pytest
- How the eight repository mini projects are structured and what each one
  demonstrates
- A complete worked example: building a simple notes CLI from scratch

---

## 3. Core Concepts

### 3.1 Breaking Down Requirements

Every project starts as a description of what it should do. Before writing
any code, turn that description into a list of concrete, specific behaviors.

Take the `todo-cli` project as an example. The description is:
"A command-line todo list."

That is too vague to code directly. Break it down:

- Add a task with a description
- List all tasks, showing each one with a number
- Mark a task as done by its number
- Delete a task by its number
- Save tasks between runs (persist to a file)
- Show a helpful message when no tasks exist

Now you have six specific behaviors. Each one maps to a function or a small
block of code. You know when you are done because you can check each item off.

**Questions to ask when breaking down requirements:**

- What are the inputs? (command-line arguments, a file, user input?)
- What are the outputs? (printed text, a file, a return value?)
- What are the error cases? (file not found, invalid input, empty list?)
- What needs to persist between runs? (a file, a database?)
- What is the simplest version that is still useful?

Start with the simplest version. You can always add features later.

---

### 3.2 Planning the File Structure

For a small project (under ~200 lines), a single `main.py` is fine. For
anything larger, split the code into modules by responsibility.

A typical small project layout:

```text
my-project/
    main.py          ← entry point, argument parsing, top-level flow
    storage.py       ← reading and writing data to disk
    logic.py         ← pure functions: calculations, transformations
    display.py       ← formatting output for the terminal
    tests/
        test_logic.py
        test_storage.py
    README.md
```

You do not need all of these files for every project. The point is to think
about which parts of the code belong together before you start writing.

**Separation of concerns** means each module has one clear job:

- `main.py` handles the CLI and calls other modules. It should not contain
  business logic.
- `storage.py` handles reading and writing files. It should not know about
  the CLI.
- `logic.py` contains pure functions that transform data. It should not do
  any I/O.
- `display.py` formats data for output. It should not modify data.

This separation makes each part easier to test and easier to change. If you
decide to switch from a plain text file to JSON storage, you only change
`storage.py`. The logic and display code stay the same.

---

### 3.3 Writing a Thin Entry Point

The `main()` function in `main.py` should read like a summary of what the
program does, not like the implementation of it.

```python
# Good — main() is a high-level summary
def main() -> None:
    args = parse_args()
    notes = load_notes(DATA_FILE)

    match args.command:
        case "add":
            notes = add_note(notes, args.text)
            save_notes(DATA_FILE, notes)
            print(f"Added: {args.text}")
        case "list":
            print_notes(notes)
        case "delete":
            notes = delete_note(notes, args.index)
            save_notes(DATA_FILE, notes)
```

Each line in `main()` calls a named function. The names tell you what is
happening. The details are in the functions themselves.

Compare that to a `main()` that does everything inline — it becomes a wall
of code where the high-level flow is buried in implementation details.

---

### 3.4 Separating I/O from Logic

The most important separation in any project is between code that does I/O
(reads files, prints to the terminal, takes user input) and code that
transforms data (calculations, filtering, sorting).

Pure functions — functions with no side effects — are easy to test because
you can call them with any input and check the output without setting up
files or capturing terminal output.

```python
# Pure function — easy to test
def filter_done(tasks: list[dict]) -> list[dict]:
    """Return only tasks that are not yet completed."""
    return [t for t in tasks if not t["done"]]


# I/O function — harder to test, but thin
def load_tasks(path: Path) -> list[dict]:
    if not path.exists():
        return []
    import json
    return json.loads(path.read_text(encoding="utf-8"))
```

Test `filter_done` with a list of dicts — no files needed. Test `load_tasks`
with `tmp_path` from pytest. Keep the two concerns separate and both become
manageable.

---

### 3.5 Using pathlib, f-strings, and Type Hints

These three tools appear throughout the mini projects. Here is a quick
reminder of how they work together in a project context.

**pathlib** for all file paths:

```python
from pathlib import Path

DATA_FILE = Path.home() / ".notes" / "notes.json"

def ensure_data_dir() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
```

`Path.home()` returns the user's home directory on any platform. Joining
with `/` builds paths without string concatenation. `mkdir(parents=True,
exist_ok=True)` creates the directory and any missing parents without
raising an error if it already exists.

**f-strings** for all output:

```python
def print_note(index: int, note: dict) -> None:
    status = "✓" if note["done"] else " "
    print(f"  [{status}] {index + 1}. {note['text']}")
```

**Type hints** on all function signatures:

```python
def add_note(notes: list[dict], text: str) -> list[dict]:
    return notes + [{"text": text, "done": False}]


def delete_note(notes: list[dict], index: int) -> list[dict]:
    if index < 0 or index >= len(notes):
        raise IndexError(f"No note at position {index + 1}")
    return notes[:index] + notes[index + 1:]
```

Type hints do not change how the code runs, but they make the function's
contract explicit. A reader — or mypy — can see at a glance what goes in
and what comes out.

---

### 3.6 Testing Project Behavior

Testing a project is the same as testing any other Python code: write
functions that call your code and assert the results. The key is to test
the logic functions directly, not the CLI layer.

```python
# tests/test_logic.py
from notes_app.logic import add_note, delete_note, filter_done


def test_add_note_appends():
    notes = []
    result = add_note(notes, "Buy milk")
    assert len(result) == 1
    assert result[0]["text"] == "Buy milk"
    assert result[0]["done"] is False


def test_delete_note_removes_correct_item():
    notes = [
        {"text": "Buy milk", "done": False},
        {"text": "Call dentist", "done": False},
    ]
    result = delete_note(notes, 0)
    assert len(result) == 1
    assert result[0]["text"] == "Call dentist"


def test_delete_note_out_of_range_raises():
    import pytest
    notes = [{"text": "Buy milk", "done": False}]
    with pytest.raises(IndexError):
        delete_note(notes, 5)
```

Notice that none of these tests touch the filesystem or the terminal. They
test the logic in isolation. The storage functions get tested separately
using `tmp_path`.

---

### 3.7 The Repository Mini Projects

The `projects/` directory contains eight mini projects. They are ordered
roughly by complexity. Here is what each one demonstrates:

| Project | Key skills |
|---|---|
| `number-guessing-game` | `random`, loops, user input, basic game logic |
| `todo-cli` | `argparse`, JSON file storage, list manipulation |
| `word-counter` | File reading, `collections.Counter`, CLI output |
| `csv-sales-report` | `csv` module, aggregation, formatted output |
| `password-generator` | `random.choices`, `string` module, CLI flags |
| `budget-tracker` | JSON persistence, running totals, categories |
| `log-analyzer` | File parsing, `re`, date filtering, summaries |
| `personal-notes-app` | Multi-command CLI, search, persistent storage |

Start with `number-guessing-game` if you are new to projects. It is short
enough to read in one sitting and covers the core loop of: get input, do
something with it, show output, repeat.

Move to `todo-cli` once you are comfortable. It introduces persistent
storage and a multi-command CLI — patterns that appear in almost every
real-world tool.

The later projects (`log-analyzer`, `personal-notes-app`) are longer and
involve more modules. Read the `README.md` in each project directory before
starting. It describes what the project does and what you should build.

---

## 4. Practical Examples

### 4.1 Worked Example: Building a Notes CLI from Scratch

This section walks through building a small notes application step by step.
The finished program lets you add, list, and delete short text notes. Notes
are saved to a JSON file so they persist between runs.

This is similar to `personal-notes-app` in the repository, but simpler —
a good starting point before reading the full version.

#### Step 1: Define the requirements

What should the program do?

- `python notes.py add "Buy milk"` — add a note
- `python notes.py list` — show all notes, numbered
- `python notes.py done 1` — mark note 1 as done
- `python notes.py delete 1` — delete note 1
- Notes persist to `~/.notes/notes.json`
- Show a message when the list is empty

That is five behaviors. Each one is concrete and testable.

#### Step 2: Plan the structure

This project is small enough for two files:

```text
notes/
    notes.py     ← entry point + CLI
    logic.py     ← pure functions for note manipulation
    tests/
        test_logic.py
```

Storage (reading/writing JSON) will live in `notes.py` for now, since it is
only a few lines. If the project grew, it would move to `storage.py`.

#### Step 3: Write the logic module first

Start with the pure functions. They have no dependencies on the CLI or the
filesystem, so you can write and test them immediately.

```python
# logic.py
"""Pure functions for note manipulation."""

from __future__ import annotations


def add_note(notes: list[dict], text: str) -> list[dict]:
    """Return a new list with the note appended."""
    return notes + [{"text": text, "done": False}]


def mark_done(notes: list[dict], index: int) -> list[dict]:
    """Return a new list with note at index marked done.

    Raises IndexError if index is out of range.
    """
    if index < 0 or index >= len(notes):
        raise IndexError(f"No note at position {index + 1}.")
    updated = [dict(n) for n in notes]
    updated[index]["done"] = True
    return updated


def delete_note(notes: list[dict], index: int) -> list[dict]:
    """Return a new list with note at index removed.

    Raises IndexError if index is out of range.
    """
    if index < 0 or index >= len(notes):
        raise IndexError(f"No note at position {index + 1}.")
    return notes[:index] + notes[index + 1:]


def filter_pending(notes: list[dict]) -> list[dict]:
    """Return only notes that are not yet done."""
    return [n for n in notes if not n["done"]]
```

Notice that every function takes a list and returns a new list. None of them
modify the input in place. This makes them easy to test and reason about.

#### Step 4: Write the tests

Before writing the CLI, write tests for the logic. This confirms the logic
works and gives you a safety net for later changes.

```python
# tests/test_logic.py
import pytest
from logic import add_note, delete_note, filter_pending, mark_done


def test_add_note_to_empty_list():
    result = add_note([], "Buy milk")
    assert result == [{"text": "Buy milk", "done": False}]


def test_add_note_does_not_mutate_original():
    original = [{"text": "Existing", "done": False}]
    result = add_note(original, "New note")
    assert len(original) == 1   # original unchanged
    assert len(result) == 2


def test_mark_done_sets_flag():
    notes = [{"text": "Buy milk", "done": False}]
    result = mark_done(notes, 0)
    assert result[0]["done"] is True


def test_mark_done_does_not_mutate_original():
    notes = [{"text": "Buy milk", "done": False}]
    mark_done(notes, 0)
    assert notes[0]["done"] is False   # original unchanged


def test_mark_done_out_of_range():
    notes = [{"text": "Buy milk", "done": False}]
    with pytest.raises(IndexError):
        mark_done(notes, 5)


def test_delete_note_removes_correct_item():
    notes = [
        {"text": "Buy milk", "done": False},
        {"text": "Call dentist", "done": False},
    ]
    result = delete_note(notes, 0)
    assert len(result) == 1
    assert result[0]["text"] == "Call dentist"


def test_delete_note_out_of_range():
    with pytest.raises(IndexError):
        delete_note([], 0)


def test_filter_pending_excludes_done():
    notes = [
        {"text": "Buy milk", "done": True},
        {"text": "Call dentist", "done": False},
    ]
    result = filter_pending(notes)
    assert len(result) == 1
    assert result[0]["text"] == "Call dentist"


def test_filter_pending_empty_list():
    assert filter_pending([]) == []
```

Run the tests:

```bash
pytest tests/ -v
```

All nine tests should pass. Now you have confidence in the logic before
writing a single line of CLI code.

#### Step 5: Write the entry point

Now write `notes.py`. It handles argument parsing, loads and saves the JSON
file, and calls the logic functions.

```python
# notes.py
"""A simple command-line notes application.

Usage:
    python notes.py add "Buy milk"
    python notes.py list
    python notes.py done 1
    python notes.py delete 1
"""
import argparse
import json
import sys
from pathlib import Path

from logic import add_note, delete_note, mark_done

DATA_FILE = Path.home() / ".notes" / "notes.json"


# ---------------------------------------------------------------------------
# Storage helpers
# ---------------------------------------------------------------------------

def load_notes(path: Path) -> list[dict]:
    """Load notes from a JSON file. Return an empty list if the file does
    not exist yet."""
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_notes(path: Path, notes: list[dict]) -> None:
    """Save notes to a JSON file, creating parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notes, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def print_notes(notes: list[dict]) -> None:
    """Print all notes to stdout."""
    if not notes:
        print("No notes yet. Add one with: notes.py add \"your note\"")
        return
    for i, note in enumerate(notes):
        status = "✓" if note["done"] else " "
        print(f"  [{status}] {i + 1}. {note['text']}")


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notes.py",
        description="A simple command-line notes manager.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    add_p = subparsers.add_parser("add", help="Add a new note")
    add_p.add_argument("text", help="Text of the note")

    # list
    subparsers.add_parser("list", help="List all notes")

    # done
    done_p = subparsers.add_parser("done", help="Mark a note as done")
    done_p.add_argument("number", type=int, help="Note number (from list)")

    # delete
    del_p = subparsers.add_parser("delete", help="Delete a note")
    del_p.add_argument("number", type=int, help="Note number (from list)")

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    notes = load_notes(DATA_FILE)

    match args.command:
        case "add":
            notes = add_note(notes, args.text)
            save_notes(DATA_FILE, notes)
            print(f"Added: {args.text}")

        case "list":
            print_notes(notes)

        case "done":
            try:
                notes = mark_done(notes, args.number - 1)
                save_notes(DATA_FILE, notes)
                print(f"Marked done: {notes[args.number - 1]['text']}")
            except IndexError as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)

        case "delete":
            try:
                deleted_text = notes[args.number - 1]["text"]
                notes = delete_note(notes, args.number - 1)
                save_notes(DATA_FILE, notes)
                print(f"Deleted: {deleted_text}")
            except IndexError as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
```

#### Step 6: Try it out

```bash
python notes.py add "Buy milk"
# Added: Buy milk

python notes.py add "Call dentist"
# Added: Call dentist

python notes.py list
#   [ ] 1. Buy milk
#   [ ] 2. Call dentist

python notes.py done 1
# Marked done: Buy milk

python notes.py list
#   [✓] 1. Buy milk
#   [ ] 2. Call dentist

python notes.py delete 2
# Deleted: Call dentist

python notes.py list
#   [✓] 1. Buy milk
```

The program works. The logic is tested. The entry point is thin and readable.

---

### 4.2 Testing Storage with tmp_path

The storage functions (`load_notes`, `save_notes`) touch the filesystem.
Test them with pytest's `tmp_path` fixture so tests do not write to your
actual home directory.

```python
# tests/test_storage.py
import json
from pathlib import Path

# Import the functions directly from notes.py
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from notes import load_notes, save_notes


def test_load_notes_missing_file(tmp_path: Path):
    path = tmp_path / "notes.json"
    result = load_notes(path)
    assert result == []


def test_save_and_load_roundtrip(tmp_path: Path):
    path = tmp_path / "notes.json"
    notes = [
        {"text": "Buy milk", "done": False},
        {"text": "Call dentist", "done": True},
    ]
    save_notes(path, notes)
    loaded = load_notes(path)
    assert loaded == notes


def test_save_creates_parent_directory(tmp_path: Path):
    path = tmp_path / "subdir" / "notes.json"
    save_notes(path, [])
    assert path.exists()


def test_save_writes_valid_json(tmp_path: Path):
    path = tmp_path / "notes.json"
    notes = [{"text": "Test", "done": False}]
    save_notes(path, notes)
    raw = path.read_text(encoding="utf-8")
    parsed = json.loads(raw)
    assert parsed == notes
```

---

### 4.3 Notes on the Repository Mini Projects

The table in section 3.7 lists the key skills each project covers. A few
additional notes on how to approach them:

**Start with `number-guessing-game`.** It is short enough to read in one
sitting. The core is a `while True` loop that calls `input()`, converts the
result to an integer, and compares it to a secret number. Handle the case
where the user types something that is not a number — `"abc".isdigit()` is
`False`, so you can check before calling `int()`.

**`todo-cli` is the template project.** Once you understand it, the pattern
repeats in `budget-tracker` and `personal-notes-app`: parse arguments → load
JSON → modify data with a pure function → save JSON → print result. The
differences are in the data shape and the commands, not the structure.

**`csv-sales-report` and `log-analyzer` are data-processing projects.** They
do not have interactive loops. They read a file, transform the data, and
print a report. Focus on separating the parsing step (reading the file into
a list of dicts) from the aggregation step (summing, grouping, sorting). The
aggregation functions are pure and easy to test.

**`personal-notes-app` is the capstone.** It combines everything: a
multi-command CLI, JSON persistence, search, and a multi-module structure.
Read the `README.md` carefully before starting. Build it in layers: get
`add` and `list` working first, then add `search`, then `delete`.

---

## 5. Common Mistakes

### 5.1 Starting to Code Before Planning

The most common mistake is opening a blank file and starting to type. Without
a plan, you end up with a tangled `main()` function that does everything, and
refactoring it later is painful.

Spend five minutes writing down the behaviors you need before writing any
code. Even a rough list on paper is enough. You will write better code faster.

---

### 5.2 Putting Everything in main()

A `main()` function that is 150 lines long is a sign that concerns have not
been separated. It is hard to read, hard to test, and hard to change.

```python
# Hard to maintain — main() does everything
def main() -> None:
    args = parse_args()
    path = Path.home() / ".notes" / "notes.json"
    if not path.exists():
        notes = []
    else:
        notes = json.loads(path.read_text(encoding="utf-8"))
    if args.command == "add":
        notes.append({"text": args.text, "done": False})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(notes, indent=2), encoding="utf-8")
        print(f"Added: {args.text}")
    elif args.command == "list":
        if not notes:
            print("No notes.")
        else:
            for i, note in enumerate(notes):
                status = "✓" if note["done"] else " "
                print(f"  [{status}] {i + 1}. {note['text']}")
    # ... and so on for every command
```

Extract each responsibility into a named function. `main()` becomes a
readable summary; the details live in functions with clear names.

---

### 5.3 Mixing Logic and I/O in the Same Function

A function that both calculates something and writes to a file is harder to
test than two separate functions.

```python
# Hard to test — calculation and file write are tangled
def summarize_and_save(records: list[dict], path: Path) -> None:
    total = sum(r["amount"] for r in records)
    by_category: dict[str, float] = {}
    for r in records:
        by_category[r["category"]] = by_category.get(r["category"], 0) + r["amount"]
    result = {"total": total, "by_category": by_category}
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")


# Easy to test — calculation is pure, I/O is separate
def summarize(records: list[dict]) -> dict:
    total = sum(r["amount"] for r in records)
    by_category: dict[str, float] = {}
    for r in records:
        by_category[r["category"]] = by_category.get(r["category"], 0) + r["amount"]
    return {"total": total, "by_category": by_category}


def save_summary(summary: dict, path: Path) -> None:
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
```

Now you can test `summarize` with a list of dicts and no filesystem involved.

---

### 5.4 Using Global Variables for State

Global variables make it hard to understand what a function does and hard to
test it in isolation. Pass state as function arguments instead.

```python
# Fragile — function depends on a global
notes: list[dict] = []

def add_note(text: str) -> None:
    notes.append({"text": text, "done": False})   # modifies global


# Better — function takes and returns data
def add_note(notes: list[dict], text: str) -> list[dict]:
    return notes + [{"text": text, "done": False}]
```

The second version is a pure function. You can call it with any list and
check the result. The first version requires the global to be in a specific
state before the test.

---

### 5.5 Not Handling the "File Does Not Exist" Case

Every project that reads from a file needs to handle the case where the file
does not exist yet — especially on the first run.

```python
# Crashes on first run
def load_data(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))   # FileNotFoundError


# Handles first run gracefully
def load_data(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))
```

Similarly, always create parent directories before writing:

```python
def save_data(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
```

---

### 5.6 Printing Errors to stdout

Error messages should go to `sys.stderr`, not `sys.stdout`. When a user
pipes your program's output to another command, error messages in stdout
corrupt the data stream.

```python
import sys

# Wrong — error mixed into stdout
print("Error: file not found.")

# Correct — error goes to stderr
print("Error: file not found.", file=sys.stderr)
sys.exit(1)
```

---

### 5.7 Skipping Tests Because "It's Just a Small Project"

Small projects are the best time to practice testing. The tests are short,
the functions are simple, and you build the habit before the projects get
complex. A project with ten tested functions is easier to extend than a
project with fifty untested lines in `main()`.

Write at least a few tests for the core logic of every project you build.
You will catch bugs earlier and gain confidence to refactor later.

---

### 5.8 Hardcoding File Paths

Hardcoding a path like `"/home/alice/.notes/notes.json"` breaks on any
other machine. Use `Path.home()` for paths in the user's home directory,
or accept the path as a command-line argument.

```python
# Fragile — only works on one machine
DATA_FILE = Path("/home/alice/.notes/notes.json")

# Portable — works on any machine
DATA_FILE = Path.home() / ".notes" / "notes.json"

# Even better for tools — let the user override it
parser.add_argument(
    "--data-file",
    type=Path,
    default=Path.home() / ".notes" / "notes.json",
    help="Path to the notes file",
)
```

---

## 6. Practice Tasks

1. **Extend the notes CLI.** Add a `search` subcommand to `notes.py` that
   accepts a keyword and prints all notes whose text contains that keyword
   (case-insensitive). Write at least two tests for the search logic in
   `tests/test_logic.py`.

2. **Build the number-guessing game.** Implement the `number-guessing-game`
   project from scratch. The program should pick a random number between 1
   and 100, accept guesses in a loop, give "higher" or "lower" hints, and
   report the number of attempts when the user guesses correctly. Handle
   non-numeric input without crashing.

3. **Add a `--pending` flag to the notes CLI.** When `--pending` is passed
   to the `list` command, show only notes that are not yet done. Implement
   this using the existing `filter_pending` function from `logic.py`. Write
   a test that verifies the flag filters correctly.

4. **Build a word counter.** Write a script `wordcount.py` that accepts a
   file path and prints the number of lines, words, and characters. Add a
   `--top N` flag (default 10) that shows the N most frequent words. Use
   `collections.Counter`. Write tests for the word-counting logic.

5. **Build a password generator.** Write a script `passgen.py` that
   generates a random password. Add `--length N` (default 16), `--no-symbols`
   (exclude punctuation), and `--count N` (generate N passwords) flags. Use
   `random.choices` and the `string` module. Ensure the generated password
   always contains at least one digit.

6. **Add persistence to the budget tracker.** Implement the `budget-tracker`
   project. Store transactions as a JSON list where each entry has `type`
   (`"income"` or `"expense"`), `amount`, `category`, and `description`.
   Implement `add`, `list`, and `summary` subcommands. The summary should
   show total income, total expenses, and current balance.

7. **Write a CSV report script.** Write a script `sales_report.py` that
   reads a CSV file with columns `product`, `region`, `quantity`, and
   `price`. Print total revenue, revenue by product, and revenue by region.
   Use `csv.DictReader`. Write tests for the aggregation logic using
   in-memory data (no files needed for the logic tests).

8. **Refactor a monolithic script.** Take any script you have written that
   has a long `main()` function and refactor it: extract the logic into
   named functions, separate I/O from calculation, and add at least three
   tests for the extracted functions. Run `pytest` to confirm everything
   still works.

---

## 7. Key Takeaways

- Before writing any code, break the requirements into a list of specific,
  concrete behaviors. Each behavior maps to a function or a small block of
  code. You know you are done when every behavior works.
- Plan the file structure before you start. For small projects, a single
  `main.py` is fine. For larger ones, split by responsibility: entry point,
  storage, logic, display.
- Keep `main()` thin. It should read like a summary of what the program
  does, calling named functions for the details. A thin `main()` is easy to
  follow and easy to change.
- Separate I/O from logic. Pure functions — no side effects, same output for
  the same input — are easy to test. I/O functions are harder to test, so
  keep them small and focused.
- Use `pathlib` for all file paths. `Path.home()` gives you a portable home
  directory. `mkdir(parents=True, exist_ok=True)` creates directories safely.
  Always handle the "file does not exist" case on first run.
- Use f-strings for output and type hints on all function signatures. They
  make the code clearer and catch mistakes earlier.
- Test the logic functions directly with pytest. Use `tmp_path` for storage
  functions that touch the filesystem. Write tests before or alongside the
  code, not after.
- Print error messages to `sys.stderr` and exit with a non-zero code on
  failure. This makes your tools composable with shell scripts and CI
  pipelines.
- The eight mini projects in `projects/` cover the most common patterns:
  game loops, multi-command CLIs, JSON persistence, CSV processing, file
  parsing, and search. Read each `README.md`, then build it yourself before
  reading the solution.
- The best way to learn project structure is to build projects. Start small,
  get it working, then refactor. Each project you finish teaches you
  something the next one will benefit from.

---

### Further Reading

- [Project Ideas](https://docs.python.org/3/faq/programming.html#faq-programming-questions)
- [Python Cookbook](https://docs.python.org/3/tutorial/index.html)
- [Real Python Tutorials](https://realpython.com/)

### What's Next

Ready to continue? Head to the next chapter: **Where to Go Next**.

→ [Chapter 23 — Where to Go Next](23-where-to-go-next.md)

*See also:*
- [Exercise](../exercises/22-practical-projects.md)
- [Solution](../solutions/22-practical-projects.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
