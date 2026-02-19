# calculator.py
# A simple calculator with 4 basic math operations.

def add(a, b):
    return a + b          # returns the sum of two numbers

def subtract(a, b):
    return a - b          # returns the difference

def multiply(a, b):
    return a * b          # returns the product

def divide(a, b):
    if b == 0:            # guard: division by zero would crash Python
        raise ValueError("Cannot divide by zero")
    return a / b          # returns the quotient
