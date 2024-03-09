"""This module creates a user record"""

from phone import Phone
from name import Name
from birthday import Birthday


class Record:
    """This class contains name and phone numbers"""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ""

    def add_phone(self, phone):
        """This func adds phone number"""

        validated_phone = Phone(phone)
        self.phones.append(validated_phone)

    def remove_phone(self, phone):
        """This func removes phone number"""

        for user_phone in self.phones:
            if user_phone.value == phone:
                self.phones.remove(user_phone)

    def edit_phone(self, new_phone):
        """This func edits the first phone number"""

        self.phones[0].value = new_phone

    def find_phone(self, phone):
        """This func finds phone number and reutns Phone class"""

        for user_phone in self.phones:
            if user_phone.value == phone:
                return user_phone

    def add_birthday(self, birthday):
        """This func adds birthday"""

        validated_birthday = Birthday(birthday)
        self.birthday = validated_birthday.value
        return self

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)},  birthday: {self.birthday}"
