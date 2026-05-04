# src/calculator.py — updated with validation
import math


def _validate_numbers(*args):
    for arg in args:
        if isinstance(arg, bool) or not isinstance(arg, (int, float)) or not math.isfinite(arg):  # Q1: Three conditions — what are they?
            raise TypeError(f"Expected a finite real number, got {type(arg).__name__}")


def add(a, b):
    ___(a, b)        # Q2: Call the validator
    return a + b


def subtract(a, b):
    ___(a, b)
    return a - b


def multiply(a, b):
    ___(a, b)
    return a * b


def divide(a, b):
    ___(a, b)
    if b == 0:
        raise ValueError("Division by zero")
    return a / b