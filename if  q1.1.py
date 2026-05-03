number = int(input("Enter a number: "))
if number>=1 and number<=100:
    print("The number is between 1 and 100")
else:
    print("The number is not between 1 and 100")


#q2
number = int(input("Enter a number: "))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")

#q3
number = int(input("Enter a number: "))

if number == 1:
    Month = "January"
elif number == 2:
    Month = "February"
elif number == 3:
    Month = "March"
elif number == 4:
    Month = "April"
elif number == 5:
    Month = "May"
elif number == 6:
    Month = "June"
elif number == 7:
    Month = "July"
elif number == 8:
    Month = "August"
elif number == 9:
    Month = "September"
elif number == 10:
    Month = "October"
elif number == 11:
    Month = "November"
elif number == 12:
    Month = "December"
else:
    Month = None
    print("The number is not between 1 and 12")

if Month:
    print("The month is", Month)



n= int(input("Enter your marks: "))
if n < 25:
    print("grade : F")
elif n>=25 and n<45:
    print("grade : E")
elif n>=45 and n<50:
    print("grade : D")
elif n>=50 and n<60:
    print("grade : C")
elif n>=60 and n<80:
    print("grade : B")
elif n>=80 and n<=100:
    print("grade : A")
else:
    print("invalid marks")




