total = 0
count = 0

while True:
    score = float(input("Enter score (-1 to stop): "))

    if score == -1:
        break

    total += score
    count += 1

if count > 0:
    print("Average =", total / count)
else:
    print("No scores entered")