m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())

total = m1+m2+m3+m4
per = total/4

if per > 70:
    grade = "Distinction"
elif per > 60:
    grade = "First"
elif per > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Total =", total)
print("Percentage =", per)
print("Grade =", grade)


balance = 5000
pin = int(input("Enter PIN: "))

if pin == 123:
    print("1.Withdraw\n2.Check Balance\n3.Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        amt = int(input("Amount: "))
        balance -= amt
        print("Remaining Balance =", balance)

    elif choice == 2:
        print("Balance =", balance)

    elif choice == 3:
        print("Thank you for visiting")

    else:
        print("Invalid option")

else:
    print("Wrong PIN")




floor = int(input("Floor: "))
weight = float(input("Weight: "))
door = input("Door status (open/closed): ")

if floor < 0 or floor > 10:
    print("INVALID FLOOR")

elif weight > 500:
    print("OVERWEIGHT: LIFT CANNOT MOVE")

elif door != "closed":
    print("WARNING: CLOSE THE DOOR")

else:
    print("ACTIVATE ELEVATOR MOTION")



fname = input("First Name: ")
lname = input("Last Name: ")
email = input("Email: ")
reemail = input("Re-enter Email: ")
password = input("Password: ")

if fname.isalpha() and lname.isalpha() and fname and lname:
    if "@" in email and "." in email:
        if email == reemail:
            if len(password) >= 6:
                print("Registration Successful")
            else:
                print("Password too short")
        else:
            print("Emails do not match")
    else:
        print("Invalid email")
else:
    print("Invalid name")