from string import ascii_letters, digits, punctuation
from secrets import SystemRandom

length = int(input("Password length: "))
password = ""
characters = ascii_letters + digits + punctuation
print("".join(SystemRandom().sample(characters, length)))
