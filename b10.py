balance = 1000
while True:
    print("\n----ATM Machine-----")
    print("1. check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("enter your choice"))
    if choice== 1:
        print("Your balance is; ", balance)
    elif choice == 2:
        amount = float(input("enter the amount: "))
        balance += amount
        print("Amount added successfully")
        print("your current balance is:",balance )
    elif choice == 3:
        amount = float(input("enter the amount: "))
        if balance>=amount:
            balance -= amount
            print("withdraw successful")
            print("New balance:", balance )
        else:
            print("Insufficient balance")
    elif choice == 4:
        print("Thank you for using ATM")
        break
    else:
        print("invalid choice")
