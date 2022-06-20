from random import randint


class Die:
    """Class that represents one die."""

    def __init__(self, num_sides=6):
        """6 sides default."""
        self.num_sides = num_sides

    def roll(self):
        """Returns random number from 1 to number of sides."""
        return randint(1, self.num_sides)