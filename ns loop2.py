numbers =  [3,5,7,8]
for i in numbers:
    if i ==5:
        continue
    for i in range(1,11):
        print(f'{i} * {j} = {i*j}')
        print()