import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from src.d88fc886.calculator import add, subtract, multiply, divide

assert add(2, 3) == 5, "add(2, 3) should be 5"
assert subtract(10, 4) == 6, "subtract(10, 4) should be 6"
assert multiply(3, 4) == 12, "multiply(3, 4) should be 12"
assert divide(10, 2) == 5, "divide(10, 2) should be 5"

try:
    divide(1, 0)
    assert False, "divide by zero should raise"
except ValueError:
    print("divide by zero correctly raises ValueError")

try:
    add("two", 3)
    assert False, "should raise TypeError on string input"
except TypeError:
    print("string input correctly raises TypeError")

try:
    multiply(True, 4)
    assert False, "should raise TypeError on bool input"
except TypeError:
    print("bool input correctly raises TypeError")

try:
    divide(10, float("inf"))
    assert False, "should raise TypeError on inf input"
except TypeError:
    print("inf input correctly raises TypeError")

print("All tests passed")
