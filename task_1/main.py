"""This module creates a contact book"""

from modules.address_book import AddressBook
from modules.record import Record


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
            name, new_phone = args
            contact = book.find(name)
            contact.edit_phone(new_phone)

        elif command == "phone":
            [name] = args
            contact = book.find(name)
            print(contact.phones[0].value)

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
