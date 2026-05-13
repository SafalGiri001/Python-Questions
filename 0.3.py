#6
a= int(input("Enter first number: " ))
b = int(input("Enter second number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


#7
salary = int(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary>= 50000 and credit_score>=700:
    print("you are eligible for car loan")
else:
    print("you are not eligible for car loan")

#8
number = int(input("Enter your number: "))
if number%3==0 and number%5==0:
    print("FizzBuzz")
elif number%5==0:
    print("Buzz")
elif number%3==0:
    print("Fizz")
else:
    print("your number is: ", number)

#9
a = input("enter a word(a,e,i,o,u): ").lower()
if a in "aeiou":
    print("It is vowel")
else:
    print("It is consonant")

#10
grades = int(input("Enter your grades: "))
if grades >= 90 and grades <= 100:
    print("A")
elif grades >= 80 and grades < 90:
    print("B")
elif grades >= 70 and grades < 80:
    print("C")
elif grades<70:
    print("Fail")
else:
    print("Invalid grades")
