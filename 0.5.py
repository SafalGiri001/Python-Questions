#16
menu = input("Enter the menu(Pasta,Burger,Pasta): ")
match menu:
    case "Pizza": print("It cost $10")
    case "Burger": print("It cost $7")
    case "Pasta": print("It cost $8")
    case _ : print("Not in menu")

#q17
height = float(input("Enter the height(feet): "))
if height>=6:
    print("selected")
else:
    print("Not selected")

#q18
age = int(input("Enter the age: "))
if age>=18:
    print("Allowed")
else:
    print("Not allowed")

#q19
username = input("Enter your name: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Access granted")
else:
    print("Access denied")

#q20
number = int(input("Enter a number(1-12): "))
match number:
    case 12|1|2: print("Winter")
    case 3|4|5: print("Spring")
    case 6|7|8: print("Summer")
    case 9|10|11: print("Autumn")
    case _ : print("Invalid number")