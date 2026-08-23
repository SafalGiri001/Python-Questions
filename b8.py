import random
choices= ["rock", "paper","scissors"]
while True:
    choice = input ("enter your choice(rock, paper, scissors):  ").lower()

    if choice == "exit":
        print("thanks for playing")
        break
    if choice not in choices:
        print("invalid choice")
        continue
    computer = random.choice(choices)
    if choice == computer:
        print("Its a draw")
    elif (
        (choice == "rock" and computer == "scissors")
        or
        (choice =="paper" and computer == "rock")
        or
        (choice=="scissors" and computer =="rock")

        ):
        print("You win")
    else:
        print("computer wins")
