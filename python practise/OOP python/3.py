number = int(input("Enter a number: "))
if number ==1:
    print("Spring")
elif number ==2:
    print("Summer")
else:
    print("Invalid number")


#match case
number = int(input("Enter a number: "))
match number:
    case 1: print("Spring")
    case 2: print("Summer")
    case _: print("Invalid number")
