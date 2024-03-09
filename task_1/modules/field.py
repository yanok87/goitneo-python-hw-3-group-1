"""This module creates a generic field"""


class Field:
    """This class contains a generic field"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
