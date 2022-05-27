def clear():
    "Clears the screen."
    print("\033[H\033[J", end="")


def display(names: tuple):
    "Displays a menu of given names."
    for name in names:
        print(f"{names.index(name) + 1}. {name}")


def execute(commands: tuple, n: str):
    "Executes correct command index by the input."
    if n.isdigit():
        if 0 <= int(n) - 1 < len(commands):
            commands[int(n) - 1]()
        elif int(n) - 1 == len(commands):
            return True


def create(items: tuple):
    "Creates a menu in the terminal from the given items tuple containing items \
        of the (str, callable) type."

    # Extract only names from the items tuple
    names = tuple(item[0] for item in items)
    display(names + ("Exit\n",))

    # Extract only commands from the items tuple
    commands = tuple(item[1] for item in items)
    return execute(commands, input("Your selection: "))
