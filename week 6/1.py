# 1.

for i in range(1, 6):
    if i % 2 == 0:
        print(f"Number {i} is even.")
    else:
        print(f"Number {i} is odd.")


# 2.

lst = [10, 20, 30, 40]
total = 0
for i in lst:
    total += i
    print(f"Added {i}. Running total is {total}.")
print("------------------------------")
print("Total Sum:", total)

# 3.

student_names = ["Ram", "Hari", "Sita"]
print("--- Email Greetings Generated ---")
for name in student_names:
    print(f"Hi {name}, your course approval is ready!")


# 4.

chapters = [45, 30, 50, 40]
print("--- Book Chapter Summary ---")
for i in range(len(chapters)):
    print(f"Chapter {i+1} has {chapters[i]} pages.")

# 5.

lst = [4, 5, 3, 2]
product = 1
for i in lst:
    product *= i
print("Product =", product)



# 6.

number = 11
for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 7.

lst = [3, 2, 1, 4, 5]
print(lst[::-1])



# 8.

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
for i in a:
    if i in b:
        print(i)



# 9.

lst = [1, 2, 3, 4]
for i in lst:
    if i == 1 or i == 4:
        print(i)


# 10.

s = "programming"
vowels = "aeiouAEIOU"
result = ""
for ch in s:
    if ch not in vowels:
        result += ch

print(result)