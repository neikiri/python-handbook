# Chapter 02: Installation and Setup — Exercises

## Overview

These exercises guide you through setting up Python on your computer, verifying the installation, choosing an editor, and writing your first programs. By the end, you will have a working Python environment and the confidence to run code.

---

## How to Use These Exercises

- Follow each exercise in order.
- Use your terminal (Command Prompt, PowerShell, or Terminal depending on your OS).
- If you get stuck, re-read the relevant handbook section or check the hints at the end.

---

## Warm-up Exercises

### Exercise 1: Verify Your Python Installation

Open a terminal and run these commands one at a time. Write down the output for each.

```bash
python --version
```

```bash
python3 --version
```

```bash
pip --version
```

**Expected behavior:** At least one of the first two commands should print a version number starting with `3.10` or higher. The `pip` command should also work.

**What to do if it fails:** Re-read the installation section for your operating system in the handbook.

---

### Exercise 2: Explore the Python REPL

Open a terminal and type `python3` (or `python` on Windows). You should see the `>>>` prompt.

Try these expressions one at a time:

```python
>>> 2 + 2
>>> "hello" + " world"
>>> len("Python")
>>> 10 / 3
>>> 10 // 3
>>> 2 ** 8
```

Write down the output for each. Then exit the REPL:

```python
>>> exit()
```

**Expected behavior:** Each expression should produce a result immediately.

---

### Exercise 3: Create Your First Python File

1. Create a folder called `python-learning` on your computer.
2. Open your code editor (VS Code, PyCharm, or Thonny).
3. Create a new file called `hello.py` in the `python-learning` folder.
4. Type this code:

```python
print("Hello, Python!")
```

5. Save the file.
6. Open a terminal, navigate to the `python-learning` folder, and run:

```bash
python hello.py
```

**Expected output:**

```text
Hello, Python!
```

---

## Practice Exercises

### Exercise 4: Run a Script with User Input

Create a file called `greet.py` in your `python-learning` folder:

```python
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python.")
```

Run it:

```bash
python greet.py
```

Type your name when prompted. The program should greet you by name.

**Expected output:**

```text
What is your name? Alice
Hello, Alice! Welcome to Python.
```

---

### Exercise 5: Understand the Python Interpreter

Create a file called `check_python.py`:

```python
import sys

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Platform: {sys.platform}")
```

Run it:

```bash
python check_python.py
```

Write down the output. This tells you exactly which Python is running.

**Expected behavior:** The output shows your Python version, the path to the interpreter, and your operating system.

---

### Exercise 6: Use the REPL for Quick Calculations

Open the REPL and use it to solve these problems. Write down your answers.

1. What is 15 × 23?
2. What is 100 ÷ 7 (float division)?
3. What is 100 ÷ 7 (integer division)?
4. What is 2 to the power of 10?
5. What is the remainder when 100 is divided by 7?

**Hint:** Use the operators `+`, `-`, `*`, `/`, `//`, `%`, and `**`.

---

### Exercise 7: Explore Your Editor's Run Button

If you are using VS Code or PyCharm:

1. Open `hello.py` in your editor.
2. Look for a "Run" button (usually a green triangle or play icon).
3. Click it.
4. The output should appear in a terminal panel at the bottom.

If you are using Thonny, click the green "Run" button in the toolbar.

**Expected behavior:** The program runs and prints output without you typing a command in the terminal.

---

## Challenge Exercises

### Challenge 1: Create a Multi-Step Program

Create a file called `calculator.py` that:

1. Asks the user for two numbers
2. Asks the user which operation they want: `+`, `-`, `*`, or `/`
3. Performs the operation
4. Prints the result

Example run:

```text
Enter first number: 10
Enter second number: 3
Enter operation (+, -, *, /): /
10 / 3 = 3.3333333333333335
```

**Hint:** Use `input()` to get user input and `float()` to convert strings to numbers.

---

### Challenge 2: Explore pip and Install a Package

1. Open a terminal and run:

```bash
pip list
```

This shows all installed packages. Write down 5 packages you see.

2. Install the `requests` package:

```bash
pip install requests
```

3. Run `pip list` again and verify that `requests` appears in the list.

4. Create a file called `test_requests.py`:

```python
import requests

response = requests.get("https://httpbin.org/get")
print(f"Status code: {response.status_code}")
```

5. Run it:

```bash
python test_requests.py
```

**Expected output:** The status code should be `200`.

**Note:** This requires an internet connection. If it fails, that is okay — you will learn more about packages in Chapter 15.

---

### Challenge 3: Set Up Your Project Folder Structure

Create a folder structure for your learning:

```text
python-learning/
    chapter-02/
        hello.py
        greet.py
        check_python.py
        calculator.py
    chapter-03/
        (empty for now)
    chapter-04/
        (empty for now)
```

Move your files into the appropriate folders. This organization will help you stay organized as you work through the handbook.

---

### Challenge 4: Understand Virtual Environments (Preview)

This is optional and advanced. If you are curious:

1. Read the "Virtual Environments: A Brief Introduction" section in the handbook.
2. Create a virtual environment in your `python-learning` folder:

```bash
python3 -m venv .venv
```

3. Activate it:

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

**On Windows (Command Prompt):**

```bash
.venv\Scripts\activate.bat
```

**On Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

4. Your prompt should change to show `(.venv)` at the beginning.

5. Install a package:

```bash
pip install requests
```

6. Deactivate when done:

```bash
deactivate
```

**Note:** You do not need to do this for the exercises in this handbook. It is just a preview of a best practice you will use in Chapter 15.

---

## Hints

**"python: command not found"** → Try `python3` instead. On macOS and Linux, the command is usually `python3`.

**"pip: command not found"** → Try `pip3` instead.

**Editor not running code** → Make sure you saved the file first. Most editors require you to save before running.

**REPL not starting** → Make sure Python is installed and on your PATH. Re-read the installation section for your OS.

**Virtual environment not activating** → Make sure you are in the correct folder and using the right activation command for your OS.

---

## What to Review If You Get Stuck

- **Installation issues** → Handbook section 2.3 (Windows), 2.4 (macOS), or 2.5 (Linux)
- **Verifying installation** → Handbook section 2.6
- **The Python REPL** → Handbook section 2.7
- **Choosing an editor** → Handbook section 2.8
- **Creating your first file** → Handbook section 2.9
- **Using pip** → Handbook section 2.10

---

## Key Takeaways

After completing these exercises, you should be able to:

- Verify that Python is installed and working on your computer
- Use the Python REPL for quick experiments
- Create and run Python files from the terminal
- Use your code editor to write and run Python programs
- Understand which Python interpreter is running
- Know where to find help when something goes wrong
