#!/usr/bin/env python3
"""Unit tests for hello.py"""

import sys
import io
from contextlib import redirect_stdout


def test_greeting_constant():
    """Test that GREETING constant is defined correctly."""
    import hello
    assert hasattr(hello, 'GREETING')
    assert hello.GREETING == "Hello, World!"


def test_greeting_type():
    """Test that GREETING is a string."""
    import hello
    assert isinstance(hello.GREETING, str)


def test_greeting_not_empty():
    """Test that GREETING is not empty."""
    import hello
    assert len(hello.GREETING) > 0


def test_greeting_length():
    """Test that GREETING has expected length."""
    import hello
    assert len(hello.GREETING) == 13


def test_main_output():
    """Test that running the module prints the correct output."""
    # Capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        # Execute the hello module
        import hello
        # Force re-execution by reloading
        import importlib
        importlib.reload(hello)

    output = f.getvalue()
    assert "Hello, World!" in output


if __name__ == "__main__":
    # Run tests if pytest is available, otherwise run basic checks
    try:
        import pytest
        pytest.main([__file__, "-v"])
    except ImportError:
        print("pytest not installed. Running basic checks...")
        test_greeting_constant()
        test_greeting_type()
        test_greeting_not_empty()
        test_greeting_length()
        test_main_output()
        print("All basic checks passed!")
