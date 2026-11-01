# app.py — Basic Calculator
# This file is used across all 4 Claude Code setup demos (Lecture 6.1)

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a multiplied by b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Basic Calculator")
    print("----------------")
    print(f"10 + 5  = {add(10, 5)}")
    print(f"10 - 5  = {subtract(10, 5)}")
    print(f"10 * 5  = {multiply(10, 5)}")
    print(f"10 / 5  = {divide(10, 5)}")
    try:
        print(f"10 / 0  = {divide(10, 0)}")
    except ValueError as error:
        print(f"10 / 0  = Error: {error}")
