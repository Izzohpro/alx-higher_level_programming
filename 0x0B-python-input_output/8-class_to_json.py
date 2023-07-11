#!/usr/bin/python3
"""Defines the Python class-to-JSON function."""


def class_to_json(obj):
    """Return the simple data structure of a dictionary represntation."""
    return obj.__dict__
