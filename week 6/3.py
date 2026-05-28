# 21.
total = 0
for i in range(1, 11):
    if i % 2 != 0:
        total += i

print(total)

# 22.
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print(total)


# 23.
s = "Python is fun"
count = 0
for ch in s:
    if ch == " ":
        count += 1
print("Spaces:", count)



# 24
lst = [1, 2, 3, 4]
new_list = []
for i in lst:
    new_list.append(i ** 3)
print(new_list)



# 25.
a = "programming"
print(a[::-1])

# 26.
for i in range(50):
    if i == 8:
        break

    print(i)

 # 27.
s = "Python"
for ch in s:
    print(ch)



# 28.
a = ["ram", "shyam", 1, 2]
for i in a:
    if type(i) == str:
        print("Hello!", i)

# 29.
a = ["ram", "shyam", 1, 2]
new_list = []
for i in a:
    new_list.append("Dr." + str(i))
print(new_list)


# 30.
lst = [1, 2, 3, 4]
new_list = []
for i in lst:
    new_list.append(i ** 2)
print(new_list)