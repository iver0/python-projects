import sys
from src import dice_roll, mad_libs_gen, rnd_password_gen, rock_paper_scissors


def main():
    while True:
        print("\033[H\033[J", end="")
        print("Python Projects")
        print(
            """
1. Dice Roll
2. Mad Libs Generator
3. Random Password Generator
4. Rock Paper Scissors
5. Exit
"""
        )
        match input("Your selection: "):
            case "1":
                dice_roll.main()
            case "2":
                mad_libs_gen.main()
            case "3":
                rnd_password_gen.main()
            case "4":
                rock_paper_scissors.main()
            case "5":
                break


if __name__ == "__main__":
    sys.exit(main())
