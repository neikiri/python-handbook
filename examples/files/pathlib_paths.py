"""
Pathlib Paths - Working with File Paths using pathlib

This example demonstrates:
- Creating Path objects
- Path operations (join, parent, name, etc.)
- Checking if paths exist
- Creating directories
- Iterating over directory contents
"""

from pathlib import Path

print("=== Creating Path Objects ===")

# Create a Path object
current_dir = Path(".")
print(f"Current directory: {current_dir}")

# Path from string
path = Path("some/directory/file.txt")
print(f"Path from string: {path}")

# Path from multiple parts
path2 = Path("some") / "directory" / "file.txt"
print(f"Path from parts: {path2}")

# Get the directory where this script is located
script_dir = Path(__file__).parent
print(f"Script directory: {script_dir}")
print()

print("=== Path Properties ===")

path = Path("/home/user/documents/file.txt")
print(f"Path: {path}")
print(f"  .parent: {path.parent}")
print(f"  .name: {path.name}")
print(f"  .stem: {path.stem}")
print(f"  .suffix: {path.suffix}")
print(f"  .suffixes: {path.suffixes}")
print()

# Example with multiple extensions
path2 = Path("archive.tar.gz")
print(f"Path: {path2}")
print(f"  .stem: {path2.stem}")
print(f"  .suffix: {path2.suffix}")
print(f"  .suffixes: {path2.suffixes}")
print()

print("=== Checking if Path Exists ===")

# Check if path exists
path = Path("nonexistent.txt")
print(f"Path.exists(): {path.exists()}")

# Check if it's a file
print(f"Path.is_file(): {path.is_file()}")

# Check if it's a directory
print(f"Path.is_dir(): {path.is_dir()}")
print()

# Check the script directory
script_dir = Path(__file__).parent
print(f"Script directory exists: {script_dir.exists()}")
print(f"Script directory is_dir: {script_dir.is_dir()}")
print()

print("=== Creating Directories ===")

# Create a single directory
new_dir = Path("new_directory")
new_dir.mkdir(exist_ok=True)  # exist_ok=True won't raise error if exists
print(f"Created directory: {new_dir}")
print(f"Directory exists: {new_dir.exists()}")

# Create nested directories
nested_dir = Path("parent/child/grandchild")
nested_dir.mkdir(parents=True, exist_ok=True)  # parents=True creates parent dirs
print(f"Created nested directories: {nested_dir}")
print()

print("=== Path Operations ===")

# Join paths
base = Path("/home/user")
path = base / "documents" / "file.txt"
print(f"Joined path: {path}")

# Get relative path
full_path = Path("/home/user/documents/file.txt")
relative = full_path.relative_to("/home/user")
print(f"Relative to /home/user: {relative}")

# Resolve absolute path
path = Path("relative/path.txt")
absolute = path.resolve()
print(f"Absolute path: {absolute}")
print()

print("=== Iterating Over Directory Contents ===")

# Get all files in directory
script_dir = Path(__file__).parent
print(f"Files in {script_dir.name}:")
for item in script_dir.iterdir():
    if item.is_file():
        print(f"  {item.name}")

print()

# Get all .txt files
print(f".txt files in {script_dir.name}:")
for txt_file in script_dir.glob("*.txt"):
    print(f"  {txt_file.name}")

print()

# Recursive search with **
print("All .py files in subdirectories:")
for py_file in script_dir.glob("**/*.py"):
    print(f"  {py_file}")

print()

print("=== Working with File Extensions ===")

# Change file extension
path = Path("file.txt")
new_path = path.with_suffix(".md")
print(f"Change .txt to .md: {new_path}")

# Add prefix or suffix
path = Path("file.txt")
prefixed = path.with_name("prefix_" + path.name)
print(f"Add prefix: {prefixed}")
print()

print("=== Common Path Operations ===")

# Get home directory
home = Path.home()
print(f"Home directory: {home}")

# Get current working directory
cwd = Path.cwd()
print(f"Current working directory: {cwd}")

# Check if path is absolute
path1 = Path("/home/user/file.txt")
path2 = Path("relative/path.txt")
print(f"{path1} is absolute: {path1.is_absolute()}")
print(f"{path2} is absolute: {path2.is_absolute()}")
print()

print("=== Path Comparison ===")

path1 = Path("/home/user/file.txt")
path2 = Path("/home/user/file.txt")
path3 = Path("/home/user/other.txt")

print(f"path1 == path2: {path1 == path2}")
print(f"path1 == path3: {path1 == path3}")
print()

print("=== Practical Example: Find Large Files ===")

# Find files larger than 1KB
print(f"Files larger than 1KB in {script_dir.name}:")
for item in script_dir.rglob("*"):
    if item.is_file():
        size = item.stat().st_size
        if size > 1024:  # 1KB
            print(f"  {item.name}: {size} bytes")
