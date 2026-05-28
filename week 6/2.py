# 11.
s = "Loops are Fun"
vowels = 0
consonants = 0
for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("vowels:", vowels)
print("consonants:", consonants)


# 12.
lst = [1, 2, 3, 4, 5]
odd = []
even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Odd:", odd)
print("Even:", even)



# 13.
num = 7
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not Prime")


# 14.
lst = [1, 2, 3, 4, "a", "b"]
types = []
for i in lst:
    types.append(type(i))
print(types)


# 15.
s = "Python123"
letters = 0
digits = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
print("Letters:", letters)
print("Digits:", digits)



# 16.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Valid")
else:
    print("Invalid")


# 17.
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 18.
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)


# 19.
for i in range(1, 9):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()



# 20.
lst = [1, 2, 3, 4]
for i in lst:
    if i == 1 or i == 2:
        print(i)



















































































