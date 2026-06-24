numbers = [15, 25, 30, 45, 60, 12, 90, 7]

count = 0
i = 0

while i < len(numbers):

    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        count += 1

    i += 1

print("Count =", count)