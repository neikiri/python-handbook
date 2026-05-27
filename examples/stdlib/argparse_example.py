"""
Argparse Example - Parsing Command-Line Arguments

This example demonstrates:
- Creating argument parsers
- Adding positional and optional arguments
- Argument types and validation
- Help messages
- Subcommands
"""

import argparse
import sys

print("=== Basic Argument Parser ===")

# Create parser
parser = argparse.ArgumentParser(description="A simple example script.")

# Add positional argument
parser.add_argument("name", help="Name of the person to greet")

# Add optional argument
parser.add_argument("--age", type=int, default=0, help="Age of the person")

# Parse arguments
args = parser.parse_args(["Alice", "--age", "30"])

print(f"Name: {args.name}")
print(f"Age: {args.age}")
print()

print("=== Positional Arguments ===")

parser = argparse.ArgumentParser(description="Process some integers.")

# Positional argument (required)
parser.add_argument("filename", help="Input file name")

# Multiple positional arguments
parser.add_argument("numbers", nargs="+", type=int, help="Numbers to process")

args = parser.parse_args(["data.txt", "1", "2", "3"])
print(f"Filename: {args.filename}")
print(f"Numbers: {args.numbers}")
print()

print("=== Optional Arguments ===")

parser = argparse.ArgumentParser(description="Configure a service.")

# Simple flag
parser.add_argument("--debug", action="store_true", help="Enable debug mode")

# With short form
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

# With default value
parser.add_argument("--port", type=int, default=8080, help="Port number")

# With choices
parser.add_argument("--level", choices=["low", "medium", "high"], default="medium", help="Log level")

args = parser.parse_args(["--debug", "-v", "--port", "3000", "--level", "high"])
print(f"Debug: {args.debug}")
print(f"Verbose: {args.verbose}")
print(f"Port: {args.port}")
print(f"Level: {args.level}")
print()

print("=== Argument Types ===")

parser = argparse.ArgumentParser(description="Type conversion examples.")

# Integer
parser.add_argument("--count", type=int, help="Number of items")

# Float
parser.add_argument("--price", type=float, help="Price per item")

# Boolean (store_true/store_false)
parser.add_argument("--enabled", action="store_true", help="Enable feature")
parser.add_argument("--disabled", action="store_false", help="Disable feature")

# Custom type
def positive_int(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not an integer")


parser.add_argument("--positive", type=positive_int, help="Positive integer")

args = parser.parse_args(["--count", "5", "--price", "19.99", "--enabled", "--positive", "10"])
print(f"Count: {args.count} (type: {type(args.count).__name__})")
print(f"Price: {args.price} (type: {type(args.price).__name__})")
print(f"Enabled: {args.enabled}")
print(f"Positive: {args.positive}")
print()

print("=== Required Arguments ===")

parser = argparse.ArgumentParser(description="Required arguments example.")

# Required argument
parser.add_argument("--username", required=True, help="Username")

# Required optional argument (with dest)
parser.add_argument("--config", dest="config_file", required=True, help="Config file path")

# Try with missing required argument
try:
    args = parser.parse_args([])
except SystemExit:
    print("Error: --username is required")
    print("Error: --config is required")
print()

print("=== Subcommands ===")

# Main parser
parser = argparse.ArgumentParser(description="Git-like CLI tool.")

# Subparsers
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Create command
create_parser = subparsers.add_parser("create", help="Create a new item")
create_parser.add_argument("name", help="Name of the item")
create_parser.add_argument("--type", default="file", help="Item type")

# Delete command
delete_parser = subparsers.add_parser("delete", help="Delete an item")
delete_parser.add_argument("name", help="Name of the item to delete")
delete_parser.add_argument("--force", action="store_true", help="Force delete")

# Parse arguments
args = parser.parse_args(["create", "myproject", "--type", "directory"])
print(f"Command: {args.command}")
print(f"Name: {args.name}")
print(f"Type: {args.type}")

args = parser.parse_args(["delete", "oldfile", "--force"])
print(f"\nCommand: {args.command}")
print(f"Name: {args.name}")
print(f"Force: {args.force}")
print()

print("=== Custom Help ===")

parser = argparse.ArgumentParser(
    description="A custom help example.",
    epilog="For more information, visit https://example.com"
)

parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

# Custom formatter
class CustomFormatter(argparse.RawDescriptionHelpFormatter):
    pass


parser = argparse.ArgumentParser(
    description="Custom formatter example.",
    formatter_class=CustomFormatter
)

parser.add_argument("--option", help="This is my option")

# Show help
print("Run with --help to see the help message:")
print("  python argparse_example.py --help")
print()

print("=== Practical Example: File Processor ===")

# Create a realistic argument parser
def create_parser():
    """Create argument parser for file processor."""
    parser = argparse.ArgumentParser(
        description="Process files in a directory.",
        epilog="Example: python script.py --input ./data --output ./results --verbose"
    )
    
    # Input directory (required)
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Input directory containing files"
    )
    
    # Output directory (required)
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output directory for results"
    )
    
    # Optional: file pattern
    parser.add_argument(
        "-p", "--pattern",
        default="*.txt",
        help="File pattern to match (default: *.txt)"
    )
    
    # Optional: verbose
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    # Optional: dry run
    parser.add_argument(
        "-n", "--dry-run",
        action="store_true",
        help="Show what would be done without doing it"
    )
    
    return parser


# Parse arguments
args = create_parser().parse_args([
    "-i", "./data",
    "-o", "./results",
    "-v",
    "-n"
])

print(f"Input directory: {args.input}")
print(f"Output directory: {args.output}")
print(f"Pattern: {args.pattern}")
print(f"Verbose: {args.verbose}")
print(f"Dry run: {args.dry_run}")
print()

print("=== Running the Script ===")

print("To run this script with arguments:")
print("  python argparse_example.py --help")
print("  python argparse_example.py Alice --age 30 --debug")
print("  python argparse_example.py create myproject --type directory")
print()

print("Note: This example shows how to set up argparse.")
print("To actually use it, save this code to a file and run it from the command line.")
