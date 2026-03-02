#!/usr/bin/env python3
"""
Tests for hello.py

This test module ensures that the Hello, World! program maintains its
impeccable standards of greeting the world.
"""

import subprocess
import sys
import unittest


class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello.py module."""

    def test_greeting_output(self):
        """Test that running hello.py outputs 'Hello, World!'."""
        result = subprocess.run(
            [sys.executable, "hello.py"],
            capture_output=True,
            text=True,
            cwd="/home/daytona/slopslopslop"
        )
        self.assertEqual(result.stdout.strip(), "Hello, World!")
        self.assertEqual(result.returncode, 0)

    def test_no_errors(self):
        """Test that hello.py runs without any errors."""
        result = subprocess.run(
            [sys.executable, "hello.py"],
            capture_output=True,
            text=True,
            cwd="/home/daytona/slopslopslop"
        )
        self.assertEqual(result.stderr, "")

    def test_greeting_constant(self):
        """Test that the GREETING constant has the expected value."""
        # Import the module to check the constant
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "hello", "/home/daytona/slopslopslop/hello.py"
        )
        # We need to capture stdout since importing will execute print
        from io import StringIO
        import sys as sys_module
        old_stdout = sys_module.stdout
        sys_module.stdout = StringIO()

        hello_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hello_module)

        sys_module.stdout = old_stdout

        self.assertEqual(hello_module.GREETING, "Hello, World!")


if __name__ == "__main__":
    unittest.main()
