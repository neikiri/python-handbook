# Chapter 01: Introduction to Python

## 1. Overview

Every programming language has a personality. Python's personality is clarity. It was designed
from the start to be readable, practical, and approachable -- not just for computer scientists,
but for anyone who wants to get things done with code.

This chapter introduces Python: what it is, where it came from, why so many people use it, and
what you can realistically expect to build after working through this handbook. You will not write
complex programs yet. The goal here is to understand the landscape before you start walking
through it.

By the end of this chapter you will have a clear mental model of what Python is, why it matters,
and how this handbook will help you learn it. You will also see a handful of short Python snippets
that demonstrate the language's expressiveness -- not to teach syntax, but to give you a feel for
what Python code looks like before you dive into the details.

---

## 2. What You Will Learn

- What Python is and how it works at a high level
- A brief history of Python and why Python 3 is the only version that matters today
- Why Python became one of the most popular programming languages in the world
- What Python is used for in the real world
- Python's design philosophy and what makes it different from other languages
- Where Python is not the right tool
- What this handbook covers and how to use it effectively
- A first look at Python code -- short, motivating examples to show you what the language feels like

---

## 3. Core Concepts

### 3.1 What Is Python?

Python is a **programming language** -- a formal system for giving instructions to a computer.
But that definition applies to hundreds of languages. What makes Python distinctive is a
combination of four properties that work together to make it both powerful and approachable.

**Interpreted**

Most programming languages require you to *compile* your code before running it. Compilation is
a separate step that translates your source code into machine instructions the processor can
execute directly. You write code, run the compiler, fix any errors the compiler finds, and only
then run the resulting program.

Python skips that explicit step. You write code, and Python runs it directly. This makes the
feedback loop fast: write a line, run it, see what happens. There is no compile step to wait for.

Under the hood, Python does compile your code -- but to an intermediate format called *bytecode*,
and it does this automatically, invisibly, every time you run a script. The bytecode is then
executed by the Python interpreter. You never have to think about any of this. From your
perspective, you write code and it runs.

This interpreted nature also means Python is highly interactive. You can open a Python session
in your terminal and type expressions one at a time, seeing the result of each one immediately.
This is called the REPL (Read-Eval-Print Loop), and it is one of the best tools for learning
and experimentation.

**High-level**

"High-level" means Python handles many low-level details for you. You do not manage memory
manually. You do not worry about how many bytes a number takes up in memory. You do not deal
with pointers or memory addresses. Python handles all of that so you can focus on solving the
actual problem.

Compare this to a low-level language like C, where you must explicitly allocate and free memory.
In Python, you create a list, use it, and Python cleans it up when you are done. This is called
*garbage collection*, and Python does it automatically in the background.

The tradeoff is performance. High-level abstractions have overhead. Python programs are generally
slower than equivalent C or C++ programs. For most applications this does not matter -- the
bottleneck is network I/O, database queries, or human reading speed, not raw CPU cycles. But for
performance-critical code, this is a real consideration.

**Dynamically typed**

In some languages, you must declare the type of every variable before using it:

```text
int age = 30;          // Java or C -- you must declare the type
String name = "Alice"; // Java or C -- you must declare the type
```

In Python, you just write:

```python
age = 30
name = "Alice"
```

Python figures out the type from the value you assign. This is called *dynamic typing*. The
variable `age` holds an integer because you assigned an integer to it. If you later assign a
string to `age`, it becomes a string. The variable does not have a fixed type -- the value does.

Dynamic typing makes code shorter and faster to write. The tradeoff is that type errors can
appear at runtime rather than before the program runs. A statically typed language would catch
certain mistakes at compile time; Python will only catch them when that line of code actually
executes.

Later chapters cover how to use *type hints* to annotate your code with type information. Type
hints do not change how Python runs your code, but they enable tools like mypy and your editor
to catch type errors before you run the program. You get the flexibility of dynamic typing with
optional static analysis on top.

**General-purpose**

Python is not specialized for one domain. It is used for web development, data analysis,
automation, scientific computing, machine learning, system administration, game scripting, and
more. The same language that powers a data pipeline at a tech company also runs a simple script
that renames files on your desktop.

This generality is one of Python's greatest strengths. Once you learn Python, you can apply
those skills across many different problem domains without switching languages.

---

### 3.2 A Brief History of Python

Python was created by **Guido van Rossum**, a Dutch programmer working at Centrum Wiskunde &
Informatica (CWI) in the Netherlands. He started working on Python in the late 1980s as a hobby
project during the Christmas holidays, wanting to create a language that improved on ABC -- a
language he had worked on at CWI that had good ideas but significant limitations.

The first public version was released in **1991**. Python 1.0 arrived in 1994. Python 2.0 came
in 2000, introducing important features like list comprehensions and garbage collection
improvements.

**The name**

The name "Python" does not come from the snake. Guido was a fan of the British comedy group
*Monty Python's Flying Circus*, and he wanted a name that was short, slightly irreverent, and
fun. The snake imagery came later and stuck. You will see snake-related names throughout the
Python ecosystem -- the package manager is called pip, the mascot is a snake, and many libraries
use snake-related names.

**Python 2 vs Python 3**

Python went through a major redesign in 2008 with the release of **Python 3.0**. The redesign
fixed several inconsistencies and design mistakes from the original language. The key changes:

- In Python 2, `print` was a statement: `print "Hello"`. In Python 3, it is a function:
  `print("Hello")`.
- In Python 2, dividing two integers always gave an integer: `5 / 2` gave `2`. In Python 3,
  it gives `2.5`. Integer division uses `//`: `5 // 2` gives `2`.
- In Python 2, strings were bytes by default. In Python 3, strings are Unicode by default,
  which is the correct behavior for modern software that handles international text.
- Python 3 cleaned up many inconsistencies in the standard library, renaming modules and
  reorganizing functionality that had grown organically over the years.

These changes were not backward-compatible -- code written for Python 2 would not run on Python 3
without changes. This created a long, awkward transition period where both versions coexisted.
For years, many tutorials, libraries, and production systems were still on Python 2.

That era is over. **Python 2 reached end-of-life on January 1, 2020.** It no longer receives
security updates, bug fixes, or support of any kind. If you encounter Python 2 code in the wild,
treat it as a historical artifact. Do not use it for new work.

This handbook uses **Python 3.10 and later**. All examples, syntax, and features assume Python
3.10+. Python 3.10 introduced structural pattern matching (the `match` statement) and
significantly improved error messages. Python 3.11 and 3.12 brought further performance
improvements and better tracebacks. If you are on an older version, upgrade before continuing.

**Python's growth**

Since Python 3 stabilized, Python's popularity has grown dramatically. As of the mid-2020s, it
consistently ranks as one of the top two or three most popular programming languages in the
world, according to indices like TIOBE and Stack Overflow's annual developer surveys. The rise
of data science and machine learning accelerated this growth significantly -- both fields adopted
Python as their primary language, which brought millions of new users to the ecosystem.

Guido van Rossum served as Python's "Benevolent Dictator For Life" (BDFL) -- the person with
final say on language decisions -- until 2018, when he stepped down. Python is now governed by
the Python Steering Council, a five-person elected body that guides the language's development.

---

### 3.3 Why Python Became Popular

Python did not become popular by accident. Several concrete properties explain why it gained
widespread adoption and continues to grow.

**Readability**

Python code reads closer to plain English than almost any other mainstream language. Consider
this example:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit.startswith("b"):
        print(fruit)
```

Even without knowing Python, you can probably read this: "for each fruit in the list, if the
fruit starts with 'b', print it." That readability is intentional. Python uses indentation to
define structure instead of curly braces, and it avoids a lot of the punctuation that clutters
other languages.

This matters more than it might seem. Code is read far more often than it is written. When you
come back to code you wrote six months ago, or when a colleague reads your code, readability
determines how quickly they can understand it. Python's syntax makes readable code the default.

**Versatility**

The same language works for a one-line script and a million-line application. You can use Python
interactively in a terminal, write standalone scripts, build web applications, analyze data,
automate tasks, and build command-line tools -- all with the same language and the same skills.

This means that learning Python is a durable investment. You are not learning a language that
only works in one context. The skills transfer across domains.

**Batteries included**

Python ships with an extensive standard library. You can work with files, dates, regular
expressions, JSON, CSV, HTTP, email, databases, compression, cryptography, and much more without
installing anything beyond Python itself. This "batteries included" philosophy means you can
accomplish a lot before you ever need a third-party package.

On top of the standard library, the Python Package Index (PyPI) hosts hundreds of thousands of
third-party packages. Whatever you want to do -- parse HTML, send emails, build REST APIs, train
machine learning models, generate PDFs -- there is almost certainly a well-maintained library
for it.

**Community**

Python has a large, active, and generally welcoming community. There are extensive official
docs, thousands of tutorials, active forums (Stack Overflow, Reddit's r/learnpython), and a
culture of writing beginner-friendly documentation. When you get stuck, help is easy to find.

The community also produces a large number of high-quality open-source libraries. Many of the
most important Python libraries -- NumPy, pandas, Django, Flask, requests -- are maintained by
volunteers and funded by foundations or corporate sponsors.

**Low barrier to entry**

You can write a useful Python program in five minutes. The language does not require you to
understand compilers, memory management, or type systems before you can do anything meaningful.
This makes it an excellent first language and a practical tool for non-programmers -- scientists,
analysts, writers, and others who need to automate tasks but are not professional developers.

**Consistency and stability**

Python's core language has been stable for years. Code written for Python 3.6 still runs on
Python 3.12 with minimal changes. The language evolves, but it does not break existing code
carelessly. This stability makes Python a safe investment for long-term projects.

---

### 3.4 Where Python Is Used Today

Python's versatility means it shows up in many different fields today. Here is a realistic
picture of the domains and industries where Python is actually used in practice.

**Web development**

Python powers web applications through frameworks like Django, Flask, and FastAPI. Django is a
full-featured framework that includes an ORM, admin interface, authentication, and much more.
It is used by companies like Instagram, Pinterest, and Disqus. Flask is a lightweight framework
good for smaller applications and APIs -- it gives you the basics and lets you add what you need.
FastAPI is a newer framework focused on building APIs quickly, with automatic documentation and
built-in support for type hints.

Web development with Python typically means writing the server-side logic -- handling requests,
querying databases, returning responses. The frontend (HTML, CSS, JavaScript) is a separate
concern.

**Data science and analysis**

Python is the dominant language for data science. The core libraries are:

- **pandas** -- data manipulation and analysis, working with tabular data
- **NumPy** -- numerical computing, arrays, and mathematical operations
- **Matplotlib** and **seaborn** -- data visualization
- **Jupyter** -- interactive notebooks that mix code, output, and text

Data scientists use Python to clean and transform data, explore datasets, build statistical
models, and communicate findings. Jupyter notebooks are widely used for this kind of exploratory
work.

**Machine learning and AI**

TensorFlow and PyTorch, the two most widely used deep learning frameworks, both have Python as
their primary interface. Scikit-learn provides classical machine learning algorithms --
classification, regression, clustering, dimensionality reduction. Hugging Face's transformers
library has made large language models accessible from Python.

If you want to work in AI or ML, Python is essentially required. The entire ecosystem is built
around it.

**Automation and scripting**

Python excels at automating repetitive tasks: renaming files in bulk, processing spreadsheets,
scraping websites, sending automated emails, interacting with REST APIs, scheduling jobs,
monitoring systems. Many system administrators and DevOps engineers use Python for these tasks
because it is faster to write than shell scripts and more readable than Perl.

The standard library's `os`, `pathlib`, `shutil`, `subprocess`, and `re` modules cover most
automation needs without any third-party dependencies.

**DevOps and infrastructure**

Tools like Ansible (infrastructure automation) and SaltStack are written in Python and
configured with Python or YAML. Many cloud providers -- AWS, Google Cloud, Azure -- offer Python
SDKs for interacting with their services programmatically. Python scripts are common in CI/CD
pipelines and deployment workflows.

**Scientific computing**

Physicists, biologists, economists, and engineers use Python for simulations, modeling, and
analysis. SciPy extends NumPy with algorithms for optimization, signal processing, statistics,
linear algebra, and more. SymPy provides symbolic mathematics. Matplotlib and Plotly handle
visualization. The scientific Python ecosystem is mature and widely used in academia and
industry.

**Education**

Python is the most commonly taught first programming language at universities worldwide. Its
readability makes it easier to focus on concepts -- loops, functions, data structures, algorithms
-- rather than syntax. The MIT OpenCourseWare introductory programming course uses Python. Many
high school curricula use Python. If you are learning to program for the first time, you are in
good company.

**Command-line tools**

Python is excellent for building command-line programs. The standard library includes `argparse`
for parsing command-line arguments, `sys` for interacting with the interpreter, and `subprocess`
for running other programs. Third-party libraries like Click and Typer make building polished
CLI tools even easier.

---

### 3.5 Python's Design Philosophy: The Zen of Python

Python has a documented philosophy. You can read it by running this in any Python interpreter:

```python
import this
```

This prints a poem called *The Zen of Python*, written by Tim Peters in 1999. It is not a formal
specification -- it is a set of guiding principles that shaped how Python was designed and how
experienced Python programmers think about writing code. Here is the full text:

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Here are the most important principles and what they mean in practice.

**Beautiful is better than ugly.**

Code is read far more often than it is written. Python encourages you to write code that is
pleasant to read, not just code that works. This is not about aesthetics for its own sake --
readable code is easier to debug, maintain, and share with others. When you have two ways to
write something and one is cleaner, choose the cleaner one.

**Explicit is better than implicit.**

Python prefers code that says what it does clearly over code that relies on hidden behavior. If
something important is happening, it should be visible in the code. This is why Python does not
have a lot of "magic" that happens behind the scenes without you knowing. When you see Python
code, you should be able to understand what it does by reading it, without needing to know about
hidden rules.

**Simple is better than complex. Complex is better than complicated.**

Prefer the simplest solution that works. If complexity is unavoidable, keep it organized and
understandable. Avoid unnecessary cleverness. A function that does one thing clearly is better
than a function that does five things in a confusing way. This principle pushes back against
over-engineering -- the tendency to build elaborate solutions to simple problems.

**Flat is better than nested.**

Deeply nested code -- functions inside functions inside loops inside conditionals -- is hard to
read and reason about. Python encourages you to keep your code flat. If you find yourself
nesting four levels deep, that is usually a sign to refactor.

**Readability counts.**

This is stated explicitly because it matters enough to say twice. Code that is hard to read is
a liability. Python's syntax -- indentation, clean keywords, minimal punctuation -- is designed
to make readability the default, not something you have to work for.

**Errors should never pass silently. Unless explicitly silenced.**

If something goes wrong, Python should tell you. Swallowing errors quietly makes bugs hard to
find. This principle encourages you to handle errors explicitly and intentionally, not to hide
them. When you do want to ignore an error, you should do so deliberately and visibly, not by
accident.

**There should be one obvious way to do it.**

Python tries to avoid having five different ways to accomplish the same thing. When there is one
clear, idiomatic way to do something, code written by different people looks similar and is
easier to understand. This is sometimes called the "Pythonic" way. As you learn Python, you will
develop a sense for what Pythonic code looks like.

**If the implementation is hard to explain, it's a bad idea.**

If you cannot explain what your code does in plain language, that is a signal that the design
might be wrong. Good code is explainable. If you find yourself struggling to describe what a
function does, consider whether it is doing too much or doing it in the wrong way.

These principles are not rules enforced by the language. They are values that the Python
community has internalized. As you write more Python, you will start to recognize code that
follows them and code that does not. Code that follows these principles is often called
"Pythonic." Code that ignores them -- even if it works -- is sometimes called "unpythonic."

---

### 3.6 What Python Is NOT Good For

Being honest about a tool's limitations is as important as understanding its strengths. Python
is not the right choice for everything.

**Mobile app development**

Python is not used for building native iOS or Android apps. Swift and Kotlin are the standard
languages for those platforms. There are projects like Kivy and BeeWare that attempt to bring
Python to mobile, but they are not mainstream and have significant limitations in terms of
performance, app store distribution, and access to platform APIs. If your goal is to build
mobile apps, Python is not the right starting point.

**Game development**

Python is used for game scripting -- Civilization IV used Python for its scripting layer, and
tools like Blender use Python for automation and plugins. But Python is not used to build game
engines or performance-critical games. C++ is the dominant language for game engines. Unity uses
C#. Unreal Engine uses C++. If you want to build games professionally, Python is not the primary
tool. Pygame exists for simple 2D games and learning, but it is not used for commercial game
development.

**Ultra-low-latency systems**

Python's garbage collector and interpreted nature introduce unpredictable pauses and overhead
that make it unsuitable for systems where microsecond response times matter -- high-frequency
trading systems, real-time audio processing, embedded firmware, operating system kernels,
network packet processing. C and C++ are used here. Python can call into C extensions for
performance-critical sections, but if your entire application needs to be fast, Python is the
wrong foundation.

**Large-scale desktop GUI applications**

While Python has GUI libraries -- Tkinter (built-in), PyQt, wxPython, Dear PyGui -- building
polished, native-feeling desktop applications is not Python's strength. The libraries exist and
work, but they require significant effort to produce applications that feel native on Windows,
macOS, and Linux. For serious desktop apps, languages like Swift (macOS), C# (Windows), or
frameworks like Electron (cross-platform) are more appropriate.

**Embedded systems with tight resource constraints**

Standard Python requires too much memory and processing power for microcontrollers and embedded
systems. MicroPython is a stripped-down Python implementation for microcontrollers like the
Raspberry Pi Pico, but it is a different environment with significant limitations compared to
standard Python. If you are programming microcontrollers, C is still the dominant language.

Understanding these boundaries helps you make good decisions. Python is a powerful, versatile
tool -- but it is not the right tool for every job. Knowing when to use it and when to reach for
something else is part of being a good programmer.

---

### 3.7 What to Expect from This Handbook

This handbook is designed to take you from zero programming knowledge to the point where you
can write real, useful Python programs independently. That is a specific, achievable goal -- and
it is worth being precise about what it means.

**What you will be able to do after this handbook**

- Write Python scripts that automate real tasks on your computer
- Read and write files, work with JSON and CSV data
- Build simple command-line programs with proper argument handling
- Understand and use Python's standard library effectively
- Write functions and classes that are clean, reusable, and well-organized
- Handle errors gracefully so your programs fail informatively rather than silently
- Write tests for your code using pytest
- Use virtual environments and manage dependencies with pip
- Read other people's Python code and understand what it does
- Know where to go to keep learning after this handbook

**What this handbook does not cover in depth**

- Web frameworks (Django, Flask, FastAPI) -- these deserve their own dedicated resources
- Data science libraries (pandas, NumPy, Matplotlib) -- same reason
- Machine learning -- same reason
- Async programming -- mentioned but not covered deeply
- Packaging and publishing to PyPI -- out of scope for this handbook

The goal is a solid, practical foundation. With that foundation, you can pick up any of those
specialized topics on your own. The final chapter points you toward resources for each of them.

**How to get the most out of this handbook**

Each chapter follows the same structure: overview, what you will learn, core concepts, practical
examples, common mistakes, practice tasks, and key takeaways. The chapters build on each other.
Do not skip ahead unless you are already confident with the material.

The most important rule: **type the code yourself**. Do not copy and paste. Typing forces you to
read every character, and that is where learning happens. You will notice things you would miss
by scanning. You will make typos, get error messages, and learn to fix them. That process is the
learning.

The practice tasks at the end of each chapter are not optional. They are where the concepts
become skills. Reading about programming is not the same as programming. You can read every
chapter in this handbook and still not be able to write a program from scratch. The practice
tasks are where passive knowledge becomes active skill.

**How long will this take?**

That depends entirely on how much time you invest and how consistently you practice. A rough
estimate: if you spend one to two hours per day working through the material and doing the
exercises, you can complete this handbook in four to eight weeks. If you can only dedicate a few
hours per week, it will take longer -- but that is fine. Consistency matters more than speed.

**What to do when you get stuck**

Getting stuck is normal. It is not a sign that you are bad at programming or that Python is too
hard. It is a sign that you have reached the edge of your current understanding, which is exactly
where learning happens.

When you get stuck:

1. Read the error message carefully. Python's error messages are generally specific and helpful.
2. Re-read the relevant section of this handbook.
3. Search for the error message or concept online. Stack Overflow and the official Python docs
   are your best resources.
4. Try a simpler version of the problem to isolate what is going wrong.
5. Take a break. Seriously. Coming back to a problem after a few hours often makes it obvious.

---

## 4. Practical Examples

These examples are not exercises. They are here to show you what Python looks like and to give
you a sense of the language before you learn the details. Do not worry if you do not understand
every line -- that is expected. Just read them and notice how the code feels.

### Example 1: Hello, World

The traditional first program in any language:

```python
print("Hello, world!")
```

Output:

```text
Hello, world!
```

That is the entire program. One line. No boilerplate, no imports, no class definitions, no main
function. Python runs it directly.

Compare this to the equivalent in Java:

```text
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

Both programs do the same thing. Python's version is shorter because Python does not require you
to wrap everything in a class or declare a main function. You can just write code.

This is not a trivial difference. The Java version requires you to understand classes, static
methods, access modifiers, and the concept of a main entry point before you can print a single
line. Python lets you start with the actual task.

---

### Example 2: A Simple Function

Functions let you give a name to a block of code so you can reuse it:

```python
def greet(name):
    message = f"Hello, {name}! Welcome to Python."
    return message


print(greet("Alice"))
print(greet("Bob"))
print(greet("everyone"))
```

Output:

```text
Hello, Alice! Welcome to Python.
Hello, Bob! Welcome to Python.
Hello, everyone! Welcome to Python.
```

`def` defines a function. `f"..."` is an f-string -- a way to embed variables directly inside a
string by wrapping them in curly braces. `return` sends a value back to whoever called the
function.

Notice that calling `greet` three times with different names produces three different outputs.
That is the point of functions: write the logic once, use it many times. You will learn
functions in depth in Chapter 10.

---

### Example 3: Working with a List

Lists are one of Python's most useful built-in types. Here is a list of temperatures in Celsius
being converted to Fahrenheit:

```python
celsius_temps = [0, 20, 37, 100]

for temp in celsius_temps:
    fahrenheit = (temp * 9 / 5) + 32
    print(f"{temp}C = {fahrenheit:.1f}F")
```

Output:

```text
0C = 32.0F
20C = 68.0F
37C = 98.6F
100C = 212.0F
```

`for temp in celsius_temps` loops over each item in the list. Python's `for` loop is clean and
readable -- no index variables, no `i++`, no bounds checking. The `:.1f` inside the f-string
formats the number to one decimal place.

---

### Example 4: A List Comprehension

List comprehensions are a concise way to build a new list from an existing one. This example
filters a list to keep only the even numbers:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```

Output:

```text
[2, 4, 6, 8, 10]
```

Read it as: "give me `n` for each `n` in `numbers`, but only if `n` is even." The `%` operator
is the modulo operator -- it gives the remainder after division. `n % 2 == 0` is true when `n`
is divisible by 2, i.e., when it is even.

This is one of Python's most expressive features. In many other languages, this would require
a loop, a conditional, and appending to a new list -- four or five lines. Python does it in one.
You will learn list comprehensions in depth in Chapter 11.

---

### Example 5: Reading a File

Python makes file I/O straightforward. This example reads a text file and prints its contents:

```python
from pathlib import Path

file_path = Path("notes.txt")

if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
    print(content)
else:
    print("File not found.")
```

`pathlib.Path` is Python's modern way to work with file paths. It works the same way on
Windows, macOS, and Linux. `.read_text()` reads the entire file as a string. The `if/else`
checks whether the file exists before trying to read it.

You will learn file handling in depth in Chapter 13.

---

### Example 6: A Simple Class

Classes let you bundle data and behavior together. This example defines a `Dog` class:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.breed}."


rex = Dog("Rex", "Labrador")
bella = Dog("Bella", "Poodle")

print(rex.speak())
print(bella.speak())
print(rex.describe())
```

Output:

```text
Rex says: Woof!
Bella says: Woof!
Rex is a Labrador.
```

`class` defines a new type. `__init__` is the constructor -- it runs when you create a new
instance. `self` refers to the specific instance being operated on. `rex` and `bella` are two
separate `Dog` objects, each with their own `name` and `breed`.

You will learn object-oriented programming in depth in Chapter 16.

---

### Example 7: Automation -- Renaming Files

Here is a taste of what Python automation looks like. This script renames all `.txt` files in
a folder by adding a `backup_` prefix:

```python
from pathlib import Path

folder = Path("my_documents")

for txt_file in folder.glob("*.txt"):
    new_name = txt_file.parent / f"backup_{txt_file.name}"
    txt_file.rename(new_name)
    print(f"Renamed: {txt_file.name} -> {new_name.name}")
```

Output (assuming the folder contains `notes.txt` and `todo.txt`):

```text
Renamed: notes.txt -> backup_notes.txt
Renamed: todo.txt -> backup_todo.txt
```

This is the kind of task that would take several minutes to do manually and two minutes to
automate with Python. `Path.glob()` finds all files matching a pattern. The loop processes each
one. You will learn all of this in Chapters 13 and 17.

---

### Example 8: Handling User Input

Python can read input from the user at the command line:

```python
name = input("What is your name? ")
age_str = input("How old are you? ")
age = int(age_str)

if age >= 18:
    print(f"Hello, {name}. You are an adult.")
else:
    years_left = 18 - age
    print(f"Hello, {name}. You will be an adult in {years_left} year(s).")
```

Sample run:

```text
What is your name? Alice
How old are you? 16
Hello, Alice. You will be an adult in 2 year(s).
```

`input()` reads a line of text from the user and returns it as a string. `int()` converts the
string to an integer. The `if/else` branches based on the value. You will learn all of this in
Chapters 5 and 8.

---

These eight examples cover a lot of ground: output, functions, loops, list comprehensions, file
I/O, classes, automation, and user input. You will understand all of them deeply by the time you
finish this handbook. For now, just notice how readable the code is. Even without knowing the
syntax, you can follow what each example does.

---

## 5. Common Mistakes

Even before writing a single line of code, beginners make some predictable mistakes in how they
approach learning Python. Here are the most common ones -- and how to avoid them.

### Mistake 1: Using Python 2

If you search for Python tutorials online, you will still find Python 2 content. It looks almost
identical to Python 3 but has important differences. The most visible one: in Python 2, `print`
is a statement, not a function.

```python
# Python 2 -- do not use this
print "Hello"

# Python 3 -- use this
print("Hello")
```

Other differences include integer division behavior, string handling, and many standard library
changes. If you mix Python 2 habits with Python 3, you will get confusing errors.

Always verify that any tutorial or resource you use targets Python 3.10 or later. If you see
`print` without parentheses, that resource is outdated. Close it and find a Python 3 one.

---

### Mistake 2: Copying code without typing it

It is tempting to copy and paste example code to see it work. Resist this. Typing code forces
you to read every character. You will notice things you would miss by scanning. You will make
typos, get error messages, and learn to fix them. That process is the learning.

When you copy and paste, you can get code running without understanding it. That feels like
progress, but it is not. The goal is not to have working code -- it is to understand how to
write working code yourself.

---

### Mistake 3: Trying to memorize everything

Python has hundreds of built-in functions, methods, and standard library modules. You do not
need to memorize them. Professional Python programmers look things up constantly. The goal is
to know what is possible and where to find the details, not to hold everything in your head.

Focus on understanding concepts and patterns. The specific syntax and method names will become
familiar through use. When you forget something, look it up. That is normal and expected.

---

### Mistake 4: Skipping the practice tasks

Reading about programming is not the same as programming. You can read every chapter in this
handbook and still not be able to write a program from scratch. The practice tasks are where
passive knowledge becomes active skill. Do them.

If a practice task feels too easy, do it anyway -- it takes two minutes and reinforces the
concept. If a practice task feels too hard, that is a signal to re-read the chapter before
moving on.

---

### Mistake 5: Giving up when you get an error

Error messages are not failures. They are information. Python's error messages are generally
clear and specific. When you get an error, read the message carefully. It usually tells you
exactly what went wrong and where.

For example:

```text
Traceback (most recent call last):
  File "script.py", line 3, in <module>
    print(mesage)
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

This error tells you: on line 3 of `script.py`, you used a name `mesage` that does not exist.
Python even suggests that you might have meant `message`. That is a typo -- easy to fix once you
read the error.

Learning to read error messages is one of the most valuable skills you will develop. Chapter 12
covers error handling and debugging in depth.

---

### Mistake 6: Tutorial paralysis

Some learners consume tutorial after tutorial without ever building anything. They feel like
they need to understand everything before they can start. This is a trap.

A better approach: learn enough to build something small, build it, get stuck, look things up,
and repeat. You learn faster by doing than by reading. After you finish each chapter in this
handbook, build something -- even something tiny -- that uses what you just learned.

---

### Mistake 7: Installing the wrong Python version

Python 2 and Python 3 can coexist on the same machine. On some systems, the command `python`
still runs Python 2, while `python3` runs Python 3. Always check which version you are running:

```bash
python --version
python3 --version
```

If the output shows Python 2.x, use `python3` instead of `python` for all commands. Chapter 2
covers installation and setup in detail. Make sure you are on Python 3.10 or later before
proceeding.

---

### Mistake 8: Ignoring indentation

Python uses indentation to define code structure. This is not optional or stylistic -- it is
part of the syntax. Code that is not indented correctly will either fail with an error or do
something different from what you intended.

```python
# Correct -- the print is inside the if block
if True:
    print("This runs")

# Wrong -- IndentationError
if True:
print("This will cause an error")
```

Use four spaces for each level of indentation. Do not mix tabs and spaces. Most editors handle
this automatically. Chapter 4 covers Python's syntax and indentation rules in detail.

---

### Mistake 9: Treating Python 3.10+ features as optional

This handbook targets Python 3.10 and later. Features like structural pattern matching (`match`
statements), improved error messages, and `X | Y` union type syntax are available to you. Do
not avoid them because an older tutorial did not use them. Use the language you have.

If you are on Python 3.9 or earlier, upgrade. The newer versions are faster, have better error
messages, and include features that make code cleaner. There is no good reason to stay on an
older version for new projects.

---

### Mistake 10: Confusing Python the language with Python the ecosystem

Python the language is the syntax and semantics -- the rules for writing valid Python code.
Python the ecosystem is everything built on top of it: the standard library, third-party
packages, frameworks, tools, and community conventions.

When you are learning, focus on the language first. Understand variables, functions, loops,
classes, and the standard library before reaching for third-party packages. A solid foundation
in the language makes everything else easier to learn.

---

## 6. Practice Tasks

These tasks do not require writing complex code yet. They are about orientation, preparation,
and getting your first hands-on experience with Python.

---

**Task 1: Verify your Python version**

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS or Linux) and run:

```bash
python --version
```

or

```bash
python3 --version
```

You should see output like `Python 3.11.4` or similar. If you do not have Python installed, or
if your version is below 3.10, go to Chapter 2 before continuing.

If you are not sure how to open a terminal, Chapter 2 covers that as well.

---

**Task 2: Run the Zen of Python**

Open a Python interactive session by typing `python` or `python3` in your terminal and pressing
Enter. You should see a prompt that looks like `>>>`. Then type:

```python
import this
```

Press Enter. Read through the output. Pick two or three principles that resonate with you. Think
about what they might mean in practice -- not in the context of programming specifically, but as
general principles for doing careful work.

To exit the interactive session, type:

```python
exit()
```

or press `Ctrl+D` on macOS/Linux, or `Ctrl+Z` then Enter on Windows.

---

**Task 3: Run your first Python script**

Create a new file called `hello.py` in any folder on your computer. Open it in a text editor
and type:

```python
print("Hello, world!")
print("I am learning Python.")
```

Save the file. In your terminal, navigate to the folder where you saved it and run:

```bash
python hello.py
```

or

```bash
python3 hello.py
```

You should see:

```text
Hello, world!
I am learning Python.
```

If you see that output, you have run your first Python program.

---

**Task 4: Explore the Python website**

Visit [https://www.python.org](https://www.python.org). Find:

- The current stable version of Python
- The official documentation at [https://docs.python.org](https://docs.python.org)
- The Python Package Index (PyPI) at [https://pypi.org](https://pypi.org)

You do not need to read anything in depth. Just get familiar with where these resources are.
The official documentation will become one of your most important references as you learn.

---

**Task 5: Identify Python in the wild**

Find one real-world example of Python being used in a domain that interests you. This could be:

- A GitHub repository for a Python project you have heard of
- A job posting that lists Python as a required skill
- A blog post or article about a Python library or tool
- A data science notebook on Kaggle or GitHub

The goal is to connect what you are learning to something concrete and relevant to your
interests. Knowing why you are learning Python makes it easier to stay motivated.

---

**Task 6: Reflect on your goals**

Write down -- on paper or in a text file -- answers to these questions:

1. Why do you want to learn Python?
2. What do you want to be able to build or do with it?
3. How much time can you realistically dedicate to learning each week?

Having clear goals helps you stay motivated when things get difficult. Return to these answers
when you feel stuck or when progress feels slow.

---

**Task 7: Set up your learning environment**

Before moving to Chapter 2, decide where you will write and run your code. Options include:

- A terminal and a text editor (VS Code is a good choice and is free)
- An IDE like PyCharm (has a free Community edition)
- An online environment like [https://replit.com](https://replit.com) for quick experiments

Chapter 2 will walk you through installation and setup in detail. For now, just decide which
approach you want to take and, if you are using VS Code or PyCharm, download and install it.

---

**Task 8: Read a short Python program**

Look at Example 7 from the Practical Examples section -- the file-renaming script. Without
running it, try to describe in plain English what each line does. Write your description in a
comment next to each line, like this:

```python
from pathlib import Path  # import the Path class from the pathlib module

folder = Path("my_documents")  # create a Path object pointing to a folder

for txt_file in folder.glob("*.txt"):  # loop over all .txt files in the folder
    new_name = txt_file.parent / f"backup_{txt_file.name}"  # build the new filename
    txt_file.rename(new_name)  # rename the file
    print(f"Renamed: {txt_file.name} -> {new_name.name}")  # print what happened
```

You do not need to understand every detail. The goal is to practice reading code and making
reasonable guesses about what it does. This skill -- reading unfamiliar code -- is one of the
most important you will develop as a programmer.

---

## 7. Key Takeaways

- Python is an interpreted, high-level, dynamically typed, general-purpose programming language.
- "Interpreted" means you run code directly without a separate compile step. The feedback loop
  is fast: write code, run it, see what happens.
- "High-level" means Python handles memory management and other low-level details for you.
- "Dynamically typed" means variables do not have fixed types -- the value determines the type.
  Type hints are available for optional static analysis.
- Python was created by Guido van Rossum and first released in 1991.
- **Python 2 is dead.** Use Python 3.10 or later. There is no reason to use Python 2 for new
  work. It reached end-of-life on January 1, 2020.
- Python 3.10 introduced structural pattern matching and significantly improved error messages.
  Python 3.11 and 3.12 brought further performance improvements.
- Python is popular because of its readability, versatility, "batteries included" standard
  library, welcoming community, and low barrier to entry.
- Python is used in web development, data science, machine learning, automation, DevOps,
  scientific computing, education, and command-line tooling.
- Python's design philosophy -- summarized in the Zen of Python -- values readability,
  simplicity, explicitness, and practicality.
- Python is not the right tool for mobile apps, game engines, ultra-low-latency systems, or
  resource-constrained embedded systems.
- This handbook will take you from zero to practical, independent Python programming. It covers
  the language and standard library in depth, but not specialized frameworks or libraries.
- The most important habit: **type the code yourself**, make mistakes, and experiment. Do not
  copy and paste.
- Error messages are information, not failures. Python's error messages are specific and
  helpful. Learn to read them.
- The practice tasks are not optional. They are where passive knowledge becomes active skill.
- Consistency matters more than speed. A little practice every day beats occasional long
  sessions.
- When you get stuck: read the error message, re-read the chapter, search online, simplify the
  problem, and take a break. Getting stuck is normal and expected.

---

### Further Reading

- [Python.org](https://www.python.org/)
- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### What's Next

Ready to continue? Head to the next chapter: **Installation and Setup**.

→ [Chapter 02 — Installation and Setup](02-installation-and-setup.md)

*See also:*
- [Exercise](../exercises/01-introduction.md)
- [Solution](../solutions/01-introduction.md)
- [Cheatsheet](../cheatsheets/stdlib.md)
