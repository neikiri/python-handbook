# Tasks: python-handbook

## Phase 1 — Repository Skeleton

- [x] 1. Create root config files
  - `README.md` — project overview, badges, quick start, table of contents
  - `LICENSE` — MIT license
  - `CONTRIBUTING.md` — how to contribute
  - `CHANGELOG.md` — initial entry
  - `.gitignore` — Python standard gitignore
  - `pyproject.toml` — project metadata and dev dependencies (mkdocs-material, pytest)

- [x] 2. Create `mkdocs.yml`
  - Configure site name, theme (material), and full navigation matching all planned files
  - Add repo URL and edit URI

- [x] 3. Create `docs/` landing pages
  - `docs/index.md` — site home page
  - `docs/learning-path.md` — recommended reading order with time estimates
  - `docs/faq.md` — common beginner questions
  - `docs/projects/index.md` — overview of mini projects

- [x] 4. Create `.github/` scaffolding
  - `.github/ISSUE_TEMPLATE/bug_report.md`
  - `.github/ISSUE_TEMPLATE/feature_request.md`
  - `.github/workflows/ci.yml` — pytest on push and PR
  - `.github/workflows/docs.yml` — mkdocs build on push to main

- [x] 5. Create `tests/conftest.py`
  - Shared fixtures: temp directory, sample CSV, sample log file

---

## Phase 2 — Handbook Chapters (Beginner, chapters 01–10)

- [x] 6. `docs/handbook/01-introduction.md`
- [x] 7. `docs/handbook/02-installation-and-setup.md`
- [x] 8. `docs/handbook/03-running-python.md`
- [x] 9. `docs/handbook/04-syntax-and-structure.md`
- [x] 10. `docs/handbook/05-values-variables-types.md`
- [x] 11. `docs/handbook/06-operators-expressions-input.md`
- [x] 12. `docs/handbook/07-strings.md`
- [x] 13. `docs/handbook/08-control-flow.md`
- [x] 14. `docs/handbook/09-collections.md`
- [x] 15. `docs/handbook/10-functions.md`

Each chapter must follow the 7-section structure: Overview, What you will learn, Core concepts, Practical examples, Common mistakes, Practice tasks, Key takeaways.

---

## Phase 3 — Handbook Chapters (Intermediate, chapters 11–23)

- [x] 16. `docs/handbook/11-comprehensions-generators.md`
- [x] 17. `docs/handbook/12-errors-exceptions-debugging.md`
- [x] 18. `docs/handbook/13-files-paths-json-csv.md`
- [x] 19. `docs/handbook/14-modules-packages-imports.md`
- [x] 20. `docs/handbook/15-virtual-environments-pip.md`
- [x] 21. `docs/handbook/16-oop.md`
- [x] 22. `docs/handbook/17-standard-library.md`
- [x] 23. `docs/handbook/18-testing-code-quality.md`
- [x] 24. `docs/handbook/19-type-hints.md`
- [x] 25. `docs/handbook/20-cli-programs.md`
- [x] 26. `docs/handbook/21-working-with-data.md`
- [x] 27. `docs/handbook/22-practical-projects.md`
- [x] 28. `docs/handbook/23-where-to-go-next.md`

---

## Phase 4 — Exercises and Solutions

- [x] 29. Create exercise files for chapters 01–10 in `docs/exercises/`
  - Problem statements and hints only — no solutions
- [x] 30. Create exercise files for chapters 11–23 in `docs/exercises/`
- [~] 31. Create solution files for chapters 01–10 in `docs/solutions/`
  - Include reasoning and explanation alongside code
- [~] 32. Create solution files for chapters 11–23 in `docs/solutions/`

---

## Phase 5 — Examples

- [~] 33. Create `examples/basics/` — variables, types, operators, input
- [~] 34. Create `examples/strings/` — formatting, methods, slicing
- [~] 35. Create `examples/collections/` — list, dict, set, tuple patterns
- [~] 36. Create `examples/functions/` — args, kwargs, closures, decorators
- [~] 37. Create `examples/oop/` — classes, inheritance, dataclasses
- [~] 38. Create `examples/files/` — pathlib, JSON, CSV read/write
- [~] 39. Create `examples/stdlib/` — datetime, random, re, collections, itertools

All example files must run without errors with `python filename.py`.

---

## Phase 6 — Mini Projects

- [~] 40. `projects/number-guessing-game/` — `main.py` + `README.md`
- [~] 41. `projects/todo-cli/` — `main.py` + `README.md`
- [~] 42. `projects/word-counter/` — `main.py` + `README.md`
- [~] 43. `projects/csv-sales-report/` — `main.py` + `README.md` + sample CSV
- [~] 44. `projects/password-generator/` — `main.py` + `README.md`
- [~] 45. `projects/budget-tracker/` — `main.py` + `README.md`
- [~] 46. `projects/log-analyzer/` — `main.py` + `README.md` + sample log
- [~] 47. `projects/personal-notes-app/` — `main.py` + `README.md`

Each project: standard library only, clean CLI interface, no over-engineering.

---

## Phase 7 — Cheatsheets and References

- [~] 48. `docs/cheatsheets/syntax.md`
- [~] 49. `docs/cheatsheets/builtins.md`
- [~] 50. `docs/cheatsheets/strings.md`
- [~] 51. `docs/cheatsheets/collections.md`
- [~] 52. `docs/cheatsheets/file-io.md`
- [~] 53. `docs/cheatsheets/stdlib.md`
- [~] 54. `docs/references/builtin-types.md`
- [~] 55. `docs/references/builtin-exceptions.md`
- [~] 56. `docs/references/stdlib-modules.md`
- [~] 57. `docs/references/glossary.md`

---

## Phase 8 — Tests

- [~] 58. `tests/test_examples.py` — smoke tests: import and run each example module
- [~] 59. `tests/projects/test_number_guessing_game.py`
- [~] 60. `tests/projects/test_todo_cli.py`
- [~] 61. `tests/projects/test_word_counter.py`
- [~] 62. `tests/projects/test_csv_sales_report.py`
- [~] 63. `tests/projects/test_password_generator.py`
- [~] 64. `tests/projects/test_budget_tracker.py`
- [~] 65. `tests/projects/test_log_analyzer.py`
- [~] 66. `tests/projects/test_personal_notes_app.py`

All tests must pass with `pytest` from the repository root.

---

## Phase 9 — Final Review

- [~] 67. Verify all MkDocs navigation entries match actual files
- [~] 68. Run `mkdocs build --strict` and fix any errors
- [~] 69. Run `pytest` and fix any failures
- [~] 70. Check total line count is within 45,000–55,000
- [~] 71. Review all chapters for consistent heading structure
- [~] 72. Verify no chapter duplicates content from another
- [~] 73. Confirm all code uses Python 3.10+ syntax
- [~] 74. Confirm type hints are present in chapters 16–23
- [~] 75. Final README review — badges, links, quick start accuracy
