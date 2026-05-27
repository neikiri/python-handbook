# Word Counter

A simple text file analyzer that counts lines, words, and characters in a text file, and shows the most common words.

## Concepts practiced

- File I/O
- String manipulation
- Collections (Counter)
- Command-line arguments
- Path handling with pathlib

## Files in this project

- `README.md` - This file
- `main.py` - The main application logic
- `sample.txt` - Sample text file for testing

## How to run

```bash
python main.py <file_path>
```

## Example commands

```bash
# Count words in a file
python main.py sample.txt

# Count words in any text file
python main.py path/to/your/file.txt
```

## Extension ideas

- Add case-insensitive word counting
- Show word frequency as a percentage
- Filter out common "stop words" (the, and, is, etc.)
- Generate a word cloud visualization
- Support multiple files at once
- Add a word length distribution report