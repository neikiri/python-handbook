# Chapter 15: Virtual Environments and pip — Exercises

## Overview

These exercises help you manage Python environments and dependencies using virtual environments and pip. By the end, you will confidently set up isolated development environments and manage project dependencies.

---

## How to Use These Exercises

- Create a folder called `chapter-15` in your `python-learning` directory.
- Follow the exercises to create and manage virtual environments.
- Run commands in your terminal or command prompt.
- Experiment with variations to deepen your understanding.

---

## Warm-up Exercises

### Exercise 1: Create and Activate a Virtual Environment

**On Windows (Command Prompt):**

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
myenv\Scripts\activate

# You should see (myenv) in your prompt
```

**On macOS/Linux:**

```bash
# Create a virtual environment
python3 -m venv myenv

# Activate it
source myenv/bin/activate

# You should see (myenv) in your prompt
```

Once activated, verify the Python version:

```bash
python --version
which python  # or 'where python' on Windows
```

Deactivate the environment:

```bash
deactivate
```

---

### Exercise 2: Install and List Packages

Activate your virtual environment, then:

```bash
# Install a package
pip install requests

# List installed packages
pip list

# Show details about a package
pip show requests

# Install a specific version
pip install requests==2.28.0

# Install multiple packages
pip install flask django

# Uninstall a package
pip uninstall requests
```

---

### Exercise 3: Create a requirements.txt File

Create a file called `requirements.txt`:

```
requests==2.28.0
flask==2.2.0
pytest==7.1.0
```

Install all requirements:

```bash
pip install -r requirements.txt
```

Generate requirements from current environment:

```bash
pip freeze > requirements.txt
```

---

### Exercise 4: Use Different Python Versions

Check available Python versions:

```bash
python --version
python3 --version
python3.10 --version  # if available
```

Create a virtual environment with a specific version:

```bash
# On Windows
python -m venv myenv_py310

# On macOS/Linux
python3.10 -m venv myenv_py310
```

---

## Practice Exercises

### Exercise 5: Set Up a Project Environment

Create a project structure:

```
my_project/
  myenv/
  src/
    main.py
  requirements.txt
  README.md
```

Create `requirements.txt`:

```
requests==2.28.0
python-dotenv==0.20.0
```

Create `src/main.py`:

```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Example: fetch data from an API
response = requests.get("https://api.github.com")
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
```

Set up the environment:

```bash
# Create virtual environment
python -m venv myenv

# Activate it
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the script
python src/main.py
```

---

### Exercise 6: Manage Development Dependencies

Create `requirements-dev.txt`:

```
# Production dependencies
requests==2.28.0

# Development dependencies
pytest==7.1.0
black==22.6.0
flake8==4.0.1
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Use the tools:

```bash
# Format code with black
black src/

# Check code style with flake8
flake8 src/

# Run tests with pytest
pytest tests/
```

---

### Exercise 7: Troubleshoot Environment Issues

Create a test script `test_env.py`:

```python
import sys
import os

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Virtual environment: {sys.prefix}")
print(f"Python path: {sys.path}")

# Check if packages are installed
try:
    import requests
    print("✓ requests is installed")
except ImportError:
    print("✗ requests is NOT installed")

try:
    import flask
    print("✓ flask is installed")
except ImportError:
    print("✗ flask is NOT installed")

# List installed packages
import pkg_resources
print("\nInstalled packages:")
for dist in pkg_resources.working_set:
    print(f"  {dist.project_name}=={dist.version}")
```

Run it to diagnose environment issues:

```bash
python test_env.py
```

---

## Challenge Exercises

### Challenge 1: Create Multiple Environments

Create separate environments for different projects:

```bash
# Project 1: Web development
python -m venv web_env
web_env\Scripts\activate  # Windows
pip install flask flask-sqlalchemy

# Project 2: Data analysis
python -m venv data_env
data_env\Scripts\activate  # Windows
pip install pandas numpy matplotlib

# Project 3: Testing
python -m venv test_env
test_env\Scripts\activate  # Windows
pip install pytest pytest-cov
```

Switch between environments by activating/deactivating.

---

### Challenge 2: Upgrade and Downgrade Packages

```bash
# Check for outdated packages
pip list --outdated

# Upgrade a specific package
pip install --upgrade requests

# Upgrade all packages
pip install --upgrade -r requirements.txt

# Downgrade a package
pip install requests==2.27.0

# Pin a package to a specific version
pip install requests==2.28.0 --force-reinstall
```

---

### Challenge 3: Create a Project Template

Create a template directory structure:

```
project_template/
  myenv/
  src/
    __init__.py
    main.py
  tests/
    __init__.py
    test_main.py
  requirements.txt
  requirements-dev.txt
  README.md
  .gitignore
```

Create `.gitignore`:

```
myenv/
__pycache__/
*.pyc
.pytest_cache/
.coverage
dist/
build/
*.egg-info/
```

Create `README.md`:

```markdown
# My Project

## Setup

1. Create virtual environment:
   ```bash
   python -m venv myenv
   ```

2. Activate it:
   ```bash
   myenv\Scripts\activate  # Windows
   source myenv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Development

Install dev dependencies:
```bash
pip install -r requirements-dev.txt
```

Run tests:
```bash
pytest
```

Format code:
```bash
black src/
```
```

---

## Hints

**"python: command not found"** → Python may not be in your PATH. Try `python3` instead, or reinstall Python.

**"No module named X"** → The package is not installed. Use `pip install X` or check that the virtual environment is activated.

**Virtual environment not activating** → Check the path and ensure you're using the correct activation script for your OS.

**Conflicting dependencies** → Use `pip install --upgrade pip` and check for version conflicts with `pip check`.

---

## What to Review If You Get Stuck

- **Virtual environments** → Handbook section 2.1
- **pip basics** → Handbook section 2.2
- **requirements.txt** → Handbook section 2.3
- **Managing dependencies** → Handbook section 2.4
- **Troubleshooting** → Handbook section 2.5

---

## Key Takeaways

After completing these exercises, you should be able to:

- Create and activate virtual environments
- Install and manage packages with pip
- Create and use requirements.txt files
- Manage development dependencies
- Troubleshoot environment issues
- Use multiple environments for different projects
- Upgrade and downgrade packages
- Set up project templates

