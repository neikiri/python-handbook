"""Budget Tracker - Track income and expenses."""

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path


DATA_FILE = Path(__file__).parent / "transactions.csv"


CATEGORIES = {
    "income": ["salary", "freelance", "investment", "gift", "other"],
    "expense": ["food", "transport", "housing", "utilities", "entertainment", "health", "shopping", "other"]
}


def load_transactions():
    """Load transactions from the CSV file."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except (IOError, csv.Error):
        return []


def save_transactions(transactions):
    """Save transactions to the CSV file."""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ["date", "type", "description", "amount", "category"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except IOError as e:
        print(f"Error saving transactions: {e}")


def add_transaction(trans_type, description, amount, category="other"):
    """Add a new transaction."""
    transactions = load_transactions()
    
    # Validate category
    if category.lower() not in CATEGORIES.get(trans_type, []):
        print(f"Warning: Unknown category '{category}'. Using 'other'.")
        category = "other"
    
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": trans_type,
        "description": description,
        "amount": float(amount),
        "category": category.lower()
    }
    
    transactions.append(transaction)
    save_transactions(transactions)
    print(f"Added {trans_type}: {description} - ${amount:.2f} ({category})")


def list_transactions():
    """List all transactions."""
    transactions = load_transactions()
    
    if not transactions:
        print("No transactions found.")
        return
    
    print("\n" + "=" * 70)
    print("                        TRANSACTIONS")
    print("=" * 70)
    
    for i, t in enumerate(transactions, 1):
        print(f"{i}. [{t['type'].upper():8}] {t['date']}")
        print(f"   {t['description']}")
        print(f"   ${float(t['amount']):.2f} | Category: {t['category']}")
        print()
    
    print("=" * 70)


def show_summary():
    """Show balance summary."""
    transactions = load_transactions()
    
    if not transactions:
        print("No transactions found.")
        return
    
    income = sum(float(t["amount"]) for t in transactions if t["type"] == "income")
    expense = sum(float(t["amount"]) for t in transactions if t["type"] == "expense")
    balance = income - expense
    
    print("\n" + "=" * 50)
    print("                      BUDGET SUMMARY")
    print("=" * 50)
    print(f"\nTotal Income:    ${income:,.2f}")
    print(f"Total Expenses:  ${expense:,.2f}")
    print(f"Balance:         ${balance:,.2f}")
    
    # Summary by category
    print("\n" + "-" * 50)
    print("EXPENSES BY CATEGORY")
    print("-" * 50)
    
    expenses_by_category = {}
    for t in transactions:
        if t["type"] == "expense":
            cat = t["category"]
            expenses_by_category[cat] = expenses_by_category.get(cat, 0) + float(t["amount"])
    
    for cat, total in sorted(expenses_by_category.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:15} ${total:,.2f}")
    
    print("-" * 50)
    print("=" * 50 + "\n")


def main():
    """Main function to run the budget tracker."""
    parser = argparse.ArgumentParser(
        description="Track your income and expenses."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add income command
    income_parser = subparsers.add_parser("add-income", help="Add income transaction")
    income_parser.add_argument("description", help="Description of income")
    income_parser.add_argument("amount", type=float, help="Amount")
    income_parser.add_argument("--category", default="other", help="Category (default: other)")
    
    # Add expense command
    expense_parser = subparsers.add_parser("add-expense", help="Add expense transaction")
    expense_parser.add_argument("description", help="Description of expense")
    expense_parser.add_argument("amount", type=float, help="Amount")
    expense_parser.add_argument("--category", default="other", help="Category (default: other)")
    
    # List command
    subparsers.add_parser("list", help="List all transactions")
    
    # Summary command
    subparsers.add_parser("summary", help="Show budget summary")
    
    args = parser.parse_args()
    
    if args.command == "add-income":
        add_transaction("income", args.description, args.amount, args.category)
    elif args.command == "add-expense":
        add_transaction("expense", args.description, args.amount, args.category)
    elif args.command == "list":
        list_transactions()
    elif args.command == "summary":
        show_summary()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()