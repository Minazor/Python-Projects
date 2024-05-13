import random

user_wins = 0
computer_wins = 0

items = ["rock", "paper", "scissors"]
while True:

    if user_wins == 3 or computer_wins == 3:
        break

    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in items:
        continue

    random_number = random.randint(0, len(items) - 1)
    computer_pick = items[random_number]
    print(computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tie!")
    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
