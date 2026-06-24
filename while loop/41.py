numbers = [10, 20, 30, 40, 20]

i = 0
duplicate = False

while i < len(numbers):

    j = i + 1

    while j < len(numbers):

        if numbers[i] == numbers[j]:
            duplicate = True
            break

        j += 1

    if duplicate:
        break

    i += 1

if duplicate:
    print("Has Duplicates")
else:
    print("No Duplicates")