list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

i = 0

while i < len(list1):

    j = 0

    while j < len(list2):

        if list1[i] == list2[j]:
            print(list1[i])

        j += 1

    i += 1