numbers = [10, 15, 25, 30, 45]

i = 0
sorted_list = True

while i < len(numbers) - 1:

    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break

    i += 1

if sorted_list:
    print("Sorted")
else:
    print("Not Sorted")