#1
a = int(input("Enter a number: "))
if a >=1 and a <=100:
    print("It exists between 1 and 100")
else:
    print("It doesn't exist between 1 and 100")

#2
a = int(input("Enter a number: "))
if a%2 == 0:
    print("The given number is even")
else:
    print("THe given number is odd")

#3
number = int(input("Enter a number from 1 to 12: "))
if number >= 1 and number <= 12:
    if number ==1:
        print("january")
    elif number ==2:
        print("february")
    elif number ==3:
        print("march")
    elif number ==4:
        print("april")
    elif number ==5:
        print("may")
    elif number ==6:
        print("june")
    elif number ==7:
        print("july")
    elif number ==8:
        print("august")
    elif number ==9:
        print("september")
    elif number ==10:
        print("october")
    elif number ==11:
        print("november")
    elif number ==12:
        print("december")
else:
    print("Invalid number")


#4
marks = int(input("Enter marks: "))
if marks <25:
    print("F")
elif marks>=25 and marks<45:
    print("E")
elif marks>=45 and marks<50:
    print("D")
elif marks>=50 and marks<60:
    print("C")
elif marks>=60 and marks<80:
    print("B")
elif marks>=80 and marks<=100:
    print("A")
else:
    print("Invalid marks")

#5
number = int(input("Enter a number: "))
if number%7==0:
    print("It is divisible by 7")
else:
    print("It is not divisible by 7")