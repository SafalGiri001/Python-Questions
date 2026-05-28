sample_data = {'A': [1,2,3], 'B': {1,2,3,4,5}}
for column,row in sample_data.items():
    print(column)
    for cell in row:
        print(cell)
    print()

for i in range(1,5):
    if i==2:
        continue
    print(i)


sample_data = {'A': [1,2,3], 'B': {1,2,3,4,5}, 'C': [1,2]}
for column,row in sample_data.items():
    if column=='B':
        continue
    print(column)
    for cell in row:
        print(cell)
    print()

sample_data = {'A': [1,2,3], 'B': {1,2,3,4,5}, 'C': [1,2]}
for column,row in sample_data.items():
    if column=='B':
        continue
    print(column)
    for cell in row:
        if cell ==3 and column=='A':
            continue
        print(cell)
    print()

