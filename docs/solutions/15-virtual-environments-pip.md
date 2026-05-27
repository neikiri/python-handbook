# Solutions 15: Virtual Environments and pip

## Overview

Chapter 15 exercises cover creating and activating virtual environments, installing and managing packages with pip, creating `requirements.txt` files, and setting up project environments. This chapter is mostly command-line work rather than Python code, so solutions focus on explaining the commands and the reasoning behind each step.

---

## Notes Before Checking Solutions

Virtual environments are not optional — they are essential. Without them, every project on your machine shares the same Python installation, and installing a package for one project can break another. Always create a virtual environment before starting a new project.

---

## Warm-up Exercise Solutions

### Exercise 1: Create and Activate a Virtual Environment

**On Windows:**

```bash
python -m venv myenv
myenv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv myenv
source myenv/bin/activate
```

After activation, your prompt shows `(myenv)`. Verify:

```bash
python --version
which python   # macOS/Linux: shows path inside myenv
where python   # Windows: shows path inside myenv
```

Deactivate:

```bash
deactivate
```

**Why `python -m venv` instead of `virtualenv`?** `venv` is built into Python 3.3+ and requires no installation. `virtualenv` is a third-party tool with more features, but `venv` is sufficient for most projects.

**What does activation do?** It prepends the virtual environment's `bin` (or `Scripts` on Windows) directory to your `PATH`. This means `python` and `pip` now refer to the virtual environment's copies, not the system-wide ones.

---

### Exercise 2: Install and List Packages

```bash
# Install a package
pip install requests

# List installed packages
pip list

# Show details about a package
pip show requests

# Install a specific version
pip install requests==2.28.0

# Uninstall a package
pip uninstall requests
```

**`pip show requests`** displays the version, location, dependencies, and other metadata. Useful for checking what is installed and where.

**Always activate your virtual environment before running `pip install`.** If you forget, you install into the system Python, which affects all projects.

---

### Exercise 3: Create a requirements.txt File

`requirements.txt`:

```
requests==2.28.0
flask==2.2.0
pytest==7.1.0
```

Install from file:

```bash
pip install -r requirements.txt
```

Generate from current environment:

```bash
pip freeze > requirements.txt
```

**Pin exact versions** (`==2.28.0`) in `requirements.txt` to ensure reproducible installs. If you use `>=2.28.0`, a future `pip install -r requirements.txt` might install a newer version that breaks your code.

**`pip freeze`** outputs all installed packages with exact versions. This is useful for capturing the current state of an environment, but it includes transitive dependencies (packages your packages depend on). For a cleaner file, list only your direct dependencies manually.

---

### Exercise 4: Use Different Python Versions

```bash
# Check available versions
python --version
python3 --version
python3.10 --version

# Create environment with specific version
python3.10 -m venv myenv_py310
```

**Why use different Python versions?** Some projects require a specific Python version. A library might not support the latest Python yet, or you might be maintaining code that must run on an older version.

**`pyenv`** (macOS/Linux) and **`py` launcher** (Windows) make it easier to manage multiple Python versions. They are worth learning once you are comfortable with the basics.

---

## Practice Exercise Solutions

### Exercise 5: Set Up a Project Environment

```bash
# Create project structure
mkdir my_project
cd my_project

# Create virtual environment
python -m venv myenv

# Activate
myenv\Scripts\activate      # Windows
source myenv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the script
python src/main.py
```

`requirements.txt`:

```
requests==2.28.0
python-dotenv==0.20.0
```

`src/main.py`:

```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

response = requests.get("https://api.github.com")
print(f"Status: {response.status_code}")
```

**`python-dotenv`** loads environment variables from a `.env` file. This is the standard way to manage secrets (API keys, passwords) without hardcoding them in source code. Add `.env` to `.gitignore` so secrets are never committed.

---

### Exercise 6: Manage Development Dependencies

`requirements.txt` (production only):

```
requests==2.28.0
```

`requirements-dev.txt` (development tools):

```
-r requirements.txt
pytest==7.1.0
black==22.6.0
flake8==4.0.1
```

```bash
pip install -r requirements-dev.txt

# Format code
black src/

# Check style
flake8 src/

# Run tests
pytest tests/
```

**Separate production and development dependencies.** Production servers should not have `pytest` and `black` installed — they are only needed during development. The `-r requirements.txt` line in `requirements-dev.txt` includes the production dependencies automatically.

---

### Exercise 7: Troubleshoot Environment Issues

`test_env.py`:

```python
import sys
import os

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Virtual environment: {sys.prefix}")

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
```

**`sys.executable`** shows the full path to the Python interpreter being used. If it points inside your virtual environment directory, the environment is active. If it points to the system Python, you forgot to activate.

**`sys.prefix`** shows the root of the Python installation. For a virtual environment, this is the `myenv` directory.

---

## Challenge Exercise Solutions

### Challenge 1: Create Multiple Environments

```bash
# Web development environment
python -m venv web_env
source web_env/bin/activate
pip install flask flask-sqlalchemy
deactivate

# Data analysis environment
python -m venv data_env
source data_env/bin/activate
pip install pandas numpy matplotlib
deactivate

# Testing environment
python -m venv test_env
source test_env/bin/activate
pip install pytest pytest-cov
deactivate
```

**Each project gets its own environment.** This prevents version conflicts between projects. If Project A needs `requests==2.27.0` and Project B needs `requests==2.28.0`, they can coexist in separate environments.

---

### Challenge 2: Upgrade and Downgrade Packages

```bash
# Check for outdated packages
pip list --outdated

# Upgrade a specific package
pip install --upgrade requests

# Downgrade to a specific version
pip install requests==2.27.0

# Force reinstall
pip install requests==2.28.0 --force-reinstall
```

**`pip check`** verifies that all installed packages have compatible dependencies. Run it after upgrading to catch conflicts.

---

### Challenge 3: Create a Project Template

`.gitignore`:

```
myenv/
__pycache__/
*.pyc
.pytest_cache/
.coverage
dist/
build/
*.egg-info/
.env
```

**Always add `myenv/` (or whatever you name your virtual environment) to `.gitignore`.** Virtual environments are large, machine-specific, and can be recreated from `requirements.txt`. Never commit them to version control.

**Also add `.env`** to `.gitignore` to prevent secrets from being committed.

---

## Common Mistakes

**Running `pip install` without activating the environment.** This installs into the system Python. Always check that `(myenv)` appears in your prompt before running `pip`.

**Committing the virtual environment to git.** The `myenv/` directory can be hundreds of megabytes. Add it to `.gitignore` and share `requirements.txt` instead.

**Not pinning versions in `requirements.txt`.** Using `requests` without a version means different developers (or CI servers) might install different versions, leading to inconsistent behavior.

**Using `pip freeze` for the main `requirements.txt`.** `pip freeze` includes all transitive dependencies, making the file hard to maintain. List only your direct dependencies manually, with pinned versions.

---

## What to Review Next
- Review the matching handbook chapter if any exercise felt difficult.
- Revisit the matching exercise set and try solving it again without looking at the solution.
- Continue with the next handbook chapter: [Chapter 16 - OOP](../handbook/16-oop.md)
