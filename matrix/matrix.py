"""
Given a string representing a matrix of numbers, return the rows
and columns of that matrix.
"""


class Matrix(object):
    """A 2-d matrix constructed from a string of numbers."""

    def __init__(self, matrix_string):
        self._matrix = []
        for line in matrix_string.splitlines():
            row = [int(n) for n in line.split()]
            self._matrix.append(row)

    def row(self, index):
        """Return the matrix row at the given 1-based index."""
        return self._matrix[index-1]

    def column(self, index):
        """Return the matrix column at the given 1-based index."""
        return [row[index-1] for row in self._matrix]
