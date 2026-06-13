while True:
    user_input = int(input ("Enter a number: "))
    if user_input <18:
        print("you are a minor ")
    elif user_input >18 and user_input <60:
        print("you are a adult ")
    elif user_input >=60:
        print("you are a senior citizen")
    else:
        print("invalid input")
    choice = input("Do you want to continue? (y/n)")
    if choice == "n":
        break
