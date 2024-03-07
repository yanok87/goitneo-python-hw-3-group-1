"""This module creates a contact booke"""

from collections import UserDict, defaultdict
from datetime import datetime


class Field:
    """This class contains a generic field"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """This class stands for name field"""

    pass


class Phone(Field):
    """This class validates user's number"""

    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise Exception("Phone number has to be 10 digits")


class Birthday(Field):
    """This class validates user's birthday"""

    def __init__(self, birthday):
        try:
            valid_birthday = datetime.strptime(birthday, "%d/%m/%Y").date()
            super().__init__(valid_birthday)

        except ValueError:
            print("Birthday must be in format DD/MM/YYYY")


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

    def edit_phone(self, old_phone, new_phone):
        """This func edits phone number"""

        self.remove_phone(old_phone)
        self.add_phone(new_phone)

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


class AddressBook(UserDict):
    """This class contains user records"""

    def add_record(self, record: Record):
        """This func adds user record"""
        self.data[record.name.value] = record

    def find(self, n):
        """This func finds and returns user record"""
        res = self.data[n]
        return res

    def add_birthday(self, name, birthday):
        """This func adds birthday to user record"""
        contact = self.find(name)
        contact.add_birthday(birthday)
        return self.data[name]

    def show_birthday(self, name):
        """This func shows a birthday of user record"""

        return self.data[name].birthday

    def delete(self, n):
        """This func deletes user record"""
        del self.data[n]

    def all(self):
        """This func shows all records in the address book"""
        for _, record in self.data.items():
            print(record.__str__())

    def birthdays(self):
        """This function returns birthday reminder"""
        res = defaultdict(list)
        today = datetime.today().date()
        users = self.data

        for _, user in users.items():
            name = user.name
            birthday = user.birthday
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

            if birthday_this_year.year == today.year:
                if delta_days < 7:  # Birthday for the upcoming 7 days
                    week_day = birthday_this_year.weekday()
                    if week_day == 5 or week_day == 6:  # Birthday on weekend
                        res["Monday"].append(name)
                    if week_day < 5:  # Birthday on week day
                        day_name = birthday_this_year.strftime("%A")
                        res[day_name].append(name)
        for day, names in res.items():
            names_list = list()
            for name_class in names:
                name = name_class.value
                names_list.append(name)

            names_str = ", ".join(names_list)
            formated = f"{day}: {names_str}"
            print(formated)


def parse_input(user_input):
    """This function parses user input"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    """This function interacts with user and creates a phone book"""
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            print("Good bye!")
            break
        elif command == "hello":

            print("How can I help you?")
        elif command == "add":
            name, phone = args
            contact = Record(name)
            contact.add_phone(phone)
            book.add_record(contact)

        elif command == "change":
            name, phone = args
            contact = book.find(name)
            # contact.edit

        elif command == "phone":
            name = args
            # print(contact(args, book))
        elif command == "all":
            print(book.all())

        elif command == "add-birthday":
            name, birthday = args
            book.add_birthday(name, birthday)

        elif command == "show-birthday":
            [name] = args
            print(book.show_birthday(name))

        elif command == "birthdays":
            print(book.birthdays())

        else:
            print("Invalid command.")


if __name__ == "__main__":

    main()
