import random


def main():
    while True:
        print("\033[H\033[J", end="")
        print("1. Roll the Dice\n2. Exit\n")
        s = input("Your selection: ")
        print()

        if s == "1":
            print(f"Rolled {random.randint(1, 6)}")
        elif s == "2":
            break
