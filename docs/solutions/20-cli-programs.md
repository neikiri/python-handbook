# Solutions 20: CLI Programs

## Overview

Chapter 20 exercises cover building command-line programs using `sys.argv`, `argparse`, subcommands, interactive input, progress indicators, and configuration files. This guide explains the reasoning behind each solution and highlights best practices for professional CLI tools.

---

## Notes Before Checking Solutions

A good CLI program behaves like a Unix tool: it does one thing well, provides helpful error messages, supports `--help`, and exits with a non-zero status code on failure. `argparse` handles most of this automatically.

---

## Warm-up Exercise Solutions

### Exercise 1: Use sys.argv

```python
import sys

def main():
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

Run:

```bash
python simple_cli.py Alice
# Hello, Alice!

python simple_cli.py
# Usage: python simple_cli.py <name>
# (exits with code 1)
```

**`sys.exit(1)`** exits the program with a non-zero status code, signaling failure to the shell. Exit code `0` means success; any non-zero value means failure. This matters for shell scripts and CI pipelines that check exit codes.

**`sys.argv[0]`** is the script name. Arguments start at `sys.argv[1]`. All values are strings — convert them explicitly if you need numbers.

**`sys.argv` is fine for very simple scripts**, but `argparse` is better for anything with more than one argument because it handles `--help`, type conversion, and error messages automatically.

---

### Exercise 2: Use argparse

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="A simple greeting program"
    )

    parser.add_argument("name", help="Name to greet")
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

Run:

```bash
python argparse_cli.py Alice
# Hello, Alice!

python argparse_cli.py Alice --greeting Hi --count 3
# Hi, Alice!
# Hi, Alice!
# Hi, Alice!

python argparse_cli.py --help
# usage: argparse_cli.py [-h] [--greeting GREETING] [--count COUNT] name
# ...
```

**Positional arguments** (like `name`) are required and have no `--` prefix. **Optional arguments** (like `--greeting`) have a `--` prefix and a default value.

**`type=int`** tells argparse to convert the string argument to an integer. If the user passes a non-integer, argparse prints an error and exits automatically.

**`argparse` generates `--help` automatically** from the `description` and `help` strings. Always provide helpful `help` text for each argument.

---

### Exercise 3: Handle User Input

```python
def main():
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

**`.strip().lower()`** normalizes user input — it removes leading/trailing whitespace and converts to lowercase. This makes the program more forgiving of minor input variations.

**`continue`** skips the rest of the loop body and goes back to the top. Use it to handle invalid input without deeply nested `if` statements.

---

### Exercise 4: Add Subcommands

```python
import argparse

def cmd_greet(args):
    print(f"Hello, {args.name}!")

def cmd_add(args):
    print(f"{args.a} + {args.b} = {args.a + args.b}")

def cmd_multiply(args):
    print(f"{args.a} * {args.b} = {args.a * args.b}")

def main():
    parser = argparse.ArgumentParser(description="Multi-command CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", help="Name to greet")
    greet_parser.set_defaults(func=cmd_greet)

    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=int)
    add_parser.add_argument("b", type=int)
    add_parser.set_defaults(func=cmd_add)

    mult_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    mult_parser.add_argument("a", type=int)
    mult_parser.add_argument("b", type=int)
    mult_parser.set_defaults(func=cmd_multiply)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Run:

```bash
python subcommand_cli.py greet Alice
python subcommand_cli.py add 5 3
python subcommand_cli.py --help
python subcommand_cli.py greet --help
```

**`set_defaults(func=cmd_greet)`** attaches the handler function to the subparser. When the user runs `greet`, `args.func` is `cmd_greet`. This pattern avoids a long `if args.command == "greet":` chain.

**`hasattr(args, "func")`** checks whether a subcommand was provided. If the user runs the program with no subcommand, `args.func` does not exist, so we print help instead.

---

## Practice Exercise Solutions

### Exercise 5: Build a File Processor

```python
import argparse
from pathlib import Path

def count_lines(filepath):
    return len(Path(filepath).read_text().splitlines())

def count_words(filepath):
    return len(Path(filepath).read_text().split())

def count_chars(filepath):
    return len(Path(filepath).read_text())

def main():
    parser = argparse.ArgumentParser(description="File processor")
    parser.add_argument("file", help="File to process")
    parser.add_argument("--lines", action="store_true", help="Count lines")
    parser.add_argument("--words", action="store_true", help="Count words")
    parser.add_argument("--chars", action="store_true", help="Count characters")

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

**`action="store_true"`** makes a flag that stores `True` when present and `False` when absent. No value is needed: `--lines` sets `args.lines = True`.

**Show all stats when no flags are given** — this is a common CLI convention. The tool is useful with no flags (shows everything) and more focused with specific flags.

---

### Exercise 6: Add Progress Indicators

```python
import argparse
import time

def show_progress(total):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar_length = 40
        filled = int(bar_length * i / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\r[{bar}] {percent:.1f}%", end="", flush=True)
        time.sleep(0.05)
    print()  # newline after progress bar

def main():
    parser = argparse.ArgumentParser(description="Progress demo")
    parser.add_argument("--steps", type=int, default=100)
    args = parser.parse_args()

    print("Processing...")
    show_progress(args.steps)
    print("Done!")

if __name__ == "__main__":
    main()
```

**`\r`** (carriage return) moves the cursor to the beginning of the current line without advancing to the next line. Combined with `end=""` and `flush=True`, this overwrites the same line on each iteration, creating the animation effect.

**`flush=True`** forces the output buffer to be written immediately. Without it, the progress bar might not update until the buffer is full.

---

### Exercise 7: Create a Configuration File Handler

```python
import argparse
import json
from pathlib import Path

def load_config(filepath):
    if Path(filepath).exists():
        return json.loads(Path(filepath).read_text())
    return {}

def save_config(filepath, config):
    Path(filepath).write_text(json.dumps(config, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Config manager")
    parser.add_argument("--config", default="config.json")
    subparsers = parser.add_subparsers(dest="command")

    set_parser = subparsers.add_parser("set")
    set_parser.add_argument("key")
    set_parser.add_argument("value")

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("key")

    subparsers.add_parser("list")

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

---

## Challenge Exercise Solutions

### Challenge 1: Build a Todo CLI

```python
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
        if not self.todos:
            print("No todos yet.")
            return
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

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    subparsers.add_parser("list")

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int)

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

---

## Common Mistakes

**Not using `if __name__ == "__main__":`** — Without this guard, `main()` runs when the module is imported, which breaks testing and reuse.

**Not validating file existence before reading.** Always check `Path(args.file).exists()` before reading a file argument. argparse does not do this automatically.

**Forgetting `flush=True` in progress bars.** Without it, the progress bar may not update until the buffer fills, making it appear frozen.

**Using `sys.exit()` inside functions.** Prefer raising exceptions or returning error codes. `sys.exit()` makes functions hard to test and reuse.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 21 - Working with Data](../handbook/21-working-with-data.md)
