numbers = []

while True:
    num = int(input("Enter a number: "))

    if num in numbers:
        print("Duplicate number entered!")
        break

    numbers.append(num)