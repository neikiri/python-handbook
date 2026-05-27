# Solutions 22: Practical Projects

## Overview

Chapter 22 exercises guide you through building four complete applications: a personal budget tracker, a note-taking app, a file organizer, and a quiz application. This guide explains the design decisions behind each project and highlights patterns that apply to real-world Python development.

---

## Notes Before Checking Solutions

These projects combine everything from earlier chapters. The goal is not just to make them work, but to understand why they are structured the way they are. Pay attention to how each project separates concerns: data storage, business logic, and the user interface are kept in different places.

---

## Project 1: Personal Budget Tracker

### Design Decisions

The project is split into two files: `budget.py` (the data and logic layer) and `main.py` (the CLI layer). This separation means you could swap the CLI for a web interface without touching `budget.py`.

`budget.py`:

```python
import json
from pathlib import Path
from datetime import datetime

class BudgetTracker:
    def __init__(self, filename="data.json"):
        self.filename = Path(filename)
        self.transactions = self._load()

    def _load(self):
        if self.filename.exists():
            return json.loads(self.filename.read_text())
        return []

    def _save(self):
        self.filename.write_text(json.dumps(self.transactions, indent=2))

    def add_income(self, amount, category, description=""):
        self.transactions.append({
            "type": "income",
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().isoformat(),
        })
        self._save()

    def add_expense(self, amount, category, description=""):
        self.transactions.append({
            "type": "expense",
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().isoformat(),
        })
        self._save()

    def get_balance(self):
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        return income - expenses

    def get_summary(self):
        summary = {}
        for t in self.transactions:
            key = f"{t['type']}_{t['category']}"
            summary[key] = summary.get(key, 0) + t["amount"]
        return summary

    def list_transactions(self):
        return self.transactions.copy()
```

**Why `_load()` and `_save()` are private methods** (prefixed with `_`): They are implementation details. Callers use `add_income()`, `add_expense()`, etc. — they should not need to call `_save()` directly.

**`datetime.now().isoformat()`** stores the timestamp as a string in ISO 8601 format (`2024-01-15T14:30:00.123456`). This format is sortable, human-readable, and parseable with `datetime.fromisoformat()`.

`main.py`:

```python
import argparse
from budget import BudgetTracker

def main():
    parser = argparse.ArgumentParser(description="Budget Tracker")
    subparsers = parser.add_subparsers(dest="command")

    income_parser = subparsers.add_parser("income")
    income_parser.add_argument("amount", type=float)
    income_parser.add_argument("category")
    income_parser.add_argument("--description", default="")

    expense_parser = subparsers.add_parser("expense")
    expense_parser.add_argument("amount", type=float)
    expense_parser.add_argument("category")
    expense_parser.add_argument("--description", default="")

    subparsers.add_parser("balance")
    subparsers.add_parser("summary")
    subparsers.add_parser("list")

    args = parser.parse_args()
    tracker = BudgetTracker()

    if args.command == "income":
        tracker.add_income(args.amount, args.category, args.description)
        print(f"Added income: ${args.amount} ({args.category})")
    elif args.command == "expense":
        tracker.add_expense(args.amount, args.category, args.description)
        print(f"Added expense: ${args.amount} ({args.category})")
    elif args.command == "balance":
        print(f"Balance: ${tracker.get_balance():.2f}")
    elif args.command == "summary":
        for key, amount in tracker.get_summary().items():
            print(f"  {key}: ${amount:.2f}")
    elif args.command == "list":
        for t in tracker.list_transactions():
            print(f"  {t['date'][:10]}: {t['type']} ${t['amount']} ({t['category']})")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Test it:

```bash
python main.py income 3000 salary
python main.py expense 500 rent
python main.py expense 100 groceries
python main.py balance
python main.py summary
python main.py list
```

---

## Project 2: Note-Taking Application

### Design Decisions

Notes are stored as individual JSON files in a `notes/` directory. This makes each note a separate file, which is easy to inspect, back up, and version-control.

`notes.py`:

```python
import json
from pathlib import Path
from datetime import datetime

class NoteApp:
    def __init__(self, notes_dir="notes"):
        self.notes_dir = Path(notes_dir)
        self.notes_dir.mkdir(exist_ok=True)

    def create_note(self, title, content):
        filename = self.notes_dir / f"{title}.txt"
        note = {
            "title": title,
            "content": content,
            "created": datetime.now().isoformat(),
            "modified": datetime.now().isoformat(),
        }
        filename.write_text(json.dumps(note, indent=2))
        return title

    def read_note(self, title):
        filename = self.notes_dir / f"{title}.txt"
        if filename.exists():
            return json.loads(filename.read_text())
        return None

    def update_note(self, title, content):
        note = self.read_note(title)
        if note:
            note["content"] = content
            note["modified"] = datetime.now().isoformat()
            filename = self.notes_dir / f"{title}.txt"
            filename.write_text(json.dumps(note, indent=2))
            return True
        return False

    def delete_note(self, title):
        filename = self.notes_dir / f"{title}.txt"
        if filename.exists():
            filename.unlink()
            return True
        return False

    def list_notes(self):
        notes = []
        for file in self.notes_dir.glob("*.txt"):
            note = json.loads(file.read_text())
            notes.append(note)
        return notes
```

**Returning `True`/`False` from `update_note()` and `delete_note()`** lets the CLI report whether the operation succeeded without the CLI needing to know how notes are stored.

**Using the title as the filename** is simple but has a limitation: titles with special characters (slashes, colons) would cause problems. A production app would use a sanitized filename or a UUID.

---

## Project 3: File Organizer

### Design Decisions

The `FileOrganizer` class takes a directory path and provides methods to analyze it. It does not move or delete files — it only reports. This is a safe design: the user can see what would happen before committing to any changes.

```python
import argparse
from pathlib import Path
from collections import defaultdict

class FileOrganizer:
    def __init__(self, directory):
        self.directory = Path(directory)

    def organize_by_extension(self):
        by_ext = defaultdict(list)
        for file in self.directory.glob("*"):
            if file.is_file():
                ext = file.suffix or "no_extension"
                by_ext[ext].append(file.name)
        return dict(by_ext)

    def organize_by_size(self):
        by_size = {"small": [], "medium": [], "large": []}
        for file in self.directory.glob("*"):
            if file.is_file():
                size = file.stat().st_size
                if size < 1_000_000:
                    by_size["small"].append(file.name)
                elif size < 10_000_000:
                    by_size["medium"].append(file.name)
                else:
                    by_size["large"].append(file.name)
        return by_size

    def get_statistics(self):
        total_files = 0
        total_size = 0
        for file in self.directory.glob("*"):
            if file.is_file():
                total_files += 1
                total_size += file.stat().st_size
        return {
            "total_files": total_files,
            "total_size": total_size,
            "total_size_mb": total_size / 1_000_000,
        }
```

**`file.stat().st_size`** returns the file size in bytes. `1_000_000` (1 MB) uses Python's numeric literal underscore separator for readability.

**`file.suffix`** returns the extension including the dot (`.txt`, `.py`). An empty string means no extension. The `or "no_extension"` fallback groups extension-less files together.

---

## Project 4: Quiz Application

### Design Decisions

The quiz data is stored in a JSON file, making it easy to add or modify questions without changing the code. The `Quiz` class handles loading, running, and scoring.

```python
import json
from pathlib import Path

class Quiz:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.questions = self._load()
        self.score = 0
        self.total = 0

    def _load(self):
        if self.filename.exists():
            return json.loads(self.filename.read_text())
        return []

    def run(self):
        if not self.questions:
            print("No questions loaded")
            return

        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for j, option in enumerate(q["options"], 1):
                print(f"  {j}. {option}")

            while True:
                try:
                    answer = int(input("Your answer (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    print("Invalid choice")
                except ValueError:
                    print("Enter a number")

            self.total += 1
            if answer == q["correct"]:
                self.score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {q['correct']}")

        self.show_results()

    def show_results(self):
        percentage = (self.score / self.total) * 100
        print(f"\n{'='*40}")
        print(f"Score: {self.score}/{self.total} ({percentage:.1f}%)")
        print(f"{'='*40}")
```

**Storing the correct answer as an index** (1-4) rather than the answer text makes the quiz format flexible — you can change the answer text without updating the `correct` field.

**The input validation loop** inside `run()` keeps asking until the user enters a valid number. This is the standard pattern for interactive input validation.

---

## Common Patterns Across All Projects

**Separate data from presentation.** The `BudgetTracker`, `NoteApp`, `FileOrganizer`, and `Quiz` classes handle data. The `main()` functions handle user interaction. This makes the classes reusable and testable.

**Load on startup, save on every mutation.** Each project loads data when the object is created and saves after every change. This keeps the file in sync with memory.

**Return meaningful values from methods.** `update_note()` returns `True`/`False`. `get_balance()` returns a number. The CLI uses these values to give feedback to the user.

**Use `if __name__ == "__main__":`** in every script so the module can be imported without running the CLI.

---

## Common Mistakes

**Putting all code in one file.** As projects grow, a single file becomes hard to navigate. Separate concerns into modules early.

**Not handling missing files.** Always check `Path.exists()` before reading, or wrap reads in `try-except FileNotFoundError`.

**Hardcoding file paths.** Use a default filename but allow it to be configured (like `BudgetTracker(filename="data.json")`). This makes testing easier — tests can use a temporary file.

**Not testing the application.** Each class in these projects can be tested independently. Write tests for `BudgetTracker.get_balance()`, `NoteApp.read_note()`, etc.

---

## What to Review Next

- Chapter 18: Testing and Code Quality — adding tests to these projects
- Chapter 19: Type Hints — adding type annotations to the project classes
- Chapter 23: Where to Go Next — extending these projects with web interfaces, databases, or APIs
