# Contributing to Python Handbook

Thank you for your interest in contributing to the Python Handbook! This document outlines the process for contributing to this open-source learning repository.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors are expected to adhere to our code of conduct:

- Be respectful and inclusive
- Accept constructive feedback gracefully
- Focus on what is best for the community
- Show empathy toward other community members

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check the existing issues to avoid duplicates. When creating a bug report, include:

1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Any error messages or screenshots
6. Your environment (Python version, OS, etc.)

### Suggesting Features

Feature requests are welcome! When submitting a feature request:

1. Use a clear and descriptive title
2. Describe the proposed feature in detail
3. Explain why this feature would be useful
4. Include any relevant examples or use cases

### Contributing Code

1. Fork the repository
2. Create a branch for your changes (`git checkout -b feature/your-feature`)
3. Make your changes following the project's coding standards
4. Run tests to ensure everything passes (`pytest`)
5. Build the documentation locally (`mkdocs serve`)
6. Commit your changes with clear, descriptive messages
7. Push your branch and open a pull request

## Development Setup

1. Clone the repository
2. Install dev dependencies: `pip install -e .[dev]`
3. Run tests: `pytest`
4. Build docs: `mkdocs build`

## Coding Standards

- Use Python 3.10+ syntax
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write clear, descriptive variable and function names
- Include docstrings for functions and classes
- Keep examples simple and runnable
- Use American English in all content

## Documentation Standards

- Use Markdown for all documentation
- Follow the 7-section structure for handbook chapters:
  1. Overview
  2. What you will learn
  3. Core concepts
  4. Practical examples
  5. Common mistakes
  6. Practice tasks
  7. Key takeaways
- Use consistent heading styles
- Keep examples practical and beginner-friendly

## Pull Request Guidelines

- Target your pull request against the `main` branch
- Include a clear description of your changes
- Reference any related issues
- Ensure all tests pass
- Ensure MkDocs builds without errors
- Keep changes focused and well-scoped

## Questions?

If you have questions about contributing, feel free to:

- Open an issue for discussion
- Join our community discussions
- Contact the maintainers

Thank you for helping make the Python Handbook better for everyone!