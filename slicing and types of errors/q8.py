num = int(input("Enter number (1-4): "))

match num:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Unknown")