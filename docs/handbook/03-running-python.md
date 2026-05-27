# Chapter 03: Running Python Programs

## 1. Overview

Before you can write useful Python programs, you need to understand how Python actually runs
your code. This chapter covers the mechanics of the Python interpreter, the three main ways to
run Python, and the practical workflow you will use every day as a developer.

Python is an interpreted language. That means you do not compile your code into a standalone
executable before running it — you hand your source code to the Python interpreter, and it takes
care of the rest. Understanding what happens under the hood will help you make sense of error
messages, file organization, and the different tools available to you.

---

## 2. What You Will Learn

By the end of this chapter you will be able to:

- Explain what the Python interpreter does when it runs your code
- Use the interactive REPL for quick experiments
- Run a Python script from the terminal
- Run scripts from VS Code using the Run button and the integrated terminal
- Pass command-line arguments to a script using `sys.argv`
- Use the `if __name__ == "__main__":` guard and explain why it matters
- Use `python -m` to run standard library modules as programs
- Read a basic traceback and know where to look first
- Use `print()` as a simple debugging tool
- Write single-line comments with `#` and understand when to use docstrings

---

## 3. Core Concepts

### 3.1 Python's Execution Model: Source → Bytecode → Interpreter

When you run a Python file, the interpreter does not execute your source code directly. It goes
through several steps.

**Step 1 — Parsing**

The interpreter reads your `.py` file and checks that the syntax is valid. If you have a syntax
error — a missing colon, an unclosed parenthesis, a misspelled keyword — Python stops here and
reports the problem before running a single line.

**Step 2 — Compilation to bytecode**

Python compiles your source code into an intermediate format called *bytecode*. Bytecode is a
lower-level, platform-independent set of instructions. It is not machine code — it cannot run
directly on your CPU. It is designed to run on the Python Virtual Machine (PVM).

**Step 3 — Execution by the Python Virtual Machine**

The PVM reads the bytecode and executes it instruction by instruction. This is where your
program actually runs.

**The `.pyc` cache files**

After compiling your code, Python saves the bytecode to disk in a `__pycache__` directory next
to your source file. These files have a `.pyc` extension and a name that includes the Python
version:

```text
__pycache__/
    my_script.cpython-311.pyc
```

The next time you run the same file, Python checks whether the source has changed. If it has
not, Python skips the compilation step and loads the cached bytecode directly. This makes
startup slightly faster for large programs.

You do not need to manage `.pyc` files yourself. Python handles them automatically. It is safe
to delete the `__pycache__` directory — Python will recreate it the next time you run your code.

> **Note:** `.pyc` files are an implementation detail of CPython, the standard Python
> interpreter. You will rarely need to think about them directly.

**Why this matters for beginners**

The key takeaway is that Python catches *syntax errors* before running anything, but *runtime
errors* only appear when the problematic line actually executes. A file can have a bug on line
50 that you will never see until your program reaches that line. This is why testing and careful
reading of output matters.

---

### 3.2 Three Ways to Run Python

There are three main ways to run Python code. Each has its place, and you will use all three
regularly.

| Method | Command | Best for |
|---|---|---|
| Interactive REPL | `python3` | Quick experiments, exploring APIs |
| Script file | `python3 script.py` | Programs you want to save and reuse |
| Module runner | `python3 -m module_name` | Running standard library tools |

---

### 3.3 The Interactive REPL

REPL stands for **Read–Eval–Print Loop**. It is a live Python session where you type one
expression or statement at a time, Python evaluates it immediately, and prints the result.

**Starting the REPL**

Open a terminal and type:

```bash
python3
```

On Windows, depending on your installation, you may use:

```bash
python
```

You will see output similar to this:

```text
Python 3.11.4 (main, Jul  5 2023, 13:45:01)
[GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` prompt means Python is waiting for your input.

**Basic usage**

```python
>>> 2 + 2
4
>>> "hello" + " world"
'hello world'
>>> len("Python")
6
```

Each time you press Enter, Python evaluates the expression and prints the result on the next
line. If an expression produces no meaningful value (like an assignment), nothing is printed.

```python
>>> x = 10
>>> x
10
>>> x * 3
30
```

**The `_` variable**

The REPL stores the result of the last evaluated expression in a special variable named `_`
(a single underscore). This is useful when you forget to assign a result:

```python
>>> 100 * 3.14
314.0
>>> _
314.0
>>> _ / 2
157.0
```

The `_` variable only works in the REPL. It has no special meaning in script files.

**Multi-line input**

When you type a statement that requires a body — a function definition, a loop, or an `if`
block — the REPL switches to a continuation prompt `...` and waits for you to finish:

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```

Press Enter on a blank `...` line to signal that you are done with the block.

```python
>>> def greet(name):
...     return f"Hello, {name}!"
...
>>> greet("Alice")
'Hello, Alice!'
```

**Exploring with `help()`, `dir()`, and `type()`**

The REPL is a great place to explore Python's built-in tools.

`help()` displays documentation for any object, function, or module:

```python
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

You can also call `help()` with no arguments to enter interactive help mode. Type `quit` to
exit it.

`dir()` lists all the attributes and methods of an object:

```python
>>> dir("hello")
['__add__', '__class__', ..., 'upper', 'zfill']
```

This is useful when you want to know what methods are available on a string, list, or any other
object.

`type()` tells you what kind of object something is:

```python
>>> type(42)
<class 'int'>
>>> type("hello")
<class 'str'>
>>> type([1, 2, 3])
<class 'list'>
```

**Exiting the REPL**

There are several ways to exit:

```python
>>> exit()
```

```python
>>> quit()
```

Or use a keyboard shortcut:

- **Linux / macOS:** Press `Ctrl+D`
- **Windows:** Press `Ctrl+Z`, then `Enter`

**What the REPL is good for**

The REPL is ideal for:

- Testing a small idea before writing it into a file
- Checking how a function behaves with a specific input
- Exploring an unfamiliar module or library
- Doing quick calculations
- Verifying that you understand how an operator or built-in works

**What the REPL is not good for**

- Writing programs longer than a few lines
- Code you want to save and run again later
- Anything that requires multiple files or imports from your own modules
- Code that needs to be shared with others

Everything you type in the REPL is gone when you close it. If you want to keep your code, write
it in a `.py` file.

---

### 3.4 Running a Script File

A script is a plain text file with a `.py` extension that contains Python code. You run it by
passing the filename to the Python interpreter:

```bash
python3 script.py
```

Python reads the file from top to bottom and executes each statement in order.

**Creating and running your first script**

Create a file called `hello.py` with this content:

```python
print("Hello, world!")
print("Python is running this file.")
```

Run it from the terminal:

```bash
python3 hello.py
```

Output:

```text
Hello, world!
Python is running this file.
```

**Running from the correct directory**

Python looks for your script relative to the current working directory — the directory your
terminal is in when you run the command. If your script is in `~/projects/hello.py`, you need
to either navigate there first or provide the full path:

```bash
# Navigate first, then run
cd ~/projects
python3 hello.py

# Or provide the full path from anywhere
python3 ~/projects/hello.py
```

This also affects file operations inside your script. If your script opens `data.txt`, Python
looks for it in the directory where you ran the command, not necessarily where the script lives.
See section 5 (Common Mistakes) for how to handle this correctly.

**The shebang line (Unix/macOS only)**

On Unix-based systems, you can make a Python script directly executable by adding a *shebang
line* as the very first line of the file:

```python
#!/usr/bin/env python3

print("Hello from a directly executable script!")
```

After adding it, mark the file as executable:

```bash
chmod +x hello.py
./hello.py
```

The `#!/usr/bin/env python3` form is preferred over a hardcoded path like `#!/usr/bin/python3`
because `env` searches your `PATH` for the correct Python, which works correctly inside virtual
environments. On Windows, the shebang line is ignored — you always run scripts with
`python script.py`.

---

### 3.5 Script Arguments: `sys.argv`

You can pass extra values to a script on the command line. These are called *command-line
arguments*. Python makes them available through `sys.argv`, which is a list of strings.

```python
# greet.py
import sys

name = sys.argv[1]
print(f"Hello, {name}!")
```

Run it:

```bash
python3 greet.py Alice
```

Output:

```text
Hello, Alice!
```

`sys.argv[0]` is always the name of the script itself. The arguments you pass start at index
`1`. This is a fixed convention — `sys.argv[0]` is always the script name, regardless of how
many arguments follow.

```python
# show_args.py
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
print("Argument count:", len(sys.argv) - 1)
```

```bash
python3 show_args.py one two three
```

```text
Script name: show_args.py
Arguments: ['one', 'two', 'three']
Argument count: 3
```

**Always check the length before accessing elements**

If you access `sys.argv[1]` but the user did not pass any arguments, Python raises an
`IndexError`. Always validate before accessing:

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python3 greet.py <name>")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}!")
```

`sys.exit(1)` stops the program immediately and signals to the shell that something went wrong
(exit code `1` means error; `0` means success).

**All arguments are strings**

`sys.argv` always contains strings, even if you pass a number. You must convert explicitly:

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python3 add.py <num1> <num2>")
    sys.exit(1)

a = float(sys.argv[1])
b = float(sys.argv[2])
print(f"{a} + {b} = {a + b}")
```

```bash
python3 add.py 3.5 2.1
```

```text
3.5 + 2.1 = 5.6
```

> **Going further:** `sys.argv` is the simplest way to handle arguments. For programs with
> multiple options and flags, the standard library's `argparse` module provides a much richer
> interface. Chapter 20 covers building command-line programs in depth.

---

### 3.6 The `if __name__ == "__main__":` Guard

When Python runs a file, it sets a special variable called `__name__`. The value depends on
*how* the file is being run:

- If you run the file directly (`python3 my_module.py`), Python sets `__name__` to the string
  `"__main__"`.
- If the file is imported by another file (`import my_module`), Python sets `__name__` to the
  module's name (`"my_module"`).

This distinction matters because you often want a file to behave differently depending on
whether it is being run directly or imported.

**The problem without the guard**

```python
# calculator.py

def add(a, b):
    return a + b

# This runs every time the file is imported — almost never what you want
print("Testing add:", add(2, 3))
```

If another file does `import calculator`, the `print` statement runs automatically. That is
unexpected and annoying.

**The solution: the guard**

```python
# calculator.py

def add(a, b):
    return a + b

if __name__ == "__main__":
    # This only runs when you execute: python3 calculator.py
    print("Testing add:", add(2, 3))
```

Now when another file does `import calculator`, the `print` statement is skipped. The functions
are available, but the test code does not run.

**The standard pattern with a `main()` function**

The most common and cleanest pattern is to put the entry-point logic inside a `main()` function
and call it from the guard:

```python
# my_tool.py

def process(data):
    """Strip whitespace and convert to uppercase."""
    return data.strip().upper()

def main():
    text = input("Enter some text: ")
    result = process(text)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

This pattern has several advantages:

- The `process()` function is importable and testable by other modules
- The `main()` function is also importable (useful for testing)
- The script still runs correctly when executed directly
- The code is organized: reusable logic at the top, entry point at the bottom

You will see this pattern in virtually every Python script that is meant to be both importable
and runnable. Adopt it from the start.

---

### 3.7 Running a Module with `python -m`

The `-m` flag tells Python to run a module by name rather than by file path. Python looks up
the module in its module search path and runs it.

```bash
python3 -m module_name
```

**Why use `-m`?**

When you use `-m`, Python sets up the module's package context properly. This matters when you
are running tools that are part of a package, or when you want to avoid path-related issues.
It also ensures you are using the Python and packages from the currently active environment.

**Common uses**

Start a simple HTTP server to serve files from the current directory:

```bash
python3 -m http.server
```

```text
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Open a browser at `http://localhost:8000` to see the files in your current directory. Press
`Ctrl+C` to stop the server.

Specify a port:

```bash
python3 -m http.server 9000
```

Pretty-print a JSON file:

```bash
python3 -m json.tool data.json
```

Benchmark a small snippet with `timeit`:

```bash
python3 -m timeit "'-'.join(str(n) for n in range(100))"
```

Run your test suite with pytest (once installed):

```bash
python3 -m pytest
```

Using `python3 -m pytest` instead of just `pytest` ensures you are using the pytest that
belongs to the currently active Python environment, which avoids subtle version mismatch bugs.

**Running your own package with `-m`**

If you have a package with a `__main__.py` file, you can run it with `-m`:

```text
mypackage/
    __init__.py
    __main__.py
    utils.py
```

```bash
python3 -m mypackage
```

Python will execute `mypackage/__main__.py`. This is how many command-line tools are structured.

---

### 3.8 Running Python from VS Code

Most code editors, including VS Code, provide a "Run" button that executes your current file
with a single click. Understanding the difference between using it and running Python from the
terminal directly will save you confusion.

**The Run button**

In VS Code, the Run button (the green triangle in the top-right corner, or `Ctrl+F5`) runs the
currently open file using the Python interpreter VS Code is configured to use. Output appears
in the integrated terminal panel at the bottom.

This is convenient for quick iterations. The main things to know:

- VS Code uses whichever Python interpreter is selected in the bottom status bar. If you have
  multiple Python versions or virtual environments, make sure the right one is selected.
- You cannot easily pass command-line arguments with the Run button. For that, you need to
  configure a launch configuration in `.vscode/launch.json`, or just use the terminal.
- The integrated terminal in VS Code is a real terminal. You can run `python3 script.py` there
  exactly as you would in a standalone terminal window.

**The integrated terminal**

Open the integrated terminal with `` Ctrl+` `` (backtick). This gives you a full terminal
inside VS Code. You can run Python commands here exactly as you would anywhere else:

```bash
python3 my_script.py
python3 my_script.py arg1 arg2
python3 -m http.server
```

**Recommendation for beginners**

Use the terminal — either the integrated terminal in VS Code or a standalone terminal window.
It builds habits that transfer to any environment: a remote server, a CI pipeline, a
colleague's machine. The Run button is a shortcut, not a substitute for understanding what is
happening.

Once you are comfortable with the terminal, using the Run button for quick iterations is
perfectly fine.

---

### 3.9 Reading Error Output: Understanding Tracebacks

When Python encounters an error while running your code, it prints a *traceback* — a report
that shows where the error occurred and what the call stack looked like at that moment.

**A simple example**

Create a file called `broken.py`:

```python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```

Run it:

```bash
python3 broken.py
```

Output:

```text
Traceback (most recent call last):
  File "broken.py", line 4, in <module>
    result = divide(10, 0)
  File "broken.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

**How to read a traceback**

1. **Start at the bottom.** The last line tells you the type of error (`ZeroDivisionError`) and
   a short description (`division by zero`). This is the most important line.

2. **Work upward.** Each block above shows a step in the call chain. The most recent call is at
   the bottom; the outermost call is at the top.

3. **Find the file and line number.** Each entry shows the filename, line number, and the code
   on that line. Go to that line in your editor.

In this example:
- Line 4 called `divide(10, 0)` — this is where the bad value came from
- Line 2 inside `divide` tried to compute `a / b` — this is where the error actually happened

**Common error types you will see early on**

| Error type | What it means |
|---|---|
| `SyntaxError` | Python could not parse your code — check for typos, missing colons, unmatched brackets |
| `IndentationError` | Indentation is wrong — a block is missing or has extra spaces |
| `NameError` | You used a variable or function name that does not exist yet |
| `TypeError` | You used a value of the wrong type — e.g., adding a string and an integer |
| `ValueError` | The type is right but the value is invalid — e.g., `int("hello")` |
| `IndexError` | You accessed a list index that does not exist |
| `KeyError` | You accessed a dictionary key that does not exist |
| `ZeroDivisionError` | You divided by zero |
| `FileNotFoundError` | Python could not find the file you tried to open |
| `AttributeError` | You called a method or accessed an attribute that does not exist on that object |

**Syntax errors look different**

A `SyntaxError` is caught before the program runs, so the traceback looks slightly different:

```python
# missing_colon.py
def greet(name)
    print(f"Hello, {name}!")
```

```text
  File "missing_colon.py", line 1
    def greet(name)
                   ^
SyntaxError: expected ':'
```

Python points directly at the problem with a caret (`^`). In Python 3.10+, error messages are
significantly more descriptive than in older versions — they often tell you exactly what is
wrong and sometimes suggest a fix.

> **Full coverage:** Chapter 12 covers error types, exception handling, and debugging in depth.
> For now, focus on reading the last line and the file/line references.

---

### 3.10 `print()` for Output and Basic Debugging

`print()` is the simplest way to produce output and to understand what your program is doing.

**Basic output**

```python
print("Hello, world!")
print(42)
print(3.14)
print(True)
```

```text
Hello, world!
42
3.14
True
```

`print()` accepts any number of arguments, separated by commas. By default it puts a space
between them and a newline at the end:

```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
```

```text
Name: Alice Age: 30
```

You can change the separator with `sep` and the ending with `end`:

```python
print("one", "two", "three", sep="-")
print("no newline here", end=" ")
print("same line")
```

```text
one-two-three
no newline here same line
```

**f-strings for formatted output**

The cleanest way to embed variable values in output strings is with f-strings (formatted string
literals). Prefix the string with `f` and put variable names or expressions inside `{}`:

```python
name = "Alice"
score = 95.5
print(f"Player: {name}, Score: {score:.1f}")
```

```text
Player: Alice, Score: 95.5
```

The `:.1f` inside the braces is a format specifier — it rounds the float to one decimal place.
F-strings are covered in depth in Chapter 07.

**Using `print()` to debug**

Before you learn about debuggers and logging, `print()` is the fastest way to understand what
your program is doing. Insert `print()` calls at key points to see what values variables hold
and whether certain lines are being reached.

```python
def calculate_total(prices):
    print(f"[debug] prices received: {prices}")
    total = sum(prices)
    print(f"[debug] total calculated: {total}")
    return total

result = calculate_total([10, 20, 30])
print(f"Final result: {result}")
```

Output:

```text
[debug] prices received: [10, 20, 30]
[debug] total calculated: 60
Final result: 60
```

Labeling your debug output (with `[debug]` or a variable name prefix) makes it easy to
distinguish from real program output and easy to find and remove later.

**Useful `print()` debugging patterns**

Print a variable's type and value together:

```python
data = "42"
print(type(data), repr(data))   # <class 'str'> '42'

data = int(data)
print(type(data), repr(data))   # <class 'int'> 42
```

`repr()` shows the raw representation of a value — strings include their quotes, which makes
it clear you are looking at a string rather than a number.

Print inside a loop to trace iteration:

```python
for i, item in enumerate(["a", "b", "c"]):
    print(f"  step {i}: item={item!r}")
```

```text
  step 0: item='a'
  step 1: item='b'
  step 2: item='c'
```

The `!r` inside an f-string is equivalent to calling `repr()` on the value.

**Cleaning up debug output**

Remove or comment out debug `print` calls before sharing your code or committing it to version
control. A quick way to find them is to search for `[debug]` or whatever prefix you used.

`print()` debugging is not the most sophisticated approach, but it is fast, requires no setup,
and works everywhere. You will use it throughout your Python career.

---

### 3.11 Comments: `#` and Docstrings

Comments let you leave notes in your code for human readers. Python ignores them completely
when running your program.

**Single-line comments with `#`**

Use the `#` character to start a comment. Everything from `#` to the end of the line is
ignored:

```python
# This is a full-line comment.
x = 10  # This is an inline comment.

# Explain why, not just what:
# We add 1 here because the API uses 1-based indexing.
page_number = current_page + 1
```

Good comments explain *why* something is done, not *what* the code does. The code itself shows
what it does. Comments add context that the code cannot express on its own.

Python has no multi-line comment syntax like `/* ... */` in C or Java. For a block of
explanatory text, use multiple `#` lines:

```python
# This function calculates compound interest.
# Formula: A = P * (1 + r/n) ** (n * t)
# Where:
#   P = principal amount
#   r = annual interest rate (as a decimal)
#   n = number of times interest compounds per year
#   t = time in years
def compound_interest(principal, rate, n, t):
    return principal * (1 + rate / n) ** (n * t)
```

**Docstrings: a brief introduction**

A *docstring* is a string literal that appears as the first statement in a function, class, or
module. It documents what that thing does. Python stores it in the object's `__doc__` attribute,
and tools like `help()`, IDEs, and documentation generators can read it automatically.

Docstrings use triple quotes:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

For longer docstrings, the first line is a short summary, followed by a blank line and more
detail:

```python
def divide(a, b):
    """
    Divide a by b and return the result.

    Raises ZeroDivisionError if b is zero.
    """
    return a / b
```

You can read a docstring with `help()` or by accessing `__doc__` directly:

```python
>>> help(add)
Help on function add in module __main__:

add(a, b)
    Return the sum of a and b.

>>> add.__doc__
'Return the sum of a and b.'
```

The difference between a comment and a docstring:

- A `#` comment is for anyone reading the source code. Python discards it entirely.
- A docstring is attached to the object it documents and is accessible at runtime. It is the
  standard way to document functions, classes, and modules.

Write docstrings for every function you define. It is one of the most useful habits you can
build. Chapter 04 covers docstrings in more depth alongside the rest of Python's syntax rules.

---

### 3.12 The Practical Workflow

Every Python developer follows some version of this loop:

```text
write → save → run → read output → fix → repeat
```

**1. Write**

Open your `.py` file in an editor and write or modify your code.

**2. Save**

Save the file. Python runs the file as it exists on disk — unsaved changes are invisible to the
interpreter. Make saving a reflex: press `Ctrl+S` (or `Cmd+S` on macOS) before every run.

**3. Run**

Switch to your terminal and run the file:

```bash
python3 my_script.py
```

**4. Read output**

Look at what Python printed. If there is a traceback, read it from the bottom up. If the output
is not what you expected, add `print()` calls to investigate.

**5. Fix**

Go back to your editor, make a change, and save.

**6. Repeat**

Run the file again. Keep iterating until the output is correct.

This loop is the foundation of all Python development, from beginner scripts to large
applications. The tools get more sophisticated over time — debuggers, test runners, type
checkers — but the core cycle stays the same.

**A practical setup**

Keep your editor on one side of the screen and your terminal on the other. This lets you edit
and run without switching windows constantly. Most developers settle into this rhythm quickly.

---


---

## 4. Practical Examples

### Example 1: Exploring the REPL

Open a terminal and start the REPL:

```bash
python3
```

Try these expressions one at a time:

```python
>>> 10 + 5
15
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> 2 ** 8
256
```

Use the `_` variable:

```python
>>> 2 ** 10
1024
>>> _ - 24
1000
```

Explore a string:

```python
>>> s = "Python"
>>> type(s)
<class 'str'>
>>> dir(s)
['__add__', '__class__', ..., 'upper', 'zfill']
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.replace("P", "J")
'Jython'
>>> help(s.split)
```

Check what `help()` says about a built-in function:

```python
>>> help(print)
```

Exit when done:

```python
>>> exit()
```

---

### Example 2: A Script with Command-Line Arguments

Create a file called `word_count.py`:

```python
# word_count.py
"""Count the words in a text file."""

import sys


def count_words(text):
    """Return the number of words in the given text."""
    return len(text.split())


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 word_count.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read()

    count = count_words(content)
    print(f"{filename}: {count} words")


if __name__ == "__main__":
    main()
```

Create a sample text file called `sample.txt`:

```text
The quick brown fox jumps over the lazy dog.
Python is a great language for beginners.
```

Run the script:

```bash
python3 word_count.py sample.txt
```

Output:

```text
sample.txt: 18 words
```

Try running it without an argument to see the usage message:

```bash
python3 word_count.py
```

```text
Usage: python3 word_count.py <filename>
```

This example demonstrates:
- Checking `sys.argv` length before accessing arguments
- Providing a usage message when arguments are missing
- Using `sys.exit(1)` to signal an error to the shell
- The `if __name__ == "__main__":` guard with a `main()` function
- A module docstring and function docstrings

---

### Example 3: Using `python -m` with the Standard Library

**Serve files over HTTP**

Navigate to a directory with some files and run:

```bash
python3 -m http.server 8080
```

```text
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
```

Open `http://localhost:8080` in a browser. You will see a directory listing. Press `Ctrl+C` to
stop.

**Pretty-print JSON**

Create a file called `data.json`:

```json
{"name":"Alice","age":30,"languages":["Python","JavaScript"]}
```

Run:

```bash
python3 -m json.tool data.json
```

Output:

```json
{
    "name": "Alice",
    "age": 30,
    "languages": [
        "Python",
        "JavaScript"
    ]
}
```

**Check Python version and environment info**

```bash
python3 -m site
```

This prints information about your Python installation, including where packages are installed.
Useful for diagnosing environment issues.

**Benchmark a snippet**

```bash
python3 -m timeit "sum(range(1000))"
```

```text
50000 loops, best of 5: 8.55 usec per loop
```

---

### Example 4: Reading a Traceback

Create a file called `traceback_demo.py`:

```python
# traceback_demo.py

def get_first_item(items):
    """Return the first item in the list."""
    return items[0]


def process(data):
    """Double the first item in data."""
    first = get_first_item(data)
    return first * 2


result = process([])
print(result)
```

Run it:

```bash
python3 traceback_demo.py
```

Output:

```text
Traceback (most recent call last):
  File "traceback_demo.py", line 13, in <module>
    result = process([])
  File "traceback_demo.py", line 10, in process
    first = get_first_item(data)
  File "traceback_demo.py", line 5, in get_first_item
    return items[0]
IndexError: list index out of range
```

Reading this traceback:

1. **Bottom line:** `IndexError: list index out of range` — Python tried to access index `0`
   of an empty list.
2. **Line 5** in `get_first_item`: `return items[0]` — this is where the error actually
   happened.
3. **Line 10** in `process`: called `get_first_item(data)` — this is what triggered it.
4. **Line 13** at module level: called `process([])` — this is where the empty list came from.

The fix is to handle the empty list case:

```python
def get_first_item(items):
    """Return the first item, or None if the list is empty."""
    if not items:
        return None
    return items[0]
```

---

### Example 5: Using `print()` to Debug

Create a file called `debug_demo.py`:

```python
# debug_demo.py

def find_longest(words):
    """Return the longest word in the list."""
    longest = ""
    for word in words:
        print(f"  [debug] checking: {word!r}, current longest: {longest!r}")
        if len(word) > len(longest):
            longest = word
    return longest


word_list = ["cat", "elephant", "dog", "rhinoceros", "ant"]
print(f"Input: {word_list}")
result = find_longest(word_list)
print(f"Longest word: {result}")
```

Run it:

```bash
python3 debug_demo.py
```

Output:

```text
Input: ['cat', 'elephant', 'dog', 'rhinoceros', 'ant']
  [debug] checking: 'cat', current longest: ''
  [debug] checking: 'elephant', current longest: 'cat'
  [debug] checking: 'dog', current longest: 'elephant'
  [debug] checking: 'rhinoceros', current longest: 'elephant'
  [debug] checking: 'ant', current longest: 'rhinoceros'
Longest word: rhinoceros
```

The `print()` calls inside the loop let you see exactly how the function progresses through the
list. Once you are satisfied the function works correctly, remove or comment out the debug
lines.

---

### Example 6: Comments and Docstrings in Practice

This example shows how comments and docstrings work together in a real script:

```python
#!/usr/bin/env python3
"""
temperature.py

Convert temperatures between Celsius, Fahrenheit, and Kelvin.
Run directly to see a conversion table, or import the functions
into another module.
"""

import sys

# Absolute zero in Celsius — used as a lower bound for validation
ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit and return the result."""
    return celsius * 9 / 5 + 32


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin and return the result."""
    return celsius - ABSOLUTE_ZERO_C


def is_valid_celsius(celsius):
    """Return True if the temperature is physically possible."""
    # Temperatures below absolute zero are not physically meaningful
    return celsius >= ABSOLUTE_ZERO_C


def print_table(start, stop, step=10):
    """
    Print a conversion table from start to stop (inclusive).

    Each row shows the Celsius value alongside its Fahrenheit
    and Kelvin equivalents.
    """
    print(f"{'Celsius':>10}  {'Fahrenheit':>12}  {'Kelvin':>10}")
    print("-" * 38)
    temp = start
    while temp <= stop:
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        print(f"{temp:>10.1f}  {f:>12.1f}  {k:>10.2f}")
        temp += step


def main():
    # Default: show a table from -20°C to 100°C
    start = -20
    stop = 100

    # Allow the user to override the range from the command line
    if len(sys.argv) == 3:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
    elif len(sys.argv) != 1:
        print("Usage: python3 temperature.py [start stop]")
        sys.exit(1)

    print_table(start, stop)


if __name__ == "__main__":
    main()
```

Run it with defaults:

```bash
python3 temperature.py
```

```text
   Celsius   Fahrenheit      Kelvin
--------------------------------------
     -20.0         -4.0      253.15
     -10.0         14.0      263.15
       0.0         32.0      273.15
      10.0         50.0      283.15
      20.0         68.0      293.15
      30.0         86.0      303.15
      40.0        104.0      313.15
      50.0        122.0      323.15
      60.0        140.0      333.15
      70.0        158.0      343.15
      80.0        176.0      353.15
      90.0        194.0      363.15
     100.0        212.0      373.15
```

Run it with a custom range:

```bash
python3 temperature.py 0 40
```

Notice how the script uses:
- A module docstring at the top explaining what the file does
- A constant in `UPPER_CASE` with a comment explaining its purpose
- Function docstrings on every function
- Inline comments explaining non-obvious decisions
- The `if __name__ == "__main__":` guard with a `main()` function
- `sys.argv` with length checking

---

## 5. Common Mistakes

### Mistake 1: Running Python 2 instead of Python 3

On some systems, `python` still refers to Python 2. Always check:

```bash
python --version
python3 --version
```

If `python` gives you Python 2.x, use `python3` for everything in this handbook. Python 2
reached end-of-life in January 2020 and should not be used for new code.

---

### Mistake 2: Forgetting to save before running

This is one of the most common beginner frustrations. You edit your file, run it, and the
output does not reflect your changes. The reason is almost always that you forgot to save.

Make saving a reflex: every time before you run, press `Ctrl+S` (or `Cmd+S` on macOS).

---

### Mistake 3: Running the script from the wrong directory

If your script opens a file by name (e.g., `open("data.txt")`), Python looks for that file
relative to the *current working directory* — the directory your terminal is in when you run
the command, not the directory where the script lives.

```bash
# You are in /home/user
python3 projects/my_script.py
# Python looks for data.txt in /home/user, not in /home/user/projects
```

Fix: either navigate to the script's directory first, or use `pathlib` to build paths relative
to the script file:

```python
from pathlib import Path

# This always works, regardless of where you run the script from
script_dir = Path(__file__).parent
data_file = script_dir / "data.txt"

with open(data_file) as f:
    content = f.read()
```

`__file__` is a special variable Python sets to the path of the currently running script.

---

### Mistake 4: Accessing `sys.argv` without checking its length

If you access `sys.argv[1]` but the user did not pass any arguments, Python raises an
`IndexError`.

**Wrong:**

```python
import sys
name = sys.argv[1]   # crashes if no argument is given
```

**Right:**

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python3 script.py <name>")
    sys.exit(1)

name = sys.argv[1]
```

Always validate `sys.argv` before accessing its elements.

---

### Mistake 5: Omitting the `if __name__ == "__main__":` guard

If you write a module that is meant to be both importable and runnable, and you put executable
code at the top level without the guard, that code runs every time the module is imported.

**Wrong:**

```python
# utils.py
def helper():
    return 42

print("utils loaded!")   # runs on every import — annoying and unexpected
```

**Right:**

```python
# utils.py
def helper():
    return 42

if __name__ == "__main__":
    print("Running utils directly")
    print(helper())
```

---

### Mistake 6: Confusing the REPL and a script file

Code typed in the REPL is not saved anywhere. If you close the REPL, everything you typed is
gone. If you want to keep your code, write it in a `.py` file.

Conversely, if you paste multi-line code into the REPL and it does not behave as expected, it
may be because the REPL handles indentation and blank lines differently from a file. For
anything more than a few lines, use a script file.

---

### Mistake 7: Misreading a traceback — looking at the top instead of the bottom

A common mistake is to look at the *first* line of a traceback instead of the *last*. The
first line just says "Traceback (most recent call last):" — it is a header, not the error. The
actual error type and message are always on the last line.

```text
Traceback (most recent call last):       ← header, not the error
  File "script.py", line 5, in <module>
    result = int("hello")
ValueError: invalid literal for int() with base 10: 'hello'   ← read this first
```

Start at the bottom, then work upward to find where in your code the problem originated.

---

### Mistake 8: Forgetting that `sys.argv` values are always strings

Every value in `sys.argv` is a string, even if it looks like a number. Forgetting to convert
leads to confusing bugs:

```python
import sys

# Wrong — this concatenates strings instead of adding numbers
result = sys.argv[1] + sys.argv[2]
print(result)   # "35" instead of 8 if you passed 3 and 5
```

```python
import sys

# Right — convert to the appropriate type first
result = int(sys.argv[1]) + int(sys.argv[2])
print(result)   # 8
```

---

### Mistake 9: Using triple-quoted strings as block comments

You will sometimes see triple-quoted strings used as multi-line comments:

```python
"""
This is not really a comment.
It is a string that is evaluated and then discarded.
"""
x = 10
```

This works in practice — Python evaluates the string and throws it away — but it is not the
same as a comment. It is a string expression used as a statement. The correct way to write a
block of explanatory text is with multiple `#` lines. Reserve triple-quoted strings for
docstrings (the first statement in a function, class, or module).

---

### Mistake 10: Leaving debug `print()` calls in production code

It is easy to forget to remove debug `print()` calls before sharing or deploying your code.
Stray debug output can confuse users, pollute logs, and expose internal state.

Develop the habit of searching for your debug prefix (e.g., `[debug]`) before committing code.
As you advance, you will learn to use Python's `logging` module, which lets you control output
levels without removing statements from your code.

---

## 6. Practice Tasks

These tasks are designed to be completed in order. Each one builds on the previous.

---

### Task 1: REPL Exploration

Open the Python REPL and complete the following:

1. Calculate `(2 ** 16) - 1`. Then use the `_` variable to divide the result by `255`.
2. Create a string `s = "the quick brown fox"` and use `dir(s)` to find a method that converts
   it to title case. Call that method.
3. Use `help(str.split)` to read the documentation for the `split` method.
4. Use `type()` to check the type of `3.14`, `True`, and `[1, 2, 3]`.
5. Exit the REPL using a keyboard shortcut.

---

### Task 2: Your First Script

Create a file called `greeting.py` that:

1. Asks the user for their name using `input()`
2. Asks the user for their age using `input()`
3. Prints a message like: `Hello, Alice! In 10 years you will be 40.`

Add a module docstring at the top of the file and a comment explaining what the script does.

Run it from the terminal:

```bash
python3 greeting.py
```

---

### Task 3: Command-Line Arguments

Create a file called `repeat.py` that:

1. Reads a word from `sys.argv[1]`
2. Reads a number from `sys.argv[2]`
3. Prints the word repeated that many times, separated by spaces

Example:

```bash
python3 repeat.py hello 4
```

Expected output:

```text
hello hello hello hello
```

Requirements:
- Check that exactly two arguments are provided. If not, print a usage message and exit.
- Convert the second argument to an integer.
- Add a docstring to any functions you write.

---

### Task 4: The `__name__` Guard

Create a file called `math_utils.py` with:

1. A function `square(n)` that returns `n * n`
2. A function `cube(n)` that returns `n * n * n`
3. A `main()` function that tests both functions by printing their results for a few values
4. The `if __name__ == "__main__":` guard that calls `main()`

Then create a second file called `use_math.py` that imports and uses `square` and `cube` from
`math_utils`:

```python
# use_math.py
from math_utils import square, cube

print(square(5))
print(cube(3))
```

Run `use_math.py` and confirm that the test output from `math_utils.py` does not appear.

---

### Task 5: Using `python -m`

1. Navigate to a directory that contains some files.
2. Start a local HTTP server on port 9000:

```bash
python3 -m http.server 9000
```

3. Open `http://localhost:9000` in a browser and confirm you can see the directory listing.
4. Stop the server with `Ctrl+C`.
5. Create a file called `test.json` with some JSON content and use `python3 -m json.tool` to
   pretty-print it.

---

### Task 6: Reading a Traceback

Create a file called `buggy.py` with this content:

```python
def get_value(data, key):
    return data[key]

config = {"host": "localhost", "port": 8080}
value = get_value(config, "timeout")
print(value)
```

1. Run the file and read the traceback carefully.
2. Identify the error type and the line where it occurred.
3. Fix the bug by providing a default value when the key is not found. (Hint: look up
   `dict.get()`.)

---

### Task 7: Debug with `print()`

Create a file called `fizzbuzz.py` with this implementation:

```python
def fizzbuzz(n):
    results = []
    for i in range(n):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(i)
    return results

print(fizzbuzz(16))
```

1. Run the file and look at the output.
2. The output is almost correct, but there is a subtle bug. Add `print()` statements inside the
   loop to trace the values of `i` and what gets appended.
3. Find and fix the bug. (Hint: FizzBuzz traditionally starts at 1, not 0.)

---

### Task 8: A Documented Script

Write a script called `stats.py` that:

1. Accepts one or more numbers as command-line arguments
2. Calculates and prints the minimum, maximum, and average
3. Has a module docstring, function docstrings, and at least two inline comments

Example:

```bash
python3 stats.py 4 8 15 16 23 42
```

Expected output:

```text
Count:   6
Min:     4.0
Max:     42.0
Average: 18.0
```

Requirements:
- Use the `if __name__ == "__main__":` guard
- Validate that at least one argument is provided
- Convert all arguments to floats

---

## 7. Key Takeaways

- **Python's execution model has three steps:** parsing (syntax check), compilation to bytecode,
  and execution by the Python Virtual Machine. The `.pyc` files in `__pycache__` are cached
  bytecode — Python manages them automatically.

- **There are three main ways to run Python:**
  1. The interactive REPL (`python3`) — for quick experiments and exploration
  2. Script files (`python3 script.py`) — for code you want to save and reuse
  3. The module runner (`python3 -m module_name`) — for running standard library tools and
     packages

- **The REPL is a powerful exploration tool.** Use `help()`, `dir()`, and `type()` to learn
  about objects interactively. The `_` variable holds the last result. Everything you type is
  gone when you close it — use script files for code you want to keep.

- **`sys.argv` gives you command-line arguments.** `sys.argv[0]` is the script name; your
  arguments start at index `1`. All values are strings — convert them explicitly. Always check
  the length before accessing elements.

- **`if __name__ == "__main__":` is a standard Python convention.** It separates code that
  runs when a file is executed directly from code that runs when the file is imported. Use it
  in any file that is meant to be both importable and runnable. Pair it with a `main()`
  function for clean organization.

- **`python3 -m` is the correct way to run module-based tools.** It ensures the right Python
  environment is used and sets up package context properly. Use it for `pytest`, `json.tool`,
  `http.server`, and similar tools.

- **VS Code's Run button is a shortcut, not a substitute.** Learn to run Python from the
  terminal first. The integrated terminal in VS Code is a real terminal — use it.

- **Read tracebacks from the bottom up.** The last line tells you the error type and message.
  The entries above show the call chain that led to the error. Python 3.10+ error messages are
  especially descriptive — read them carefully before searching online.

- **`print()` is your first debugging tool.** Insert labeled `print()` calls to inspect
  variable values and trace execution. Use `repr()` or the `!r` format specifier to see the
  raw representation of values. Remove debug output before sharing your code.

- **Comments explain why; code shows what.** Use `#` for inline and block comments. Use
  triple-quoted docstrings as the first statement in functions, classes, and modules — they are
  accessible at runtime via `help()` and `__doc__`.

- **The core development workflow is:** write → save → run → read output → fix → repeat.
  Mastering this loop is more important than any specific tool.

---

## What's Next

Chapter 04 covers Python's syntax and structure — indentation, statements, expressions,
comments, naming conventions, and how Python code is organized at the file level. Once you
understand how to run Python, understanding how to write it correctly is the natural next step.

→ [Chapter 04: Syntax and Structure](04-syntax-and-structure.md)
