database = {"admin": "1234", "user": "abcd"}

user_input = "admin"
user_pass = "1234"

if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")