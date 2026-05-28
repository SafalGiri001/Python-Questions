cart = {
    'rice' : (2,140),
    'milk' : (3,50),
    'bread' : (4,55),
}
total_price = 0
for i,(j,k) in cart.items():
    print(f'{i} {j} {k} {j*k}')
    total_price += j*k
print(total_price)

