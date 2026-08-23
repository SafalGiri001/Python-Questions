num1 = float(input("enter a number: "))
num2 = float(input("Enter a number: " ))
operator = input("enter an operator(+,-,*,/): ")
if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator =="*":
    result = num1 *num2
elif operator == "/":
    result = num1 / num2
else:
    print("invalid operator")
print(result)