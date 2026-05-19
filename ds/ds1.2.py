

shopping_list = {'Milk', 'Bread', 'Egg'}
bought = {'Bread', 'Egg'}

diff = shopping_list.difference(bought)
if diff:
    print(diff)
else:
    print("Shopping complete")

