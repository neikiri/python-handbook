"""CSV Sales Report - Generate summary reports from sales data."""

import argparse
import csv
import sys
from pathlib import Path


def read_sales_data(file_path):
    """Read sales data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of dictionaries containing sales records
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    sales = []
    with open(path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sales.append({
                "product": row["product"],
                "amount": float(row["amount"]),
                "quantity": int(row["quantity"])
            })
    
    return sales


def calculate_totals(sales):
    """Calculate total sales amount."""
    return sum(item["amount"] * item["quantity"] for item in sales)


def calculate_by_product(sales):
    """Calculate sales totals by product.
    
    Returns:
        Dictionary mapping product names to total sales
    """
    totals = {}
    for item in sales:
        product = item["product"]
        total = item["amount"] * item["quantity"]
        totals[product] = totals.get(product, 0) + total
    return totals


def calculate_average(sales):
    """Calculate average sale amount."""
    if not sales:
        return 0
    total = sum(item["amount"] * item["quantity"] for item in sales)
    return total / len(sales)


def display_report(sales):
    """Display the sales report."""
    print("\n" + "=" * 60)
    print("                    SALES REPORT")
    print("=" * 60)
    
    # Overall totals
    total_sales = calculate_totals(sales)
    avg_sale = calculate_average(sales)
    
    print(f"\nTotal Sales:      ${total_sales:,.2f}")
    print(f"Number of Items:  {len(sales)}")
    print(f"Avg Sale Amount:  ${avg_sale:,.2f}")
    
    # Sales by product
    print("\n" + "-" * 60)
    print("SALES BY PRODUCT")
    print("-" * 60)
    
    by_product = calculate_by_product(sales)
    for product, total in sorted(by_product.items(), key=lambda x: x[1], reverse=True):
        print(f"  {product:20} ${total:,.2f}")
    
    print("-" * 60)
    print("=" * 60)


def main():
    """Main function to run the sales report."""
    parser = argparse.ArgumentParser(
        description="Generate a sales report from CSV data."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default=Path(__file__).parent / "sales.csv",
        help="Path to the sales CSV file (default: sales.csv)"
    )
    
    args = parser.parse_args()
    
    try:
        sales = read_sales_data(args.file)
        display_report(sales)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error processing CSV: {e}")
        print("Make sure the CSV has columns: product, amount, quantity")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()