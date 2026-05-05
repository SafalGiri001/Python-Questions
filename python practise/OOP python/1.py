first_name =input("Enter you first name: ")
last_name =input("Enter you last name: ")
email = input("Enter you email: ")
re_email = input("Re-enter your email: ")
password = input("Enter your password: ")
if not (first_name or not last_name):
    print("All fields are required")
elif not (first_name.isalpha() and not last_name.isalpha()):
    print("First and last name should only contain letters")
elif ("@"not in email and "." not in email):
    print("Invalid email")
elif re_email != email:
    print("Invalid email")
elif len(password) < 8:
    print("Password must be at least 8 characters")
else:
    print("Password is valid")
    is_valid = True
if is_valid:
    print("Registration successful")
else:
    print("Registration failed")






