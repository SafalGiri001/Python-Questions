age = int(input("Enter age: "))

if age < 12:
    price = 0

elif age <= 60:
    member = input("Membership card? (yes/no): ")
    if member == "yes":
        price = 150
    else:
        price = 200

else:
    price = 100

print("Ticket Price =", price)