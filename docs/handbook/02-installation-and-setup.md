# Chapter 02: Installation and Setup

## Overview

Before you can write and run Python code, you need Python installed on your computer and a place to write your programs. This chapter walks you through every step: downloading and installing Python 3.10+, verifying the installation, choosing a code editor, writing your first Python file, and understanding a few essential tools like the Python REPL and pip.

The process takes about 15–30 minutes depending on your operating system and internet speed. By the end you will have a working Python environment and a running "Hello, World!" program.

---

## What You Will Learn

- How to install Python 3.10+ on Windows, macOS, and Linux
- How to verify that Python is installed and working
- What the Python REPL is and how to use it
- How to choose and set up a code editor
- How to create and run your first Python file
- The difference between the `python` and `python3` commands
- What pip is and how to use it for basic package management
- What pyenv is and when you might need it
- How to organize your project folders as a learner

---

## Core Concepts

### Python Versions

Python has two major version lines: Python 2 and Python 3. Python 2 reached end-of-life in January 2020 and is no longer maintained. This handbook uses **Python 3.10 or later**. When you install Python, make sure you are installing a 3.10+ release.

You can always check the current stable release at [python.org/downloads](https://www.python.org/downloads/).

---

### Installing Python on Windows

#### Option 1: The Official Installer (Recommended)

1. Open your browser and go to [python.org/downloads](https://www.python.org/downloads/).
2. Click the **Download Python 3.x.x** button. The site detects your OS automatically.
3. Run the downloaded `.exe` installer.
4. On the first screen of the installer, check the box that says **"Add Python to PATH"** before clicking Install Now.

   > This step is critical. If you skip it, Windows will not know where to find Python when you type `python` in the terminal.

5. Click **Install Now** and wait for the installation to finish.
6. Click **Close** when done.

#### Option 2: winget (Windows Package Manager)

If you prefer the command line, Windows 10 and 11 include `winget`. Open PowerShell or Command Prompt and run:

```bash
winget install Python.Python.3.12
```

Replace `3.12` with the version you want. You can search available versions with:

```bash
winget search Python.Python
```

After installation via winget, Python is added to your PATH automatically.

#### Verifying on Windows

Open **Command Prompt** or **PowerShell** and run:

```bash
python --version
```

You should see output like:

```text
Python 3.12.3
```

If you see `Python 2.x.x`, your system is pointing to an old Python 2 installation. Try `python3 --version` instead. If neither works, the PATH was not set correctly — re-run the installer and make sure the "Add to PATH" checkbox is checked.

---

### Installing Python on macOS

macOS ships with a system Python, but it is often Python 2.7 or an older Python 3 version that Apple uses internally. You should **not** use the system Python for your own projects. Install a fresh copy instead.

#### Option 1: Homebrew (Recommended)

[Homebrew](https://brew.sh) is a package manager for macOS. If you do not have it installed, open **Terminal** and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions. Once Homebrew is installed, install Python:

```bash
brew install python
```

Homebrew installs the latest stable Python 3 release and makes it available as `python3`.

#### Option 2: Official Installer

You can also download the macOS `.pkg` installer from [python.org/downloads](https://www.python.org/downloads/) and run it like any other macOS application.

#### Verifying on macOS

Open **Terminal** and run:

```bash
python3 --version
```

You should see:

```text
Python 3.12.3
```

On macOS, the command is almost always `python3`, not `python`. The `python` command may still point to the system Python 2 or may not exist at all. Always use `python3` on macOS unless you have explicitly configured otherwise.

#### A Note on the System Python

The Python that ships with macOS lives at `/usr/bin/python3` and is managed by Apple. Do not install packages into it with pip. Always use a Homebrew-installed Python or a virtual environment (covered in Chapter 15).

---

### Installing Python on Linux

Most Linux distributions either include Python 3 or make it easy to install through the system package manager.

#### Ubuntu and Debian-based Distributions

Check if Python 3 is already installed:

```bash
python3 --version
```

If it is not installed, or if the version is older than 3.10, install it with apt:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

To install a specific version (for example, 3.12) on Ubuntu, you can use the deadsnakes PPA:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev
```

#### Fedora and RHEL-based Distributions

```bash
sudo dnf install python3 python3-pip
```

For a specific version:

```bash
sudo dnf install python3.12
```

#### Verifying on Linux

```bash
python3 --version
```

```text
Python 3.12.3
```

#### pyenv: Managing Multiple Python Versions on Linux (and macOS)

If you need to switch between multiple Python versions — for example, one project requires 3.10 and another requires 3.12 — consider using **pyenv**.

pyenv lets you install and switch between Python versions without touching your system Python. Installation instructions are at [github.com/pyenv/pyenv](https://github.com/pyenv/pyenv).

A quick example of what pyenv looks like in use:

```bash
# Install a specific Python version
pyenv install 3.12.3

# Set it as the global default
pyenv global 3.12.3

# Check the active version
python --version
```

pyenv is not required for beginners, but it is worth knowing about. You will not need it for this handbook.

---

### Verifying Your Installation

Regardless of your operating system, the verification steps are the same in principle. Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS and Linux) and run one or both of these commands:

```bash
python --version
```

```bash
python3 --version
```

One of them should print a version number starting with `3.10` or higher. If both commands fail, Python is not on your PATH — revisit the installation steps for your OS.

You can also check where Python is installed:

```bash
which python3
```

On macOS and Linux this prints the path to the Python executable, for example:

```text
/usr/local/bin/python3
```

On Windows, use `where` instead:

```bash
where python
```

---

### The `python` vs `python3` Command

This is a common source of confusion for beginners.

- On **Windows**, the installer typically sets up `python` (and `python3` as an alias). After a fresh install with "Add to PATH" checked, both usually work.
- On **macOS**, `python` may point to Python 2 or may not exist. Always use `python3`.
- On **Linux**, the situation varies by distribution. Many modern distros only provide `python3`. Some provide both.

The safest habit is to always type `python3` when you are on macOS or Linux, and to check which version `python` points to on Windows.

Throughout this handbook, examples use `python` in command-line instructions. If `python` does not work on your system, substitute `python3`.

---

### Understanding the Python Interpreter

When you run a Python file, a program called the **Python interpreter** reads your code and executes it. Understanding what the interpreter is — even at a high level — helps you make sense of error messages and the overall workflow.

#### What the Interpreter Does

The interpreter works in two stages:

1. **Compilation to bytecode.** Python first compiles your source code (the `.py` file you wrote) into an intermediate format called *bytecode*. Bytecode is a lower-level representation of your program that is not human-readable but is faster for the interpreter to process. You will sometimes see `.pyc` files appear in a `__pycache__` folder next to your `.py` files — those are the cached bytecode files. You never need to create or edit them manually.

2. **Execution by the Python Virtual Machine (PVM).** The bytecode is then run by the Python Virtual Machine, which is the engine that actually carries out your instructions — doing arithmetic, calling functions, reading files, and so on.

This all happens automatically and invisibly every time you run `python hello.py`. From your perspective, you write code and it runs. The two-stage process is an implementation detail you do not need to think about day to day.

#### CPython: The Standard Interpreter

The interpreter you download from [python.org](https://www.python.org/) is called **CPython**. It is the reference implementation of Python, written in C. When people say "Python", they almost always mean CPython. There are other implementations — PyPy (focused on speed), Jython (runs on the Java Virtual Machine), MicroPython (for microcontrollers) — but CPython is what you will use throughout this handbook and in virtually all real-world Python work.

#### Interactive vs. Script Mode

The Python interpreter has two modes:

- **Interactive mode (the REPL).** When you run `python3` with no arguments, the interpreter starts in interactive mode. It reads one expression or statement at a time, evaluates it, and prints the result. This is the `>>>` prompt you saw earlier.

- **Script mode.** When you run `python3 hello.py`, the interpreter reads the entire file, compiles it, and executes it from top to bottom. There is no `>>>` prompt — the program just runs.

Both modes use the same interpreter. The difference is only in how you feed code to it.

#### Checking the Interpreter from Inside Python

You can inspect the interpreter itself using the `sys` module:

```python
>>> import sys
>>> sys.version
'3.12.3 (main, Apr  9 2024, 08:09:14) [GCC 13.2.0]'
>>> sys.executable
'/usr/local/bin/python3'
>>> sys.platform
'linux'
```

- `sys.version` shows the full version string including the build date and compiler.
- `sys.executable` shows the full path to the Python interpreter binary that is currently running.
- `sys.platform` identifies the operating system: `'linux'`, `'darwin'` (macOS), or `'win32'` (Windows).

This is useful when you have multiple Python versions installed and want to confirm which one is actually running.

#### The Shebang Line (macOS and Linux)

On macOS and Linux, you can make a Python script executable so you can run it directly without typing `python3` first. Add this as the very first line of your script:

```python
#!/usr/bin/env python3
```

This is called a **shebang line**. It tells the operating system which interpreter to use when running the file. After adding it, make the file executable:

```bash
chmod +x hello.py
./hello.py
```

You do not need this for normal learning. It is a convenience for scripts you run frequently from the terminal.

---

### The Python REPL

REPL stands for **Read-Eval-Print Loop**. It is an interactive Python session where you type one line of Python at a time and see the result immediately. It is useful for experimenting, testing small ideas, and learning.

#### Launching the REPL

Open your terminal and type:

```bash
python3
```

You will see something like this:

```text
Python 3.12.3 (main, Apr  9 2024, 08:09:14) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` prompt means Python is waiting for your input.

#### Basic REPL Usage

Type any Python expression and press Enter:

```python
>>> 2 + 2
4
>>> "hello"
'hello'
>>> 10 / 3
3.3333333333333335
```

You can assign variables:

```python
>>> name = "Alice"
>>> name
'Alice'
>>> len(name)
5
```

You can call built-in functions:

```python
>>> print("Hello, World!")
Hello, World!
>>> type(42)
<class 'int'>
>>> type("hello")
<class 'str'>
```

Multi-line code (like a loop) works too. Python shows `...` to indicate it is waiting for more input:

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```

Press Enter on a blank `...` line to execute the block.

#### Exiting the REPL

Type `exit()` or `quit()` and press Enter:

```python
>>> exit()
```

On macOS and Linux you can also press `Ctrl+D`. On Windows, press `Ctrl+Z` then Enter.

#### When to Use the REPL

The REPL is great for:

- Quickly testing a small piece of code
- Checking what a function returns
- Exploring a module you are not familiar with
- Doing quick calculations

It is not the right place to write programs you want to save. For that, you write a `.py` file.

---

### Choosing a Code Editor

A code editor is where you write and save your Python files. You do not need anything special — Python files are plain text — but a good editor makes the experience much better with features like syntax highlighting, error detection, and the ability to run code directly.

Here are the main options for beginners.

#### VS Code (Recommended for Most Beginners)

[Visual Studio Code](https://code.visualstudio.com/) is a free, open-source editor made by Microsoft. It is lightweight, fast, and has excellent Python support through an extension.

**Installing VS Code:**

1. Go to [code.visualstudio.com](https://code.visualstudio.com/) and download the installer for your OS.
2. Run the installer and follow the prompts.

**Installing the Python Extension:**

1. Open VS Code.
2. Click the **Extensions** icon in the left sidebar (it looks like four squares).
3. Search for **Python** in the search box.
4. Click **Install** on the extension published by Microsoft.

VS Code will now highlight Python syntax, show errors as you type, and let you run Python files directly.

**Running a Python File in VS Code:**

1. Open a `.py` file.
2. Click the **Run** button (a triangle/play icon) in the top-right corner of the editor.
3. The output appears in the integrated terminal at the bottom.

Alternatively, right-click anywhere in the file and choose **Run Python File in Terminal**.

**Selecting the Python Interpreter:**

If you have multiple Python versions installed, VS Code needs to know which one to use.

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
2. Type **Python: Select Interpreter** and press Enter.
3. Choose the Python version you installed.

#### PyCharm Community Edition

[PyCharm](https://www.jetbrains.com/pycharm/) is a full-featured Python IDE made by JetBrains. The Community Edition is free. It has more Python-specific features than VS Code out of the box, but it is heavier and takes longer to start up.

PyCharm is a good choice if you want an IDE that is entirely focused on Python and does not require any extension setup. For beginners, VS Code is usually simpler to get started with.

Download it at [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/) and choose **Community**.

#### Thonny

[Thonny](https://thonny.org/) is a Python IDE designed specifically for beginners. It comes with Python bundled, so you do not even need to install Python separately. It has a simple interface and a built-in debugger that shows you exactly what Python is doing step by step.

Thonny is an excellent choice if you are an absolute beginner and want the simplest possible setup. It is less suitable once you start working on larger projects.

Download it at [thonny.org](https://thonny.org/).

#### Useful VS Code Extensions

The Python extension from Microsoft is the essential one, but a few others are worth installing once you are comfortable:

- **Pylance** — a fast, feature-rich language server that improves autocomplete, type checking, and code navigation. It is often installed automatically alongside the Python extension.
- **Ruff** — a linter and formatter that catches style issues and common errors as you type. Useful once you start writing more than a few lines.
- **GitLens** — enhances VS Code's built-in Git support. Not Python-specific, but helpful once you start using version control.

You do not need any of these to get started. Install them when you feel ready for more tooling.

#### Terminal Editors (vim, nano, emacs)

You can write Python in any text editor, including terminal-based editors like vim, nano, or emacs. These are powerful tools used by experienced developers, but they have a steep learning curve. If you are new to programming, do not start here. Use VS Code or Thonny instead.

#### Summary: Which Editor Should You Choose?

| Editor | Best for | Notes |
|---|---|---|
| VS Code | Most beginners | Free, great Python extension, widely used |
| PyCharm Community | Python-focused learners | More features, heavier |
| Thonny | Absolute beginners | Simplest setup, bundled Python |
| vim/nano/emacs | Experienced terminal users | Not recommended for beginners |

---

### Creating Your First Python File

Now that Python is installed and you have an editor, it is time to write your first program.

#### Step 1: Create a Project Folder

Create a folder on your computer where you will keep your Python files. A good location is your home directory or Documents folder.

```bash
mkdir python-projects
cd python-projects
```

#### Step 2: Create hello.py

Open your editor and create a new file called `hello.py`. Type the following:

```python
print("Hello, World!")
```

Save the file.

#### Step 3: Run the File

Open your terminal, navigate to the folder where you saved `hello.py`, and run:

```bash
python hello.py
```

You should see:

```text
Hello, World!
```

That is your first Python program running. The `print()` function outputs text to the terminal. The text inside the parentheses and quotes is called a **string**.

If you get an error like `python: command not found`, try `python3 hello.py` instead.

#### Step 4: Try a Slightly More Interesting Program

Edit `hello.py` to ask for your name:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

Run it again:

```bash
python hello.py
```

```text
What is your name? Alice
Hello, Alice!
```

The `input()` function pauses the program and waits for you to type something. The `f"..."` syntax is called an **f-string** — it lets you embed variables directly inside a string. Both of these will be covered in detail in later chapters.

---

### pip: Python's Package Installer

Python comes with a large standard library, but the Python community has also published hundreds of thousands of additional packages that you can install and use in your programs. **pip** is the tool that downloads and installs those packages.

#### Checking pip

pip is included with Python 3.4+. Verify it is available:

```bash
pip --version
```

Or on macOS/Linux:

```bash
pip3 --version
```

You should see something like:

```text
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

#### Installing a Package

To install a package, use `pip install` followed by the package name:

```bash
pip install requests
```

This downloads and installs the `requests` package (a popular library for making HTTP requests).

#### Listing Installed Packages

```bash
pip list
```

This shows all packages currently installed in your Python environment.

#### A Word of Caution

When you install packages with pip, they go into your global Python installation by default. This can cause problems when different projects need different versions of the same package. The solution is **virtual environments**, which are covered in detail in Chapter 15. For now, just know that pip exists and that you will learn the proper way to use it later.

---

### Recommended Project Folder Structure

As a learner, you do not need a complex folder structure. But having some organization from the start will save you confusion later.

Here is a simple structure that works well for learning:

```text
python-projects/
    hello.py
    calculator.py
    chapter-03/
        exercises.py
    chapter-04/
        exercises.py
    my-first-project/
        main.py
        README.md
```

A few guidelines:

- Keep each chapter's exercises in their own folder.
- When you start a small project, give it its own folder with a `main.py` file.
- Use lowercase names with hyphens for folder names (e.g., `my-project`, not `MyProject` or `my_project`).
- Avoid spaces in file and folder names — they cause problems in the terminal.

As you progress, you will learn about more structured layouts with `src/`, `tests/`, and configuration files. For now, keep it simple.

---

### Virtual Environments: A Brief Introduction

When you install a package with pip, it goes into your global Python installation. That works fine when you are just learning, but it creates a problem as soon as you have multiple projects: Project A might need version 1.0 of a library, while Project B needs version 2.0. If both are installed globally, they conflict.

The solution is a **virtual environment** — an isolated Python environment that belongs to a single project. Each virtual environment has its own copy of pip and its own set of installed packages, completely separate from every other environment and from the global Python installation.

Here is what creating and using a virtual environment looks like, just so you have seen it:

```bash
# Create a virtual environment called .venv in the current folder
python3 -m venv .venv

# Activate it (macOS / Linux)
source .venv/bin/activate

# Activate it (Windows Command Prompt)
.venv\Scripts\activate.bat

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Your prompt changes to show the active environment
(.venv) $

# Now pip installs go into .venv, not the global Python
pip install requests

# Deactivate when you are done
deactivate
```

You do not need to master this right now. The important thing to know is:

- Virtual environments exist to keep project dependencies isolated.
- You should use one for every project once you start working on real code.
- Chapter 15 covers virtual environments in full detail, including how to manage them with pip and how to share your project's dependencies with others.

For the exercises in this handbook, you can work without a virtual environment. Just be aware that the proper habit — one you will build in Chapter 15 — is to always activate a virtual environment before installing packages.

---

## Practical Examples

### Example 1: Checking Your Python Installation

Open your terminal and run these commands one at a time. The output tells you exactly what is installed and where.

```bash
python3 --version
```

```text
Python 3.12.3
```

```bash
which python3
```

```text
/usr/local/bin/python3
```

```bash
pip3 --version
```

```text
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

If all three commands produce output without errors, your installation is working correctly.

---

### Example 2: A Quick REPL Session

Launch the REPL and try these expressions:

```bash
python3
```

```python
>>> 100 / 4
25.0
>>> "Python" + " " + "3"
'Python 3'
>>> 2 ** 10
1024
>>> len("hello world")
11
>>> "hello".upper()
'HELLO'
>>> sorted([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]
>>> exit()
```

Each line is evaluated immediately and the result is printed. This is a great way to explore Python's built-in functions and operators without writing a full program.

---

### Example 3: Your First Real Python File

Create a file called `greeting.py`:

```python
# greeting.py
# A simple program that greets the user

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"In 10 years, you will be {int(age) + 10} years old.")
```

Run it:

```bash
python greeting.py
```

```text
Enter your name: Bob
Enter your age: 25
Hello, Bob!
You are 25 years old.
In 10 years, you will be 35 years old.
```

Notice the `int(age) + 10` part. The `input()` function always returns a string, so you need to convert it to an integer with `int()` before doing math. This is a concept you will explore in depth in Chapter 05.

---

### Example 4: Using pip to Install and Use a Package

This example shows the basic pip workflow. You do not need to follow along right now — it is just to show you what it looks like.

```bash
# Install the requests library
pip install requests
```

```text
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Installing collected packages: requests
Successfully installed requests-2.31.0
```

```python
# make_request.py
import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.json())
```

```bash
python make_request.py
```

```text
200
{'args': {}, 'headers': {...}, 'url': 'https://httpbin.org/get'}
```

The `import requests` line loads the package you installed. Chapter 14 covers imports in detail, and Chapter 15 covers pip and virtual environments properly.

---

### Example 5: Exploring the Python REPL for Learning

The REPL is especially useful when you want to understand how something works. Here is an example of using it to explore strings:

```python
>>> word = "python"
>>> word.upper()
'PYTHON'
>>> word.capitalize()
'Python'
>>> word.replace("p", "P")
'Python'
>>> word[0]
'p'
>>> word[-1]
'n'
>>> word[0:3]
'pyt'
>>> len(word)
6
```

You can also use `help()` to read documentation for any function or object:

```python
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

Press `q` to exit the help viewer.

---

### Example 6: Inspecting the Interpreter

This example shows how to use the `sys` module to confirm which Python is running. It is useful when you have multiple versions installed and want to be sure you are using the right one.

Open the REPL:

```bash
python3
```

Then run:

```python
>>> import sys
>>> sys.version
'3.12.3 (main, Apr  9 2024, 08:09:14) [GCC 13.2.0]'
>>> sys.executable
'/usr/local/bin/python3'
>>> sys.platform
'linux'
>>> sys.version_info
sys.version_info(major=3, minor=12, micro=3, releaselevel='final', serial=0)
>>> sys.version_info >= (3, 10)
True
```

The last line is a practical check: it returns `True` if the running Python is 3.10 or newer. You can use this in a script to guard against running on an old version:

```python
# version_check.py
import sys

if sys.version_info < (3, 10):
    print("This script requires Python 3.10 or later.")
    print(f"You are running Python {sys.version_info.major}.{sys.version_info.minor}.")
    sys.exit(1)

print("Python version is OK.")
print(f"Running: {sys.version}")
```

Run it:

```bash
python version_check.py
```

```text
Python version is OK.
Running: 3.12.3 (main, Apr  9 2024, 08:09:14) [GCC 13.2.0]
```

---

### Example 7: Running the Same Code Three Ways

This example shows the three ways you will interact with Python throughout this handbook, using the same simple calculation as the subject.

**Way 1: The REPL**

```bash
python3
```

```python
>>> width = 8
>>> height = 5
>>> area = width * height
>>> print(f"Area: {area}")
Area: 40
```

Quick, interactive, throwaway. Good for checking an idea.

**Way 2: A Script File**

Create `area.py`:

```python
# area.py
width = 8
height = 5
area = width * height
print(f"Area: {area}")
```

Run it:

```bash
python area.py
```

```text
Area: 40
```

Saved, repeatable, shareable. This is how you write real programs.

**Way 3: VS Code's Integrated Terminal**

Open `area.py` in VS Code. Press the Run button (▶) in the top-right corner. The integrated terminal at the bottom of the window opens and runs the file automatically:

```text
Area: 40
```

All three approaches produce the same result. The REPL is for exploration, script files are for programs you want to keep, and VS Code's run button is a convenient shortcut for running the file you are currently editing.

---

## Common Mistakes

### Mistake 1: Not Checking "Add to PATH" on Windows

**What happens:** You install Python on Windows but forget to check the "Add Python to PATH" box. When you open Command Prompt and type `python`, you get:

```text
'python' is not recognized as an internal or external command
```

**Fix:** Re-run the Python installer. On the first screen, check the "Add Python to PATH" box, then click "Repair" or "Modify". Alternatively, add Python to your PATH manually through Windows System Properties → Environment Variables.

---

### Mistake 2: Using the System Python on macOS

**What happens:** You run `pip install somepackage` on macOS and get a permission error, or you accidentally modify Apple's system Python.

**Fix:** Always install Python via Homebrew (`brew install python`) and use `python3` and `pip3`. Never run `sudo pip install` — if pip asks for sudo, something is wrong with your setup.

---

### Mistake 3: Confusing `python` and `python3`

**What happens:** You type `python` and get Python 2.7, or you get a "command not found" error.

**Fix:** On macOS and Linux, always use `python3`. On Windows, check which version `python` points to by running `python --version`. If it shows Python 2, use `python3` instead.

---

### Mistake 4: Running Python from the Wrong Directory

**What happens:** You create `hello.py` in your Documents folder, but your terminal is in a different directory. You run `python hello.py` and get:

```text
python: can't open file 'hello.py': [Errno 2] No such file or directory
```

**Fix:** Use `cd` to navigate to the folder where your file is saved before running it.

```bash
cd ~/Documents/python-projects
python hello.py
```

Or provide the full path to the file:

```bash
python ~/Documents/python-projects/hello.py
```

---

### Mistake 5: Saving the File Without the .py Extension

**What happens:** You save your file as `hello` or `hello.txt` instead of `hello.py`. Python can still run it if you specify the full filename, but your editor will not apply Python syntax highlighting, and some tools will not recognize it as Python.

**Fix:** Always save Python files with the `.py` extension.

---

### Mistake 6: Mixing Tabs and Spaces

**What happens:** You write a multi-line block (like a loop or function) and mix tabs and spaces for indentation. Python raises a `TabError` or `IndentationError`.

```text
TabError: inconsistent use of tabs and spaces in indentation
```

**Fix:** Use spaces only (4 spaces per indent level is the Python convention). Configure your editor to insert spaces when you press Tab. In VS Code, this is the default for Python files.

---

### Mistake 7: Installing Packages Globally Instead of in a Virtual Environment

**What happens:** You install packages with `pip install` directly, and over time your global Python environment becomes cluttered with packages from different projects. Eventually, two projects need different versions of the same package and they conflict.

**Fix:** Use virtual environments. This is covered in Chapter 15. For now, just be aware that `pip install` without a virtual environment installs packages globally.

---

### Mistake 8: Closing the REPL and Losing Your Work

**What happens:** You write several lines of code in the REPL, then close the terminal. Everything is gone.

**Fix:** The REPL is for experimentation only. If you write something you want to keep, save it to a `.py` file. You can copy code from the REPL into a file, or just write the file directly in your editor.

---

## Practice Tasks

These tasks help you confirm that your environment is set up correctly and that you are comfortable with the basic workflow.

**Task 1: Verify Your Installation**

Open your terminal and run the following commands. Write down the output of each one.

```bash
python3 --version
pip3 --version
which python3
```

If any command fails, revisit the installation section for your operating system.

---

**Task 2: Explore the REPL**

Launch the Python REPL and try the following:

1. Calculate `17 * 6`
2. Calculate `2 ** 8` (2 to the power of 8)
3. Type `"hello" * 3` and observe the result
4. Type `type(3.14)` and observe the result
5. Type `help(print)` and read the documentation
6. Exit the REPL

---

**Task 3: Write and Run hello.py**

1. Create a folder called `python-projects` in your home directory or Documents folder.
2. Inside it, create a file called `hello.py`.
3. Write a `print()` statement that outputs your name.
4. Run the file from the terminal with `python hello.py`.

---

**Task 4: Write a Simple Input Program**

Create a file called `about_me.py` with the following content:

```python
name = input("What is your name? ")
city = input("What city are you from? ")
print(f"Nice to meet you, {name} from {city}!")
```

Run it and make sure it works correctly.

---

**Task 5: Install and Check pip**

Run the following command to see what packages are already installed in your Python environment:

```bash
pip list
```

You do not need to install anything yet. Just confirm that pip is working and note what is already there.

---

**Task 6: Set Up VS Code (Optional but Recommended)**

If you have not already:

1. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
2. Install the Python extension from Microsoft.
3. Open your `hello.py` file in VS Code.
4. Run it using the Run button or by right-clicking and choosing "Run Python File in Terminal".
5. Confirm the output appears in the integrated terminal.

---

**Task 7: Explore Your Python Installation**

In the REPL, run the following to see where Python is installed and what version of pip you have:

```python
>>> import sys
>>> sys.version
'3.12.3 (main, Apr  9 2024, 08:09:14) [GCC 13.2.0]'
>>> sys.executable
'/usr/local/bin/python3'
>>> import pip
>>> pip.__version__
'24.0'
```

The `sys` module is part of Python's standard library and gives you information about the Python interpreter itself.

---

**Task 8: Write a Version Check Script**

Create a file called `check_version.py` with the following content:

```python
import sys

print(f"Python version: {sys.version}")
print(f"Interpreter path: {sys.executable}")
print(f"Platform: {sys.platform}")

if sys.version_info >= (3, 10):
    print("Good — Python 3.10+ is required and you have it.")
else:
    print("Warning: Python 3.10 or later is required.")
```

Run it from the terminal:

```bash
python check_version.py
```

Confirm that the version shown is 3.10 or higher. If it is not, revisit the installation steps for your operating system.

---

**Task 9: Create a Virtual Environment (Preview)**

This task gives you a first look at virtual environments before Chapter 15 covers them in depth. You do not need to understand every detail yet — just follow the steps and observe what happens.

1. Open your terminal and navigate to your `python-projects` folder.
2. Create a virtual environment:

```bash
python3 -m venv .venv
```

3. Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows Command Prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

4. Notice that your terminal prompt now shows `(.venv)` at the start.
5. Run `pip list` to see the packages in this isolated environment (there will be very few).
6. Deactivate the environment:

```bash
deactivate
```

7. Run `pip list` again and compare the output. The global environment has more packages.

You have just created, activated, and deactivated your first virtual environment. Chapter 15 explains everything about how and why to use them.

---

## Key Takeaways

- **Install Python 3.10 or later.** Python 2 is obsolete. Always check the version number after installing.

- **On Windows**, use the official installer from python.org and check "Add Python to PATH". The `winget` command is a convenient alternative.

- **On macOS**, install Python via Homebrew with `brew install python`. Do not use the system Python that comes with macOS.

- **On Linux**, use your distribution's package manager (`apt` or `dnf`). Python 3 is often already installed.

- **Verify your installation** by running `python3 --version` in the terminal. You should see a version number starting with 3.10 or higher.

- **The `python` vs `python3` command** depends on your OS. On macOS and Linux, always use `python3`. On Windows, `python` usually works after a fresh install.

- **The Python REPL** is an interactive session where you can type Python code and see results immediately. Launch it with `python3`. Exit with `exit()` or `Ctrl+D`.

- **VS Code with the Python extension** is the recommended editor for most beginners. Thonny is a good alternative for absolute beginners.

- **Python files use the `.py` extension.** Run them from the terminal with `python hello.py`.

- **pip** is Python's package installer. Use `pip install package-name` to install packages and `pip list` to see what is installed. Chapter 15 covers pip and virtual environments in full.

- **Virtual environments** isolate a project's packages from the global Python installation. Create one with `python3 -m venv .venv` and activate it before installing packages. Chapter 15 covers this in full.

- **pyenv** lets you manage multiple Python versions on the same machine. You do not need it as a beginner, but it is worth knowing about.

- **Keep your project files organized** in a dedicated folder. Use lowercase names with hyphens for folders and files.

- **The Python interpreter** (CPython) compiles your `.py` files to bytecode and executes them. You can inspect it with `import sys` and check `sys.version`, `sys.executable`, and `sys.platform`.

---

### Further Reading

- [Python Downloads](https://www.python.org/downloads/)
- [Installing Python](https://docs.python.org/3/using/index.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [PyPI - Python Package Index](https://pypi.org/)

### What's Next

Ready to continue? Head to the next chapter: **Running Python**.

→ [Chapter 03 — Running Python](03-running-python.md)

*See also:*
- [Exercise](../exercises/02-installation-and-setup.md)
- [Solution](../solutions/02-installation-and-setup.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
