units = int(input("Enter units: "))

if units < 100:
    cost = units * 5

elif units <= 300:
    cost = 100 * 5 + (units - 100) * 8

else:
    cost = 100 * 5 + 200 * 8 + (units - 300) * 10

print("Cost =", cost)