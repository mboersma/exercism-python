"""
Given a diagram, determine which plants each child in the kindergarten class is
responsible for.
"""


class Garden(object):
    """Models a garden farmed by kindergarten students."""

    PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V':'Violets',
    }

    STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    def __init__(self, diagram, students=None):
        self._rows = diagram.splitlines()
        self._students = sorted(students or self.STUDENTS)

    def plants(self, student):
        """Return the unabbreviated list of plants for a given student."""
        i = self._students.index(student) * 2
        string = self._rows[0][i:i+2] + self._rows[1][i:i+2]
        return [self.PLANTS[c] for c in string]
