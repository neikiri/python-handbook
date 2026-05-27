# Solutions 21: Working with Data

## Overview

Chapter 21 exercises cover loading, cleaning, transforming, aggregating, validating, merging, and exporting data. This guide explains the reasoning behind each solution and highlights practical patterns for real-world data processing.

---

## Notes Before Checking Solutions

Data processing in Python follows a consistent pattern: load → clean → transform → analyze → export. Each step should be a separate function. This makes the pipeline easy to test, debug, and modify.

---

## Warm-up Exercise Solutions

### Exercise 1: Load and Explore Data

```python
import json
import csv
from pathlib import Path

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Carol", "age": 28, "city": "Chicago"},
]

# Save and load JSON
json_file = Path("people.json")
json_file.write_text(json.dumps(data, indent=2))

loaded = json.loads(json_file.read_text())
print(f"Loaded {len(loaded)} records")
print(f"Keys: {list(loaded[0].keys())}")

# Save and load CSV
csv_file = Path("people.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

with open(csv_file, "r") as f:
    records = list(csv.DictReader(f))
    print(f"Loaded {len(records)} CSV records")

# Clean up
json_file.unlink()
csv_file.unlink()
```

**Always explore data before processing it.** Check the number of records, the field names, and a sample record. This catches format issues early.

**JSON preserves types** (integers stay integers). CSV does not — everything becomes a string. Always convert numeric fields after reading from CSV.

---

### Exercise 2: Clean Data

```python
def clean_record(record):
    cleaned = {}
    for key, value in record.items():
        if isinstance(value, str):
            value = value.strip()
            if key == "name":
                value = value.title()
        cleaned[key] = value
    return cleaned

def clean_data(data):
    cleaned = []
    for record in data:
        cleaned_record = clean_record(record)
        if cleaned_record.get("age"):
            cleaned_record["age"] = int(cleaned_record["age"])
            cleaned.append(cleaned_record)
    return cleaned

messy_data = [
    {"name": "  Alice  ", "age": "30", "city": "New York"},
    {"name": "Bob", "age": "25", "city": "  Los Angeles  "},
    {"name": "CAROL", "age": "28", "city": "Chicago"},
    {"name": "David", "age": "", "city": "Boston"},  # missing age — skipped
]

cleaned = clean_data(messy_data)
# [
#   {'name': 'Alice', 'age': 30, 'city': 'New York'},
#   {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
#   {'name': 'Carol', 'age': 28, 'city': 'Chicago'},
# ]
```

**`.strip()`** removes leading and trailing whitespace. **`.title()`** capitalizes the first letter of each word. These two operations fix the most common string quality issues.

**Skip records with missing required fields** rather than crashing. The `if cleaned_record.get("age"):` check skips David because his age is an empty string. Decide upfront which fields are required and which are optional.

---

### Exercise 3: Transform Data

```python
people = [
    {"name": "Alice", "age": 30, "salary": 80000},
    {"name": "Bob", "age": 25, "salary": 70000},
    {"name": "Carol", "age": 28, "salary": 75000},
]

# Extract specific fields
names = [p["name"] for p in people]
# ['Alice', 'Bob', 'Carol']

# Add computed fields
for person in people:
    person["age_group"] = "30+" if person["age"] >= 30 else "20-29"
    person["salary_level"] = "high" if person["salary"] >= 75000 else "low"

# Group by field
by_age_group = {}
for person in people:
    group = person["age_group"]
    if group not in by_age_group:
        by_age_group[group] = []
    by_age_group[group].append(person)

# Sort
sorted_by_salary = sorted(people, key=lambda p: p["salary"], reverse=True)
```

**`sorted()` with a `key` function** is the standard way to sort complex objects. `key=lambda p: p["salary"]` extracts the sort key from each record. `reverse=True` sorts descending.

**Adding computed fields** to records is a common transformation. Use `{**record, "new_field": value}` to create a new dict without modifying the original, or modify in place if you own the data.

---

### Exercise 4: Aggregate Data

```python
sales = [
    {"product": "A", "quantity": 10, "price": 100},
    {"product": "B", "quantity": 5, "price": 200},
    {"product": "A", "quantity": 8, "price": 100},
    {"product": "C", "quantity": 3, "price": 300},
    {"product": "B", "quantity": 2, "price": 200},
]

total_quantity = sum(s["quantity"] for s in sales)
total_revenue = sum(s["quantity"] * s["price"] for s in sales)
# total_revenue = 10*100 + 5*200 + 8*100 + 3*300 + 2*200 = 3500

# Aggregate by product
by_product = {}
for sale in sales:
    product = sale["product"]
    if product not in by_product:
        by_product[product] = {"quantity": 0, "revenue": 0}
    by_product[product]["quantity"] += sale["quantity"]
    by_product[product]["revenue"] += sale["quantity"] * sale["price"]

# Find top product by revenue
top_product = max(by_product.items(), key=lambda x: x[1]["revenue"])
print(f"Top product: {top_product[0]}")
```

**`max()` with a `key` function** finds the item that produces the highest key value. `max(by_product.items(), key=lambda x: x[1]["revenue"])` returns the `(product_name, stats)` tuple with the highest revenue.

**`collections.defaultdict`** simplifies the grouping pattern:

```python
from collections import defaultdict

by_product = defaultdict(lambda: {"quantity": 0, "revenue": 0})
for sale in sales:
    by_product[sale["product"]]["quantity"] += sale["quantity"]
    by_product[sale["product"]]["revenue"] += sale["quantity"] * sale["price"]
```

---

## Practice Exercise Solutions

### Exercise 5: Validate Data

```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    digits = "".join(c for c in phone if c.isdigit())
    return len(digits) == 10

def validate_record(record):
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
```

**Return a list of errors** rather than a single boolean. This lets the caller show all validation errors at once instead of one at a time.

**Validate only what is present.** `if record.get("phone") and not validate_phone(...)` only validates the phone if it is provided. Optional fields should not fail validation when absent.

---

### Exercise 6: Merge Data

```python
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

# Group orders by user
merged = []
for user in users:
    user_orders = [o for o in orders if o["user_id"] == user["id"]]
    merged.append({
        "user": user,
        "orders": user_orders,
        "total_spent": sum(o["price"] for o in user_orders),
    })

# Join (flat)
joined = []
for order in orders:
    user = next((u for u in users if u["id"] == order["user_id"]), None)
    if user:
        joined.append({
            "user_name": user["name"],
            "product": order["product"],
            "price": order["price"],
        })
```

**`next((u for u in users if ...), None)`** finds the first matching user or returns `None` if not found. This is the Python equivalent of a SQL LEFT JOIN lookup.

**For large datasets**, build a lookup dictionary first to avoid O(n²) scanning:

```python
user_by_id = {u["id"]: u for u in users}
for order in orders:
    user = user_by_id.get(order["user_id"])
```

---

### Exercise 7: Export Data

```python
import json
import csv
from pathlib import Path

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
]

# JSON
json_file = Path("export.json")
json_file.write_text(json.dumps(data, indent=2))

# CSV
csv_file = Path("export.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

# Plain text table
txt_file = Path("export.txt")
with open(txt_file, "w") as f:
    f.write("Name | Age | City\n")
    f.write("-" * 30 + "\n")
    for record in data:
        f.write(f"{record['name']} | {record['age']} | {record['city']}\n")

# Clean up
for f in [json_file, csv_file, txt_file]:
    f.unlink()
```

**Choose the export format based on the consumer.** JSON for APIs and other Python programs; CSV for spreadsheets and data tools; plain text for human-readable reports.

---

## Challenge Exercise Solutions

### Challenge 1: Build a Data Pipeline

```python
class DataPipeline:
    def __init__(self, data):
        self.data = data

    def filter(self, predicate):
        self.data = [item for item in self.data if predicate(item)]
        return self

    def map(self, transform):
        self.data = [transform(item) for item in self.data]
        return self

    def sort(self, key, reverse=False):
        self.data = sorted(self.data, key=key, reverse=reverse)
        return self

    def get(self):
        return self.data

people = [
    {"name": "Alice", "age": 30, "salary": 80000},
    {"name": "Bob", "age": 25, "salary": 70000},
    {"name": "Carol", "age": 28, "salary": 75000},
    {"name": "David", "age": 35, "salary": 90000},
]

result = (DataPipeline(people)
    .filter(lambda p: p["age"] >= 28)
    .map(lambda p: {**p, "salary_level": "high" if p["salary"] >= 75000 else "low"})
    .sort(key=lambda p: p["salary"], reverse=True)
    .get())
```

**Method chaining** works because each method returns `self`. This is the builder pattern — each call modifies the object and returns it for the next call.

**`{**p, "salary_level": ...}`** creates a new dict with all of `p`'s keys plus the new `salary_level` key. This is non-destructive — the original `p` is unchanged.

---

### Challenge 2: Analyze Sales Data

```python
from collections import Counter

sales = [
    {"date": "2023-01-01", "product": "A", "quantity": 10, "price": 100},
    {"date": "2023-01-01", "product": "B", "quantity": 5, "price": 200},
    {"date": "2023-01-02", "product": "A", "quantity": 8, "price": 100},
    {"date": "2023-01-02", "product": "C", "quantity": 3, "price": 300},
    {"date": "2023-01-03", "product": "B", "quantity": 2, "price": 200},
]

total_revenue = sum(s["quantity"] * s["price"] for s in sales)

by_product = {}
for sale in sales:
    product = sale["product"]
    revenue = sale["quantity"] * sale["price"]
    by_product[product] = by_product.get(product, 0) + revenue

# Most popular by units sold
products = [s["product"] for s in sales for _ in range(s["quantity"])]
most_common = Counter(products).most_common(1)
print(f"Most popular: {most_common[0][0]} ({most_common[0][1]} units)")
```

**`for _ in range(s["quantity"])`** repeats the product name `quantity` times, so `Counter` counts total units sold rather than number of transactions.

---

## Common Mistakes

**Modifying data while iterating over it.** Never add or remove items from a list while iterating over it. Build a new list instead.

**Forgetting to convert CSV strings to numbers.** After reading from CSV, `record["age"]` is `"30"`, not `30`. Always convert explicitly.

**O(n²) lookups in merge operations.** Scanning a list for each record in another list is slow for large datasets. Build a lookup dictionary first.

**Not handling missing keys.** Use `record.get("field", default)` instead of `record["field"]` when a field might be absent.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 22 - Practical Projects](../handbook/22-practical-projects.md)
