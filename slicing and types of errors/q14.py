age = int(input("Age: "))
gender = input("Gender (M/F): ")

if 18 <= age < 30:
    if gender == "M":
        print("Wage = 700")
    else:
        print("Wage = 750")

elif 30 <= age <= 40:
    if gender == "M":
        print("Wage = 800")
    else:
        print("Wage = 850")

else:
    print("Invalid")