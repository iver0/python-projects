from src import menu
import random


def roll():
    print(f"Rolled {random.randint(1, 6)}")
    input()


def main():
    menu_items = (("Roll the Dice", roll),)
    while True:
        menu.clear()
        print("Dice Roll")

        if menu.create(menu_items):
            return
