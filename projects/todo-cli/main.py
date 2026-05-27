"""Todo CLI - A simple command-line todo list manager."""

import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "todos.json"


def load_todos():
    """Load todos from the JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_todos(todos):
    """Save todos to the JSON file."""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, indent=2)
    except IOError as e:
        print(f"Error saving todos: {e}")


def add_todo(description):
    """Add a new todo item."""
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "description": description,
        "completed": False
    }
    todos.append(todo)
    save_todos(todos)
    print(f"Added task: '{description}' (ID: {todo['id']})")


def list_todos():
    """List all todo items."""
    todos = load_todos()
    
    if not todos:
        print("No tasks found.")
        return
    
    print("\nYour Tasks:")
    print("-" * 50)
    
    for todo in todos:
        status = "[x]" if todo["completed"] else "[ ]"
        print(f"{status} ID {todo['id']}: {todo['description']}")
    
    print("-" * 50)
    completed = sum(1 for t in todos if t["completed"])
    total = len(todos)
    print(f"Completed: {completed}/{total}")


def complete_todo(todo_id):
    """Mark a todo item as completed."""
    todos = load_todos()
    
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            save_todos(todos)
            print(f"Marked task {todo_id} as complete.")
            return
    
    print(f"Error: Task with ID {todo_id} not found.")


def delete_todo(todo_id):
    """Delete a todo item."""
    todos = load_todos()
    
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            removed = todos.pop(i)
            # Renumber remaining todos
            for j, t in enumerate(todos, 1):
                t["id"] = j
            save_todos(todos)
            print(f"Deleted task: '{removed['description']}'")
            return
    
    print(f"Error: Task with ID {todo_id} not found.")


def main():
    """Main function to run the todo CLI."""
    parser = argparse.ArgumentParser(
        description="A simple command-line todo list manager."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")
    
    # List command
    subparsers.add_parser("list", help="List all tasks")
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID to complete")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_todo(args.description)
    elif args.command == "list":
        list_todos()
    elif args.command == "complete":
        complete_todo(args.id)
    elif args.command == "delete":
        delete_todo(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()