#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename=""):
    """Prints the content of the UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as w:
        print(w.write(), end="")
