"""
Datetime Example - Working with Dates and Times

This example demonstrates:
- Creating datetime objects
- Formatting and parsing dates
- Date arithmetic
- Time zones
"""

from datetime import datetime, date, time, timedelta, timezone
import math

print("=== Creating Datetime Objects ===")

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")

# Current date only
today = date.today()
print(f"Today's date: {today}")

# Current time only
current_time = datetime.now().time()
print(f"Current time: {current_time}")
print()

# Create specific datetime
birthday = datetime(1990, 5, 15, 14, 30, 0)  # Year, month, day, hour, minute, second
print(f"Birthday: {birthday}")
print()

# Create from timestamp (seconds since 1970-01-01)
timestamp = 1609459200  # 2021-01-01 00:00:00 UTC
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print(f"From timestamp: {dt_from_timestamp}")
print()

print("=== Accessing Datetime Components ===")

now = datetime.now()
print(f"Current datetime: {now}")
print(f"  Year: {now.year}")
print(f"  Month: {now.month}")
print(f"  Day: {now.day}")
print(f"  Hour: {now.hour}")
print(f"  Minute: {now.minute}")
print(f"  Second: {now.second}")
print(f"  Weekday (0=Monday, 6=Sunday): {now.weekday()}")
print()

print("=== Date Arithmetic ===")

# Create dates
date1 = date(2024, 1, 15)
date2 = date(2024, 2, 1)

# Calculate difference
diff = date2 - date1
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference: {diff.days} days")
print()

# Add/subtract timedelta
today = date.today()
one_week = timedelta(days=7)
next_week = today + one_week
last_week = today - one_week

print(f"Today: {today}")
print(f"Next week: {next_week}")
print(f"Last week: {last_week}")
print()

print("=== Time Arithmetic ===")

# Create times
time1 = datetime(2024, 1, 1, 10, 30, 0)
time2 = datetime(2024, 1, 1, 14, 45, 30)

diff = time2 - time1
print(f"Time 1: {time1.time()}")
print(f"Time 2: {time2.time()}")
print(f"Difference: {diff}")
print(f"  Total seconds: {diff.total_seconds()}")
print()

# Add time
start = datetime(2024, 1, 1, 10, 0, 0)
duration = timedelta(hours=2, minutes=30)
end = start + duration

print(f"Start: {start.time()}")
print(f"Duration: {duration}")
print(f"End: {end.time()}")
print()

print("=== Formatting Dates ===")

now = datetime.now()

# Using strftime() (string format time)
print("Formatting with strftime():")
print(f"  Full date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Date only: {now.strftime('%Y-%m-%d')}")
print(f"  Time only: {now.strftime('%H:%M:%S')}")
print(f"  Month name: {now.strftime('%B')}")
print(f"  Day name: {now.strftime('%A')}")
print(f"  Short format: {now.strftime('%b %d, %Y')}")
print()

# Common format codes
print("Format codes:")
print("  %Y - Year (4 digits)")
print("  %m - Month (01-12)")
print("  %d - Day (01-31)")
print("  %H - Hour (00-23)")
print("  %M - Minute (00-59)")
print("  %S - Second (00-59)")
print("  %B - Full month name")
print("  %b - Abbreviated month name")
print("  %A - Full weekday name")
print("  %a - Abbreviated weekday name")
print()

print("=== Parsing Dates ===")

# Using strptime() (string parse time)
date_string = "2024-01-15 14:30:00"
parsed = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed from '{date_string}': {parsed}")

# Different format
date_string2 = "January 15, 2024"
parsed2 = datetime.strptime(date_string2, "%B %d, %Y")
print(f"Parsed from '{date_string2}': {parsed2}")
print()

print("=== Time Zones ===")

# UTC timezone
utc_now = datetime.now(timezone.utc)
print(f"UTC time: {utc_now}")

# Create timezone with offset
est = timezone(timedelta(hours=-5))
est_time = datetime.now(est)
print(f"EST time: {est_time}")

# Convert between timezones
utc_time = datetime.now(timezone.utc)
est_time = utc_time.astimezone(est)
print(f"UTC converted to EST: {est_time}")
print()

print("=== Practical Examples ===")

# Calculate age
birth_date = date(1990, 5, 15)
today = date.today()
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Birth date: {birth_date}")
print(f"Age: {age} years")
print()

# Calculate due date
start_date = date.today()
project_duration = timedelta(days=30)
due_date = start_date + project_duration

print(f"Start date: {start_date}")
print(f"Project duration: {project_duration.days} days")
print(f"Due date: {due_date}")
print()

# Check if date is in the past
test_date = date(2020, 1, 1)
is_past = test_date < date.today()
print(f"Is {test_date} in the past? {is_past}")
