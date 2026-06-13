user_name = "admin"
password = "1234"
max_attempt = 3
while True:
    entered_name = input("enter your name: ")
    entered_password = input("enter your password: ")
    if entered_password == password and entered_name == user_name:
        print("welcome ",  entered_name)
        break
    else:
        max_attempt -=1
        print("wrong password")
        if max_attempt==3:
            print("you dont have any attempts remaining")


