# Chapter 23: Where to Go Next

## 1. Overview

You have reached the end of this handbook. You know how Python works: its
syntax, its data structures, its standard library, how to write functions and
classes, how to test your code, how to handle errors, and how to build small
programs that do real things.

That is a solid foundation. But Python is a large ecosystem, and there is a
lot more to explore. The question is: what should you learn next, and in what
order?

This chapter does not teach you any of those topics in depth. Instead, it maps
the territory — what each area is, why it matters, what the key tools are, and
roughly how long it takes to get useful with it. Think of it as a guide to
planning your own continued learning.

The honest answer to "what should I learn next?" is: it depends on what you
want to build. This chapter will help you figure that out.

---

## 2. What You Will Learn

- How to go deeper with testing: fixtures, parametrize, and coverage
- What type checking tools like mypy and pyright do and when to use them
- How Python packaging works and how to share your own code
- How to make HTTP requests and build simple web APIs
- What web frameworks like Flask and Django are for
- How pandas and numpy fit into data analysis work
- How to automate tasks with scripts, scheduling, and subprocess
- How to read official Python documentation effectively
- How to pick projects that will actually teach you something
- How to contribute to open source without it being overwhelming
- How to stay motivated when learning gets slow

---

## 3. Core Concepts

### 3.1 Going Deeper with Testing

Chapter 18 introduced pytest and the basics of writing tests. Once you are
comfortable with that, there are three areas worth learning next.

#### pytest fixtures in depth

You saw fixtures used for setup and teardown. They go further than that.
Fixtures can be **scoped** — run once per test, once per module, or once per
entire test session. This matters when setup is expensive (like starting a
database connection).

```python
import pytest


@pytest.fixture(scope="module")
def database_connection():
    """Set up once for the whole module, not once per test."""
    conn = connect_to_db()
    yield conn
    conn.close()
```

Fixtures can also **depend on other fixtures**, which lets you compose setup
logic cleanly. The built-in `tmp_path`, `monkeypatch`, and `capsys` fixtures
are worth reading about in the pytest documentation.

#### Parametrize

`@pytest.mark.parametrize` lets you run the same test with multiple inputs
without writing a separate test function for each case.

```python
import pytest


def is_palindrome(text: str) -> bool:
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),
    ("a", True),
])
def test_is_palindrome(text: str, expected: bool) -> None:
    assert is_palindrome(text) == expected
```

Each tuple in the list becomes one test case. pytest names them automatically
and reports each one separately if it fails. This is much cleaner than five
separate test functions or a loop inside one test.

#### Coverage

**Coverage** measures which lines of your code are actually executed when
your tests run. A line that is never executed by any test is a line that
could have a bug you have not caught yet.

Install `pytest-cov`:

```bash
pip install pytest-cov
```

Run tests with coverage:

```bash
pytest --cov=my_module --cov-report=term-missing
```

The `term-missing` report shows which line numbers were not covered. A
coverage percentage is a rough guide, not a goal in itself — 100% coverage
does not mean your tests are good, but 40% coverage usually means large
parts of your code are untested.

---

### 3.2 Type Checking: mypy and pyright

Chapter 19 introduced type hints and mypy. If you are working on a project
that will grow or be shared with others, it is worth going further.

**mypy** is the original static type checker. It is mature, widely used, and
integrates well with most editors. You configure it in `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.12"
strict = true
ignore_missing_imports = true
```

**pyright** is a newer type checker from Microsoft, written in TypeScript. It
is faster than mypy on large codebases and is the engine behind Pylance, the
Python language server used in VS Code. If you use VS Code, you are likely
already getting pyright-powered type checking inline.

The two tools agree on most things but differ on some edge cases. For most
projects, pick one and stick with it. mypy is the safer default for CI
pipelines; pyright is better for real-time editor feedback.

**What to learn next with type checking:**

- `TypedDict` — for typing dictionaries with known keys
- `Protocol` — for structural subtyping (duck typing with type safety)
- `dataclasses` with full type annotations
- `overload` — for functions that behave differently based on argument types
- How to handle third-party libraries that have no type stubs (the
  `types-*` packages on PyPI, or writing your own `.pyi` stub files)

Type checking pays off most when you are working on a codebase with multiple
contributors or one you will maintain for a long time. For short scripts and
one-off tools, it is often not worth the overhead.

---

### 3.3 Packaging: Sharing Your Code

When you write a Python library or tool that other people should be able to
install with `pip install`, you need to package it. Packaging in Python has
a reputation for being confusing, but the modern approach is much cleaner
than it used to be.

#### The modern approach: `pyproject.toml`

Everything lives in a single `pyproject.toml` file at the root of your
project. Here is a minimal example:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-tool"
version = "0.1.0"
description = "A short description of what this does."
requires-python = ">=3.10"
dependencies = []

[project.scripts]
my-tool = "my_tool.cli:main"
```

The `[project.scripts]` section creates a command-line entry point. After
installing the package, users can run `my-tool` directly from the terminal.

#### Building and distributing

To build a distributable package:

```bash
pip install build
python -m build
```

This creates a `.whl` (wheel) file and a `.tar.gz` (source distribution) in
a `dist/` directory. You can install the wheel locally with:

```bash
pip install dist/my_tool-0.1.0-py3-none-any.whl
```

To publish to PyPI (the public package index), use `twine`:

```bash
pip install twine
twine upload dist/*
```

You will need a PyPI account. The full process is documented at
[packaging.python.org](https://packaging.python.org).

**What to learn next with packaging:**

- How to write a good `README.md` that renders on PyPI
- How to add classifiers, license metadata, and author information
- How to manage versions (semantic versioning: `MAJOR.MINOR.PATCH`)
- How to use `hatch`, `flit`, or `poetry` as higher-level build tools
- How to set up a GitHub Actions workflow that publishes on every tagged
  release

---

### 3.4 Web APIs: Talking to the Internet

Most real-world Python programs eventually need to talk to a web API — to
fetch data, send a notification, or integrate with a service.

#### Making HTTP requests with `requests`

The `requests` library is the standard choice for making HTTP requests. It
is not in the standard library, but it is so widely used that it is
effectively the default.

```bash
pip install requests
```

A basic GET request:

```python
import requests

response = requests.get("https://api.github.com/users/python")
response.raise_for_status()   # raises an exception for 4xx/5xx responses
data = response.json()
print(data["name"])
print(data["public_repos"])
```

A POST request with JSON:

```python
import requests

payload = {"title": "Test", "body": "Hello", "userId": 1}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,
)
response.raise_for_status()
print(response.json())
```

Key things to learn with `requests`:

- How to pass query parameters (`params=`)
- How to set headers (`headers=`)
- How to handle authentication (API keys, Bearer tokens)
- How to handle timeouts (`timeout=`) — always set one
- How to handle pagination (many APIs return results in pages)

#### Building a simple API with Flask or FastAPI

If you want to build a web API rather than just consume one, Flask and
FastAPI are the two most common choices for beginners.

**Flask** is minimal and explicit. You define routes as decorated functions
and return responses. It does not impose much structure, which makes it easy
to learn but means you have to make more decisions yourself.

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name: str):
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True)
```

**FastAPI** is newer and built around type hints. It generates interactive
API documentation automatically and validates request/response data using
Pydantic. It is a better choice if you are building something that will be
used by others or needs to be well-documented.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def hello(name: str) -> dict:
    return {"message": f"Hello, {name}!"}
```

Both are worth knowing. Flask is simpler to start with; FastAPI is more
productive for larger APIs. Neither is covered in depth in this handbook —
each has its own extensive documentation and tutorials.

---

### 3.5 Web Development

If you want to build full web applications — with HTML pages, user accounts,
forms, and a database — you need a web framework.

**Django** is the most complete option. It includes an ORM (for talking to
databases), an admin interface, authentication, form handling, and a template
engine. It follows a "batteries included" philosophy: most things you need
are already there. The learning curve is steeper than Flask, but the payoff
is that you can build production-quality applications without assembling
dozens of separate packages.

**Flask** can also be used for full web applications, but you have to add
each piece yourself: a database library (SQLAlchemy), a form library
(WTForms), authentication, and so on. This gives you more control but
requires more decisions.

**What to learn first if you want web development:**

1. How HTML and CSS work (you need this regardless of which framework you
   use — Python frameworks generate HTML, but you still write it)
2. How HTTP works: requests, responses, status codes, cookies, sessions
3. How databases work: SQL basics, tables, queries, joins
4. Then pick Django or Flask and follow their official tutorial

The Django tutorial at [docs.djangoproject.com](https://docs.djangoproject.com)
is one of the best framework tutorials available. Start there.

---

### 3.6 Data Analysis: pandas and numpy

If your work involves analyzing data — spreadsheets, CSVs, time series,
statistics — pandas and numpy are the tools you will use.

**numpy** provides fast array operations. It is the foundation that pandas
and most scientific Python libraries are built on. You rarely use numpy
directly unless you are doing numerical computing or working with images and
signals.

**pandas** provides the `DataFrame` — a table-like data structure with
labeled rows and columns. It makes it easy to load, filter, transform, and
summarize tabular data.

```python
import pandas as pd

df = pd.read_csv("sales.csv")
print(df.head())
print(df["revenue"].sum())
print(df.groupby("region")["revenue"].mean())
```

The learning curve for pandas is real. The API is large and some of it is
inconsistent. The best way to learn it is to work through a real dataset
that you care about, not to read the documentation from start to finish.

**What to learn first with pandas:**

- Loading data: `read_csv`, `read_json`, `read_excel`
- Inspecting data: `head`, `info`, `describe`, `shape`
- Selecting data: column selection, boolean indexing, `loc` and `iloc`
- Transforming data: `apply`, `map`, `assign`, `rename`
- Aggregating data: `groupby`, `agg`, `pivot_table`
- Handling missing data: `isna`, `dropna`, `fillna`

**Jupyter notebooks** are the standard environment for data analysis work.
They let you run code in cells and see results inline, which makes
exploration much faster than running a script repeatedly.

```bash
pip install jupyter pandas numpy
jupyter notebook
```

---

### 3.7 Automation: Scripts, Scheduling, and subprocess

Python is excellent for automation — replacing repetitive manual tasks with
scripts that run on a schedule or in response to events.

#### File and system automation

You already know `pathlib` for working with files. Combined with the
standard library modules you learned in Chapter 17, you can automate a lot:

```python
import shutil
from pathlib import Path
from datetime import date

# Archive old log files
log_dir = Path("logs")
archive_dir = Path("archive") / str(date.today())
archive_dir.mkdir(parents=True, exist_ok=True)

for log_file in log_dir.glob("*.log"):
    if log_file.stat().st_size > 0:
        shutil.move(str(log_file), archive_dir / log_file.name)
```

#### Running other programs with `subprocess`

`subprocess` lets you run shell commands and other programs from Python,
capture their output, and check whether they succeeded.

```python
import subprocess

result = subprocess.run(
    ["git", "log", "--oneline", "-5"],
    capture_output=True,
    text=True,
    check=True,   # raises CalledProcessError if the command fails
)
print(result.stdout)
```

Use `subprocess.run` for most cases. Avoid `os.system` — it does not give
you access to the output and is harder to use safely.

Key things to know:

- `capture_output=True` captures stdout and stderr
- `text=True` decodes the output as a string (instead of bytes)
- `check=True` raises an exception if the command exits with a non-zero code
- Pass arguments as a list, not a string, to avoid shell injection issues

#### Scheduling

To run a script on a schedule:

- **On Linux/macOS**: use `cron`. Edit your crontab with `crontab -e` and
  add a line like `0 9 * * 1 python /path/to/script.py` (runs every Monday
  at 9am).
- **On Windows**: use Task Scheduler.
- **In Python**: the `schedule` library provides a simple API for running
  functions at intervals within a long-running script.

```python
import schedule
import time


def daily_report() -> None:
    print("Running daily report...")


schedule.every().day.at("09:00").do(daily_report)

while True:
    schedule.run_pending()
    time.sleep(60)
```

`schedule` is a third-party library (`pip install schedule`). It is simple
and readable, but it only works while the Python process is running. For
production automation, cron or a proper task queue (like Celery) is more
reliable.

---

### 3.8 Reading Official Documentation

One of the most valuable skills you can develop is reading documentation
effectively. It is faster than searching Stack Overflow for every question,
and it gives you a more complete picture of what a tool can do.

#### The Python standard library docs

The official Python documentation at [docs.python.org](https://docs.python.org)
is well-written and comprehensive. The structure to know:

- **Library Reference** — every standard library module, with full API
  documentation. This is the reference you will use most often.
- **Language Reference** — the formal specification of Python's syntax and
  semantics. Useful when you need to understand exactly how something works.
- **Tutorial** — a gentle introduction to Python. You have gone beyond this,
  but it is worth skimming to fill any gaps.
- **What's New** — a summary of changes in each Python version. Useful for
  understanding what features are available in which version.

#### How to read a module's documentation

When you encounter a new standard library module, follow this pattern:

1. Read the first paragraph — it tells you what the module is for.
2. Skim the list of classes and functions — get a sense of the API surface.
3. Find the function or class you need and read its signature and docstring.
4. Look at the examples at the bottom of the page — they show common usage.

You do not need to read every module from top to bottom. Read what you need,
when you need it.

#### Third-party library docs

Most popular libraries have their own documentation sites. The quality varies,
but the pattern is similar: start with the "Getting Started" or "Quickstart"
section, then use the API reference when you need details.

When a library's documentation is poor, reading the source code is often
faster than searching for answers. Most Python libraries are readable.

#### Using `help()` and `dir()` in the REPL

When you are exploring a module interactively, `help()` and `dir()` are
your friends:

```python
import pathlib
help(pathlib.Path.glob)   # prints the docstring
dir(pathlib.Path)         # lists all attributes and methods
```

`help()` works on modules, classes, functions, and methods. It is the
fastest way to check a function's signature and docstring without leaving
your terminal.

---

## 4. Practical Examples

### 4.1 A Parametrized Test Suite

Here is a realistic example of using `@pytest.mark.parametrize` to test a
function thoroughly without repetitive code.

```python
# password_validator.py
def validate_password(password: str) -> list[str]:
    """
    Validate a password and return a list of error messages.
    An empty list means the password is valid.
    """
    errors: list[str] = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters.")
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one digit.")
    return errors
```

```python
# test_password_validator.py
import pytest
from password_validator import validate_password


@pytest.mark.parametrize("password, expected_errors", [
    ("Secret1!", []),
    ("short1A", ["Password must be at least 8 characters."]),
    ("alllowercase1", ["Password must contain at least one uppercase letter."]),
    ("NoDigitsHere", ["Password must contain at least one digit."]),
    ("ab", [
        "Password must be at least 8 characters.",
        "Password must contain at least one uppercase letter.",
        "Password must contain at least one digit.",
    ]),
])
def test_validate_password(password: str, expected_errors: list[str]) -> None:
    assert validate_password(password) == expected_errors


def test_valid_password_returns_empty_list() -> None:
    assert validate_password("Correct1Horse") == []
```

Each row in the parametrize list is a separate test case. If one fails,
pytest tells you exactly which input caused the failure.

---

### 4.2 Making an HTTP Request with Error Handling

A realistic pattern for calling a web API, with proper error handling and
a timeout.

```python
# github_user.py
import sys
import requests


def get_github_user(username: str) -> dict:
    """
    Fetch a GitHub user's public profile.
    Raises requests.HTTPError on 4xx/5xx responses.
    Raises requests.Timeout if the request takes too long.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python github_user.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    try:
        user = get_github_user(username)
    except requests.HTTPError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.Timeout:
        print("Error: request timed out.", file=sys.stderr)
        sys.exit(1)
    except requests.ConnectionError:
        print("Error: could not connect to GitHub.", file=sys.stderr)
        sys.exit(1)

    print(f"Name:    {user.get('name', 'N/A')}")
    print(f"Company: {user.get('company', 'N/A')}")
    print(f"Repos:   {user.get('public_repos', 0)}")
    print(f"Profile: {user.get('html_url')}")


if __name__ == "__main__":
    main()
```

The key habits here: always set a `timeout`, always call `raise_for_status`,
and always catch specific exceptions rather than a bare `except`.

---

### 4.3 A Simple Automation Script

A script that finds all `.py` files modified in the last 7 days and prints
a summary. Useful as a template for file-based automation.

```python
# recent_changes.py
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path


def files_modified_since(directory: Path, days: int) -> list[Path]:
    """Return .py files modified within the last `days` days."""
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=days)
    results: list[Path] = []
    for path in directory.rglob("*.py"):
        mtime = datetime.fromtimestamp(
            path.stat().st_mtime, tz=timezone.utc
        )
        if mtime >= cutoff:
            results.append(path)
    return sorted(results)


def line_count(path: Path) -> int:
    """Return the number of lines in a file."""
    return sum(1 for _ in path.open(encoding="utf-8"))


def main() -> None:
    root = Path(".")
    recent = files_modified_since(root, days=7)

    if not recent:
        print("No Python files modified in the last 7 days.")
        return

    print(f"Python files modified in the last 7 days ({len(recent)} files):\n")
    total_lines = 0
    for path in recent:
        lines = line_count(path)
        total_lines += lines
        print(f"  {path}  ({lines} lines)")

    print(f"\nTotal: {total_lines} lines across {len(recent)} files.")


if __name__ == "__main__":
    main()
```

---

### 4.4 Reading a Module's Documentation

Here is a practical workflow for learning a new standard library module —
using `textwrap` as an example.

```python
# In the Python REPL or a script:
import textwrap

# Step 1: read the module-level docstring
help(textwrap)

# Step 2: see what's available
print(dir(textwrap))

# Step 3: read a specific function
help(textwrap.wrap)

# Step 4: try it
text = "Python is a high-level, general-purpose programming language."
print(textwrap.wrap(text, width=40))
# ['Python is a high-level,', 'general-purpose programming language.']

print(textwrap.fill(text, width=40))
# Python is a high-level,
# general-purpose programming language.

print(textwrap.dedent("""
    def hello():
        print("hi")
"""))
```

This pattern — `help()`, `dir()`, then experiment — works for any module.
You do not need to read the full documentation before using something.

---

## 5. Common Mistakes

### 5.1 Trying to Learn Everything at Once

The Python ecosystem is large. There are frameworks for web development,
data science, machine learning, automation, game development, embedded
systems, and more. Trying to learn all of them in parallel leads to shallow
knowledge of everything and deep knowledge of nothing.

Pick one direction based on what you want to build. Learn that area well
enough to build something real. Then expand from there.

---

### 5.2 Tutorial Paralysis

Watching tutorials and reading documentation is not the same as learning.
You learn by writing code, hitting errors, and figuring out why they happen.

A common trap: finishing one tutorial, then immediately starting another
tutorial on the same topic because the first one did not feel complete. This
loop can go on indefinitely without producing any real skills.

The fix: after any tutorial, build something small with what you just learned
— even if it is imperfect. The friction of building is where the learning
happens.

---

### 5.3 Skipping Testing When Learning New Tools

When you are learning a new library, it is tempting to skip writing tests
because you are "just exploring." But tests are especially valuable when you
are learning, because they force you to understand what a function actually
does rather than what you think it does.

Write at least a few tests for any non-trivial code you write, even in
learning projects. The habit is more important than the coverage percentage.

---

### 5.4 Ignoring Error Messages

Error messages in Python are usually informative. A `TypeError` tells you
what types were involved. An `ImportError` tells you what could not be found.
A `requests.HTTPError` tells you the status code.

Read the full traceback before searching for the error online. The last line
is the error; the lines above it show you where in your code it happened.
Often the answer is in the traceback itself.

---

### 5.5 Not Using Version Control

If you are not using git for your learning projects, start now. You do not
need to push everything to GitHub, but having a local git history means you
can experiment freely and roll back when something breaks.

```bash
git init
git add .
git commit -m "Initial commit"
```

That is enough to get started. Learn branching and merging when you need
them.

---

### 5.6 Waiting Until You Are "Ready" to Contribute to Open Source

Many people plan to contribute to open source "once they know enough." That
threshold never arrives on its own. You learn by contributing, not before.

Start small: fix a typo in documentation, improve an error message, add a
missing test. These contributions are genuinely useful and they teach you
how real projects are structured.

---

## 6. Practice Tasks

These tasks are intentionally open-ended. They are meant to push you toward
building real things rather than completing exercises with known answers.

1. **Go deeper with testing.** Take a project you have already written and
   add `@pytest.mark.parametrize` to at least two test functions. Then
   install `pytest-cov` and run coverage. Find one uncovered code path and
   write a test for it.

2. **Set up mypy on a project.** Install mypy, add a `[tool.mypy]` section
   to `pyproject.toml` with `strict = true`, and run it on a Python file
   you have written. Fix every error it reports. If you have no errors,
   find a function that is missing type hints and add them.

3. **Make an HTTP request.** Pick a public API (GitHub, Open-Meteo for
   weather, or any other free API that does not require authentication).
   Write a script that fetches data from it, parses the JSON response, and
   prints a useful summary. Handle timeouts and HTTP errors properly.

4. **Build a minimal package.** Create a new directory with a
   `pyproject.toml`, a `src/` layout, and at least one module with a
   function. Install it in editable mode with `pip install -e .` and import
   it from a separate script. Verify it works.

5. **Automate something you do manually.** Think of a repetitive task you
   do on your computer — renaming files, organizing downloads, generating a
   report from a CSV. Write a Python script that does it. Use `pathlib`,
   `subprocess`, or `shutil` as needed.

6. **Read a module's documentation.** Pick a standard library module you
   have not used before — `itertools`, `functools`, `contextlib`, or
   `dataclasses`. Read its documentation page on docs.python.org. Then
   write three small examples that use different parts of the module.

7. **Find a beginner-friendly open source project.** Search GitHub for
   Python projects with the `good first issue` label. Read the contributing
   guide. Find one issue you could address — even a documentation fix — and
   try to submit a pull request.

8. **Build a project you actually want.** Pick something you would use
   yourself: a CLI tool, a small web scraper, a script that automates
   something annoying, a simple web API. It does not have to be original or
   impressive. Build it, test it, and use it.

---

## 7. Key Takeaways

- **Testing deeper**: `@pytest.mark.parametrize` runs one test function
  with many inputs. Fixtures can be scoped to avoid expensive setup.
  `pytest-cov` shows which lines your tests do not reach.

- **Type checking**: mypy and pyright catch type errors before runtime.
  pyright is faster and powers VS Code's inline checking; mypy is the
  standard for CI. Both are configured in `pyproject.toml`.

- **Packaging**: modern Python packaging uses `pyproject.toml`. `python -m
  build` creates distributable files. `twine upload` publishes to PyPI.
  Learn this when you have something worth sharing.

- **HTTP requests**: the `requests` library is the standard tool. Always
  set a timeout, call `raise_for_status`, and catch specific exceptions.
  Flask and FastAPI are the two main options for building APIs.

- **Web development**: Django is the most complete framework for full web
  applications. Flask is simpler but requires more assembly. Learn HTML,
  CSS, and SQL basics before diving into either.

- **Data analysis**: pandas and numpy are the standard tools. The best way
  to learn pandas is to work through a real dataset. Jupyter notebooks make
  exploration faster.

- **Automation**: `pathlib` and `shutil` for files, `subprocess` for
  running other programs, `cron` or Task Scheduler for scheduling. Always
  pass arguments to `subprocess.run` as a list, not a string.

- **Documentation**: `docs.python.org` is comprehensive and well-written.
  Use `help()` and `dir()` in the REPL for quick lookups. Read the
  "Getting Started" section of any new library before the full API
  reference.

- **Projects**: build things you actually want to use. Imperfect projects
  that exist teach you more than perfect projects that never get started.

- **Open source**: start with documentation fixes and small bug reports.
  The `good first issue` label on GitHub is a real signal, not just a
  courtesy.

- **Staying motivated**: the learning curve flattens after the basics, but
  it never disappears. Expect to spend time confused. That is not a sign
  you are doing it wrong — it is the process.

---

### You Have Reached the End

This handbook started with installing Python and ended here, at the edge of
a much larger ecosystem. The foundation you have built — understanding how
Python works, how to structure programs, how to test them, and how to read
documentation — is what makes everything else learnable.

The next step is yours to choose. Pick something that interests you, build
something real, and keep going.

---

*See also:*
- [Exercises for Chapter 23](../exercises/23-where-to-go-next.md)
- [Solutions for Chapter 23](../solutions/23-where-to-go-next.md)
- [Learning Path](../learning-path.md)
- [FAQ](../faq.md)
