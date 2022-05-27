import sys
from src import (
    menu,
    dice_roll,
    mad_libs_gen,
    rnd_password_gen,
    rock_paper_scissors,
)
from src.todo_app import main as todo_app


def main():
    menu_items = (
        ("Dice Roll", dice_roll.main),
        ("Mad Libs Generator", mad_libs_gen.main),
        ("Random Password Generator", rnd_password_gen.main),
        ("Rock Paper Scissors", rock_paper_scissors.main),
        ("Todo App", todo_app.main),
    )

    while True:
        menu.clear()
        print("Python Projects\n")

        if menu.create(menu_items):
            return


if __name__ == "__main__":
    sys.exit(main())
