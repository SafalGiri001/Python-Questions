menu = {
    "Pizza": 15,
    "Burger": 10,
    "Salad": 8
}

order = "Pizza"

if order in menu:
    print(menu[order])
else:
    print("item not found")