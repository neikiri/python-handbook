# Design: python-handbook

## Repository Layout

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

## Tooling

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
