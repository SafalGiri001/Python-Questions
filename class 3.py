import random
r = random.randint(1,10)
attempt = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess> r:
        print("Your guess is too high")
    elif guess< r:
        print("Your guess is too low")
    elif guess == r:
        print ("congrats, you guessed it")
        attempt = attempt + 1
        print(f'You attempted in {attempt} attempts ')
        break

