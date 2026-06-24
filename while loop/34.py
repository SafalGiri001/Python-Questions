numbers = [45, 60, 12, 75, 30, 55, 8, 90]

i = 0

while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0

    i += 1

print(numbers)