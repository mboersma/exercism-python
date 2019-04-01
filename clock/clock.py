"""Implements a clock that handles times without dates."""


HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60


class Clock(object):
    """A simple clock that supports addition, subtraction, and equality."""

    def __init__(self, hour, minute):
        self.hour = hour
        self._rationalize(minute)

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self._rationalize(self.minute + minutes)
        return self

    def __sub__(self, minutes):
        self._rationalize(self.minute - minutes)
        return self

    def _rationalize(self, minutes):
        quotient, self.minute = divmod(minutes, MINUTES_PER_HOUR)
        self.hour = (self.hour + quotient) % HOURS_PER_DAY
