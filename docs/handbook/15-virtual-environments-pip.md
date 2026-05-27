# Chapter 15: Virtual Environments and pip

## 1. Overview

When you install a Python package with `pip install requests`, it lands in
your system-wide Python installation. That works fine for a single project,
but the moment you have two projects that need different versions of the same
library — or you want to share your project with someone else and guarantee
they get exactly the same dependencies — the global approach breaks down.

**Virtual environments** solve this by giving each project its own isolated
Python environment: its own copy of pip, its own installed packages, and no
interference with anything else on your machine. They are a fundamental part
of everyday Python work, and learning to use them early will save you a lot of
confusion later.

This chapter covers everything you need to go from a bare Python installation
to a fully reproducible project environment.

---

## 2. What You Will Learn

- Why virtual environments exist and why you should always use them
- Creating a virtual environment with `python -m venv`
- Activating and deactivating environments on Windows, macOS, and Linux
- Installing, upgrading, and removing packages with `pip`
- Listing installed packages with `pip list` and `pip freeze`
- Generating a `requirements.txt` file
- Recreating an environment from `requirements.txt`
- Pinning package versions for reproducibility
- Keeping pip itself up to date
- What to add to `.gitignore`
- A brief look at modern tooling (uv, Poetry) as a next step

---

## 3. Core Concepts

### 3.1 Why Virtual Environments Exist

Python packages are installed into a specific location on your filesystem.
Without virtual environments, every package goes into the same global
location. This creates two problems.

**Version conflicts.** Project A needs `requests==2.28.0` and Project B needs
`requests==2.31.0`. You cannot have both installed globally at the same time.
Upgrading for one project breaks the other.

**Reproducibility.** When you share your project, the other person needs to
know exactly which packages to install. If you have been installing things
globally over months, there is no clean record of what your project actually
needs.

A virtual environment is a self-contained directory that holds:

- A copy of (or a symlink to) the Python interpreter
- Its own `pip`
- Its own `site-packages` directory where installed packages live

Each project gets its own environment. Packages installed in one environment
are invisible to all others.

---

### 3.2 Creating a Virtual Environment

Python 3.3+ ships with the `venv` module in the standard library. No
installation required.

```bash
python -m venv venv
```

This creates a directory called `venv` in your current folder. The name
`venv` is a convention — you can call it anything, but `venv` and `.venv` are
the two most common choices.

```text
my-project/
    venv/               ← the virtual environment lives here
        bin/            ← (macOS/Linux) Python, pip, activate script
        Scripts/        ← (Windows) Python, pip, activate script
        lib/
            python3.x/
                site-packages/   ← installed packages go here
    main.py
    requirements.txt
```

The `venv` directory is generated — you never edit it by hand, and you never
commit it to version control.

#### Specifying a Python version

If you have multiple Python versions installed, pass the interpreter you want:

```bash
python3.11 -m venv venv
python3.12 -m venv venv
```

On Windows you may need to use the `py` launcher:

```bash
py -3.11 -m venv venv
```

---

### 3.3 Activating the Environment

Creating the environment does not automatically use it. You need to
**activate** it, which adjusts your shell's `PATH` so that `python` and `pip`
refer to the environment's copies rather than the system ones.

#### macOS and Linux

```bash
source venv/bin/activate
```

#### Windows (Command Prompt)

```bash
venv\Scripts\activate
```

#### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

> **Note for PowerShell users:** If you see an error about execution policy,
> run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
> once to allow local scripts to run.

After activation, your prompt changes to show the environment name:

```text
(venv) $
```

Now `python` and `pip` point to the environment:

```bash
which python        # macOS/Linux: .../my-project/venv/bin/python
where python        # Windows:     ...\my-project\venv\Scripts\python.exe
```

Everything you install with `pip` from this point goes into the environment,
not the global Python installation.

---

### 3.4 Deactivating the Environment

When you are done working on the project, deactivate the environment to return
to your normal shell:

```bash
deactivate
```

Your prompt returns to normal and `python` / `pip` point back to the system
installation.

You do not need to deactivate before switching to another project — you can
just activate a different environment and it will replace the current one.

---

### 3.5 Installing Packages with pip

With the environment active, install packages using `pip install`:

```bash
pip install requests
```

```text
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 1.2 MB/s eta 0:00:00
Collecting charset-normalizer<4,>=2 (from requests)
  ...
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1
```

pip automatically installs any packages that `requests` depends on
(its **dependencies**).

#### Installing a specific version

```bash
pip install requests==2.31.0
```

#### Installing multiple packages at once

```bash
pip install requests flask pytest
```

#### Installing a minimum version

```bash
pip install "requests>=2.28"
```

#### Upgrading an already-installed package

```bash
pip install --upgrade requests
```

#### Uninstalling a package

```bash
pip uninstall requests
```

pip will ask for confirmation before removing the package.

---

### 3.6 Listing Installed Packages

#### `pip list`

Shows all installed packages in a readable table:

```bash
pip list
```

```text
Package            Version
------------------ ---------
certifi            2024.2.2
charset-normalizer 3.3.2
idna               3.6
pip                24.0
requests           2.31.0
urllib3            2.2.1
```

#### `pip freeze`

Shows installed packages in a format suitable for a requirements file:

```bash
pip freeze
```

```text
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

Note that `pip freeze` does not include `pip` itself. It only lists packages
that were installed into the environment (not the tools that come with it).

#### Checking a single package

```bash
pip show requests
```

```text
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
License: Apache 2.0
Location: .../venv/lib/python3.11/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:
```

---

### 3.7 The `requirements.txt` File

A `requirements.txt` file is a plain text list of packages (and their
versions) that your project needs. It is the standard way to record and share
dependencies.

#### Generating `requirements.txt`

```bash
pip freeze > requirements.txt
```

This redirects the output of `pip freeze` into a file. The result looks like:

```text
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

Run this command whenever you add or upgrade a package so the file stays
up to date.

#### Installing from `requirements.txt`

When someone else clones your project (or when you set it up on a new
machine), they recreate the environment like this:

```bash
python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

The `-r` flag tells pip to read the file and install everything listed in it.
This gives them exactly the same package versions you used.

---

### 3.8 Pinning Versions

Pinning means specifying an exact version number in `requirements.txt` using
`==`. This is what `pip freeze` produces automatically.

```text
requests==2.31.0
flask==3.0.2
pytest==8.1.1
```

**Why pin?** If you write `requests` without a version, pip installs the
latest version available. That is fine today, but six months from now the
latest version might have breaking changes. Pinning ensures that anyone who
installs your requirements gets the exact same versions you tested with.

**Direct vs. transitive dependencies.** Your project directly depends on
`requests`. But `requests` itself depends on `certifi`, `charset-normalizer`,
`idna`, and `urllib3`. These are **transitive dependencies** — you did not
ask for them, but they are required. `pip freeze` captures all of them,
which is why the file is longer than just the packages you explicitly
installed.

Some teams prefer to keep two files:

- `requirements.in` — only the packages you directly depend on, with loose
  version constraints
- `requirements.txt` — the full pinned output from `pip freeze`, used for
  reproducible installs

Tools like `pip-tools` can manage this workflow, but for most beginner
projects a single `requirements.txt` from `pip freeze` is sufficient.

---

### 3.9 Upgrading pip

pip itself is a package and can become outdated. You may see a warning like:

```text
WARNING: You are using pip version 23.0; however, version 24.0 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

Upgrade pip inside the active environment:

```bash
python -m pip install --upgrade pip
```

Using `python -m pip` (rather than just `pip`) ensures you are upgrading the
pip that belongs to the current environment, not some other one on your
system.

---

### 3.10 Keeping `venv/` Out of Version Control

The `venv/` directory is generated from `requirements.txt`. It is large,
platform-specific, and contains no source code you wrote. Never commit it to
git.

Add it to your `.gitignore`:

```text
# .gitignore
venv/
.venv/
```

Both `venv/` and `.venv/` are common names — add both to be safe. GitHub's
default Python `.gitignore` template already includes these entries, so if
you initialize a repository with the Python template you are covered.

What you **do** commit:

- `requirements.txt` — so others can recreate the environment
- Your source code
- Configuration files (`pyproject.toml`, `setup.cfg`, etc.)

What you **do not** commit:

- `venv/` or `.venv/`
- `__pycache__/` directories
- `.pyc` files

---

## 4. Practical Examples

### 4.1 Starting a New Project from Scratch

Here is the complete workflow for starting a new project:

```bash
# 1. Create the project directory
mkdir my-project
cd my-project

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate          # macOS/Linux
# venv\Scripts\activate           # Windows

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install your dependencies
pip install requests

# 6. Write your code
# ... (create main.py, etc.)

# 7. Save your dependencies
pip freeze > requirements.txt

# 8. Initialize git and add .gitignore
git init
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .
git commit -m "Initial commit"
```

---

### 4.2 A Simple Script Using an Installed Package

With `requests` installed in the active environment:

```python
# main.py

import requests


def get_public_ip() -> str:
    """Return the machine's public IP address."""
    response = requests.get("https://api.ipify.org?format=json", timeout=5)
    response.raise_for_status()
    return response.json()["ip"]


def main() -> None:
    ip = get_public_ip()
    print(f"Your public IP address is: {ip}")


if __name__ == "__main__":
    main()
```

```bash
python main.py
```

```text
Your public IP address is: 203.0.113.42
```

If you try to run this script without activating the environment (or without
installing `requests`), you get:

```text
ModuleNotFoundError: No module named 'requests'
```

That error is the clearest sign that either the environment is not active or
the package was not installed.

---

### 4.3 Cloning a Project and Recreating the Environment

Imagine a colleague shares their project with you. The repository contains
source code and a `requirements.txt` but no `venv/` directory (correctly).

```bash
# 1. Clone the repository
git clone https://github.com/example/their-project.git
cd their-project

# 2. Create a fresh virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate          # macOS/Linux
# venv\Scripts\activate           # Windows

# 4. Install all dependencies from the requirements file
pip install -r requirements.txt

# 5. Run the project
python main.py
```

Because `requirements.txt` pins exact versions, you get the same environment
your colleague used.

---

### 4.4 Adding a New Dependency Mid-Project

You are working on an existing project and decide to add a new package:

```bash
# Make sure the environment is active first
pip install httpx

# Update requirements.txt to include the new package
pip freeze > requirements.txt

# Commit the updated requirements file
git add requirements.txt
git commit -m "Add httpx dependency"
```

Always regenerate `requirements.txt` after installing or upgrading anything.
It is easy to forget, and then your requirements file drifts out of sync with
what is actually installed.

---

### 4.5 Checking What Is Installed vs. What Is Required

Over time, you might install packages for experimentation and forget to remove
them. A quick way to audit:

```bash
# See everything currently installed
pip list

# Compare with what requirements.txt specifies
pip install -r requirements.txt --dry-run
```

Or install `pip-check` for a more detailed report:

```bash
pip install pip-check
pip-check
```

For a clean slate, delete the environment and recreate it from
`requirements.txt`:

```bash
deactivate
rm -rf venv                       # macOS/Linux
# rmdir /s /q venv                # Windows

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This is the nuclear option, but it guarantees your environment matches your
requirements file exactly.

---

### 4.6 A `requirements.txt` for a Real Project

Here is what a realistic `requirements.txt` might look like for a small web
scraping project:

```text
beautifulsoup4==4.12.3
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
lxml==5.1.0
requests==2.31.0
soupsieve==2.5
urllib3==2.2.1
```

The project directly uses `requests` and `beautifulsoup4`. Everything else is
a transitive dependency that pip installed automatically. All versions are
pinned so the project is reproducible.

---

### 4.7 Multiple Environments for the Same Project

You might want separate environments for different purposes:

```bash
# Development environment (includes testing and linting tools)
python -m venv venv-dev
source venv-dev/bin/activate
pip install requests pytest ruff mypy
pip freeze > requirements-dev.txt

# Production environment (only runtime dependencies)
python -m venv venv-prod
source venv-prod/bin/activate
pip install requests
pip freeze > requirements.txt
```

This pattern keeps your production environment lean. Testing tools like
`pytest` and linters like `ruff` are only needed during development, not when
running the application.

---

## 5. Common Mistakes

### 5.1 Forgetting to Activate the Environment

This is the most common mistake. You create the environment, then install
packages or run your script without activating first. The packages go into
the global Python installation (or you get a `ModuleNotFoundError`).

```bash
# Wrong — environment exists but is not active
python -m venv venv
pip install requests          # installs globally, not into venv!
python main.py                # may fail if requests is not globally installed

# Right — activate first
python -m venv venv
source venv/bin/activate      # (venv) appears in prompt
pip install requests          # installs into venv
python main.py                # works
```

**How to check:** Look at your prompt. If you see `(venv)` at the start, the
environment is active. If not, activate it.

You can also check which Python is being used:

```bash
which python        # macOS/Linux
where python        # Windows
```

If the path points inside your project's `venv/` directory, you are good.

---

### 5.2 Committing `venv/` to Git

The `venv/` directory can contain thousands of files and tens of megabytes of
data. It is platform-specific (a `venv/` created on macOS will not work on
Windows). And it is entirely reproducible from `requirements.txt`.

Committing it to git bloats your repository, causes merge conflicts, and
provides no benefit.

```text
# .gitignore — always include these
venv/
.venv/
```

If you accidentally committed `venv/` already:

```bash
# Remove it from git tracking (but keep the directory locally)
git rm -r --cached venv/
echo "venv/" >> .gitignore
git add .gitignore
git commit -m "Remove venv from version control"
```

---

### 5.3 Not Pinning Versions

Writing `requirements.txt` by hand with unpinned versions is a common
shortcut that causes problems later:

```text
# Fragile — versions are not pinned
requests
flask
pytest
```

Six months from now, `pip install -r requirements.txt` might install newer
versions with breaking changes. Your project stops working and you have no
record of what versions you were using.

Always generate `requirements.txt` with `pip freeze`:

```bash
pip freeze > requirements.txt
```

This captures exact versions for everything, including transitive
dependencies.

---

### 5.4 Installing Packages Globally Instead of in the Environment

If you run `pip install` without an active environment, packages go into your
global Python installation. This pollutes the global environment and defeats
the purpose of virtual environments.

```bash
# Wrong — no environment active
pip install requests            # goes into global Python

# Right — activate first
source venv/bin/activate
pip install requests            # goes into venv
```

A useful habit: if you ever run `pip install` and do not see `(venv)` in your
prompt, stop and activate the environment first.

---

### 5.5 Forgetting to Update `requirements.txt`

After installing a new package, it is easy to forget to regenerate
`requirements.txt`. Your code works locally because the package is installed,
but when someone else clones the project and runs `pip install -r
requirements.txt`, the package is missing.

Make it a habit: every time you run `pip install`, immediately follow it with:

```bash
pip freeze > requirements.txt
```

Some teams add a reminder comment at the top of `requirements.txt`:

```text
# Generated with: pip freeze > requirements.txt
# Regenerate after any pip install or pip uninstall
```

---

### 5.6 Using the Wrong Python to Create the Environment

If you have multiple Python versions installed, make sure you create the
environment with the version your project requires.

```bash
# Check which Python you are using
python --version
python3 --version
python3.11 --version

# Create the environment with a specific version
python3.11 -m venv venv
```

Once the environment is created and activated, `python` inside it always
refers to the version it was created with, regardless of what `python` means
globally.

---

### 5.7 Deleting the Environment and Losing Track of Dependencies

If you delete `venv/` before generating `requirements.txt`, you lose the
record of what was installed. Always generate `requirements.txt` before
deleting an environment.

```bash
# Before deleting, save dependencies
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Save dependencies before cleanup"

# Now safe to delete
deactivate
rm -rf venv
```

---

## 6. Practice Tasks

1. Create a new directory called `practice-env`. Inside it, create a virtual
   environment, activate it, and verify that `python` points to the
   environment by running `which python` (macOS/Linux) or `where python`
   (Windows).

2. With the environment active, install the `requests` package. Run
   `pip list` and `pip show requests` to confirm it is installed. Then run
   `pip freeze` and observe the output.

3. Generate a `requirements.txt` file from the active environment. Open it
   and identify which packages are direct dependencies (ones you installed)
   and which are transitive dependencies (installed automatically).

4. Deactivate the environment, delete the `venv/` directory, create a fresh
   environment, and reinstall everything from `requirements.txt`. Verify the
   same packages are present.

5. Create a `.gitignore` file in `practice-env/` that excludes `venv/`,
   `.venv/`, and `__pycache__/`. Initialize a git repository and confirm that
   `git status` does not show the `venv/` directory.

6. Write a small script `fetch_title.py` that uses `requests` to fetch the
   HTML of `https://example.com` and print the content of the `<title>` tag.
   (Hint: you can find the title with simple string operations — no HTML
   parser needed for this exercise.) Run it from within the active
   environment.

7. Install `pytest` into the environment. Write a test file `test_utils.py`
   with a simple function and a test for it. Run `pytest` and confirm it
   passes. Then regenerate `requirements.txt` to include `pytest`.

8. Create two separate environments in the same project directory:
   `venv-dev` (with `pytest` and `requests`) and `venv-prod` (with only
   `requests`). Generate separate `requirements.txt` and
   `requirements-dev.txt` files. Compare them.

---

## 7. Key Takeaways

- A virtual environment is an isolated Python installation for a single
  project. Always use one — never install project packages globally.
- Create an environment with `python -m venv venv`. Activate it with
  `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate`
  (Windows). Deactivate with `deactivate`.
- Install packages with `pip install <package>`. Uninstall with
  `pip uninstall <package>`.
- `pip list` shows installed packages in a readable table. `pip freeze`
  shows them in `name==version` format, ready for a requirements file.
- Generate `requirements.txt` with `pip freeze > requirements.txt`. Recreate
  an environment from it with `pip install -r requirements.txt`.
- Always pin versions in `requirements.txt`. Use `pip freeze` to generate
  the file — do not write it by hand.
- Never commit `venv/` to git. Add it to `.gitignore`. Commit
  `requirements.txt` instead.
- Upgrade pip itself with `python -m pip install --upgrade pip`.
- The most common mistake is forgetting to activate the environment before
  running `pip install` or your script.

---

### Further Reading

- [venv - Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

### What's Next

Ready to continue? Head to the next chapter: **Object-Oriented Programming**.

→ [Chapter 16 — Object-Oriented Programming](16-oop.md)

*See also:*
- [Exercise](../exercises/15-virtual-environments-pip.md)
- [Solution](../solutions/15-virtual-environments-pip.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
