print("=============================")
print("      GRADE CALCULATOR")
print("=============================")

english = float(input("Enter English marks: "))
math = float(input("Enter Math marks: "))
python = float(input("Enter Python marks: "))
computer = float(input("Enter Computer marks: "))

total = english + math + python + computer
average = total / 4

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nTotal marks:", total)
print("Average:", average)
print("Grade:", grade)