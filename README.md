# Python Handbook

[![CI](https://github.com/neikiri/python-handbook/actions/workflows/ci.yml/badge.svg)](https://github.com/neikiri/python-handbook/actions/workflows/ci.yml)
[![Documentation](https://github.com/neikiri/python-handbook/actions/workflows/docs.yml/badge.svg)](https://github.com/neikiri/python-handbook/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A polished, beginner-friendly Python handbook that teaches Python from zero to practical independent programming. Learn Python through structured chapters, hands-on exercises, and real-world mini projects.

## What Is This?

This is a comprehensive, open-source learning resource for Python. It's not just a single document—it's a complete structured curriculum with:

- **23 handbook chapters** covering Python fundamentals through practical intermediate topics
- **23 exercise sets** with practical coding challenges
- **23 solution sets** with detailed explanations and reasoning
- **Runnable examples** demonstrating key concepts
- **8 mini projects** to build real skills
- **6 cheatsheets** for quick reference
- **4 reference pages** on built-ins and standard library
- **pytest test suite** to verify code quality
- **MkDocs documentation site** for easy navigation

All examples and projects use the Python standard library—no heavy dependencies required.

## Who This Is For

- **Complete beginners** with no programming experience
- **Self-taught learners** looking for structured guidance
- **Students** wanting a supplementary learning resource
- **Developers from other languages** transitioning to Python
- **Educators** seeking open-source curriculum materials

## Quick Start for Learners

### 1. Start Here

Begin with the [Learning Path](docs/learning-path.md) to understand the recommended reading order and how chapters connect.

### 2. Read and Learn

Work through the [Handbook](docs/handbook/) chapters in sequence. Each chapter includes:
- Clear explanations of core concepts
- Practical, runnable examples
- Common mistakes to avoid
- Key takeaways

### 3. Practice

After each chapter, try the [Exercises](docs/exercises/). If you get stuck, check the [Solutions](docs/solutions/) for detailed explanations and code.

### 4. Build Projects

Reinforce your learning by building the [Mini Projects](docs/projects/). Start with simpler projects and progress to more complex ones.

### 5. Reference

Use the [Cheatsheets](docs/cheatsheets/) and [References](docs/references/) as quick lookup guides while coding.

## Local Setup

### Prerequisites

- Python 3.10 or higher
- pip (comes with Python)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/neikiri/python-handbook.git
   cd python-handbook
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows (cmd):**
     ```bash
     venv\Scripts\activate
     ```
   - **Windows (PowerShell):**
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install development dependencies:
   ```bash
   python -m pip install -e ".[dev]"
   ```

### Common Commands

**Serve documentation locally:**
```bash
python -m mkdocs serve
```
Then open http://localhost:8000 in your browser.

**Build documentation:**
```bash
python -m mkdocs build --strict
```

**Run tests:**
```bash
python -m pytest
```

**Compile Python files (check for syntax errors):**
```bash
python -m compileall examples projects tests
```

## Repository Structure

```
python-handbook/
├── docs/
│   ├── handbook/              # 23 main chapters
│   ├── exercises/             # 23 exercise sets
│   ├── solutions/             # 23 solution sets
│   ├── projects/              # Mini project descriptions
│   ├── cheatsheets/           # 6 quick reference guides
│   ├── references/            # 4 reference pages
│   ├── index.md               # Documentation home
│   ├── learning-path.md       # Recommended reading order
│   └── faq.md                 # Frequently asked questions
├── examples/                  # Runnable Python examples
├── projects/                  # 8 mini project implementations
├── tests/                     # pytest test suite
├── .github/
│   ├── workflows/             # CI/CD pipelines
│   └── ISSUE_TEMPLATE/        # Issue templates
├── .kiro/                     # Kiro specs, steering, and local agent hooks
├── pyproject.toml             # Project metadata and dependencies
├── mkdocs.yml                 # MkDocs configuration
├── README.md                  # This file
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Contribution guidelines
├── CODE_OF_CONDUCT.md         # Community standards
├── SECURITY.md                # Security policy
├── CHANGELOG.md               # Version history
└── .gitignore                 # Git ignore rules
```

## Mini Projects

Build these projects to apply what you've learned:

| Project | Topics | Difficulty |
|---------|--------|------------|
| [Number Guessing Game](projects/number-guessing-game/) | Variables, loops, conditionals | Beginner |
| [Password Generator](projects/password-generator/) | Strings, random module, functions | Beginner |
| [Word Counter](projects/word-counter/) | File I/O, strings, dictionaries | Beginner |
| [To-Do CLI](projects/todo-cli/) | Lists, file I/O, user input | Intermediate |
| [Personal Notes App](projects/personal-notes-app/) | JSON, file I/O, functions | Intermediate |
| [CSV Sales Report](projects/csv-sales-report/) | CSV module, data processing | Intermediate |
| [Log Analyzer](projects/log-analyzer/) | File I/O, regex, data analysis | Intermediate |
| [Budget Tracker](projects/budget-tracker/) | JSON, data structures, functions | Intermediate |

## Contents at a Glance

- **[Handbook](docs/handbook/)** — Complete Python curriculum from basics to practical intermediate topics
- **[Learning Path](docs/learning-path.md)** — Structured progression through chapters
- **[Exercises](docs/exercises/)** — Practice problems for each chapter
- **[Solutions](docs/solutions/)** — Detailed solutions with explanations
- **[Projects](docs/projects/)** — Mini project descriptions and requirements
- **[Cheatsheets](docs/cheatsheets/)** — Quick reference for syntax and standard library
- **[References](docs/references/)** — In-depth documentation on built-ins and modules
- **[FAQ](docs/faq.md)** — Answers to common questions

## Tech Stack

- **Python 3.10+** — All code examples and projects
- **MkDocs Material** — Documentation site generation
- **pytest** — Testing framework
- **Python standard library** — used for all examples and mini projects

## Contributing

We welcome contributions! Whether you're fixing typos, improving explanations, adding examples, or creating new content, your help makes this resource better for everyone.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report issues
- How to submit pull requests
- Code style guidelines
- Content standards

## Community

- **Code of Conduct** — See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Security Policy** — See [SECURITY.md](SECURITY.md)
- **Changelog** — See [CHANGELOG.md](CHANGELOG.md)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Built for self-taught learners, students, and anyone starting their Python journey. This is a community-driven project created to make Python education accessible and practical.

---

**Happy coding!** 🐍