mov1 = input("Enter you first move(rock, paper, scissor): ")
mov2 = input("Enter you second move(rock, paper, scissor): ")
choice = ["rock", "paper", "scissor"]
if not(mov1 in choice) or not(mov2 in choice):
    print("Invalid choice")
elif mov1 == "rock" and mov2 == "scissor":
    print("Player1 wins")
elif mov1 =="scissor" and mov2 == "paper":
    print("Player1 wins")
elif mov1 =="paper" and mov2 == "rock":
    print("Player1 wins")
elif mov1 == mov2:
    print("It's a tie!")
else:
    print("Player2 wins")















