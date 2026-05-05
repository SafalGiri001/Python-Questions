age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))

if age >= 12:
    if height >= 140:
        print("You can ride the roller coaster")
    else:
        print("Height is not enough")
else:
    print("Age is not enough")