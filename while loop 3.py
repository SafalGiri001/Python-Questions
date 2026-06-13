total = 0
while (number := int(input("Enter a number: "))) != 0 and number != 1 and number < 50:
    total += number
print(total)