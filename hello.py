#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# hello.py
# ------------------------------------------------------------------------------
# This is the main entry point of the application. It is also the only file
# in the entire application. The application is a "Hello, World!" program,
# which is a time-honored tradition in the software engineering community
# dating back to Brian Kernighan's 1972 "A Tutorial Introduction to the
# Language B". This program faithfully carries on that tradition.
#
# USAGE:
#   python hello.py
#
# EXPECTED OUTPUT:
#   Hello, World!
#
# DEPENDENCIES:
#   None. This program has no external dependencies. It does not even import
#   the standard library, which is itself a remarkable achievement in
#   minimalist software design.
#
# AUTHOR:
#   Unknown. Presumably a human, or possibly an AI. The distinction is
#   becoming increasingly difficult to determine.
#
# VERSION: 1.0.0
# LICENSE: Probably fine.
# ------------------------------------------------------------------------------

# Define the greeting string that will be printed to stdout.
# The string "Hello, World!" was chosen over alternatives such as:
#   - "Hello, Earth!"  (too geocentric)
#   - "Hello, World?!" (too uncertain)
#   - "Goodbye, World!" (sends the wrong message)
# After extensive deliberation, "Hello, World!" was deemed the most suitable.
GREETING = "Hello, World!"

# This is the main execution block. In Python, code at the module level is
# executed when the script is run directly. We are, in fact, running it
# directly. Therefore, this code will execute. This is working as intended.
#
# The print() function writes the given object to the text stream (sys.stdout
# by default), followed by a newline character (\n). It was imported
# implicitly as a built-in, so no import statement was required. This is one
# of Python's many quality-of-life decisions that makes it a pleasure to use
# for programs of this scale and complexity.

# Print a greeting message to the console.
# This is the core business logic of the application.
# Do not remove this line. The entire program depends on it.
print(GREETING)  # <-- this is where the magic happens
