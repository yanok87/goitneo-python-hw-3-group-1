"""This module creates a user birthday"""

from datetime import datetime
from field import Field


class Birthday(Field):
    """This class validates user's birthday"""

    def __init__(self, birthday):
        try:
            valid_birthday = datetime.strptime(birthday, "%d/%m/%Y").date()
            super().__init__(valid_birthday)

        except ValueError:
            print("Birthday must be in format DD/MM/YYYY")
