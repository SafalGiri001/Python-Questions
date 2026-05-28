# 31.
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
new_list = []
for i in lst1:
    if i > 0:
        new_list.append(i)
print(new_list)



# 32.
lst = [0, 1, 2, 3, 4, 5, 6]
for i in lst:
    if i == 3 or i == 6:
        continue

    print(i)


# 33.
lst1 = [1, "a", 3.5, True]
lst2 = []
for i in lst1:
    lst2.append(type(i))
print(lst2)


# 34.
for i in range(5):
    print(i)
else:
    print("Done")


# 35.
for i in range(105, 6, -7):
    print(i, end=" ")



# 36.
bad_chars = [';', ':', '!', '*']
string = "py;th* o:n ! ;py * t*h:o !n"
result = ""
for ch in string:
    if ch not in bad_chars and ch != " ":
        result += ch
print(result)


# 37.
numbers = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)



# 38.
total = 0
for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


# 39.
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)


# 40.
lst = [1, 2, 3, 2, 4, 2, 5]
target = 2
count = 0
for i in lst:
    if i == target:
        count += 1
print(target, "appears", count, "times")









