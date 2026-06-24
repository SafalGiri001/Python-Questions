numbers = [2, 4, 6, 7, 8]

i = 0

while i < len(numbers):

    print("\nTable of", numbers[i])

    j = 1

    while j <= 10:
        print(numbers[i], "x", j, "=", numbers[i] * j)
        j += 1

    i += 1