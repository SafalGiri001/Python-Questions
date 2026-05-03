#qns9
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#qns10
marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    print("A")
elif 80 <= marks <= 89:
    print("B")
elif 70 <= marks <= 79:
    print("C")
else:
    print("Fail")

#qns11
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")

#qns12
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Other")

#qns13
color = input("Enter color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

#qns14
age = int(input("Enter age: "))
exp = int(input("Enter experience (years): "))

if age > 18 and exp >= 2:
    print("Eligible")
else:
    print("Not Eligible")

#qns15
temp = float(input("Enter temperature: "))

if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

#qns16
item = input("Enter item: ").lower()

if item == "pizza":
    print("$10")
elif item == "burger":
    print("$7")
elif item == "pasta":
    print("$8")
else:
    print("Item not available")

#qns17
height = float(input("Enter height (in feet): "))

if height >= 6:
    print("Selected")
else:
    print("Not Selected")

#qns18
age = int(input("Enter age: "))

if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")

#qns19
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")

#qns20
month = int(input("Enter month number: "))

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month")
