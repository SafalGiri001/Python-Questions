age = int(input("What is your age? "))
height = int(input("What is your height(cm)?"))
if age >= 12:
    if height>=140:
        print("You are acceptable")
    else:
        print("You are not acceptable")
else:
    print("You can not ride the roller coaster")

#q2
color = input("Enter the color of traffic light(red,yellow,green): )")
if color ==