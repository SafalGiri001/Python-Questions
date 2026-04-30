pin = input("Enter PIN: ")

if pin.isupper():
    print("Valid PIN")
else:
    print("Invalid PIN (must be uppercase)")