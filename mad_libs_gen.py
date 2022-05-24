pronoun = input("Who drives the story? ").lower()
if pronoun == "me":
    pronoun = "I"
cake = input("What is your favorite cake? ").lower()
stranger = input("What is your name? ")

print(
    f"While {pronoun} was eating a {cake} cake, \
{pronoun} met {stranger}!"
)
