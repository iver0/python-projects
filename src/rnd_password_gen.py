from string import ascii_letters, digits, punctuation
from secrets import SystemRandom


def main():
    length = int(input("Password length: "))
    characters = ascii_letters + digits + punctuation
    print("".join(SystemRandom().sample(characters, length)))
