age = int(input("Age: "))
income = int(input("Monthly Income: "))
credit = int(input("Credit Score: "))

if 21 <= age <= 60 and income >= 30000 and credit >= 700:
    print("Loan Approved")

else:
    print("Loan Rejected")
    if not (21 <= age <= 60):
        print("Age condition failed")
    if income < 30000:
        print("Income condition failed")
    if credit < 700:
        print("Credit score failed")