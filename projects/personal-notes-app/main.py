"""Personal Notes App - A simple command-line notes manager."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


DATA_FILE = Path(__file__).parent / "notes.json"


def load_notes():
    """Load notes from the JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_notes(notes):
    """Save notes to the JSON file."""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(notes, f, indent=2)
    except IOError as e:
        print(f"Error saving notes: {e}")


def add_note(content):
    """Add a new note."""
    notes = load_notes()
    
    note = {
        "id": len(notes) + 1,
        "content": content,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    notes.append(note)
    save_notes(notes)
    print(f"Added note (ID: {note['id']})")


def list_notes():
    """List all notes."""
    notes = load_notes()
    
    if not notes:
        print("No notes found.")
        return
    
    print("\n" + "=" * 60)
    print("                        YOUR NOTES")
    print("=" * 60)
    
    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Created: {note['created']}")
        print("-" * 40)
        print(note['content'])
        print("-" * 40)
    
    print("\n" + "=" * 60)


def search_notes(query):
    """Search notes by content."""
    notes = load_notes()
    
    query_lower = query.lower()
    matches = [n for n in notes if query_lower in n['content'].lower()]
    
    if not matches:
        print(f"No notes found matching '{query}'.")
        return
    
    print(f"\nFound {len(matches)} note(s) matching '{query}':")
    print("=" * 60)
    
    for note in matches:
        print(f"\nID: {note['id']}")
        print(f"Created: {note['created']}")
        print("-" * 40)
        print(note['content'])
        print("-" * 40)
    
    print("=" * 60)


def delete_note(note_id):
    """Delete a note by ID."""
    notes = load_notes()
    
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            removed = notes.pop(i)
            # Renumber remaining notes
            for j, n in enumerate(notes, 1):
                n["id"] = j
            save_notes(notes)
            print(f"Deleted note: '{removed['content'][:30]}...'")
            return
    
    print(f"Error: Note with ID {note_id} not found.")


def main():
    """Main function to run the notes app."""
    parser = argparse.ArgumentParser(
        description="A simple command-line notes manager."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("content", help="Note content")
    
    # List command
    subparsers.add_parser("list", help="List all notes")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search notes")
    search_parser.add_argument("query", help="Search query")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a note")
    delete_parser.add_argument("id", type=int, help="Note ID to delete")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_note(args.content)
    elif args.command == "list":
        list_notes()
    elif args.command == "search":
        search_notes(args.query)
    elif args.command == "delete":
        delete_note(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()