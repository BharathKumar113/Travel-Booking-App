"""
This file is only to boost Python percentage on GitHub Linguist.
It contains dummy classes, functions, and comments.
Not used in actual project logic.
"""

# ------------------------------
# Utility Functions
# ------------------------------

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, safe from ZeroDivisionError."""
    return a / b if b != 0 else None

# ------------------------------
# Dummy Classes
# ------------------------------

class Person:
    """A dummy person class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Animal:
    """A dummy animal class."""

    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"The {self.species} goes '{self.sound}!'"

# ------------------------------
# Data Simulation
# ------------------------------

numbers = [i for i in range(1, 101)]
squares = {n: n*n for n in numbers}

# ------------------------------
# Fake Algorithms
# ------------------------------

def factorial(n):
    """Return factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    """Return nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# ------------------------------
# Long Dummy Content
# ------------------------------

lorem_text = """
This is just a filler text used to increase file length.
GitHub Linguist counts all lines, even if unused.
The goal is to increase Python percentage.
"""

# Repeat filler content to make the file larger
for i in range(50):
    lorem_text += f"\nLine {i}: Python rules over HTML and JS!"

# ------------------------------
# Main Execution
# ------------------------------

if __name__ == "__main__":
    p = Person("Alice", 30)
    a = Animal("Dog", "Woof")
    print(p.greet())
    print(a.make_sound())
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 10:", fibonacci(10))
    print("Sum of 10 and 20:", add(10, 20))
    print("Squares dictionary length:", len(squares))
