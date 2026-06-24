while True:
    age = int(input("Enter age: "))

    if 0 <= age <= 120:
        print("Valid age")
        break
    else:
        print("Invalid age")