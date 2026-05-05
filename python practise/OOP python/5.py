age = int(input("Enter your age: "))
monthly_income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
if age>=21 and age<=60:
    print("You are elgible")
    is_eligible = False
elif monthly_income>=30000:
    print("You are eligible")
    is_eligible = False
elif credit_score>=700:
    print("You are eligible")
    is_eligible = False
else:
    print("You are not eligible")
