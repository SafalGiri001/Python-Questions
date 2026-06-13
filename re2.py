age = int (input("Enter your age: "))
height = float (input("Enter your height(cm): "))
if age>=12:
    if height>=140:
        print("you are eligible to ride the roller coaster")
    else:
        print("you are not eligible to ride the roller coaster")
else:
    print("you are not eligible to ride the roller coaster")

#q2
password= input("Enter your password: ")
username= input("Enter your username: ")
if password == "ad123" and username == "admin":
    print("you are eligible ")
elif username == "student" and password == "st123":
    print("Access granted")
else:
    print("Access denied")

#q3
for i in range(1,6):
    print(i)