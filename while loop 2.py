#while (password := input('Enter your password: ')) != 'hellopython':
#    print('Enter a correct password')


total = 0
while (num1 :=int(input('Enter a number: '))) !=0:
    total += num1
print(total)


#q3
import random
random_number = random.randint(1, 100)
i = 0
print("Welcome to the number guessing game!")
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Your guess is too low")
    elif guess > random_number:
        print("Your guess is too high")
    else:
        print(f"Correct! You guessed it in {i} attempts")
        break
    i = i + 1

#q4
while (numbers := int("Enter a number: ")) != 8:
    print("Enter a correct number")



















































