"""Word Counter - Analyze text files for word and line counts."""

import argparse
import sys
from collections import Counter
from pathlib import Path


def count_text_stats(file_path):
    """Count lines, words, and characters in a text file.
    
    Args:
        file_path: Path to the text file
        
    Returns:
        Dictionary with line_count, word_count, char_count, and word_freq
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.splitlines()
    words = content.split()
    word_freq = Counter(words)
    
    return {
        "line_count": len(lines),
        "word_count": len(words),
        "char_count": len(content),
        "word_freq": word_freq
    }


def display_results(file_path, stats):
    """Display the analysis results."""
    print(f"\nAnalysis of: {file_path}")
    print("=" * 50)
    print(f"Lines:      {stats['line_count']}")
    print(f"Words:      {stats['word_count']}")
    print(f"Characters: {stats['char_count']}")
    print("=" * 50)
    
    # Show most common words
    print("\nMost Common Words:")
    print("-" * 30)
    for word, count in stats['word_freq'].most_common(10):
        print(f"  {word}: {count}")
    print("-" * 30)


def main():
    """Main function to run the word counter."""
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a text file."
    )
    parser.add_argument(
        "file",
        help="Path to the text file to analyze"
    )
    
    args = parser.parse_args()
    
    try:
        stats = count_text_stats(args.file)
        display_results(args.file, stats)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()