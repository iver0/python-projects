import random


def roll():
    return f"Rolled {random.randint(1, 6)}"


def main():
    print("1. Roll the Dice\n2. Exit")
    # keyboard.add_hotkey("1", print, args=[roll])
    # keyboard.add_hotkey("2", exit)
