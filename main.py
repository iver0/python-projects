import sys
from pynput.keyboard import Key, Listener
from src import dice_roll, mad_libs_gen, rnd_password_gen, rock_paper_scissors


def check_key(key):
    match key:
        case Key.5:
            exit
    # keyboard.add_hotkey("1", dice_roll.main)
    # keyboard.add_hotkey("2", mad_libs_gen.main)
    # keyboard.add_hotkey("3", rnd_password_gen.main)
    # keyboard.add_hotkey("4", rock_paper_scissors.main)
    # keyboard.add_hotkey("5", exit)


def main():
    while True:
        print("\033[H\033[J", end="")
        print("Python Projects")
        print(
            """
0. Exit
1. Dice Roll
2. Mad Libs Generator
3. Random Password Generator
4. Rock Paper Scissors
"""
        )
        with Listener(on_press=check_key) as listener:
            listener.join()


if __name__ == "__main__":
    sys.exit(main())
