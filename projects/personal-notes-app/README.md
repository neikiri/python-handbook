# Personal Notes App

A simple command-line notes application that allows you to add, list, search, and delete notes. Notes are stored in a JSON file.

## Concepts practiced

- File I/O with JSON
- Data structures (lists, dictionaries)
- String search and filtering
- Command-line interface
- Basic CRUD operations

## Files in this project

- `README.md` - This file
- `main.py` - The main application logic
- `notes.json` - Data file (created automatically)

## How to run

```bash
python main.py
```

## Example commands

```bash
# Add a new note
python main.py add "Remember to buy milk"

# List all notes
python main.py list

# Search notes
python main.py search "grocery"

# Delete a note
python main.py delete 1
```

## Extension ideas

- Add note categories or tags
- Add timestamps to notes
- Allow editing existing notes
- Export notes to a file
- Add note backup functionality
- Include a note priority system
- Add a simple text editor for note content