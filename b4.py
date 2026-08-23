import random
number = random.randint(1,100)
attempt = 0
while True:
    guess = int(input("enter a number: " ))
    attempt +=1
    if guess>number:
        print("Too High")
    elif guess<number:
        print("Too low")
    else:
        print("correct! you guessed it right")
        print(f'you guessed it in {attempt} attempt')
        break
