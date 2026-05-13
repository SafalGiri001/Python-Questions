cart = ["apple","orange"]
cart.append("orange")
cart.extend("orange")
print(cart)
cart.insert(0,"cocacola")
print(cart)

cart = ["apple","orange"]
cart.remove(cart[0])
print(cart)
a = cart.pop(0)
print(cart)


cart.clear()
print(cart)

cart = 1,2,3,4
cart1 = list(cart)
cart1.pop(0)
print(tuple(cart1))

items = set()
print(type(items))
items = {*()}
print(type(items))

items= {1,2,3,4,5}
items.add(3)
items.update({3,4})
print(items)


items = {1,2,3,4,5}
items.remove(4)
items.discard(4)
print(items)

items = {1,2,3,4,5}
items.clear()
print(items)

items = {1,2,3,'ram','shyam',4,5}
print(items)
a = items.pop()
print(items)
print(a)

items1 = {1,2,3,'ram','shyam',4,5}
items2 = {8,9,10,'ram','shyam',4,5}
items3 = items.difference(items2)
items4 = items.symmetric_difference(items2)
items5 = items.union(items2)
print(items3)
print(items4)
print(items5)



items1 = {1,2,3,'ram','shyam',4,5}
items2 = {'ram','shyam',4,5}
items3 = items.isdisjoint(items2)
items4 = items.issuperset(items2)
items5 = items.issubset(items2)
print(items3)
print(items4)
print(items5)
















