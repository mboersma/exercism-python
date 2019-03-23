"""Calculate the Hamming Distance between two DNA strands."""


def distance(strand_a, strand_b):
    """Return the Hamming Distance calculated between two DNA strands
    represented as strings."""
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands must be of equal length.")

    return sum(1 for x, y in zip(strand_a, strand_b) if x != y)
