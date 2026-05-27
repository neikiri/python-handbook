"""Log Analyzer - Analyze log files for patterns and errors."""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def parse_log_file(file_path):
    """Parse a log file and extract information.
    
    Args:
        file_path: Path to the log file
        
    Returns:
        Dictionary with log statistics and error lines
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    level_counts = Counter()
    error_lines = []
    total_lines = 0
    
    # Pattern to match log level
    level_pattern = re.compile(r'\b(' + '|'.join(LOG_LEVELS) + r')\b', re.IGNORECASE)
    
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            line = line.strip()
            
            # Find log level
            match = level_pattern.search(line)
            if match:
                level = match.group(0).upper()
                level_counts[level] += 1
            
            # Track error and critical lines
            if 'ERROR' in level_counts or match and match.group(0).upper() in ('ERROR', 'CRITICAL'):
                if match and match.group(0).upper() in ('ERROR', 'CRITICAL'):
                    error_lines.append(line)
    
    return {
        "total_lines": total_lines,
        "level_counts": level_counts,
        "error_lines": error_lines
    }


def display_analysis(file_path, stats):
    """Display the log analysis results."""
    print(f"\nLog Analysis: {file_path}")
    print("=" * 60)
    
    # Overall stats
    print(f"\nTotal Lines: {stats['total_lines']}")
    
    # Level counts
    print("\nLog Level Distribution:")
    print("-" * 40)
    for level in LOG_LEVELS:
        count = stats['level_counts'].get(level, 0)
        if count > 0:
            print(f"  {level:10} {count}")
    
    # Error details
    error_count = stats['level_counts'].get('ERROR', 0)
    critical_count = stats['level_counts'].get('CRITICAL', 0)
    
    if error_count > 0 or critical_count > 0:
        print("\n" + "-" * 40)
        print(f"ERRORS AND CRITICAL MESSAGES ({error_count + critical_count} total)")
        print("-" * 40)
        
        for i, line in enumerate(stats['error_lines'][:20], 1):
            print(f"{i:3}. {line}")
        
        if len(stats['error_lines']) > 20:
            print(f"\n... and {len(stats['error_lines']) - 20} more errors.")
    else:
        print("\n" + "-" * 40)
        print("No errors or critical messages found.")
    
    print("-" * 40)
    print("=" * 60)


def main():
    """Main function to run the log analyzer."""
    parser = argparse.ArgumentParser(
        description="Analyze a log file for errors and patterns."
    )
    parser.add_argument(
        "logfile",
        help="Path to the log file to analyze"
    )
    
    args = parser.parse_args()
    
    try:
        stats = parse_log_file(args.logfile)
        display_analysis(args.logfile, stats)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing log file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()