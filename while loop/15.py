password = "secret123"
attempts = 0

while attempts < 3:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted")
        break

    attempts += 1

if attempts == 3:
    print("Access Denied")