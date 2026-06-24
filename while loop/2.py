n = int(input("Enter a positive integer: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)