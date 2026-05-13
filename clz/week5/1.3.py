first_set = {27,43,34}
second_set = {34,93,22,27,43,53,48}

if first_set.issubset(second_set):
    print("first_set is subset of second_set")
    first_set.clear()
    print("first_set after deletion:", first_set)

elif first_set.issuperset(second_set):
    print("first_set is superset of second_set")
    second_set.clear()
    print("second_set after deletion:", second_set)

else:
    print("No subset or superset relationship")