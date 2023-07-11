#!/usr/bin/python3
"""Defines the text file-reading function."""


def read_file(filename=""):
    """Prints the content of the UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
