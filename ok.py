first_name =input("Enter you first name: ")
last_name =input("Enter you last name: ")
email = input("Enter you email: ")
re_email = input("Re-enter your email: ")
password = input("Enter your password: ")
if not (first_name and last_name and email and re_email and password):
    print("All fields are required")
elif not(first_name.isalpha() and last_name.isalpha() and email and re_email and password):
    print("Must enter or type letters only")
elif not("@" in email and "." in email and "@" in re_email and "." in password):
    print("Invalid email address")
elif email != re_email:
    print("email do not match")
elif len(password) < 8:
    print("Password must be at least 8 characters")
else:
    print("registered successfully")


