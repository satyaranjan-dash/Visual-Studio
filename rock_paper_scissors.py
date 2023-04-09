import random
print("Let's play Rock_Paper_Scissors")
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"] #rock:0, paper:1, scissors:2

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Opps! Enter a valid input.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer choose", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Draw! No points.")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Come soon! Goodbye!")