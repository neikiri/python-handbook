"""
JSON Read/Write - Reading and Writing JSON Files

This example demonstrates:
- Reading JSON files with json.load()
- Writing JSON files with json.dump()
- Converting between JSON and Python objects
- Pretty printing JSON
"""

import json
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

print("=== Reading JSON Files ===")

# Read the sample_settings.json file
json_file = SCRIPT_DIR / "sample_settings.json"

if json_file.exists():
    # Method 1: Using json.load()
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print("Content of sample_settings.json:")
    print(json.dumps(data, indent=2))  # Pretty print
    print()
    
    # Access data
    print(f"App name: {data.get('app_name')}")
    print(f"Version: {data.get('version')}")
    print(f"Debug mode: {data.get('debug')}")
    print(f"Database host: {data.get('database', {}).get('host')}")
    print()

print("=== Reading JSON from String ===")

# JSON as a string
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Parse JSON string
data = json.loads(json_string)
print(f"Parsed from string: {data}")
print(f"Name: {data['name']}")
print()

print("=== Writing JSON Files ===")

# Create data to write
person = {
    "name": "Bob",
    "age": 25,
    "city": "Boston",
    "hobbies": ["reading", "coding", "music"],
    "is_active": True,
    "scores": [85, 92, 78],
}

output_file = SCRIPT_DIR / "output.json"

# Write JSON with pretty formatting
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2)

print(f"Written to {output_file}")
print()

# Read it back to verify
with open(output_file, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"Loaded back: {loaded}")
print()

print("=== Pretty Printing JSON ===")

# Use indent for pretty printing
data = {"name": "Alice", "age": 30, "city": "New York"}

# Compact (no spaces)
compact = json.dumps(data)
print(f"Compact: {compact}")

# Pretty printed
pretty = json.dumps(data, indent=2)
print(f"Pretty:\n{pretty}")

# With custom separators
custom = json.dumps(data, separators=(", ", ": "))
print(f"Custom separators:\n{custom}")
print()

print("=== Sorting Keys ===")

# Sort keys alphabetically
data = {"z": 3, "a": 1, "m": 2}
sorted_json = json.dumps(data, sort_keys=True)
print(f"Sorted keys: {sorted_json}")
print()

print("=== Handling Different Data Types ===")

# JSON supports: dict, list, str, int, float, bool, None
data = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3],
    "nested": {"key": "value"},
}

json_str = json.dumps(data, indent=2)
print(f"JSON with different types:\n{json_str}")
print()

print("=== Converting JSON to Python Objects ===")

# JSON object -> dict
json_obj = '{"name": "Alice", "age": 30}'
py_obj = json.loads(json_obj)
print(f"JSON object -> Python dict: {py_obj}")

# JSON array -> list
json_arr = '[1, 2, 3, 4, 5]'
py_arr = json.loads(json_arr)
print(f"JSON array -> Python list: {py_arr}")

# JSON string -> Python str
json_str = '"hello"'
py_str = json.loads(json_str)
print(f"JSON string -> Python str: {py_str}")
print()

print("=== Error Handling ===")

# Invalid JSON
invalid_json = '{"name": "Alice", "age": 30,'  # Missing closing brace

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    print(f"  Line: {e.lineno}, Column: {e.colno}")
print()

# Missing key
data = {"name": "Alice"}
try:
    value = data["age"]  # KeyError
except KeyError:
    print("Key 'age' not found")

# Better: use .get()
age = data.get("age", "Unknown")
print(f"Age (using .get()): {age}")
print()

print("=== Practical Example: Configuration File ===")

# Create a config file
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "features": ["auth", "api", "admin"],
}

config_file = SCRIPT_DIR / "config.json"
with open(config_file, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

print(f"Created config file: {config_file}")

# Read and use config
with open(config_file, "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print(f"App: {loaded_config['app_name']} v{loaded_config['version']}")
print(f"Database: {loaded_config['database']['host']}:{loaded_config['database']['port']}")
print(f"Features: {', '.join(loaded_config['features'])}")
