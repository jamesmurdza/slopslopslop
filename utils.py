#!/usr/bin/env python3
"""
utils.py - Utility functions for the application
"""


def greet(name):
    """
    Returns a personalized greeting.

    Args:
        name (str): The name to greet

    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int|float): First number
        b (int|float): Second number

    Returns:
        int|float: The sum of a and b
    """
    return a + b


def is_even(number):
    """
    Checks if a number is even.

    Args:
        number (int): The number to check

    Returns:
        bool: True if even, False otherwise
    """
    return number % 2 == 0


if __name__ == "__main__":
    # Example usage
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Is 4 even? {is_even(4)}")
