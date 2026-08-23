import random

while True:
    dice = random.randint(1, 6)
    print("you rolled ", dice)
    choice = input("roll again(yes/no)").lower()
    if choice =="no":
        print("thanks for playing")
        break