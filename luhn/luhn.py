"""Given a number determine whether or not it is valid per the Luhn formula."""


class Luhn(object):
    """Luhn accepts a card number and validates it by a checksum formula."""

    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        """Return True if a number passes the Luhn checksum formula."""

        def luhnify(digit):
            return sum(divmod(digit*2, 10))

        card_num = self.card_num.replace(' ', '')
        if len(card_num) < 2 or not card_num.isdigit():
            return False
        digits = [int(c) for c in card_num]
        odds, evens = digits[-2::-2], digits[-1::-2]
        return sum([luhnify(d) for d in odds] + evens) % 10 == 0
