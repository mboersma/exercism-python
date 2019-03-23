"""Determine if a word or a phrase is an isogram."""


def is_isogram(string):
    """Return True if a string contains no repeating letters, ignoring
    spaces and hyphens."""
    letters = string.replace('-', '').replace(' ', '').lower()
    return len(set(letters)) == len(letters)
