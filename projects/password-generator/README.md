# Password Generator

A simple command-line tool that generates secure random passwords with customizable options for length and character types.

## Concepts practiced

- Random number generation
- String manipulation
- Command-line arguments
- Input validation
- Security best practices

## Files in this project

- `README.md` - This file
- `main.py` - The main application logic

## How to run

```bash
python main.py
```

## Example commands

```bash
# Generate a default password (12 characters)
python main.py

# Generate a 16 character password
python main.py --length 16

# Generate a password without symbols
python main.py --no-symbols

# Generate a short password
python main.py --length 8 --no-symbols
```

## Extension ideas

- Add options to include/exclude numbers and uppercase letters
- Generate multiple passwords at once
- Add a password strength indicator
- Save generated passwords to a file
- Add a "memorable" mode that creates pronounceable passwords
- Include a clipboard copy feature