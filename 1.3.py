
#q1
items = [3,4,7,9,11,13]
r_items = items.pop(4)
items.insert(3,r_items)
items.append(r_items)
print(items)

#q2
first_set = {23,42,65,57,78,83,29}
second_set = {57,83,29,67.73,43,48}
common_elements = first_set.intersection(second_set)
print(common_elements)
if common_elements:
    unique_items = first_set.difference(second_set)
    print(unique_items)
    print(f'common elements: {common_elements}')
else:
    print("No common elements")


#q3
first_set = {27,43,34}
second_set = {34,93,22,27,43,53,48}
common_elements = first_set.issuperset(second_set)
print(common_elements)
if common_elements:
    unique_items = first_set.clear()
    print(unique_items)
    print(f'common elements: {common_elements}')
else:
    print("No common elements")



