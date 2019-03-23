"""Given a phrase, count the occurrences of each word in that phrase."""

from collections import Counter
from re import findall


def word_count(phrase):
    """Return a dict counting the occurrences of each word in a phrase."""
    pattern = r"[a-zA-Z0-9]+(?<!\\)[a-zA-Z']*(?<!')"
    return Counter(findall(pattern, phrase.lower()))
