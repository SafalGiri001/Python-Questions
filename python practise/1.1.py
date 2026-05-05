import random
number = random.randint(1,100)
print("Welcome to the number guessing game! ")
attempt = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempt += 1
    if guess>number:
        print("Too high")
    elif guess<number:
        print("Too low")
    else:
        print("Correct! You guessed it in",attempt,"attempts")
        break