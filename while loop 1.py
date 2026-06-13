i = 0
while i < 5:
    print('hello')
    i += 1

i = 0
while i in range(5):
    print('hello')
    i += 1

i = 0
while True:
    if i ==5:
        break
    print(i)
    i += 1

number = [1,2,3,4,5]
i = 0
while i < len(number):
    print(number[i])
    i += 1



number = [1,2,3,4,5]
i = 0
while i<5:
    if i ==1:
        continue
    i = i + 1
    print(number[i])



