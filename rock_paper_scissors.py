from random import choice

plays = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
player_score = 0
enemy_score = 0

for _ in range(3):
    player = input("Rock, paper, or scissors? ")
    enemy = choice(["Rock", "Paper", "Scissors"])
    print(f"Enemy chose {enemy.lower()}")

    if enemy == plays[player]:
        player_score += 1
    elif player == plays[enemy]:
        enemy_score += 1

print(f"Your score: {player_score}")
print(f"Enemy score: {enemy_score}")
if player_score > enemy_score:
    print("You won!")
elif player_score < enemy_score:
    print("You lost!")
else:
    print("Draw!")
