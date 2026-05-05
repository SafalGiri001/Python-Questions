user_name = input("Enter your name: ")
password =  input("Enter your password: ")
if user_name == "admin":
    if password == "pass123":
        print("Welcome " + user_name)
    else:
        print("Invalid password")
else:
    print("Invalid username or password")