# Requirements: python-handbook

## Overview

Build a polished, beginner-friendly Python handbook as a structured open-source learning repository. The goal is to take a learner from zero Python knowledge to practical independent programming.

---

## Functional Requirements

### 1. Repository Skeleton

The repository must include all standard project files and follow the defined directory structure:

- `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `.gitignore`
- `pyproject.toml` (project metadata and dev dependencies)
- `mkdocs.yml` (MkDocs configuration with full navigation)
- `docs/` — all documentation content
- `examples/` — standalone runnable Python scripts
- `projects/` — mini project source code
- `tests/` — pytest test suite
- `.github/workflows/` — CI/CD pipelines

### 2. Handbook Chapters

Each chapter lives in `docs/handbook/` as a Markdown file. Every chapter must follow this structure:

1. Overview
2. What you will learn
3. Core concepts
4. Practical examples
5. Common mistakes
6. Practice tasks
7. Key takeaways

Required chapters (in order):

| # | Chapter |
|---|---------|
| 01 | Introduction to Python |
| 02 | Installation and Setup |
| 03 | Running Python Programs |
| 04 | Syntax and Program Structure |
| 05 | Values, Variables, and Types |
| 06 | Operators, Expressions, and Input |
| 07 | Strings and Text Processing |
| 08 | Control Flow |
| 09 | Lists, Tuples, Sets, and Dictionaries |
| 10 | Functions |
| 11 | Comprehensions, Generators, and Iteration |
| 12 | Errors, Exceptions, and Debugging |
| 13 | Files, Paths, JSON, and CSV |
| 14 | Modules, Packages, and Imports |
| 15 | Virtual Environments and pip |
| 16 | Object-Oriented Programming |
| 17 | Standard Library Tour |
| 18 | Testing and Code Quality |
| 19 | Type Hints |
| 20 | Command-Line Programs |
| 21 | Working with Data |
| 22 | Practical Projects |
| 23 | Where to Go Next |

### 3. Exercises

- One exercise file per chapter in `docs/exercises/`
- Exercises must be practical and match the chapter topic
- Exercise files must NOT contain solutions — only problem statements and hints

### 4. Solutions

- One solution file per exercise in `docs/solutions/`
- Solutions must explain the reasoning, not just show code
- Solutions use Python 3.10+ idioms

### 5. Cheatsheets

Concise reference cards in `docs/cheatsheets/`:

- Python syntax quick reference
- Built-in functions
- String methods
- List / dict / set operations
- File I/O patterns
- Common standard library modules

### 6. Reference Pages

In-depth reference pages in `docs/references/`:

- Built-in types
- Built-in exceptions
- Standard library modules used in the handbook
- Glossary of terms

### 7. Runnable Examples

- Standalone `.py` files in `examples/` organized by topic
- Every file must run without errors using Python 3.10+
- No unnecessary third-party dependencies

### 8. Mini Projects

Eight mini projects in `projects/`, each self-contained:

| Project | Description |
|---------|-------------|
| number-guessing-game | CLI game with random number and user guesses |
| todo-cli | Command-line todo list with file persistence |
| word-counter | Count words/lines/chars in a text file |
| csv-sales-report | Read CSV, compute totals and averages |
| password-generator | Generate secure random passwords |
| budget-tracker | Track income and expenses, show balance |
| log-analyzer | Parse a log file and summarize errors |
| personal-notes-app | Simple notes manager with file storage |

Each project must include a `README.md` and runnable `main.py`.

### 9. Tests

- `tests/` contains pytest tests for all mini projects and runnable examples
- Tests must pass with `pytest` from the repository root
- Aim for meaningful coverage, not 100% line coverage

### 10. MkDocs Site

- `mkdocs.yml` must define complete navigation matching all actual files
- Site must build without errors using `mkdocs build`
- Use the `material` theme (or `readthedocs` as fallback)

### 11. GitHub Actions

Two workflows in `.github/workflows/`:

- `ci.yml` — runs `pytest` on push and pull request
- `docs.yml` — builds MkDocs site on push to main

---

## Non-Functional Requirements

- Python 3.10+ throughout
- American English in all content
- No filler content — every line must add value
- Total repository size: 45,000–55,000 lines (hard max 60,000)
- All code examples must be syntactically correct and runnable
- Consistent heading style across all chapters

---

## Out of Scope (v1)

- Django, FastAPI, or framework deep dives
- pandas / numpy tutorials
- async / concurrency deep dive
- PyPI packaging guide
- Machine learning content
- Multi-language translations
- Advanced Python internals
