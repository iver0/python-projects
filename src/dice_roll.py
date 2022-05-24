from random import randint


def main():
    while int(input("Enter 1 to roll the dice, enter 0 to exit: ")) != 0:
        print(f"Rolled {randint(1, 6)}")
