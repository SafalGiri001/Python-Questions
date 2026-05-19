ram = {"apple", "banana", "mango"}
laxman = {"grapes", "orange", "watermelon"}

common = ram.intersection(laxman)

if len(common) == 0:
    print("They picked completely different items")
else:
    print("They have some common items")