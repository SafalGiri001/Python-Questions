count = 0
for i in range(5,10,15):
    count = count + 1
    print(i)

for i in [1,2]:
    print("A")
    for j in [1] :
        print('B')

folders = [['Pic1'],['Pic2', 'Pic3']]
for sub in folders:
    for item in sub :
        print(item)


