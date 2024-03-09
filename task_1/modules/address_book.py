"""This module creates an address book"""

from collections import UserDict, defaultdict
from datetime import datetime
from record import Record


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
