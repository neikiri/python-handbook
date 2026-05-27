---
inclusion: always
---
You are working inside a public GitHub repository called python-handbook.

Project goal:
Create a polished, beginner-friendly Python handbook repository that teaches Python from zero to practical independent programming.

Target audience:
- complete beginners
- self-taught learners
- students
- developers coming from another language

Core positioning:
This is not just a single Markdown file. It is a structured open-source learning repository with:
- handbook chapters
- exercises
- solutions
- cheatsheets
- references
- runnable examples
- practical mini projects
- tests
- MkDocs documentation site
- GitHub Actions

Python version:
Use Python 3.10+.

Repository size target:
- Target total size: 45,000 to 55,000 lines.
- Hard maximum: 60,000 lines.
- Do not create filler content just to increase size.
- Prioritize clarity, correctness, and usefulness over volume.

Content style:
- Write clearly and practically.
- Assume the reader may be a complete beginner.
- Do not be childish or overly simplified.
- Explain concepts from first principles.
- Prefer practical examples over abstract theory.
- Avoid repeating the same explanations across files.
- Use consistent terminology.
- Use American English for repository content.
- Keep headings consistent across chapters.

Handbook chapter structure:
Each main handbook chapter should usually include:
1. Overview
2. What you will learn
3. Core concepts
4. Practical examples
5. Common mistakes
6. Practice tasks
7. Key takeaways

Exercise rules:
- Exercises should be practical.
- Exercises should match handbook topics.
- Exercise files should not contain full solutions.
- Solutions should live in docs/solutions/.
- Solutions should explain the reasoning, not just show code.

Code rules:
- All Python code should be Python 3.10+.
- Prefer standard library examples.
- Avoid unnecessary third-party dependencies.
- Prefer pathlib for filesystem paths.
- Prefer f-strings for string formatting.
- Prefer small named functions over clever one-liners.
- Use type hints in intermediate and later examples.
- Keep beginner examples simple.
- All runnable examples and projects should compile.
- Use pytest for tests.
- Do not over-engineer beginner projects.

## Anti-loop rules

- Never repeatedly rewrite the same files in one session.
- For content generation, perform at most one full edit pass per file.
- If validation fails, report the issue and ask before attempting another broad rewrite.
- Do not chase exact line-count targets.
- Treat line budgets as soft guidance, not strict requirements.
- Prefer small targeted fixes over repeated regeneration.
- When asked to edit a set of files, modify only the requested files.
- Stop after completing the requested scope and summarize changes.
- Do not automatically run long validation loops after content-only edits.

Documentation rules:
- Use Markdown.
- Use fenced code blocks with correct language labels: python, bash, text, markdown, yaml, toml.
- Keep MkDocs navigation consistent with actual files.
- Internal links should be relative and valid where possible.
- README.md should be clear, professional, and GitHub-friendly.

Repository structure:
Use this structure unless there is a strong reason to change it:

python-handbook/
  README.md
  LICENSE
  CONTRIBUTING.md
  CHANGELOG.md
  .gitignore
  pyproject.toml
  mkdocs.yml
  docs/
    index.md
    learning-path.md
    faq.md
    handbook/
    exercises/
    solutions/
    projects/
    cheatsheets/
    references/
  examples/
  projects/
  tests/
  .github/
    ISSUE_TEMPLATE/
    workflows/

Model/budget behavior:
- Avoid unnecessary rewrites of large files.
- Prefer targeted edits.
- Before making large changes, explain the plan.
- Do not regenerate the whole repository when only a small fix is needed.
- Keep changes grouped by phase.
- After each major phase, summarize files changed and remaining work.

Do not include in v1:
- Django deep dive
- FastAPI deep dive
- pandas/numpy deep dive
- async/concurrency deep dive
- packaging to PyPI deep dive
- machine learning tutorials
- multi-language translations
- huge advanced Python sections
- unnecessary diagrams or generated assets