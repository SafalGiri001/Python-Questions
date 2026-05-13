items = [3,4,7,9,11,13]
r_items = items.pop(4)
items.insert(1, r_items)
items.append(r_items)
print(items)