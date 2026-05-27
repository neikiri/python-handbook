# Todo CLI

A simple command-line todo list manager that allows you to add, list, complete, and delete tasks. Tasks are stored in a JSON file.

## Concepts practiced

- File I/O with JSON
- Command-line argument parsing
- Data structures (lists, dictionaries)
- Basic CLI interface
- Error handling

## Files in this project

- `README.md` - This file
- `main.py` - The main application logic
- `todos.json` - Data file (created automatically)

## How to run

```bash
python main.py
```

## Example commands

```bash
# Add a new task
python main.py add "Buy groceries"

# List all tasks
python main.py list

# Mark a task as complete
python main.py complete 1

# Delete a task
python main.py delete 2
```

## Extension ideas

- Add priority levels (low, medium, high)
- Add due dates to tasks
- Allow editing existing tasks
- Add task categories or tags
- Save data to a different location
- Add a completion percentage indicator