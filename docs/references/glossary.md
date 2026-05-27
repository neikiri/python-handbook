# Glossary

A-Z reference of Python and programming terms used in this handbook.

## A

**Argument**
A value passed to a function when it is called. For example, in `print("hello")`, `"hello"` is an argument.

**Attribute**
A value or method associated with an object. Accessed using dot notation: `object.attribute`. For example, `"hello".upper` is an attribute of the string.

## B

**Boolean**
A data type with two possible values: `True` or `False`. Used in conditional statements and logical operations.

**Built-in**
A function, type, or constant that is part of Python and available without importing. Examples: `print()`, `len()`, `int`, `True`.

## C

**Class**
A blueprint for creating objects. Defines attributes and methods that instances of the class will have.

**Collection**
A data structure that holds multiple items. Examples: list, tuple, set, dictionary.

**Comprehension**
A concise way to create a collection by iterating over another collection and applying a condition or transformation. Examples: list comprehension, dictionary comprehension.

**Conditional**
A statement that executes code based on whether a condition is true or false. Examples: `if`, `elif`, `else`.

## D

**Dictionary**
A collection of key-value pairs. Keys are unique and used to access values. Created with `{}` or `dict()`.

**Docstring**
A string that documents a function, class, or module. Written as the first statement using triple quotes: `"""..."""`.

## E

**Exception**
An error that occurs during program execution. Can be caught and handled with `try`/`except` blocks.

**Expression**
A combination of values, variables, and operators that evaluates to a result. For example, `2 + 3` or `x > 5`.

## F

**File Path**
The location of a file on the filesystem. Can be absolute (from root) or relative (from current directory).

**Function**
A reusable block of code that performs a specific task. Defined with `def` and called by name.

## G

**Generator**
A function that yields values one at a time instead of returning all at once. Created using `yield` keyword.

## I

**Immutable**
Cannot be changed after creation. Examples: strings, tuples, numbers. Opposite of mutable.

**Import**
A statement that loads a module or specific items from a module into the current namespace. Examples: `import os`, `from pathlib import Path`.

**Indentation**
Whitespace at the beginning of a line used to define code blocks in Python. Must be consistent (typically 4 spaces per level).

**Index**
The position of an item in a sequence, starting from 0. For example, in `[1, 2, 3]`, the index of `2` is `1`.

**Iterable**
An object that can be looped over. Examples: lists, tuples, strings, dictionaries, sets.

**Iterator**
An object that produces values one at a time when iterated over. Created with `iter()` and advanced with `next()`.

## K

**Key**
In a dictionary, the unique identifier used to access a value. For example, in `{"name": "Alice"}`, `"name"` is a key.

## L

**List**
A mutable collection of items in a specific order. Created with `[]` or `list()`.

**Loop**
A control structure that repeats a block of code. Examples: `for` loop, `while` loop.

## M

**Method**
A function associated with an object. Called using dot notation: `object.method()`. For example, `"hello".upper()`.

**Module**
A file containing Python code that can be imported and used in other programs. Typically has a `.py` extension.

**Mutable**
Can be changed after creation. Examples: lists, dictionaries, sets. Opposite of immutable.

## N

**None**
A special value representing the absence of a value or null. Used as a default return value for functions that don't explicitly return.

## O

**Object**
An instance of a class. Everything in Python is an object, including numbers, strings, lists, and functions.

## P

**Package**
A directory containing Python modules and a special `__init__.py` file. Allows organizing related modules.

**Parameter**
A variable in a function definition that receives a value when the function is called. For example, in `def greet(name):`, `name` is a parameter.

**Path**
See "File Path".

**pip**
The Python package installer. Used to install third-party packages from PyPI.

**Project**
A collection of Python files and related resources organized for a specific purpose.

**pytest**
A popular testing framework for Python. Used to write and run tests.

## R

**REPL**
Read-Eval-Print Loop. An interactive Python environment where you can type commands and see results immediately. Accessed by running `python` in the terminal.

**Return Value**
The value that a function sends back to the caller. Specified with the `return` keyword.

## S

**Script**
A Python file designed to be run directly, typically containing a sequence of statements. Often has a `if __name__ == "__main__":` guard.

**Set**
An unordered collection of unique items. Created with `{}` (with items) or `set()`.

**Slice**
A portion of a sequence extracted using the slice operator `[start:stop:step]`. For example, `"hello"[1:4]` returns `"ell"`.

**String**
A sequence of characters. Created with quotes: `"hello"` or `'hello'`.

## T

**Tuple**
An immutable collection of items in a specific order. Created with `()` or `tuple()`.

**Type**
The category of a value, determining what operations can be performed on it. Examples: `int`, `str`, `list`, `dict`.

**Type Hint**
An annotation indicating the expected type of a variable or function parameter. For example, `def greet(name: str) -> str:`.

## V

**Variable**
A named container that stores a value. Created by assignment: `x = 10`.

**Virtual Environment**
An isolated Python environment on your system. Allows different projects to have different package versions without conflicts. Created with `venv` module.

## W

**While Loop**
A loop that repeats as long as a condition is true. Syntax: `while condition: ...`.

## Y

**Yield**
A keyword used in generators to produce values one at a time. Similar to `return` but allows the function to resume later.