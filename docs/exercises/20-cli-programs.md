# Chapter 20: CLI Programs — Exercises

## Overview

These exercises help you build command-line programs that accept arguments, provide help, and interact with users. By the end, you will write professional CLI tools.

---

## How to Use These Exercises

- Create a folder called `chapter-20` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program from the command line.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Use sys.argv

Create a file called `simple_cli.py`:

```python
"""Simple CLI using sys.argv."""

import sys

def main():
    """Main function."""
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments: {sys.argv[1:]}")
    
    if len(sys.argv) < 2:
        print("Usage: python simple_cli.py <name>")
        sys.exit(1)
    
    name = sys.argv[1]
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python simple_cli.py Alice
python simple_cli.py Bob
```

---

### Exercise 2: Use argparse

Create a file called `argparse_cli.py`:

```python
"""CLI using argparse."""

import argparse

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="A simple greeting program"
    )
    
    parser.add_argument(
        "name",
        help="Name to greet"
    )
    
    parser.add_argument(
        "--greeting",
        default="Hello",
        help="Greeting to use (default: Hello)"
    )
    
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of times to greet (default: 1)"
    )
    
    args = parser.parse_args()
    
    for _ in range(args.count):
        print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python argparse_cli.py Alice
python argparse_cli.py Alice --greeting Hi
python argparse_cli.py Alice --count 3
python argparse_cli.py --help
```

---

### Exercise 3: Handle User Input

Create a file called `interactive_cli.py`:

```python
"""Interactive CLI program."""

def main():
    """Main function."""
    print("Welcome to the Calculator")
    print("Commands: add, subtract, multiply, divide, quit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == "quit":
            print("Goodbye!")
            break
        
        if command not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid command")
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if command == "add":
                result = a + b
            elif command == "subtract":
                result = a - b
            elif command == "multiply":
                result = a * b
            elif command == "divide":
                if b == 0:
                    print("Error: Cannot divide by zero")
                    continue
                result = a / b
            
            print(f"Result: {result}")
        
        except ValueError:
            print("Error: Invalid number")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python interactive_cli.py
```

---

### Exercise 4: Add Subcommands

Create a file called `subcommand_cli.py`:

```python
"""CLI with subcommands."""

import argparse

def cmd_greet(args):
    """Greet command."""
    print(f"Hello, {args.name}!")

def cmd_add(args):
    """Add command."""
    result = args.a + args.b
    print(f"{args.a} + {args.b} = {result}")

def cmd_multiply(args):
    """Multiply command."""
    result = args.a * args.b
    print(f"{args.a} * {args.b} = {result}")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Multi-command CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Greet command
    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", help="Name to greet")
    greet_parser.set_defaults(func=cmd_greet)
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=int, help="First number")
    add_parser.add_argument("b", type=int, help="Second number")
    add_parser.set_defaults(func=cmd_add)
    
    # Multiply command
    mult_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    mult_parser.add_argument("a", type=int, help="First number")
    mult_parser.add_argument("b", type=int, help="Second number")
    mult_parser.set_defaults(func=cmd_multiply)
    
    args = parser.parse_args()
    
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Run it:

```bash
python subcommand_cli.py greet Alice
python subcommand_cli.py add 5 3
python subcommand_cli.py multiply 4 7
python subcommand_cli.py --help
```

---

## Practice Exercises

### Exercise 5: Build a File Processor

Create a file called `file_processor.py`:

```python
"""CLI for processing files."""

import argparse
from pathlib import Path

def count_lines(filepath):
    """Count lines in a file."""
    return len(Path(filepath).read_text().splitlines())

def count_words(filepath):
    """Count words in a file."""
    text = Path(filepath).read_text()
    return len(text.split())

def count_chars(filepath):
    """Count characters in a file."""
    return len(Path(filepath).read_text())

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="File processor")
    parser.add_argument("file", help="File to process")
    parser.add_argument(
        "--lines",
        action="store_true",
        help="Count lines"
    )
    parser.add_argument(
        "--words",
        action="store_true",
        help="Count words"
    )
    parser.add_argument(
        "--chars",
        action="store_true",
        help="Count characters"
    )
    
    args = parser.parse_args()
    
    if not Path(args.file).exists():
        print(f"Error: File '{args.file}' not found")
        return
    
    if args.lines:
        print(f"Lines: {count_lines(args.file)}")
    if args.words:
        print(f"Words: {count_words(args.file)}")
    if args.chars:
        print(f"Characters: {count_chars(args.file)}")
    
    if not (args.lines or args.words or args.chars):
        print(f"Lines: {count_lines(args.file)}")
        print(f"Words: {count_words(args.file)}")
        print(f"Characters: {count_chars(args.file)}")

if __name__ == "__main__":
    main()
```

Create a test file `test.txt`:

```
Hello, World!
This is a test file.
Python is great!
```

Run it:

```bash
python file_processor.py test.txt
python file_processor.py test.txt --lines
python file_processor.py test.txt --words --chars
```

---

### Exercise 6: Add Progress Indicators

Create a file called `progress_cli.py`:

```python
"""CLI with progress indicators."""

import argparse
import time

def show_progress(total):
    """Show a progress bar."""
    for i in range(total + 1):
        percent = (i / total) * 100
        bar_length = 40
        filled = int(bar_length * i / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\r[{bar}] {percent:.1f}%", end="", flush=True)
        time.sleep(0.1)
    print()

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Progress demo")
    parser.add_argument(
        "--steps",
        type=int,
        default=100,
        help="Number of steps (default: 100)"
    )
    
    args = parser.parse_args()
    
    print("Processing...")
    show_progress(args.steps)
    print("Done!")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python progress_cli.py
python progress_cli.py --steps 50
```

---

### Exercise 7: Create a Configuration File Handler

Create a file called `config_cli.py`:

```python
"""CLI with configuration file support."""

import argparse
import json
from pathlib import Path

def load_config(filepath):
    """Load configuration from file."""
    if Path(filepath).exists():
        return json.loads(Path(filepath).read_text())
    return {}

def save_config(filepath, config):
    """Save configuration to file."""
    Path(filepath).write_text(json.dumps(config, indent=2))

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Config manager")
    parser.add_argument(
        "--config",
        default="config.json",
        help="Config file (default: config.json)"
    )
    
    subparsers = parser.add_subparsers(dest="command")
    
    # Set command
    set_parser = subparsers.add_parser("set", help="Set a value")
    set_parser.add_argument("key", help="Key")
    set_parser.add_argument("value", help="Value")
    
    # Get command
    get_parser = subparsers.add_parser("get", help="Get a value")
    get_parser.add_argument("key", help="Key")
    
    # List command
    subparsers.add_parser("list", help="List all values")
    
    args = parser.parse_args()
    
    config = load_config(args.config)
    
    if args.command == "set":
        config[args.key] = args.value
        save_config(args.config, config)
        print(f"Set {args.key} = {args.value}")
    
    elif args.command == "get":
        if args.key in config:
            print(f"{args.key} = {config[args.key]}")
        else:
            print(f"Key '{args.key}' not found")
    
    elif args.command == "list":
        for key, value in config.items():
            print(f"{key} = {value}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Run it:

```bash
python config_cli.py set name Alice
python config_cli.py set age 30
python config_cli.py get name
python config_cli.py list
```

---

## Challenge Exercises

### Challenge 1: Build a Todo CLI

Create a file called `todo_cli.py`:

```python
"""Todo CLI application."""

import argparse
import json
from pathlib import Path
from datetime import datetime

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = Path(filename)
        self.todos = self._load()
    
    def _load(self):
        if self.filename.exists():
            return json.loads(self.filename.read_text())
        return []
    
    def _save(self):
        self.filename.write_text(json.dumps(self.todos, indent=2))
    
    def add(self, title):
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "completed": False,
            "created": datetime.now().isoformat(),
        }
        self.todos.append(todo)
        self._save()
        print(f"Added: {title}")
    
    def list(self):
        for todo in self.todos:
            status = "✓" if todo["completed"] else "○"
            print(f"{status} {todo['id']}: {todo['title']}")
    
    def complete(self, todo_id):
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self._save()
                print(f"Completed: {todo['title']}")
                return
        print(f"Todo {todo_id} not found")

def main():
    parser = argparse.ArgumentParser(description="Todo CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser("add", help="Add a todo")
    add_parser.add_argument("title", help="Todo title")
    
    subparsers.add_parser("list", help="List todos")
    
    complete_parser = subparsers.add_parser("complete", help="Complete a todo")
    complete_parser.add_argument("id", type=int, help="Todo ID")
    
    args = parser.parse_args()
    app = TodoApp()
    
    if args.command == "add":
        app.add(args.title)
    elif args.command == "list":
        app.list()
    elif args.command == "complete":
        app.complete(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Run it:

```bash
python todo_cli.py add "Buy groceries"
python todo_cli.py add "Write code"
python todo_cli.py list
python todo_cli.py complete 1
python todo_cli.py list
```

---

## Hints

**Arguments not parsing** → Check argument names and types. Use `--help` to verify.

**Subcommands not working** → Ensure you set `dest="command"` and use `set_defaults(func=...)`.

**File not found** → Use `Path.exists()` to check before reading.

**Progress bar not showing** → Use `flush=True` in print to update immediately.

---

## What to Review If You Get Stuck

- **sys.argv** → Handbook section 2.1
- **argparse basics** → Handbook section 2.2
- **Subcommands** → Handbook section 2.3
- **User input** → Handbook section 2.4
- **File handling** → Handbook section 2.5
- **Best practices** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Parse command-line arguments with argparse
- Create interactive CLI programs
- Implement subcommands
- Handle file operations in CLI programs
- Add progress indicators
- Load and save configuration files
- Build professional CLI tools
- Provide helpful usage information

