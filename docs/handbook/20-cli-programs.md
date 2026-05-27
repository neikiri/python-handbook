# Chapter 20: Command-Line Programs

## 1. Overview

A command-line program is a script you run from a terminal, passing arguments
directly on the command line rather than through a graphical interface. Most
developer tools, build systems, and automation scripts work this way: `git`,
`pip`, `pytest`, and `python` itself are all CLI programs.

Python makes it straightforward to build your own. The standard library
provides everything you need: `sys` for raw access to the command line,
`argparse` for structured argument parsing, and `pathlib` for working with
file paths. No third-party packages required.

This chapter starts from the basics — what `sys.argv` is and why it is
limited — then builds up to a complete, well-structured CLI tool using
`argparse`.

---

## 2. What You Will Learn

- What a CLI program is and when building one makes sense
- How `sys.argv` works and why it is not enough on its own
- How to use `argparse` to define positional arguments, optional flags,
  and automatic type conversion
- How to generate useful `--help` output automatically
- How to add subcommands with `add_subparsers`
- How exit codes work and why they matter
- Common CLI patterns: reading files, writing output, verbose/quiet modes
- How to structure a CLI script with `if __name__ == "__main__":`
- A complete worked example: a file statistics tool

---

## 3. Core Concepts

### 3.1 What Is a CLI Program?

A CLI (command-line interface) program is one you invoke from a shell prompt,
optionally passing arguments that control its behavior.

```bash
python wordcount.py report.txt --top 5 --verbose
```

Here `wordcount.py` is the program, `report.txt` is a positional argument
(required input), and `--top 5` and `--verbose` are optional flags.

**When to build a CLI program:**

- You want to automate a task and run it from a terminal or a cron job.
- You are building a developer tool that other programs will call.
- You want to expose a script's behavior without writing a full GUI.
- You need to compose your tool with other Unix tools using pipes.

CLI programs are the right choice for automation, data processing scripts,
and developer utilities. For interactive applications with menus and forms,
a different approach (like a web interface) is usually better.

---

### 3.2 `sys.argv`: Raw Command-Line Arguments

When Python runs a script, it stores the command-line arguments in a list
called `sys.argv`. The first element is always the script name; the rest are
whatever the user typed after it.

```python
# show_args.py
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
print("Argument count:", len(sys.argv) - 1)
```

Run it:

```bash
python show_args.py hello world --flag
```

Output:

```text
Script name: show_args.py
Arguments: ['hello', 'world', '--flag']
Argument count: 3
```

Every element of `sys.argv` is a string, even if the user typed a number.

#### Why `sys.argv` is limited

You can parse `sys.argv` manually, but it gets tedious fast:

```python
# manual_args.py — fragile, hard to maintain
import sys

if len(sys.argv) < 2:
    print("Usage: manual_args.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
verbose = "--verbose" in sys.argv

print(f"File: {filename}, verbose: {verbose}")
```

Problems with this approach:

- No automatic `--help` output.
- No type conversion — everything is a string.
- No validation of required vs. optional arguments.
- Error messages are inconsistent and manual.
- Adding new arguments means rewriting the parsing logic.

`argparse` solves all of these problems.

---

### 3.3 `argparse`: The Standard Solution

`argparse` is the standard library module for parsing command-line arguments.
You describe what arguments your program accepts, and `argparse` handles
parsing, validation, type conversion, and help text generation automatically.

#### Creating a parser

```python
import argparse

parser = argparse.ArgumentParser(
    description="A short description of what this program does."
)
```

The `description` appears in the `--help` output. Keep it to one or two
sentences.

#### Adding a positional argument

Positional arguments are required and identified by their position on the
command line, not by a flag name.

```python
parser.add_argument("filename", help="Path to the input file")
```

The first argument to `add_argument` is the name. Because it does not start
with `--`, `argparse` treats it as positional.

#### Adding optional arguments (flags)

Optional arguments start with `--` (long form) or `-` (short form). They are
not required by default.

```python
parser.add_argument("--output", "-o", help="Path to the output file")
parser.add_argument("--verbose", "-v", action="store_true",
                    help="Print extra information while running")
```

`action="store_true"` means the flag stores `True` when present and `False`
when absent. It takes no value — you either pass `--verbose` or you do not.

#### The `type=` parameter

By default, all argument values are strings. Use `type=` to convert them
automatically.

```python
parser.add_argument("--count", type=int, default=10,
                    help="Number of results to show (default: 10)")
parser.add_argument("--threshold", type=float, default=0.5,
                    help="Minimum score threshold (default: 0.5)")
```

`argparse` calls `int(value)` or `float(value)` on the raw string. If the
conversion fails, it prints a clear error and exits.

You can also pass `type=pathlib.Path` to get a `Path` object directly:

```python
from pathlib import Path

parser.add_argument("filename", type=Path, help="Input file path")
```

#### `default=` values

If an optional argument is not provided, its value is `None` unless you set
a default.

```python
parser.add_argument("--output", default="output.txt",
                    help="Output file (default: output.txt)")
```

Always document the default in the `help=` string so users see it in
`--help` output.

#### Parsing the arguments

Call `parser.parse_args()` to process `sys.argv` and return a namespace
object. Access each argument as an attribute.

```python
args = parser.parse_args()

print(args.filename)   # value of the positional argument
print(args.count)      # value of --count, as an int
print(args.verbose)    # True or False
```

#### Auto-generated `--help`

`argparse` generates a `--help` page automatically from the descriptions you
provide. You get this for free — no extra code needed.

```bash
python myprogram.py --help
```

```text
usage: myprogram.py [-h] [--output OUTPUT] [--count COUNT] [--verbose] filename

A short description of what this program does.

positional arguments:
  filename              Path to the input file

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Path to the output file
  --count COUNT         Number of results to show (default: 10)
  --verbose, -v         Print extra information while running
```

This is one of the biggest advantages of `argparse` over manual `sys.argv`
parsing. Users always have a reference for how to use your tool.

---

### 3.4 A Minimal Complete Example

Here is a small but complete script that uses everything above.

```python
# greet.py
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet one or more people.")
    parser.add_argument("name", help="Name of the person to greet")
    parser.add_argument("--count", "-n", type=int, default=1,
                        help="How many times to greet (default: 1)")
    parser.add_argument("--shout", action="store_true",
                        help="Print the greeting in uppercase")
    args = parser.parse_args()

    message = f"Hello, {args.name}!"
    if args.shout:
        message = message.upper()

    for _ in range(args.count):
        print(message)


if __name__ == "__main__":
    main()
```

```bash
python greet.py Alice
# Hello, Alice!

python greet.py Alice --count 3 --shout
# HELLO, ALICE!
# HELLO, ALICE!
# HELLO, ALICE!

python greet.py --help
# usage: greet.py [-h] [--count COUNT] [--shout] name
# ...
```

---

### 3.5 Subcommands with `add_subparsers`

Many real tools have subcommands — `git commit`, `git push`, `pip install`,
`pip uninstall`. Each subcommand has its own set of arguments.

`argparse` supports this with `add_subparsers`.

```python
# vault.py — a toy secrets manager with subcommands
import argparse


def cmd_add(args: argparse.Namespace) -> None:
    print(f"Adding secret: {args.key} = {args.value}")


def cmd_get(args: argparse.Namespace) -> None:
    print(f"Getting secret: {args.key}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage secrets.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' subcommand
    add_parser = subparsers.add_parser("add", help="Store a secret")
    add_parser.add_argument("key", help="Secret name")
    add_parser.add_argument("value", help="Secret value")
    add_parser.set_defaults(func=cmd_add)

    # 'get' subcommand
    get_parser = subparsers.add_parser("get", help="Retrieve a secret")
    get_parser.add_argument("key", help="Secret name")
    get_parser.set_defaults(func=cmd_get)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
```

```bash
python vault.py add DB_PASSWORD secret123
# Adding secret: DB_PASSWORD = secret123

python vault.py get DB_PASSWORD
# Getting secret: DB_PASSWORD

python vault.py --help
# usage: vault.py [-h] {add,get} ...
```

The pattern `set_defaults(func=cmd_add)` attaches a handler function to each
subcommand. After parsing, `args.func(args)` dispatches to the right handler.
This keeps the `main()` function clean regardless of how many subcommands you
add.

---

### 3.6 Exit Codes

When a program finishes, it returns an integer exit code to the shell. By
convention:

- `0` means success.
- Any non-zero value means failure.

The shell and other programs use exit codes to detect whether a command
succeeded. This matters when your tool is called from a shell script, a CI
pipeline, or another program.

```python
import sys

# Signal success
sys.exit(0)

# Signal failure
sys.exit(1)
```

`sys.exit()` raises `SystemExit`, which Python catches and uses as the
process exit code. You can also call `sys.exit("error message")` — Python
prints the message to stderr and exits with code 1.

In practice, structure your `main()` to return early with `sys.exit(1)` on
errors:

```python
import sys
from pathlib import Path


def main() -> None:
    path = Path("data.txt")

    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(1)

    # ... process the file ...
    sys.exit(0)
```

Printing errors to `sys.stderr` (not `sys.stdout`) is the Unix convention.
It keeps error messages separate from normal output, which matters when the
caller is capturing stdout.

`argparse` automatically exits with code 2 when the user passes invalid
arguments — you do not need to handle that yourself.

---

### 3.7 The `if __name__ == "__main__":` Pattern

Every CLI script should wrap its entry point in this guard:

```python
def main() -> None:
    # all the real work goes here
    ...

if __name__ == "__main__":
    main()
```

`__name__` is a special variable Python sets automatically:

- When you run a file directly (`python myscript.py`), `__name__` is
  `"__main__"`.
- When a file is imported as a module, `__name__` is the module name
  (e.g., `"myscript"`).

Without this guard, running `import myscript` from another file would
immediately execute your CLI logic — parsing arguments, printing output,
possibly calling `sys.exit()`. That is almost never what you want.

With the guard, the module can be imported safely. Other code can call
`myscript.main()` explicitly, or import helper functions from the module
without triggering the CLI.

---

## 4. Practical Examples

### 4.1 Reading from a File Path Argument

A common pattern: accept a file path, validate it exists, then process it.

```python
# linecount.py
import argparse
import sys
from pathlib import Path


def count_lines(path: Path) -> int:
    return sum(1 for _ in path.open(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Count lines in a file.")
    parser.add_argument("file", type=Path, help="File to count")
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"Error: '{args.file}' is not a file.", file=sys.stderr)
        sys.exit(1)

    n = count_lines(args.file)
    print(f"{n} lines in {args.file.name}")


if __name__ == "__main__":
    main()
```

```bash
python linecount.py README.md
# 42 lines in README.md

python linecount.py missing.txt
# Error: 'missing.txt' is not a file.
# (exits with code 1)
```

Using `type=Path` in `add_argument` means `args.file` is already a `Path`
object — no manual conversion needed.

---

### 4.2 Writing Output to stdout vs. a File

A well-designed CLI tool writes its output to stdout by default, but lets
the user redirect it to a file with `--output`.

```python
# upper.py — convert file text to uppercase
import argparse
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a text file to uppercase."
    )
    parser.add_argument("file", type=Path, help="Input file")
    parser.add_argument("--output", "-o", type=Path, default=None,
                        help="Output file (default: print to stdout)")
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"Error: '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)

    text = args.file.read_text(encoding="utf-8").upper()

    if args.output is None:
        print(text, end="")
    else:
        args.output.write_text(text, encoding="utf-8")
        print(f"Written to {args.output}")


if __name__ == "__main__":
    main()
```

```bash
# Print to terminal
python upper.py notes.txt

# Save to a file
python upper.py notes.txt --output notes_upper.txt

# Redirect stdout with the shell (also works)
python upper.py notes.txt > notes_upper.txt
```

Writing to stdout by default makes your tool composable with shell pipes:

```bash
python upper.py notes.txt | grep "IMPORTANT"
```

---

### 4.3 Verbose and Quiet Flags

Many tools support `--verbose` for extra output and `--quiet` to suppress
normal output. A clean way to handle this is to pass a verbosity level
through to your functions.

```python
# process.py
import argparse


def process_items(items: list[str], verbose: bool) -> None:
    for item in items:
        if verbose:
            print(f"  Processing: {item}")
        # ... do real work ...

    print(f"Done. Processed {len(items)} items.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Process a list of items.")
    parser.add_argument("items", nargs="+", help="Items to process")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show each item as it is processed")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Suppress all output except errors")
    args = parser.parse_args()

    if not args.quiet:
        process_items(args.items, verbose=args.verbose)
    else:
        # run silently
        for _ in args.items:
            pass  # real work would go here


if __name__ == "__main__":
    main()
```

`nargs="+"` means "one or more values". The result is a list.

```bash
python process.py a b c
# Done. Processed 3 items.

python process.py a b c --verbose
#   Processing: a
#   Processing: b
#   Processing: c
# Done. Processed 3 items.

python process.py a b c --quiet
# (no output)
```

---

### 4.4 Complete Example: File Statistics Tool

Here is a complete, runnable CLI tool that reports statistics about a text
file: line count, word count, character count, and the most common words.

```python
# filestats.py
"""
Report statistics about a text file.

Usage:
    python filestats.py <file> [--top N] [--verbose]
"""
import argparse
import sys
from collections import Counter
from pathlib import Path


def collect_stats(path: Path) -> dict:
    """Read the file and return a stats dictionary."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    # Strip punctuation from words for frequency count
    clean_words = [
        w.strip(".,!?;:\"'()[]{}").lower()
        for w in words
        if w.strip(".,!?;:\"'()[]{}").isalpha()
    ]

    return {
        "lines": len(lines),
        "words": len(words),
        "chars": chars,
        "word_freq": Counter(clean_words),
    }


def print_stats(path: Path, stats: dict, top: int, verbose: bool) -> None:
    """Print the stats to stdout."""
    print(f"File:       {path.name}")
    print(f"Lines:      {stats['lines']:,}")
    print(f"Words:      {stats['words']:,}")
    print(f"Characters: {stats['chars']:,}")

    if verbose:
        print(f"\nTop {top} words:")
        for word, count in stats["word_freq"].most_common(top):
            print(f"  {word:<20} {count:>5}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Report statistics about a text file."
    )
    parser.add_argument(
        "file",
        type=Path,
        help="Text file to analyse",
    )
    parser.add_argument(
        "--top", "-n",
        type=int,
        default=10,
        help="Number of top words to show with --verbose (default: 10)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show word frequency table",
    )
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"Error: '{args.file}' is not a file.", file=sys.stderr)
        sys.exit(1)

    stats = collect_stats(args.file)
    print_stats(args.file, stats, top=args.top, verbose=args.verbose)
    sys.exit(0)


if __name__ == "__main__":
    main()
```

Example runs:

```bash
python filestats.py README.md
# File:       README.md
# Lines:      87
# Words:      412
# Characters: 2,841

python filestats.py README.md --verbose --top 5
# File:       README.md
# Lines:      87
# Words:      412
# Characters: 2,841
#
# Top 5 words:
#   python                  18
#   the                     14
#   and                     11
#   to                       9
#   a                        8

python filestats.py missing.txt
# Error: 'missing.txt' is not a file.
# (exits with code 1)
```

This tool demonstrates the full pattern:

- `ArgumentParser` with a description
- A positional `file` argument with `type=Path`
- An optional `--top` argument with `type=int` and a default
- A boolean `--verbose` flag
- Input validation with a clear error message to stderr
- `sys.exit(0)` on success, `sys.exit(1)` on failure
- Logic split into small named functions
- `if __name__ == "__main__":` guard

---

## 5. Common Mistakes

### 5.1 Forgetting `if __name__ == "__main__":`

Without the guard, importing your module triggers the CLI logic immediately.

```python
# Wrong — runs on import
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()   # crashes when imported — no args available
print(f"Hello, {args.name}")
```

```python
# Correct — safe to import
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    print(f"Hello, {args.name}")


if __name__ == "__main__":
    main()
```

---

### 5.2 Not Printing Errors to `sys.stderr`

Error messages printed to stdout get mixed into normal output. When the
caller captures stdout (e.g., in a shell script), they will see error
messages in the data stream.

```python
import sys

# Wrong — error goes to stdout
print("Error: file not found.")

# Correct — error goes to stderr
print("Error: file not found.", file=sys.stderr)
```

---

### 5.3 Skipping Exit Codes

If your program encounters an error but exits with code 0, callers cannot
detect the failure.

```python
import sys
from pathlib import Path


def main() -> None:
    path = Path("data.csv")

    if not path.exists():
        # Wrong — exits 0 even on failure
        print("File not found.")
        return

    # ...


def main_correct() -> None:
    path = Path("data.csv")

    if not path.exists():
        # Correct — exits 1 to signal failure
        print("Error: file not found.", file=sys.stderr)
        sys.exit(1)

    # ...
    sys.exit(0)
```

---

### 5.4 Relying on `sys.argv` Directly Instead of `argparse`

Manual `sys.argv` parsing breaks as soon as you add a second argument or
want to support both `-v` and `--verbose`.

```python
import sys

# Fragile — breaks with any argument order change
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: script.py <filename>")
    sys.exit(1)

verbose = "--verbose" in sys.argv or "-v" in sys.argv
```

Use `argparse` instead. It handles all of this correctly and generates help
text automatically.

---

### 5.5 Putting All Logic Inside `main()`

A `main()` function that is hundreds of lines long is hard to test and hard
to read. Extract logic into named functions.

```python
# Hard to test — everything in main()
def main() -> None:
    args = parse_args()
    text = args.file.read_text(encoding="utf-8")
    words = text.split()
    counts = {}
    for word in words:
        word = word.lower().strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, n in top:
        print(f"{word}: {n}")
```

```python
# Easier to test — logic in named functions
from collections import Counter


def read_words(text: str) -> list[str]:
    return [w.lower().strip(".,!?") for w in text.split() if w.isalpha()]


def top_words(words: list[str], n: int) -> list[tuple[str, int]]:
    return Counter(words).most_common(n)


def main() -> None:
    args = parse_args()
    text = args.file.read_text(encoding="utf-8")
    words = read_words(text)
    for word, n in top_words(words, args.top):
        print(f"{word}: {n}")
```

---

### 5.6 Not Documenting Defaults in `help=` Text

Users reading `--help` output cannot see what the default value is unless
you include it.

```python
# Unhelpful — user does not know the default
parser.add_argument("--count", type=int, default=10, help="Number of results")

# Helpful — default is visible in --help
parser.add_argument("--count", type=int, default=10,
                    help="Number of results (default: 10)")
```

---

### 5.7 Using `print()` for All Output in Large Tools

For scripts that run long operations or need to be debugged, `print()` is
not enough. Use `logging` so you can control verbosity without changing code.

```python
import logging

# Configure once at the top of main()
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Then use logger throughout
logger.info("Processing %d files", count)
logger.debug("File details: %s", path)
logger.error("Failed to open: %s", path)
```

With `--verbose`, set the level to `DEBUG`. Without it, leave it at `INFO`.
See Chapter 17 for the full `logging` API.

---

## 6. Practice Tasks

1. Write a script `echo.py` that accepts one or more words as positional
   arguments and prints them joined by spaces. Add a `--upper` flag that
   prints the output in uppercase. Use `nargs="+"`.

2. Write a script `head.py` that accepts a file path and an optional
   `--lines N` argument (default 10) and prints the first N lines of the
   file. Exit with code 1 if the file does not exist.

3. Write a script `rename_ext.py` that accepts a directory path and two
   extension arguments (`--from` and `--to`, e.g., `--from .txt --to .md`)
   and prints what it would rename (dry run only — do not actually rename).
   Use `pathlib`.

4. Extend the `filestats.py` example from section 4.4 to also report the
   average word length. Add it to the `collect_stats` function and display
   it in `print_stats`.

5. Write a script `search.py` that accepts a file path and a search term,
   and prints every line that contains the term along with its line number.
   Add a `--ignore-case` flag. Exit with code 1 if no matches are found.

6. Write a script `jsonformat.py` that reads a JSON file, pretty-prints it
   with `indent=2`, and either writes it back to the same file (with a
   `--in-place` flag) or prints it to stdout. Use `pathlib` and `json`.

7. Add a subcommand structure to `filestats.py`: a `words` subcommand that
   shows word frequency and a `chars` subcommand that shows character
   frequency. Each subcommand should accept the same `file` positional
   argument. Use `add_subparsers`.

---

## 7. Key Takeaways

- `sys.argv` gives you raw command-line arguments as a list of strings.
  It is useful to understand, but too limited for real tools.
- `argparse` is the standard library solution. Define your arguments once
  and get parsing, validation, type conversion, and `--help` for free.
- Positional arguments are required and identified by position. Optional
  arguments start with `--` and are identified by name.
- Use `type=int`, `type=float`, or `type=Path` to convert argument values
  automatically. `argparse` handles the error message if conversion fails.
- `action="store_true"` creates a boolean flag that is `False` by default
  and `True` when the flag is present.
- Use `add_subparsers` when your tool has distinct modes of operation, like
  `git commit` vs. `git push`.
- Exit codes matter. Use `sys.exit(0)` for success and `sys.exit(1)` for
  failure. Print error messages to `sys.stderr`, not `sys.stdout`.
- Always wrap your entry point in `if __name__ == "__main__": main()`. This
  makes the module safe to import and keeps the CLI logic isolated.
- Keep `main()` thin. Extract logic into named functions so it is testable
  and readable.

---

### Further Reading

- [argparse - Command-line option parsing](https://docs.python.org/3/library/argparse.html)
- [sys - System-specific parameters](https://docs.python.org/3/library/sys.html)
- [os - Operating system interface](https://docs.python.org/3/library/os.html)

### What's Next

Ready to continue? Head to the next chapter: **Working with Data**.

→ [Chapter 21 — Working with Data](21-working-with-data.md)

*See also:*
- [Exercise](../exercises/20-cli-programs.md)
- [Solution](../solutions/20-cli-programs.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
