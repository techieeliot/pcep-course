
import datetime


print("hello world")

print("(662)", "312", "6815", sep="-")

# Guido van Rossum created python

# Compilation vs Interpretation
# Compilation: Source code is translated into machine code before execution.
# Interpretation: Source code is executed line by line at runtime.
# Python is an interpreted language, but it compiles to bytecode before execution.

# Python is a high-level, interpreted language known for its readability and simplicity.
# It is dynamically typed, meaning variable types are determined at runtime.
# Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
# Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.
# Python's standard library is extensive, providing modules for file I/O, system calls, and even web development.
# Python has a large and active community, contributing to a rich ecosystem of third-party libraries and frameworks.
# Python uses indentation to define code blocks, which enhances readability.
# Python supports both object-oriented and functional programming paradigms.
# Python's syntax is designed to be clear and intuitive, making it accessible for beginners.
# Python supports dynamic typing, meaning variable types can change at runtime.
# Python has built-in data structures like lists, tuples, sets, and dictionaries.

# Lexis - building blocks of a programming language, such as keywords, operators, and identifiers.
    # English words like "Blue", "Red", "Green".
    # Python keywords like "if", "else", "while", "for", "def", "class", "import", "return", "print", "True", "False", "None", "=", "==", "!=", "<", ">", "<=", ">=", "+", "-", "*", "/", "//", "%", "**", "and", "or", "not", "is", "in".

# Syntax - rules that define the structure of valid statements in a programming language.
# if = 5 # will not work
num = 5 # will work

# triple quotes
"""
    This is a multi-line comment or docstring.
        - It can span multiple lines and is often used to describe functions or classes.
"""

print("""This is a multi-line string.
It can also be used for multi-line comments or docstrings.""")

# Semantics - meaning of the statements in a programming language, defining what the code does.

# Python uses indentation to define code blocks, which is part of its syntax.
# Python's syntax is designed to be clear and intuitive, making it accessible for beginners.

x = 0
print("x is", x)

while x < 10:
    print(x)
    x += 1

print("Loop finished", x, sep=": ")


print(f"The {adj1} {noun} is {adj2}.")

name = input("Enter your name: ")
print("Hello", name)

# PEP 8 is the style guide for Python code, providing conventions for writing clean and readable code.
# PEP 8 is the standard for Python code style, promoting readability and consistency.

print(f'Hello, {name}!')
# f-strings (formatted string literals) allow for easy string formatting in Python.

date = datetime.date(2023, 10, 1)
print(f"Today's date is {date:%B %d, %Y}.")

