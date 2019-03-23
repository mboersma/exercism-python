"""
Convert a number to a string, the contents of which depend on the number's
factors.
"""


def raindrops(number):
    """Return raindrop sounds when a number has factors of 3, 5, or 7."""
    drops = ""

    if number % 3 == 0:
        drops += "Pling"
    if number % 5 == 0:
        drops += "Plang"
    if number % 7 == 0:
        drops += "Plong"

    return drops or str(number)
