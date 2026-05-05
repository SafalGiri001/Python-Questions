age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

if 18 <= age < 30:
    if gender == "M":
        wage = 700
    else:
        wage = 750
elif 30 <= age <= 40:
    if gender == "M":
        wage = 800
    else:
        wage = 850
else:
    print("Invalid age group")
    wage = 0

if wage > 0:
    total = wage * days
    print("Total wages:", total)