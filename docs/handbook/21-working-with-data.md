# Chapter 21: Working with Data

## 1. Overview

Most programs that do something useful work with data: reading records from a
file, cleaning up messy input, filtering down to what matters, sorting and
grouping results, and computing summaries. You do not need a third-party
library like pandas to do this well. Python's standard library — `csv`,
`json`, `pathlib`, and a handful of built-in functions — is enough for a wide
range of real tasks.

This chapter walks through the full cycle: loading data from CSV and JSON
files, cleaning it, transforming it, and producing useful output. Every
technique here uses only the standard library.

---

## 2. What You Will Learn

- Reading tabular data from CSV files with `csv.DictReader`
- Reading structured data from JSON files
- Cleaning data: stripping whitespace, handling missing values, converting types
- Filtering records with list comprehensions and functions
- Sorting records by one or more fields
- Grouping records by a key
- Using lists of dicts as an in-memory table
- Simple aggregation: sum, average, count, min, max
- Writing cleaned or processed data back to CSV or JSON
- Building small data pipelines from composable functions

---

## 3. Core Concepts

### 3.1 The List-of-Dicts Pattern

The most natural way to represent tabular data in Python — without any
third-party library — is a **list of dicts**. Each dict is one row; the keys
are column names.

```python
employees: list[dict] = [
    {"name": "Alice",   "department": "Engineering", "salary": 95000},
    {"name": "Bob",     "department": "Marketing",   "salary": 72000},
    {"name": "Charlie", "department": "Engineering", "salary": 88000},
    {"name": "Diana",   "department": "Marketing",   "salary": 76000},
]
```

This structure is easy to read, easy to filter, easy to sort, and maps
directly to what `csv.DictReader` and `json.load` produce. All the patterns
in this chapter work on lists of dicts.

---

### 3.2 Reading CSV Files

Use `csv.DictReader` to read a CSV file with a header row. Each row becomes
a dict whose keys are the column names from the header.

```python
import csv
from pathlib import Path


def load_csv(path: str | Path) -> list[dict]:
    """Load a CSV file and return a list of row dicts."""
    with Path(path).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)
```

Every value in the returned dicts is a **string** — `csv.DictReader` does
not convert types. You will handle type conversion in the cleaning step.

Always pass `newline=""` when opening CSV files. This lets the `csv` module
handle line endings correctly across platforms.

---

### 3.3 Reading JSON Files

Use `json.load` to read a JSON file. If the file contains an array of
objects, you get a list of dicts directly.

```python
import json
from pathlib import Path


def load_json(path: str | Path) -> list[dict]:
    """Load a JSON file containing an array of objects."""
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)
```

Unlike CSV, JSON preserves types: numbers stay numbers, booleans stay
booleans, and `null` becomes `None`. You may still need to clean string
fields (whitespace, empty strings), but numeric fields are ready to use.

---

### 3.4 Cleaning Data

Real data is messy. Fields may have leading or trailing whitespace, missing
values, or the wrong type. Clean your data right after loading it, before
doing anything else.

#### Stripping whitespace

```python
def strip_fields(record: dict) -> dict:
    """Strip leading/trailing whitespace from all string values."""
    return {k: v.strip() if isinstance(v, str) else v for k, v in record.items()}
```

Apply it to every record after loading:

```python
records = [strip_fields(r) for r in load_csv("data.csv")]
```

#### Handling missing values

CSV files often represent missing data as an empty string `""`. Decide what
to do with each field: skip the record, substitute a default, or keep `None`.

```python
def parse_salary(value: str, default: float = 0.0) -> float:
    """Convert a salary string to float; return default if blank or invalid."""
    value = value.strip()
    if not value:
        return default
    try:
        return float(value.replace(",", ""))
    except ValueError:
        return default
```

#### Type conversion

All CSV values start as strings. Convert them to the right type as part of
cleaning.

```python
def clean_employee(raw: dict) -> dict:
    """Clean and type-convert a raw employee record from CSV."""
    return {
        "name":       raw.get("name", "").strip(),
        "department": raw.get("department", "").strip(),
        "salary":     parse_salary(raw.get("salary", "")),
        "active":     raw.get("active", "").strip().lower() == "true",
    }
```

A clean pipeline looks like this:

```python
raw_records = load_csv("employees.csv")
employees = [clean_employee(r) for r in raw_records]
```

After this step, every record has the right types and no stray whitespace.
The rest of your code can trust the data.

---

### 3.5 Filtering Records

Use a list comprehension to keep only the records that match a condition.

```python
# Keep only Engineering employees
engineers = [e for e in employees if e["department"] == "Engineering"]

# Keep only active employees with salary above 80,000
senior = [
    e for e in employees
    if e["active"] and e["salary"] > 80_000
]
```

For reusable filters, write a function that takes a predicate:

```python
from collections.abc import Callable


def filter_records(
    records: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Return records for which predicate returns True."""
    return [r for r in records if predicate(r)]


high_earners = filter_records(employees, lambda e: e["salary"] > 90_000)
```

---

### 3.6 Sorting Records

Use `sorted()` with a `key` function. The `key` receives one record and
returns the value to sort by.

```python
# Sort by salary, highest first
by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)

# Sort by department, then by name within each department
by_dept_name = sorted(employees, key=lambda e: (e["department"], e["name"]))
```

`sorted()` always returns a new list; the original is unchanged. Use
`list.sort()` if you want to sort in place.

For descending sort on one field and ascending on another, negate the
numeric field:

```python
# Highest salary first; alphabetical name as tiebreaker
ranked = sorted(employees, key=lambda e: (-e["salary"], e["name"]))
```

---

### 3.7 Grouping Records

Grouping means collecting records that share a value into buckets. The
standard pattern uses a dict of lists.

```python
from collections import defaultdict


def group_by(records: list[dict], key: str) -> dict[str, list[dict]]:
    """Group records by the value of a given key."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        groups[record[key]].append(record)
    return dict(groups)


by_department = group_by(employees, "department")

for dept, members in sorted(by_department.items()):
    names = [m["name"] for m in members]
    print(f"{dept}: {', '.join(names)}")
```

`defaultdict(list)` automatically creates an empty list for any new key, so
you do not need to check whether the key exists before appending.

---

### 3.8 Aggregation

Once you have a list of records (or a group), computing summaries is
straightforward with Python's built-in functions.

```python
def summarize(records: list[dict], field: str) -> dict:
    """Return count, sum, average, min, and max for a numeric field."""
    values = [r[field] for r in records if r[field] is not None]
    if not values:
        return {"count": 0, "sum": 0, "avg": None, "min": None, "max": None}
    return {
        "count": len(values),
        "sum":   sum(values),
        "avg":   sum(values) / len(values),
        "min":   min(values),
        "max":   max(values),
    }


stats = summarize(employees, "salary")
print(f"Count:   {stats['count']}")
print(f"Average: {stats['avg']:,.0f}")
print(f"Min:     {stats['min']:,.0f}")
print(f"Max:     {stats['max']:,.0f}")
```

To aggregate per group, combine `group_by` and `summarize`:

```python
by_dept = group_by(employees, "department")

for dept, members in sorted(by_dept.items()):
    stats = summarize(members, "salary")
    print(f"{dept}: avg salary {stats['avg']:,.0f} ({stats['count']} people)")
```

---

### 3.9 Writing Results

After processing, write results back to CSV or JSON.

#### Writing CSV

```python
import csv
from pathlib import Path


def save_csv(records: list[dict], path: str | Path) -> None:
    """Write a list of dicts to a CSV file."""
    if not records:
        return
    fieldnames = list(records[0].keys())
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
```

#### Writing JSON

```python
import json
from pathlib import Path


def save_json(data: list | dict, path: str | Path, indent: int = 2) -> None:
    """Write data to a JSON file."""
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
```

---

## 4. Practical Examples

### 4.1 Loading and Cleaning a Sales CSV

Suppose you have a `sales.csv` file:

```text
date,product,units,revenue
2024-01-03,Widget A,12,240.00
2024-01-03,Widget B, 5,200.00
2024-01-04,Widget A,,
2024-01-04,Gadget X,3,600.00
```

Load, clean, and inspect it:

```python
import csv
import json
from pathlib import Path


def parse_int(value: str, default: int = 0) -> int:
    try:
        return int(value.strip())
    except (ValueError, AttributeError):
        return default


def parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value.strip())
    except (ValueError, AttributeError):
        return default


def clean_sale(raw: dict) -> dict:
    return {
        "date":    raw.get("date", "").strip(),
        "product": raw.get("product", "").strip(),
        "units":   parse_int(raw.get("units", "")),
        "revenue": parse_float(raw.get("revenue", "")),
    }


def load_sales(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return [clean_sale(row) for row in reader]


# sales = load_sales("sales.csv")
# for s in sales:
#     print(s)
# {'date': '2024-01-03', 'product': 'Widget A', 'units': 12, 'revenue': 240.0}
# {'date': '2024-01-03', 'product': 'Widget B', 'units': 5,  'revenue': 200.0}
# {'date': '2024-01-04', 'product': 'Widget A', 'units': 0,  'revenue': 0.0}
# {'date': '2024-01-04', 'product': 'Gadget X', 'units': 3,  'revenue': 600.0}
```

The row with missing `units` and `revenue` gets default values of `0` instead
of crashing. You can decide later whether to drop those rows or keep them.

---

### 4.2 Filtering and Sorting Sales

```python
def top_products_by_revenue(
    sales: list[dict],
    n: int = 5,
) -> list[dict]:
    """Return the top N products by total revenue."""
    # Group by product
    totals: dict[str, float] = {}
    for sale in sales:
        product = sale["product"]
        totals[product] = totals.get(product, 0.0) + sale["revenue"]

    # Convert to list of dicts and sort
    ranked = [
        {"product": p, "total_revenue": r}
        for p, r in totals.items()
    ]
    return sorted(ranked, key=lambda x: x["total_revenue"], reverse=True)[:n]


# results = top_products_by_revenue(sales)
# for r in results:
#     print(f"{r['product']:<20} ${r['total_revenue']:>10,.2f}")
```

---

### 4.3 Grouping and Summarizing by Date

```python
from collections import defaultdict


def daily_summary(sales: list[dict]) -> list[dict]:
    """Return total units and revenue per date, sorted by date."""
    by_date: dict[str, dict] = defaultdict(lambda: {"units": 0, "revenue": 0.0})

    for sale in sales:
        day = sale["date"]
        by_date[day]["units"]   += sale["units"]
        by_date[day]["revenue"] += sale["revenue"]

    return [
        {"date": d, "units": v["units"], "revenue": v["revenue"]}
        for d, v in sorted(by_date.items())
    ]


# summary = daily_summary(sales)
# for row in summary:
#     print(f"{row['date']}  units={row['units']}  revenue=${row['revenue']:.2f}")
```

---

### 4.4 Loading and Processing JSON Records

Suppose you have a `products.json` file:

```json
[
  {"id": 1, "name": "Widget A", "price": 20.00, "in_stock": true},
  {"id": 2, "name": "Widget B", "price": 40.00, "in_stock": false},
  {"id": 3, "name": "Gadget X", "price": 200.00, "in_stock": true}
]
```

Load and filter it:

```python
import json
from pathlib import Path


def load_products(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)


def available_products(products: list[dict]) -> list[dict]:
    """Return only in-stock products, sorted by price."""
    in_stock = [p for p in products if p.get("in_stock")]
    return sorted(in_stock, key=lambda p: p["price"])


# products = load_products("products.json")
# for p in available_products(products):
#     print(f"{p['name']:<20} ${p['price']:.2f}")
```

---

### 4.5 Computing Aggregates Across Groups

```python
def department_stats(employees: list[dict]) -> list[dict]:
    """Return salary statistics per department."""
    by_dept: dict[str, list[float]] = defaultdict(list)

    for emp in employees:
        if emp.get("salary") is not None:
            by_dept[emp["department"]].append(emp["salary"])

    result = []
    for dept, salaries in sorted(by_dept.items()):
        result.append({
            "department": dept,
            "count":      len(salaries),
            "avg_salary": sum(salaries) / len(salaries),
            "min_salary": min(salaries),
            "max_salary": max(salaries),
        })
    return result


# stats = department_stats(employees)
# for row in stats:
#     print(
#         f"{row['department']:<15} "
#         f"n={row['count']}  "
#         f"avg={row['avg_salary']:,.0f}  "
#         f"min={row['min_salary']:,.0f}  "
#         f"max={row['max_salary']:,.0f}"
#     )
```

---

### 4.6 A Complete Data Pipeline

Here is a self-contained pipeline that loads a CSV, cleans it, filters it,
groups it, summarizes it, and writes the result to a new CSV — all using
only the standard library.

```python
"""
pipeline.py — a complete data processing pipeline.

Input:  employees.csv  (name, department, salary, active)
Output: dept_summary.csv  (department, count, avg_salary, min_salary, max_salary)
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path


# ── Loading ──────────────────────────────────────────────────────────────────

def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


# ── Cleaning ─────────────────────────────────────────────────────────────────

def parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value.strip().replace(",", ""))
    except (ValueError, AttributeError):
        return default


def clean_employee(raw: dict) -> dict:
    return {
        "name":       raw.get("name", "").strip(),
        "department": raw.get("department", "").strip(),
        "salary":     parse_float(raw.get("salary", "")),
        "active":     raw.get("active", "").strip().lower() == "true",
    }


# ── Filtering ─────────────────────────────────────────────────────────────────

def active_only(employees: list[dict]) -> list[dict]:
    return [e for e in employees if e["active"]]


# ── Grouping ──────────────────────────────────────────────────────────────────

def group_by_department(employees: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for emp in employees:
        groups[emp["department"]].append(emp)
    return dict(groups)


# ── Aggregation ───────────────────────────────────────────────────────────────

def dept_summary(dept: str, members: list[dict]) -> dict:
    salaries = [m["salary"] for m in members]
    return {
        "department": dept,
        "count":      len(salaries),
        "avg_salary": round(sum(salaries) / len(salaries), 2) if salaries else 0,
        "min_salary": min(salaries) if salaries else 0,
        "max_salary": max(salaries) if salaries else 0,
    }


# ── Writing ───────────────────────────────────────────────────────────────────

def save_csv(records: list[dict], path: Path) -> None:
    if not records:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)


# ── Pipeline ──────────────────────────────────────────────────────────────────

def run(input_path: Path, output_path: Path) -> None:
    raw        = load_csv(input_path)
    employees  = [clean_employee(r) for r in raw]
    active     = active_only(employees)
    by_dept    = group_by_department(active)
    summaries  = [
        dept_summary(dept, members)
        for dept, members in sorted(by_dept.items())
    ]
    save_csv(summaries, output_path)
    print(f"Wrote {len(summaries)} department summaries to {output_path}.")


if __name__ == "__main__":
    run(Path("employees.csv"), Path("dept_summary.csv"))
```

Each step is a small, named function. You can test each one independently,
swap out the data source, or add a new step without touching the others.

---

### 4.7 Searching and Deduplicating Records

```python
def find_by_field(
    records: list[dict],
    field: str,
    value: object,
) -> list[dict]:
    """Return all records where records[field] == value."""
    return [r for r in records if r.get(field) == value]


def deduplicate_by(records: list[dict], key: str) -> list[dict]:
    """Return records with duplicate key values removed (keeps first occurrence)."""
    seen: set = set()
    result = []
    for record in records:
        k = record.get(key)
        if k not in seen:
            seen.add(k)
            result.append(record)
    return result


# engineers = find_by_field(employees, "department", "Engineering")
# unique_by_name = deduplicate_by(employees, "name")
```

---

## 5. Common Mistakes

### 5.1 Forgetting That CSV Values Are Always Strings

`csv.DictReader` returns every value as a string, even if the CSV contains
numbers. Arithmetic on strings silently produces wrong results.

```python
import csv, io

data = "name,score\nAlice,88\nBob,92\n"
reader = csv.DictReader(io.StringIO(data))
rows = list(reader)

# Wrong — string concatenation, not addition
total = rows[0]["score"] + rows[1]["score"]
print(total)   # '8892'  — not 180!

# Correct — convert first
total = int(rows[0]["score"]) + int(rows[1]["score"])
print(total)   # 180
```

Always convert numeric fields to `int` or `float` right after loading.

---

### 5.2 Not Handling Missing or Empty Fields

If a field is missing or blank, `int("")` and `float("")` raise `ValueError`.
Wrap conversions in a helper that returns a sensible default.

```python
# Crashes on empty string
value = int("")   # ValueError: invalid literal for int() with base 10: ''

# Safe
def to_int(s: str, default: int = 0) -> int:
    try:
        return int(s.strip())
    except (ValueError, AttributeError):
        return default
```

---

### 5.3 Mutating Records While Iterating

Modifying a list while iterating over it skips items or causes unexpected
behavior. Build a new list instead.

```python
records = [{"score": 50}, {"score": 80}, {"score": 30}]

# Wrong — modifying the list while iterating
for r in records:
    if r["score"] < 60:
        records.remove(r)   # skips items!

# Correct — build a new list
records = [r for r in records if r["score"] >= 60]
```

---

### 5.4 Using a Plain `dict` Instead of `defaultdict` for Grouping

Without `defaultdict`, you must check whether a key exists before appending.
Forgetting the check raises a `KeyError`.

```python
# Fragile — KeyError if key is new
groups = {}
for record in records:
    groups[record["dept"]].append(record)   # KeyError on first new dept

# Correct option 1 — setdefault
groups = {}
for record in records:
    groups.setdefault(record["dept"], []).append(record)

# Correct option 2 — defaultdict
from collections import defaultdict
groups = defaultdict(list)
for record in records:
    groups[record["dept"]].append(record)
```

---

### 5.5 Sorting Strings That Should Be Numbers

If you forget to convert a numeric field, `sorted()` sorts it
lexicographically (as text), which gives the wrong order.

```python
records = [
    {"name": "A", "score": "9"},
    {"name": "B", "score": "10"},
    {"name": "C", "score": "2"},
]

# Wrong — lexicographic order: "10" < "2" < "9"
wrong = sorted(records, key=lambda r: r["score"])
print([r["score"] for r in wrong])   # ['10', '2', '9']

# Correct — numeric order
right = sorted(records, key=lambda r: int(r["score"]))
print([r["score"] for r in right])   # ['2', '9', '10']
```

---

### 5.6 Assuming `json.load` Always Returns a List

A JSON file might contain a single object `{}` instead of an array `[]`.
Check the type before treating it as a list of records.

```python
import json
from pathlib import Path


def load_records(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return [data]   # wrap single object in a list
    raise ValueError(f"Unexpected JSON structure in {path}: {type(data)}")
```

---

### 5.7 Building Large Strings with `+` in a Loop

When generating a report or output string, concatenating with `+` inside a
loop creates a new string object on every iteration. Use a list and
`"".join()` instead.

```python
records = [{"name": "Alice", "score": 88}, {"name": "Bob", "score": 92}]

# Slow for large data
output = ""
for r in records:
    output += f"{r['name']}: {r['score']}\n"

# Better
lines = [f"{r['name']}: {r['score']}" for r in records]
output = "\n".join(lines)
```

---

## 6. Practice Tasks

1. Write a function `load_and_clean_csv(path: str | Path) -> list[dict]`
   that reads a CSV file, strips whitespace from all string fields, and
   returns the cleaned records.

2. Given a list of dicts with `"name"` and `"score"` keys (scores as
   strings), write a function `top_scorers(records: list[dict], n: int) ->
   list[dict]` that returns the top `n` records sorted by score descending.
   Convert scores to integers before sorting.

3. Write a function `count_by(records: list[dict], field: str) ->
   dict[str, int]` that returns a dict mapping each unique value of `field`
   to the number of records with that value.

4. Write a function `average_field(records: list[dict], field: str) ->
   float | None` that returns the average of a numeric field across all
   records, or `None` if there are no valid values.

5. Write a function `filter_range(records: list[dict], field: str,
   low: float, high: float) -> list[dict]` that returns records where the
   numeric value of `field` falls between `low` and `high` (inclusive).

6. Write a function `pivot_count(records: list[dict], row_key: str,
   col_key: str) -> dict[str, dict[str, int]]` that builds a pivot table
   counting how many records have each combination of `row_key` and
   `col_key` values.

7. Write a complete script that reads `sales.csv` (columns: `date`,
   `product`, `units`, `revenue`), computes total revenue per product,
   and writes the result to `product_totals.csv` sorted by revenue
   descending. Use `pathlib`, type hints, and small named functions.

8. Extend the pipeline from section 4.6 to also write a JSON file
   `dept_summary.json` alongside the CSV. The JSON should contain the
   same data as the CSV.

---

## 7. Key Takeaways

- Represent tabular data as a list of dicts. Each dict is one row; keys are
  column names. This structure works directly with `csv.DictReader`,
  `json.load`, and all the patterns in this chapter.
- `csv.DictReader` returns every value as a string. Always convert numeric
  fields to `int` or `float` right after loading.
- Clean data immediately after loading: strip whitespace, handle empty
  strings, and convert types. The rest of your code can then trust the data.
- Filter with list comprehensions: `[r for r in records if condition]`.
- Sort with `sorted(records, key=lambda r: r["field"])`. Use a tuple key
  to sort by multiple fields. Negate a numeric field to sort it descending.
- Group with `defaultdict(list)`: iterate once, appending each record to
  the right bucket.
- Aggregate with Python's built-ins: `len()`, `sum()`, `min()`, `max()`.
  Average is `sum(values) / len(values)`.
- Keep each step of a pipeline in its own small function. This makes the
  code testable, readable, and easy to extend.
- Write results back with `csv.DictWriter` or `json.dump`. Always pass
  `newline=""` for CSV and `encoding="utf-8"` for both.

---

### Further Reading

- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Working with Text Data](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Working with Binary Data](https://docs.python.org/3/library/stdtypes.html#bytes-objects)

### What's Next

Ready to continue? Head to the next chapter: **Practical Projects**.

→ [Chapter 22 — Practical Projects](22-practical-projects.md)

*See also:*
- [Exercise](../exercises/21-working-with-data.md)
- [Solution](../solutions/21-working-with-data.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
