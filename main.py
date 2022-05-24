import sys
from src import dice_roll, mad_libs_gen, rnd_password_gen, rock_paper_scissors


def main():
    while True:
        print("Python Projects")
        print(
            """
0. Exit
1. Dice Roll
2. Mad Libs Generator
3. Random Password Generator
4. Rock Paper Scissors"""
        )
        print("Your selection: ", end="")
        match int(input()):
            case 0:
                break
            case 1:
                sys.exit(dice_roll.main())
            case 2:
                sys.exit(mad_libs_gen.main())
            case 3:
                sys.exit(rnd_password_gen.main())
            case 4:
                sys.exit(rock_paper_scissors.main())


if __name__ == "__main__":
    sys.exit(main())
