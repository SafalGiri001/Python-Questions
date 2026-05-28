item = ['orange', 'apple', 'mango']
for i in item:
    print(i)

#printing numbers fromm 1 tp 100.
print(1)
print(2)
print(3)
print(100)

# with loop
for i in range(1,101):
    print(i)


# without loop
# Summming a list of numbers:
numbers = [4,7,1,9,3]
total = 0
total += numbers[0]
total += numbers[1]
total += numbers[2]
total += numbers[3]
total += numbers[4]
print(total)

numbers = [4,7,1,9,3]
total = 0
for n in numbers:
    total += n
print(total)


numbers = [4,7,1,9,3]
total = 0
for n in range(len(numbers)):
    total += numbers[n]
print(total)