import random
while True:
    a = input ("Roll a dice(y/n): ").lower()
    if a =="y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif a == "n":
        print("Thank you")
        break
    else:
        print("Invalid choice")