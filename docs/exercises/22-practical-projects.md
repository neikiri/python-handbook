# Chapter 22: Practical Projects — Exercises

## Overview

These exercises guide you through building complete, real-world projects. By the end, you will have practical experience combining multiple Python concepts into working applications.

---

## How to Use These Exercises

- Create a folder called `chapter-22` in your `python-learning` directory.
- Each project is a complete application. Build it step by step.
- Run each project and test it thoroughly.
- Extend projects with your own ideas.

---

## Project 1: Personal Budget Tracker

Create a directory structure:

```
budget_tracker/
  budget.py
  main.py
  data.json
```

Create `budget.py`:

```python
"""Budget tracking module."""

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

Create `main.py`:

```python
"""Budget tracker CLI."""

import argparse
from budget import BudgetTracker

def main():
    parser = argparse.ArgumentParser(description="Budget Tracker")
    subparsers = parser.add_subparsers(dest="command")
    
    # Income command
    income_parser = subparsers.add_parser("income", help="Add income")
    income_parser.add_argument("amount", type=float, help="Amount")
    income_parser.add_argument("category", help="Category")
    income_parser.add_argument("--description", default="", help="Description")
    
    # Expense command
    expense_parser = subparsers.add_parser("expense", help="Add expense")
    expense_parser.add_argument("amount", type=float, help="Amount")
    expense_parser.add_argument("category", help="Category")
    expense_parser.add_argument("--description", default="", help="Description")
    
    # Balance command
    subparsers.add_parser("balance", help="Show balance")
    
    # Summary command
    subparsers.add_parser("summary", help="Show summary")
    
    # List command
    subparsers.add_parser("list", help="List transactions")
    
    args = parser.parse_args()
    tracker = BudgetTracker()
    
    if args.command == "income":
        tracker.add_income(args.amount, args.category, args.description)
        print(f"Added income: ${args.amount} ({args.category})")
    
    elif args.command == "expense":
        tracker.add_expense(args.amount, args.category, args.description)
        print(f"Added expense: ${args.amount} ({args.category})")
    
    elif args.command == "balance":
        balance = tracker.get_balance()
        print(f"Balance: ${balance:.2f}")
    
    elif args.command == "summary":
        summary = tracker.get_summary()
        for key, amount in summary.items():
            print(f"  {key}: ${amount:.2f}")
    
    elif args.command == "list":
        for t in tracker.list_transactions():
            print(f"  {t['date']}: {t['type']} ${t['amount']} ({t['category']})")
    
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

Create a directory structure:

```
note_app/
  notes.py
  main.py
  notes/
```

Create `notes.py`:

```python
"""Note-taking module."""

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

Create `main.py`:

```python
"""Note-taking CLI."""

import argparse
from notes import NoteApp

def main():
    parser = argparse.ArgumentParser(description="Note App")
    subparsers = parser.add_subparsers(dest="command")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create a note")
    create_parser.add_argument("title", help="Note title")
    create_parser.add_argument("content", help="Note content")
    
    # Read command
    read_parser = subparsers.add_parser("read", help="Read a note")
    read_parser.add_argument("title", help="Note title")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="Update a note")
    update_parser.add_argument("title", help="Note title")
    update_parser.add_argument("content", help="New content")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a note")
    delete_parser.add_argument("title", help="Note title")
    
    # List command
    subparsers.add_parser("list", help="List all notes")
    
    args = parser.parse_args()
    app = NoteApp()
    
    if args.command == "create":
        app.create_note(args.title, args.content)
        print(f"Created note: {args.title}")
    
    elif args.command == "read":
        note = app.read_note(args.title)
        if note:
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print(f"Created: {note['created']}")
        else:
            print(f"Note '{args.title}' not found")
    
    elif args.command == "update":
        if app.update_note(args.title, args.content):
            print(f"Updated note: {args.title}")
        else:
            print(f"Note '{args.title}' not found")
    
    elif args.command == "delete":
        if app.delete_note(args.title):
            print(f"Deleted note: {args.title}")
        else:
            print(f"Note '{args.title}' not found")
    
    elif args.command == "list":
        notes = app.list_notes()
        for note in notes:
            print(f"  {note['title']} (modified: {note['modified']})")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Test it:

```bash
python main.py create "Python Tips" "Use list comprehensions for clarity"
python main.py create "Project Ideas" "Build a web scraper"
python main.py list
python main.py read "Python Tips"
python main.py update "Python Tips" "Use type hints for better code"
python main.py delete "Project Ideas"
```

---

## Project 3: File Organizer

Create a file called `file_organizer.py`:

```python
"""File organizer utility."""

import argparse
from pathlib import Path
from collections import defaultdict

class FileOrganizer:
    def __init__(self, directory):
        self.directory = Path(directory)
    
    def organize_by_extension(self):
        """Organize files by extension."""
        by_ext = defaultdict(list)
        
        for file in self.directory.glob("*"):
            if file.is_file():
                ext = file.suffix or "no_extension"
                by_ext[ext].append(file.name)
        
        return dict(by_ext)
    
    def organize_by_size(self):
        """Organize files by size category."""
        by_size = {"small": [], "medium": [], "large": []}
        
        for file in self.directory.glob("*"):
            if file.is_file():
                size = file.stat().st_size
                if size < 1_000_000:  # < 1 MB
                    by_size["small"].append(file.name)
                elif size < 10_000_000:  # < 10 MB
                    by_size["medium"].append(file.name)
                else:
                    by_size["large"].append(file.name)
        
        return by_size
    
    def get_statistics(self):
        """Get file statistics."""
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

def main():
    parser = argparse.ArgumentParser(description="File Organizer")
    parser.add_argument("directory", help="Directory to organize")
    parser.add_argument(
        "--by-extension",
        action="store_true",
        help="Organize by file extension"
    )
    parser.add_argument(
        "--by-size",
        action="store_true",
        help="Organize by file size"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics"
    )
    
    args = parser.parse_args()
    organizer = FileOrganizer(args.directory)
    
    if args.by_extension:
        result = organizer.organize_by_extension()
        print("By extension:")
        for ext, files in result.items():
            print(f"  {ext}: {len(files)} files")
    
    elif args.by_size:
        result = organizer.organize_by_size()
        print("By size:")
        for size, files in result.items():
            print(f"  {size}: {len(files)} files")
    
    elif args.stats:
        stats = organizer.get_statistics()
        print(f"Total files: {stats['total_files']}")
        print(f"Total size: {stats['total_size_mb']:.2f} MB")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Test it:

```bash
python file_organizer.py . --stats
python file_organizer.py . --by-extension
```

---

## Project 4: Quiz Application

Create a file called `quiz.py`:

```python
"""Quiz application."""

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
        """Run the quiz."""
        if not self.questions:
            print("No questions loaded")
            return
        
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for j, option in enumerate(q['options'], 1):
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
            if answer == q['correct']:
                self.score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {q['correct']}")
        
        self.show_results()
    
    def show_results(self):
        """Show quiz results."""
        percentage = (self.score / self.total) * 100
        print(f"\n{'='*40}")
        print(f"Score: {self.score}/{self.total} ({percentage:.1f}%)")
        print(f"{'='*40}")

# Create sample quiz
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct": 3
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct": 2
    },
    {
        "question": "What is the largest planet?",
        "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
        "correct": 3
    },
]

# Save quiz
quiz_file = Path("quiz.json")
quiz_file.write_text(json.dumps(quiz_data, indent=2))

# Run quiz
quiz = Quiz("quiz.json")
quiz.run()
```

Test it:

```bash
python quiz.py
```

---

## Hints

**Project too complex** → Break it into smaller functions and test each one.

**Data not persisting** → Ensure you're saving to files correctly and loading on startup.

**CLI not working** → Test argument parsing with `--help` first.

**File operations failing** → Check paths and permissions. Use `Path.exists()` to verify.

---

## What to Review If You Get Stuck

- **Project structure** → Handbook section 2.1
- **File handling** → Handbook section 2.2
- **CLI design** → Handbook section 2.3
- **Data persistence** → Handbook section 2.4
- **Testing** → Handbook section 2.5

---

## Key Takeaways

After completing these exercises, you should be able to:

- Design and build complete applications
- Organize code into modules
- Persist data to files
- Create user-friendly CLIs
- Handle errors gracefully
- Test applications thoroughly
- Extend projects with new features
- Deploy simple Python applications

