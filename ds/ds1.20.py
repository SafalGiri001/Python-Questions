inventory = {'A1': 50, 'B2': 0, "C3": 10}
restricted_zones = {'B2', 'z9'}
target = 'B2'

if target in inventory:

    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")

    else:
        if target in restricted_zones:
            print("invalid zone")
        else:
            print("stock error")

else:
    print("item not found")