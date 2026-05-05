age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if age < 21 or age > 60:
    print("Loan denied: Age condition failed")
elif income < 30000:
    print("Loan denied: Income condition failed")
elif credit < 700:
    print("Loan denied: Credit score condition failed")
else:
    print("Loan approved")