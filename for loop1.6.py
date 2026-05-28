cart = [1,2,3,-11,14,-20]

odd = []
even = []
negative = []

for i in cart:
    if i < 0:
        negative.append(i)
    elif i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)
print(negative)


