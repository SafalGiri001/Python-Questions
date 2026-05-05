username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "pass123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")