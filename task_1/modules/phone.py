"""This module creates a user phone"""

from field import Field


class Phone(Field):
    """This class validates user's number"""

    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise Exception("Phone number has to be 10 digits")
