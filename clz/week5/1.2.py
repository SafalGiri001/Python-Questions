first_set = {23,42,65,57,78,83,29}
second_set = {57,83,29,67,73,43,48}

common_elements = first_set.intersection(second_set)

print("Common elements:", common_elements)

if common_elements:
    first_set.difference_update(second_set)  # removes common elements from first_set

    print("Updated first_set:", first_set)
else:
    print("No common elements")