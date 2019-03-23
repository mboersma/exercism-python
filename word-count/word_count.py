"""Given a phrase, count the occurrences of each word in that phrase."""

from collections import Counter
import re


def word_count(phrase):
    """Return a dict counting the occurrences of each word in a phrase."""
    pattern = r"""
    [a-zA-Z0-9]+  # one or more alphanumeric characters
    (?<!\\)       # not preceded by a backslash
    [a-zA-Z']*    # zero or more alphabetic characters or an apostrophe
    (?<!')        # not preceded by an apostrophe
    """
    return Counter(re.findall(pattern, phrase.lower(), re.VERBOSE))
