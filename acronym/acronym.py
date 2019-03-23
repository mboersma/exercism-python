"""Convert a phrase to its acronym."""

import re


def abbreviate(words):
    """Return the abbreviation—or acronym—for the words provided."""
    pattern = r"""
    ([A-Z])  # capture the first capital letter
    [A-Z']*  # followed by zero or more capital letters or apostrophes
    """
    return ''.join(re.findall(pattern, words.upper(), re.VERBOSE))
