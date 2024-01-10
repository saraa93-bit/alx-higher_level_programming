#!/usr/bin/python3
"""Defines a file-appending function."""


def write_file(filename="", text=""):
    """Appends a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to Append.
        text (str): The text to Append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
