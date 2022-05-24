import sys
from curses import wrapper
from src import dice_roll, mad_libs_gen, rnd_password_gen, rock_paper_scissors


def main(stdcr):
    while True:
        stdcr.clear()
        stdcr.addstr("Python Projects\n")
        stdcr.addstr(
            """
0. Exit
1. Dice Roll
2. Mad Libs Generator
3. Random Password Generator
4. Rock Paper Scissors
"""
        )
        stdcr.refresh()
        match stdcr.getkey():
            case "0":
                break
            case "1":
                dice_roll.main()
            case "2":
                mad_libs_gen.main()
            case "3":
                rnd_password_gen.main()
            case "4":
                rock_paper_scissors.main()


if __name__ == "__main__":
    sys.exit(wrapper(main))
