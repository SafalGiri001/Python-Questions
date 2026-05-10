balance = 20000
correct_pin = 3796

print("Welcome to the Global Bank ATM ")
user_pin = int(input("Please enter your four digit PIN: "))
if user_pin == correct_pin:
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Exit")

    choice = int(input("Select an option (1-3): "))
    if choice == 1:
        print(f"Your current balance is:Rs {balance}")
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= balance and amount<0:
            balance -= amount
            print(f"Please collect your cash: Rs {amount}")
            print(f"Your current balance is:Rs {balance}")
        else:
            print("Error: Insufficient balance!")
    elif choice == 3:
        print("Thank you for visiting. Have a nice day!")
    else:
        print("Invalid choice selected")
else:
    print("Invalid PIN")




