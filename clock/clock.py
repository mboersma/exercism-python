"""Implements a clock that handles times without dates."""


class Clock(object):
    """A simple clock that supports addition, subtraction, and equality."""

    def __init__(self, hour, minute):
        minutes = (hour * 60 + minute) % (24 * 60)
        self.hour, self.minute = divmod(minutes, 60)

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
