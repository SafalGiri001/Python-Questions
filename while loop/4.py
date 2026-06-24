numbers = [10, 5, 10, 20, 10, 30]

count = 0
i = 0

while i < len(numbers):
    if numbers[i] == 10:
        count += 1
    i += 1

print("10 appears", count, "times")