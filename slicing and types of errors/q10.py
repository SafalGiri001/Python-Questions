weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi <= 25:
    status = "Normal weight"
elif bmi <= 30:
    status = "Overweight"
else:
    status = "Obese"

print("Weight:", weight)
print("Height:", height)
print("BMI:", round(bmi,1), status)