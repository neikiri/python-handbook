# Budget Tracker

A simple command-line budget tracker that allows you to record income and expenses, view your balance, and analyze spending by category.

## Concepts practiced

- File I/O with CSV
- Data aggregation
- Command-line interface
- Dictionary operations
- Basic financial tracking

## Files in this project

- `README.md` - This file
- `main.py` - The main application logic
- `transactions.csv` - Data file (created automatically)

## How to run

```bash
python main.py
```

## Example commands

```bash
# Add an income transaction
python main.py add-income "Salary" 5000

# Add an expense transaction
python main.py add-expense "Groceries" 150.50

# List all transactions
python main.py list

# Show balance summary
python main.py summary
```

## Extension ideas

- Add transaction categories (food, transport, entertainment, etc.)
- Add date tracking for each transaction
- Generate monthly reports
- Set budget limits for categories
- Add export to different file formats
- Include visual charts for spending breakdown