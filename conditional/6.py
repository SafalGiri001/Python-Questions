age = int(input("Enter age: "))
member = input("Membership card (yes/no): ").lower()

if age < 12:
    print("Ticket is free")
elif 12 <= age <= 60:
    if member == "yes":
        print("Ticket price: Rs. 150")
    else:
        print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 100 (Senior discount)")