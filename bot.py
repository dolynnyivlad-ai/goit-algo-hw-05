def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return 'Enter name and phone please.'
        except KeyError:
            return 'Enter user name'
        except IndexError:
            return 'Enter the argument for the command'

    return inner


def parse_input(user_input):
    if user_input == '':
        return '', []  # Повертаємо пусту команду і пустий список

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."


@input_error
def phone_username(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} not found."


@input_error
def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: available command: add, change, phone, all: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == 'add'.lower():
            print(add_contact(args, contacts))
        elif command == 'change'.lower():
            print(change_contact(args, contacts))
        elif command == 'phone'.lower():
            print(phone_username(args, contacts))
        elif command == 'all'.lower():
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
