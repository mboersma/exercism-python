"""Output the lyrics to 'The Twelve Days of Christmas'."""


from collections import namedtuple


Day = namedtuple('Day', 'number gift')


DAYS = [
    Day('first', 'a Partridge in a Pear Tree'),
    Day('second', 'two Turtle Doves'),
    Day('third', 'three French Hens'),
    Day('fourth', 'four Calling Birds'),
    Day('fifth', 'five Gold Rings'),
    Day('sixth', 'six Geese-a-Laying'),
    Day('seventh', 'seven Swans-a-Swimming'),
    Day('eighth', 'eight Maids-a-Milking'),
    Day('ninth', 'nine Ladies Dancing'),
    Day('tenth', 'ten Lords-a-Leaping'),
    Day('eleventh', 'eleven Pipers Piping'),
    Day('twelfth', 'twelve Drummers Drumming'),
]


def recite(start_verse, end_verse):
    """Return verses of 'The Twelve Days of Christmas' specified by indexes."""
    return [recite_verse(n) for n in range(start_verse, end_verse+1)]


def recite_verse(day):
    """Return a verse of 'The Twelve Days of Christmas' for a given day."""
    verse = "On the {} day of Christmas my true love gave to me: ".format(
        DAYS[day-1].number)

    for i in range(day, 0, -1):
        gift = DAYS[i-1].gift
        if i == 1 and day > 1:
            verse += "and "
        verse += ('{}.' if i == 1 else '{}, ').format(gift)

    return verse
