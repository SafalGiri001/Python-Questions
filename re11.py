number = int(input("Enter a number: "))
if (number>=1 and number<=100):
    print("Yes, the number is between 1 and 100")
else:
    print("No, the number is between 1 and 100")


#q2
number = int(input("Enter a number: "))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")

#q3
num = int(input("Enter a number between 1 to 12: "))
if num ==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
    print("Invalid number")


#q4
num1= int(input("Enter a number: "))
num2= int(input("Enter a number: "))
a = num1 + num2
print(a)


#q8

num = int(input("Enter a number: "))
if num== 1 or num==2 or num==12:
    print("winter")
elif num== 5 or num==3 or num==4:
    print("spring")
elif num== 6 or num==7 or num==8:
    print("summer")
elif num== 9 or num==10 or num==11:
    print("autum")
else:
    print("Invalid number")