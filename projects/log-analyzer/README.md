# Log Analyzer

A simple tool that analyzes log files, counting log levels (INFO, WARNING, ERROR) and displaying error details.

## Concepts practiced

- File I/O
- String parsing
- Collections (Counter)
- Regular expressions
- Command-line arguments

## Files in this project

- `README.md` - This file
- `main.py` - The main application logic
- `sample.log` - Sample log file for testing

## How to run

```bash
python main.py <log_file>
```

## Example commands

```bash
# Analyze a log file
python main.py sample.log

# Analyze any log file
python main.py path/to/your/logfile.log
```

## Extension ideas

- Filter logs by date range
- Show logs from a specific time period
- Export analysis to a report file
- Add log level color coding
- Parse different log formats
- Add search functionality for specific terms