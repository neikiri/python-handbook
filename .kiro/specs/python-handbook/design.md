# Design: python-handbook

## Overview

The `python-handbook` repository is a structured open-source learning resource for Python beginners. It combines a MkDocs documentation site, handbook chapters, exercises, solutions, cheatsheets, references, runnable examples, mini projects, tests, and GitHub Actions.

The design prioritizes:
- clear navigation,
- beginner-friendly content,
- runnable examples,
- maintainable file organization,
- simple standard-library-based projects,
- automated validation through MkDocs and pytest.

## Architecture

### Repository Layout

```
python-handbook/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
├── pyproject.toml
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── learning-path.md
│   ├── faq.md
│   ├── handbook/
│   │   ├── 01-introduction.md
│   │   ├── 02-installation-and-setup.md
│   │   ├── 03-running-python.md
│   │   ├── 04-syntax-and-structure.md
│   │   ├── 05-values-variables-types.md
│   │   ├── 06-operators-expressions-input.md
│   │   ├── 07-strings.md
│   │   ├── 08-control-flow.md
│   │   ├── 09-collections.md
│   │   ├── 10-functions.md
│   │   ├── 11-comprehensions-generators.md
│   │   ├── 12-errors-exceptions-debugging.md
│   │   ├── 13-files-paths-json-csv.md
│   │   ├── 14-modules-packages-imports.md
│   │   ├── 15-virtual-environments-pip.md
│   │   ├── 16-oop.md
│   │   ├── 17-standard-library.md
│   │   ├── 18-testing-code-quality.md
│   │   ├── 19-type-hints.md
│   │   ├── 20-cli-programs.md
│   │   ├── 21-working-with-data.md
│   │   ├── 22-practical-projects.md
│   │   └── 23-where-to-go-next.md
│   ├── exercises/
│   │   ├── 01-introduction.md  (one file per chapter)
│   │   └── ...
│   ├── solutions/
│   │   ├── 01-introduction.md
│   │   └── ...
│   ├── projects/
│   │   └── index.md
│   ├── cheatsheets/
│   │   ├── syntax.md
│   │   ├── builtins.md
│   │   ├── strings.md
│   │   ├── collections.md
│   │   ├── file-io.md
│   │   └── stdlib.md
│   └── references/
│       ├── builtin-types.md
│       ├── builtin-exceptions.md
│       ├── stdlib-modules.md
│       └── glossary.md
├── examples/
│   ├── basics/
│   ├── strings/
│   ├── collections/
│   ├── functions/
│   ├── oop/
│   ├── files/
│   └── stdlib/
├── projects/
│   ├── number-guessing-game/
│   │   ├── README.md
│   │   └── main.py
│   ├── todo-cli/
│   ├── word-counter/
│   ├── csv-sales-report/
│   ├── password-generator/
│   ├── budget-tracker/
│   ├── log-analyzer/
│   └── personal-notes-app/
├── tests/
│   ├── conftest.py
│   ├── test_examples.py
│   └── projects/
│       ├── test_number_guessing_game.py
│       └── ...
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── workflows/
        ├── ci.yml
        └── docs.yml
```

---

## Line Budget

| Section | Target Lines |
|---------|-------------|
| Root config files (README, pyproject, mkdocs, etc.) | ~1,500 |
| Handbook chapters (23 × ~800 avg) | ~18,400 |
| Exercises (23 × ~150 avg) | ~3,450 |
| Solutions (23 × ~200 avg) | ~4,600 |
| Cheatsheets (6 × ~200 avg) | ~1,200 |
| Reference pages (4 × ~400 avg) | ~1,600 |
| docs/ landing pages (index, learning-path, faq, projects) | ~600 |
| Examples (40 files × ~60 avg) | ~2,400 |
| Mini projects (8 × ~200 avg) | ~1,600 |
| Project READMEs (8 × ~80 avg) | ~640 |
| Tests | ~1,500 |
| GitHub Actions + templates | ~300 |
| **Total** | **~37,790 base** |

Remaining headroom (~7,000–17,000 lines) is used for richer chapters, additional examples, and expanded solutions to reach the 45,000–55,000 target.

---

## MkDocs Navigation Plan

```yaml
nav:
  - Home: index.md
  - Learning Path: learning-path.md
  - FAQ: faq.md
  - Handbook:
    - Introduction: handbook/01-introduction.md
    - Installation and Setup: handbook/02-installation-and-setup.md
    - Running Python: handbook/03-running-python.md
    - Syntax and Structure: handbook/04-syntax-and-structure.md
    - Values, Variables, and Types: handbook/05-values-variables-types.md
    - Operators, Expressions, and Input: handbook/06-operators-expressions-input.md
    - Strings: handbook/07-strings.md
    - Control Flow: handbook/08-control-flow.md
    - Collections: handbook/09-collections.md
    - Functions: handbook/10-functions.md
    - Comprehensions and Generators: handbook/11-comprehensions-generators.md
    - Errors and Exceptions: handbook/12-errors-exceptions-debugging.md
    - Files, Paths, JSON, and CSV: handbook/13-files-paths-json-csv.md
    - Modules and Packages: handbook/14-modules-packages-imports.md
    - Virtual Environments: handbook/15-virtual-environments-pip.md
    - Object-Oriented Programming: handbook/16-oop.md
    - Standard Library: handbook/17-standard-library.md
    - Testing and Code Quality: handbook/18-testing-code-quality.md
    - Type Hints: handbook/19-type-hints.md
    - CLI Programs: handbook/20-cli-programs.md
    - Working with Data: handbook/21-working-with-data.md
    - Practical Projects: handbook/22-practical-projects.md
    - Where to Go Next: handbook/23-where-to-go-next.md
  - Exercises:
    - (one entry per chapter)
  - Solutions:
    - (one entry per chapter)
  - Projects: projects/index.md
  - Cheatsheets:
    - Syntax: cheatsheets/syntax.md
    - Built-ins: cheatsheets/builtins.md
    - Strings: cheatsheets/strings.md
    - Collections: cheatsheets/collections.md
    - File I/O: cheatsheets/file-io.md
    - Standard Library: cheatsheets/stdlib.md
  - References:
    - Built-in Types: references/builtin-types.md
    - Built-in Exceptions: references/builtin-exceptions.md
    - Standard Library Modules: references/stdlib-modules.md
    - Glossary: references/glossary.md
```

---

## Components and Interfaces

### Documentation Site

The documentation site is built with MkDocs and the Material theme. The main interface for learners is the generated documentation site, backed by Markdown files in `docs/`.

### Handbook

The handbook consists of 23 ordered Markdown chapters in `docs/handbook/`. Each chapter follows the standard seven-section structure defined in the requirements.

### Exercises and Solutions

Exercises live in `docs/exercises/` and contain problem statements and hints. Matching solutions live in `docs/solutions/` and include reasoning plus code where appropriate.

### Examples

Runnable examples live in `examples/`. They are standalone Python scripts grouped by topic and should run with Python 3.10+.

### Mini Projects

Mini projects live in `projects/`. Each project has a `README.md`, a runnable `main.py`, and optional sample data.

### Tests and CI

Tests live in `tests/` and are run with pytest. GitHub Actions run tests and build the documentation site.

### Tooling

| Tool | Purpose |
|------|---------|
| MkDocs + Material theme | Documentation site |
| pytest | Test runner |
| Python 3.10+ | All code |
| GitHub Actions | CI and docs build |

`pyproject.toml` dev dependencies:
```toml
[project.optional-dependencies]
dev = ["mkdocs-material", "pytest"]
```

---

## GitHub Actions

**ci.yml** — triggers on push and pull_request:
1. Checkout repo
2. Set up Python 3.11
3. Install dev dependencies
4. Run `pytest`

**docs.yml** — triggers on push to `main`:
1. Checkout repo
2. Set up Python 3.11
3. Install `mkdocs-material`
4. Run `mkdocs build --strict`

---

## Data Models

This project does not define application database models. Its primary data models are repository content types and file conventions.

### Content File Model

Each documentation file is a Markdown document with:
- a single top-level title,
- consistent heading hierarchy,
- relative links to related pages,
- fenced code blocks with language labels where applicable.

### Handbook Chapter Model

Each handbook chapter follows this structure:
1. Overview
2. What you will learn
3. Core concepts
4. Practical examples
5. Common mistakes
6. Practice tasks
7. Key takeaways

### Exercise Model

Each exercise file contains:
- problem statements,
- hints,
- expected behavior or sample output,
- no full solutions.

### Solution Model

Each solution file contains:
- matching exercise names,
- reasoning,
- code where applicable,
- common mistakes or review guidance.

### Project Model

Each mini project contains:
- `README.md`,
- `main.py`,
- optional sample input files,
- optional tests.

## Correctness Properties

### Property 1: Documentation Build Correctness

**Validates: Requirements 10.1**

The documentation site is correct when `python -m mkdocs build --strict` completes successfully without broken navigation entries or broken internal links.

Validation:
- Every page referenced by `mkdocs.yml` exists.
- Internal Markdown links use correct relative paths.
- The site builds from the repository root.

### Property 2: Python Syntax Correctness

**Validates: Requirements 7.1**

The Python code is correct at the syntax level when all Python files compile successfully.

Validation:
- Run `python -m compileall examples projects tests`.
- No syntax errors are reported.
- Code uses Python 3.10+ compatible syntax.

### Property 3: Test Suite Correctness

**Validates: Requirements 9.1**

The test suite is correct when pytest runs successfully from the repository root.

Validation:
- Run `python -m pytest`.
- All tests pass.
- Tests should not be removed or weakened only to make the suite pass.

### Property 4: Content Structure Correctness

**Validates: Requirements 2.1**

The handbook content is correct when every handbook chapter follows the required seven-section structure.

Validation:
- Each chapter includes Overview, What you will learn, Core concepts, Practical examples, Common mistakes, Practice tasks, and Key takeaways.
- Each exercise file has a matching solution file.
- Each mini project has a README and runnable entry point.

### Property 5: Repository Scope Correctness

**Validates: Requirements 11.1**

The repository stays within the intended v1 scope.

Validation:
- Content focuses on beginner to practical intermediate Python.
- Advanced framework deep dives, machine learning tutorials, and unrelated topics remain out of scope.
- Line counts are treated as guidance, not as a reason to add filler.

## Error Handling

Errors should be handled through simple validation and targeted fixes:

- Broken MkDocs navigation should be fixed by correcting `mkdocs.yml` or creating the missing Markdown file.
- Broken internal links should be fixed by correcting relative paths.
- Python syntax errors should be caught with `python -m compileall examples projects tests`.
- Test failures should be fixed without deleting useful tests.
- Content inconsistencies should be fixed with targeted edits, not broad rewrites.
- Agent runs should avoid repeated rewrite loops and should stop after the requested scope.

## Quality Checklist

- [ ] All handbook chapters follow the 7-section structure
- [ ] Every exercise file has a matching solution file
- [ ] All Python files run without errors (`python file.py`)
- [ ] All tests pass (`pytest`)
- [ ] MkDocs builds without errors (`mkdocs build --strict`)
- [ ] No broken internal links
- [ ] No chapter duplicates content from another chapter
- [ ] All code uses Python 3.10+ syntax
- [ ] Type hints present in chapters 16–23
- [ ] Total line count is within 45,000–55,000

---

## Testing Strategy

- **Unit tests** for mini project logic (pure functions, data transformations)
- **Smoke tests** for runnable examples (import and call main entry points)
- **No UI or integration tests** — keep it simple
- Tests live in `tests/` and mirror the `projects/` structure
- `conftest.py` provides shared fixtures (temp directories, sample data files)
- CI runs the full test suite on every push
