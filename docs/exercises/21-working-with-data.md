# Chapter 21: Working with Data — Exercises

## Overview

These exercises help you work with real-world data: loading, cleaning, transforming, and analyzing it. By the end, you will confidently handle data processing tasks.

---

## How to Use These Exercises

- Create a folder called `chapter-21` in your `python-learning` directory.
- Write each program in a separate `.py` file.
- Run each program and observe the output.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Load and Explore Data

Create a file called `load_data.py`:

```python
"""Load and explore data."""

import json
import csv
from pathlib import Path

# Create sample data
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Carol", "age": 28, "city": "Chicago"},
]

# Save as JSON
json_file = Path("people.json")
json_file.write_text(json.dumps(data, indent=2))

# Load and explore JSON
loaded = json.loads(json_file.read_text())
print(f"Loaded {len(loaded)} records")
print(f"Keys: {list(loaded[0].keys())}")
print(f"First record: {loaded[0]}")

# Save as CSV
csv_file = Path("people.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

# Load and explore CSV
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    records = list(reader)
    print(f"\nLoaded {len(records)} CSV records")
    for record in records:
        print(f"  {record}")

# Clean up
json_file.unlink()
csv_file.unlink()
```

Run it and observe data loading.

---

### Exercise 2: Clean Data

Create a file called `clean_data.py`:

```python
"""Clean data."""

import json
from pathlib import Path

# Create messy data
messy_data = [
    {"name": "  Alice  ", "age": "30", "city": "New York"},
    {"name": "Bob", "age": "25", "city": "  Los Angeles  "},
    {"name": "CAROL", "age": "28", "city": "Chicago"},
    {"name": "David", "age": "", "city": "Boston"},
]

def clean_record(record):
    """Clean a single record."""
    cleaned = {}
    for key, value in record.items():
        if isinstance(value, str):
            value = value.strip()
            if key == "name":
                value = value.title()
        cleaned[key] = value
    return cleaned

def clean_data(data):
    """Clean a list of records."""
    cleaned = []
    for record in data:
        cleaned_record = clean_record(record)
        # Skip records with missing required fields
        if cleaned_record.get("age"):
            cleaned_record["age"] = int(cleaned_record["age"])
            cleaned.append(cleaned_record)
    return cleaned

# Clean the data
cleaned = clean_data(messy_data)

print("Original data:")
for record in messy_data:
    print(f"  {record}")

print("\nCleaned data:")
for record in cleaned:
    print(f"  {record}")
```

Run it and observe data cleaning.

---

### Exercise 3: Transform Data

Create a file called `transform_data.py`:

```python
"""Transform data."""

# Sample data
people = [
    {"name": "Alice", "age": 30, "salary": 80000},
    {"name": "Bob", "age": 25, "salary": 70000},
    {"name": "Carol", "age": 28, "salary": 75000},
]

# Extract specific fields
names = [p["name"] for p in people]
print(f"Names: {names}")

# Calculate new fields
for person in people:
    person["age_group"] = "30+" if person["age"] >= 30 else "20-29"
    person["salary_level"] = "high" if person["salary"] >= 75000 else "low"

print("\nWith new fields:")
for person in people:
    print(f"  {person}")

# Group by field
by_age_group = {}
for person in people:
    group = person["age_group"]
    if group not in by_age_group:
        by_age_group[group] = []
    by_age_group[group].append(person)

print("\nGrouped by age:")
for group, records in by_age_group.items():
    print(f"  {group}: {[p['name'] for p in records]}")

# Sort data
sorted_by_salary = sorted(people, key=lambda p: p["salary"], reverse=True)
print("\nSorted by salary (highest first):")
for person in sorted_by_salary:
    print(f"  {person['name']}: ${person['salary']}")
```

Run it and observe data transformation.

---

### Exercise 4: Aggregate Data

Create a file called `aggregate_data.py`:

```python
"""Aggregate data."""

# Sample data
sales = [
    {"product": "A", "quantity": 10, "price": 100},
    {"product": "B", "quantity": 5, "price": 200},
    {"product": "A", "quantity": 8, "price": 100},
    {"product": "C", "quantity": 3, "price": 300},
    {"product": "B", "quantity": 2, "price": 200},
]

# Calculate totals
total_quantity = sum(s["quantity"] for s in sales)
total_revenue = sum(s["quantity"] * s["price"] for s in sales)

print(f"Total quantity: {total_quantity}")
print(f"Total revenue: ${total_revenue}")

# Aggregate by product
by_product = {}
for sale in sales:
    product = sale["product"]
    if product not in by_product:
        by_product[product] = {"quantity": 0, "revenue": 0}
    by_product[product]["quantity"] += sale["quantity"]
    by_product[product]["revenue"] += sale["quantity"] * sale["price"]

print("\nBy product:")
for product, stats in by_product.items():
    print(f"  {product}: {stats['quantity']} units, ${stats['revenue']}")

# Find top product
top_product = max(by_product.items(), key=lambda x: x[1]["revenue"])
print(f"\nTop product: {top_product[0]} (${top_product[1]['revenue']})")
```

Run it and observe data aggregation.

---

## Practice Exercises

### Exercise 5: Validate Data

Create a file called `validate_data.py`:

```python
"""Validate data."""

import re

def validate_email(email):
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone format."""
    digits = "".join(c for c in phone if c.isdigit())
    return len(digits) == 10

def validate_record(record):
    """Validate a record."""
    errors = []
    
    if not record.get("name"):
        errors.append("Name is required")
    
    if not record.get("email"):
        errors.append("Email is required")
    elif not validate_email(record["email"]):
        errors.append("Invalid email format")
    
    if record.get("phone") and not validate_phone(record["phone"]):
        errors.append("Invalid phone format")
    
    if record.get("age"):
        try:
            age = int(record["age"])
            if age < 0 or age > 150:
                errors.append("Age must be between 0 and 150")
        except ValueError:
            errors.append("Age must be a number")
    
    return errors

# Test validation
records = [
    {"name": "Alice", "email": "alice@example.com", "age": "30"},
    {"name": "Bob", "email": "invalid-email", "age": "25"},
    {"name": "", "email": "carol@example.com", "age": "28"},
]

for i, record in enumerate(records):
    errors = validate_record(record)
    if errors:
        print(f"Record {i}: INVALID")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"Record {i}: VALID")
```

Run it and observe data validation.

---

### Exercise 6: Merge Data

Create a file called `merge_data.py`:

```python
"""Merge data from multiple sources."""

import json
from pathlib import Path

# Create sample data files
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Carol"},
]

orders = [
    {"id": 1, "user_id": 1, "product": "Laptop", "price": 1000},
    {"id": 2, "user_id": 2, "product": "Phone", "price": 500},
    {"id": 3, "user_id": 1, "product": "Monitor", "price": 300},
]

# Merge data
merged = []
for user in users:
    user_orders = [o for o in orders if o["user_id"] == user["id"]]
    merged.append({
        "user": user,
        "orders": user_orders,
        "total_spent": sum(o["price"] for o in user_orders),
    })

print("Merged data:")
for item in merged:
    print(f"  {item['user']['name']}: {len(item['orders'])} orders, ${item['total_spent']}")

# Join data
joined = []
for order in orders:
    user = next((u for u in users if u["id"] == order["user_id"]), None)
    if user:
        joined.append({
            "user_name": user["name"],
            "product": order["product"],
            "price": order["price"],
        })

print("\nJoined data:")
for item in joined:
    print(f"  {item['user_name']}: {item['product']} (${item['price']})")
```

Run it and observe data merging.

---

### Exercise 7: Export Data

Create a file called `export_data.py`:

```python
"""Export data to different formats."""

import json
import csv
from pathlib import Path

# Sample data
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Carol", "age": 28, "city": "Chicago"},
]

# Export to JSON
json_file = Path("export.json")
json_file.write_text(json.dumps(data, indent=2))
print(f"Exported to {json_file}")

# Export to CSV
csv_file = Path("export.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)
print(f"Exported to {csv_file}")

# Export to plain text
txt_file = Path("export.txt")
with open(txt_file, "w") as f:
    f.write("Name | Age | City\n")
    f.write("-" * 30 + "\n")
    for record in data:
        f.write(f"{record['name']} | {record['age']} | {record['city']}\n")
print(f"Exported to {txt_file}")

# Verify exports
print("\nJSON content:")
print(json_file.read_text())

print("\nCSV content:")
print(csv_file.read_text())

print("\nTXT content:")
print(txt_file.read_text())

# Clean up
json_file.unlink()
csv_file.unlink()
txt_file.unlink()
```

Run it and observe data export.

---

## Challenge Exercises

### Challenge 1: Build a Data Pipeline

Create a file called `data_pipeline.py`:

```python
"""Data processing pipeline."""

import json
from pathlib import Path

class DataPipeline:
    def __init__(self, data):
        self.data = data
    
    def filter(self, predicate):
        """Filter data."""
        self.data = [item for item in self.data if predicate(item)]
        return self
    
    def map(self, transform):
        """Transform data."""
        self.data = [transform(item) for item in self.data]
        return self
    
    def sort(self, key):
        """Sort data."""
        self.data = sorted(self.data, key=key)
        return self
    
    def get(self):
        """Get the result."""
        return self.data

# Sample data
people = [
    {"name": "Alice", "age": 30, "salary": 80000},
    {"name": "Bob", "age": 25, "salary": 70000},
    {"name": "Carol", "age": 28, "salary": 75000},
    {"name": "David", "age": 35, "salary": 90000},
]

# Use the pipeline
result = (DataPipeline(people)
    .filter(lambda p: p["age"] >= 28)
    .map(lambda p: {**p, "salary_level": "high" if p["salary"] >= 75000 else "low"})
    .sort(key=lambda p: p["salary"], reverse=True)
    .get())

print("Pipeline result:")
for person in result:
    print(f"  {person}")
```

Run it and observe the data pipeline.

---

### Challenge 2: Analyze Sales Data

Create a file called `sales_analysis.py`:

```python
"""Analyze sales data."""

from collections import Counter
from datetime import datetime, timedelta

# Generate sample sales data
sales = [
    {"date": "2023-01-01", "product": "A", "quantity": 10, "price": 100},
    {"date": "2023-01-01", "product": "B", "quantity": 5, "price": 200},
    {"date": "2023-01-02", "product": "A", "quantity": 8, "price": 100},
    {"date": "2023-01-02", "product": "C", "quantity": 3, "price": 300},
    {"date": "2023-01-03", "product": "B", "quantity": 2, "price": 200},
]

# Total revenue
total_revenue = sum(s["quantity"] * s["price"] for s in sales)
print(f"Total revenue: ${total_revenue}")

# Revenue by product
by_product = {}
for sale in sales:
    product = sale["product"]
    revenue = sale["quantity"] * sale["price"]
    by_product[product] = by_product.get(product, 0) + revenue

print("\nRevenue by product:")
for product, revenue in sorted(by_product.items(), key=lambda x: x[1], reverse=True):
    print(f"  {product}: ${revenue}")

# Most popular product
products = [s["product"] for s in sales for _ in range(s["quantity"])]
most_common = Counter(products).most_common(1)
print(f"\nMost popular product: {most_common[0][0]} ({most_common[0][1]} units)")

# Average price per product
avg_prices = {}
for product in set(s["product"] for s in sales):
    prices = [s["price"] for s in sales if s["product"] == product]
    avg_prices[product] = sum(prices) / len(prices)

print("\nAverage price by product:")
for product, price in avg_prices.items():
    print(f"  {product}: ${price}")
```

Run it and observe sales analysis.

---

## Hints

**Data not loading** → Check file paths and formats. Use `Path.exists()` to verify files exist.

**Validation too strict** → Adjust regex patterns and validation rules to match your data.

**Merge not working** → Ensure you're matching on the correct keys and handling missing values.

**Pipeline not chaining** → Return `self` from each method to enable method chaining.

---

## What to Review If You Get Stuck

- **Loading data** → Handbook section 2.1
- **Cleaning data** → Handbook section 2.2
- **Transforming data** → Handbook section 2.3
- **Aggregating data** → Handbook section 2.4
- **Validating data** → Handbook section 2.5
- **Exporting data** → Handbook section 2.6

---

## Key Takeaways

After completing these exercises, you should be able to:

- Load data from JSON and CSV files
- Clean and validate data
- Transform and aggregate data
- Merge data from multiple sources
- Export data to different formats
- Build data processing pipelines
- Analyze real-world data
- Handle data quality issues

