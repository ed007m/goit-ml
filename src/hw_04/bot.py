def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: please provide name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: please provide name and phone number."
    name, phone = args
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: please provide a name."
    name = args[0]
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    commands = {
        "hello":  lambda args: "How can I help you?",
        "add":    lambda args: add_contact(args, contacts),
        "change": lambda args: change_contact(args, contacts),
        "phone":  lambda args: show_phone(args, contacts),
        "all":    lambda args: show_all(contacts),
    }

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        handler = commands.get(command)
        print(handler(args) if handler else "Invalid command.")


if __name__ == "__main__":
    main()