banned_items = {'scissors', 'knife', 'lighter'}
items =  input('Enter the items you have: ').lower()
weight = int(input('Enter the weight of the item(kg): '))
if items not in banned_items and weight <=7:
    print("Bag allowed")
else:
    print("Bag not allowed")
