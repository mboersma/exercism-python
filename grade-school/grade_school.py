"""
Given students' names along with the grade that they are in, create a roster
for the school.
"""

from collections import defaultdict


class School(object):
    """Models the roster of students' names and grades."""

    def __init__(self):
        self._roster = defaultdict(list)

    def add_student(self, name, grade):
        """Add a student to the school roster."""
        self._roster[grade].append(name)
        self._roster[grade].sort()

    def roster(self):
        """Return the school student roster, sorted by grade and name."""
        students = []
        for grade_number in sorted(self._roster):
            students.extend(self._roster[grade_number])
        return students

    def grade(self, grade_number):
        """Return the students within a grade."""
        return self._roster[grade_number]
