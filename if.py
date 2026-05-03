age = 18
if age >= 18:
    print("You are an adult")

temperature = 35
if temperature>30:
    print("It is hot outside")
else:
    print("The weather is good")

score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your score is:", grade)



balance = 5000
amount = int(input("Withdraw amount:"))

balnce = balance - amount
print("New balance is:", balnce)


balance = 5000
amount = int(input("Withdraw amount:"))
if amount == 0:
    print("Enter a valid amount")
elif amount>balance:
    print("insufficient amount")
else:
    balance = balance - amount
    print("Your balance is:", balance)



correct_password = "gurkhas123"
entered = "pass123"
print("Login sucessful!")
print("Welcome!!!")



username = "adminram"
password = "gurkhas123"
entered_user = "adn=min"
entered_pass = "123"
if entered_user ==  username and entered_pass == password:
    print("Login successful Welcome")
elif entered_user != username and entered_pass != password:
    print("Wrong password")
else:
    print("Wrong username")



marks = 45
if marks >=90:
    print("Grade:A+")
elif marks >=75:
    print("Grade:A")
elif marks >=60:
    print("Grade:B")
elif marks >=50:
    print("Grade:C")
else:
    print("Grade:F Failed")



name = "Ram"
age = 14
print(f"{name} registered to vote")
print("Voter id issued")

name = "Ram"
age = 14
if age >= 18:
    print(f"{name} registered to vote")
    print("Voter id issued")
else:
    print(f"Must be 18+. You are {age}.")
    print("registration denied")




















