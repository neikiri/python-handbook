# Chapter 23: Where to Go Next — Exercises

## Overview

These exercises help you explore advanced topics and decide your next learning path. By the end, you will have a clear direction for your Python journey.

---

## How to Use These Exercises

- Create a folder called `chapter-23` in your `python-learning` directory.
- Explore each topic with the provided examples.
- Choose areas that interest you most.
- Use the resources to continue learning.

---

## Warm-up Exercises

### Exercise 1: Explore Web Development

Create a file called `web_intro.py`:

```python
"""Introduction to web development concepts."""

# Simple HTTP server
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        html = """
        <html>
        <body>
        <h1>Hello, World!</h1>
        <p>This is a simple web server.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

# To run: uncomment below and visit http://localhost:8000
# server = HTTPServer(("localhost", 8000), SimpleHandler)
# print("Server running on http://localhost:8000")
# server.serve_forever()

print("Web development concepts:")
print("- HTTP requests and responses")
print("- HTML, CSS, JavaScript")
print("- Web frameworks: Flask, Django, FastAPI")
print("- Databases: SQL, NoSQL")
print("- APIs: REST, GraphQL")
```

---

### Exercise 2: Explore Data Science

Create a file called `data_science_intro.py`:

```python
"""Introduction to data science concepts."""

# Simulate data analysis without external libraries
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Basic statistics
mean = sum(data) / len(data)
median = sorted(data)[len(data) // 2]
minimum = min(data)
maximum = max(data)

print("Data Science Concepts:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Min: {minimum}")
print(f"Max: {maximum}")

# Variance
variance = sum((x - mean) ** 2 for x in data) / len(data)
print(f"Variance: {variance}")

# Standard deviation
import math
std_dev = math.sqrt(variance)
print(f"Standard deviation: {std_dev}")

print("\nData science tools:")
print("- NumPy: numerical computing")
print("- Pandas: data manipulation")
print("- Matplotlib: visualization")
print("- Scikit-learn: machine learning")
print("- TensorFlow/PyTorch: deep learning")
```

---

### Exercise 3: Explore Automation

Create a file called `automation_intro.py`:

```python
"""Introduction to automation concepts."""

import os
import shutil
from pathlib import Path
from datetime import datetime

# File automation example
def backup_files(source_dir, backup_dir):
    """Backup files to a directory."""
    source = Path(source_dir)
    backup = Path(backup_dir)
    backup.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = backup / backup_name
    
    if source.exists():
        shutil.copytree(source, backup_path)
        print(f"Backed up to {backup_path}")
    else:
        print(f"Source directory not found: {source}")

# Task scheduling example
def schedule_task(task_name, interval_seconds):
    """Schedule a task to run periodically."""
    print(f"Task '{task_name}' scheduled to run every {interval_seconds} seconds")
    print("(In production, use APScheduler or cron jobs)")

print("Automation concepts:")
print("- File operations")
print("- Task scheduling")
print("- System administration")
print("- Web scraping")
print("- Email automation")
print("- Database maintenance")

print("\nAutomation tools:")
print("- APScheduler: task scheduling")
print("- Selenium: web automation")
print("- Requests: HTTP requests")
print("- BeautifulSoup: web scraping")
```

---

### Exercise 4: Explore Game Development

Create a file called `game_intro.py`:

```python
"""Introduction to game development concepts."""

# Simple game mechanics
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.score = 0
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
    
    def add_score(self, points):
        self.score += points
    
    def is_alive(self):
        return self.health > 0

# Example game loop
def simple_game():
    player = Player("Hero")
    
    print(f"Welcome, {player.name}!")
    print(f"Health: {player.health}, Score: {player.score}")
    
    # Simulate game events
    player.take_damage(10)
    print(f"Took damage! Health: {player.health}")
    
    player.add_score(100)
    print(f"Gained points! Score: {player.score}")
    
    player.heal(20)
    print(f"Healed! Health: {player.health}")

print("Game Development Concepts:")
print("- Game loops")
print("- Collision detection")
print("- Physics simulation")
print("- Graphics rendering")
print("- Sound and music")
print("- Game state management")

print("\nGame development libraries:")
print("- Pygame: 2D games")
print("- Arcade: 2D games (modern)")
print("- Panda3D: 3D games")
print("- Godot: game engine (uses GDScript)")

# Uncomment to run
# simple_game()
```

---

## Practice Exercises

### Exercise 5: Explore Async Programming

Create a file called `async_intro.py`:

```python
"""Introduction to async programming."""

import asyncio

async def fetch_data(name, delay):
    """Simulate fetching data."""
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Fetched {name}")
    return f"Data from {name}"

async def main():
    """Run async tasks concurrently."""
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data("API 1", 1),
        fetch_data("API 2", 2),
        fetch_data("API 3", 1.5),
    )
    
    for result in results:
        print(f"Result: {result}")

print("Async Programming Concepts:")
print("- Coroutines")
print("- async/await")
print("- Event loops")
print("- Concurrent execution")
print("- Non-blocking I/O")

print("\nAsync libraries:")
print("- asyncio: built-in async")
print("- aiohttp: async HTTP")
print("- FastAPI: async web framework")

# Uncomment to run
# asyncio.run(main())
```

---

### Exercise 6: Explore Decorators and Metaprogramming

Create a file called `decorators_intro.py`:

```python
"""Introduction to decorators and metaprogramming."""

import time
from functools import wraps

# Timing decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Logging decorator
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Use decorators
@timer
@logger
def slow_function(n):
    """Simulate a slow function."""
    time.sleep(0.1)
    return n * 2

print("Decorators and Metaprogramming Concepts:")
print("- Function decorators")
print("- Class decorators")
print("- Metaclasses")
print("- Descriptors")
print("- Context managers")

print("\nExample:")
# Uncomment to run
# result = slow_function(5)
```

---

### Exercise 7: Explore Design Patterns

Create a file called `patterns_intro.py`:

```python
"""Introduction to design patterns."""

# Singleton pattern
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal: {animal_type}")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Observer pattern
class Subject:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Observer received: {message}")

print("Design Patterns:")
print("- Singleton: single instance")
print("- Factory: object creation")
print("- Observer: event handling")
print("- Strategy: algorithm selection")
print("- Decorator: behavior modification")
print("- Adapter: interface compatibility")

print("\nExample:")
# Uncomment to run
# db1 = Database()
# db2 = Database()
# print(f"Same instance: {db1 is db2}")
```

---

## Challenge Exercises

### Challenge 1: Create a Learning Plan

Create a file called `learning_plan.md`:

```markdown
# My Python Learning Plan

## Completed
- [x] Basics (syntax, types, operators)
- [x] Collections (lists, dicts, sets)
- [x] Functions and comprehensions
- [x] OOP (classes, inheritance)
- [x] File I/O and data handling
- [x] Testing and code quality

## Next Steps (Choose Your Path)

### Path 1: Web Development
- [ ] Learn Flask or FastAPI
- [ ] Understand HTTP and REST APIs
- [ ] Learn HTML/CSS/JavaScript basics
- [ ] Build a simple web application
- [ ] Deploy to a server

### Path 2: Data Science
- [ ] Learn NumPy and Pandas
- [ ] Learn Matplotlib for visualization
- [ ] Learn Scikit-learn for ML
- [ ] Work with real datasets
- [ ] Build a data analysis project

### Path 3: Automation
- [ ] Learn web scraping (BeautifulSoup)
- [ ] Learn task scheduling (APScheduler)
- [ ] Automate file operations
- [ ] Build automation scripts
- [ ] Deploy to production

### Path 4: Game Development
- [ ] Learn Pygame
- [ ] Build simple 2D games
- [ ] Learn game design principles
- [ ] Create a complete game
- [ ] Publish on itch.io

## Resources
- Official Python docs: https://docs.python.org
- Real Python: https://realpython.com
- Stack Overflow: https://stackoverflow.com
- GitHub: https://github.com
```

---

### Challenge 2: Build a Portfolio Project

Create a file called `portfolio_project.py`:

```python
"""Template for a portfolio project."""

class PortfolioProject:
    """
    A portfolio project should demonstrate:
    1. Problem-solving skills
    2. Code organization
    3. Testing and quality
    4. Documentation
    5. Real-world applicability
    """
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.features = []
        self.technologies = []
    
    def add_feature(self, feature):
        self.features.append(feature)
    
    def add_technology(self, tech):
        self.technologies.append(tech)
    
    def get_summary(self):
        return f"""
Project: {self.name}
Description: {self.description}

Features:
{chr(10).join(f"  - {f}" for f in self.features)}

Technologies:
{chr(10).join(f"  - {t}" for t in self.technologies)}
"""

# Example portfolio project
project = PortfolioProject(
    "Task Manager",
    "A CLI application for managing tasks with persistence"
)

project.add_feature("Create, read, update, delete tasks")
project.add_feature("Save tasks to JSON file")
project.add_feature("Filter tasks by status")
project.add_feature("Command-line interface")

project.add_technology("Python 3.10+")
project.add_technology("argparse for CLI")
project.add_technology("JSON for persistence")
project.add_technology("pytest for testing")

print(project.get_summary())

print("\nPortfolio Project Ideas:")
print("1. Task Manager (CLI)")
print("2. Budget Tracker (CLI)")
print("3. Web Scraper (automation)")
print("4. Data Analysis Tool (data science)")
print("5. Simple Web App (web development)")
print("6. Game (game development)")
```

---

## Hints

**Overwhelmed by choices** → Start with one path that interests you most. You can explore others later.

**Don't know where to start** → Build a project that solves a real problem you have.

**Feeling stuck** → Join communities, ask questions, and learn from others.

**Want to contribute** → Start with open-source projects on GitHub.

---

## What to Review If You Get Stuck

- **Learning resources** → Handbook section 2.1
- **Career paths** → Handbook section 2.2
- **Community** → Handbook section 2.3
- **Continuous learning** → Handbook section 2.4

---

## Key Takeaways

After completing these exercises, you should:

- Understand multiple Python specializations
- Know your learning interests
- Have a clear next step
- Be ready to dive deeper
- Know where to find resources
- Be part of the Python community
- Continue learning and growing

---

## Final Thoughts

Congratulations on completing the Python Handbook! You now have a solid foundation in Python programming. The journey doesn't end here—it's just beginning. Choose a path that excites you, build projects, contribute to open source, and never stop learning.

Remember:
- **Practice regularly** → Code every day
- **Build projects** → Apply what you learn
- **Read others' code** → Learn from the community
- **Ask questions** → No question is too basic
- **Share your knowledge** → Help others learn
- **Stay curious** → Python is vast and evolving

Good luck on your Python journey!

