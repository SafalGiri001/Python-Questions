import random
r = random.randint(1,50)
max_attempt = 7
while True:
    guess = int(input("Guess a number between 1 and 50: "))
    attempt = 1
    if guess >r:
        print("too high")
    elif guess <r:
        print("too low")
    else:
        print("you guessed right")
    if attempt == 7:
        print("No more attempts left")
        break