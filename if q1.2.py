a = int(input("Enter a number"))
if a%7 == 0:
    print("It is divisible by 7")
else:
    print("It is not divisible by 7")

#qns6
n = int(input("Enter a number"))
m = int(input("Enter a number"))
operators = {"+":n+m,"-":n-m,"*":n*m,"/":n/m}
op = input("Enter a operator(+,-,*,/)")
if op in operators:
    print(f"Your answer is {operators[op]}")


#ans7
a = int(input("enter a salary"))
b = int(input("enter a credit score"))
if a >= 50000 and b>=700:
    print("Car loan eligible")
else:
    print("Car loan not eligible")



#qns8
n = int (input("enter integer"))
if n%3==0 and n%5==0:
    print("fizzbuzz")
elif n%3 !=0 and n%5 ==0:
    print("buzz")
elif n%3 ==0 and n%5 !=0:
    print("fizz")
else:
    print(n)







