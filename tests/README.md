# Tests

This directory contains the test suite for the Python Handbook.

## Structure

```
tests/
├── conftest.py          # Shared fixtures
├── test_examples.py     # Example smoke tests
└── projects/            # Project-specific tests
```

## Running Tests

```bash
pytest
```

## Test Types

- **Smoke tests** - Verify examples run without errors
- **Unit tests** - Test project logic functions
- **Integration tests** - Test project workflows

## Writing Tests

- Use pytest conventions
- Test edge cases
- Use descriptive test names
- Keep tests independent

## CI/CD

Tests run automatically on GitHub Actions for every push and pull request.