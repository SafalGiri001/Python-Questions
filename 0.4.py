#q11
age = int(input("Age: "))
if age<13:
    print("You are a child")
elif age>=13 and age<=18:
    print("You are a teenager")
elif age>18:
    print("You are adult")
else:
    print("Invalid number")

#q12
character = input("Enter a character: ")
if character.isupper():
    print("The character is uppercase")
elif character.islower():
    print("The character is lowercase")
elif character.isdigit():
    print("The character is a number")
else:
    print("Invalid character")


#q13
color = int(input("Enter a color(1-3): "))
match color:
    case 1: print("Stop")
    case 2: print("Get Ready")
    case 3: print("G0")
    case _: print("Invalid input")


#q14
age = int(input("Age: "))
experience = int(input("Experience: "))
if age>18 and experience>=2:
    print("Eligible")
else:
    print("Not Eligible")


#15
temperature = int(input("Enter a temperature: "))
if temperature>30:
    print("It's hot, stay hydrated")
elif temperature>=15 and temperature<=30:
    print("Enjoy the weather!")
elif temperature<15:
    print("It's cold, wear warm clothes")
else:
    print("Invalid temperature")


