#Sample code code:
# calculator.py
import math

def add(x, y):
    """Addition"""
    return x + y
 
def subtract(x, y):
    """Subtraction"""
    return x - y
 
def multiply(x, y):
    """Multiplication"""
    return x * y
 
def divide(x, y):
    """Division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
 
def square_root(x):
    """Square Root"""
    return math.sqrt(x)
