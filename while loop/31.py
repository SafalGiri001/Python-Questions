positive = 0
negative = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    if num > 0:
        positive += 1
    else:
        negative += 1

print("Positive numbers =", positive)
print("Negative numbers =", negative)