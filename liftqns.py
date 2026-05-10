
total = float(input("Enter total purchase amount: $"))

if total >= 5000:
    membership = input("Is membership card present? (yes/no): ").lower()
    if membership == "yes":
        discount = total * 0.30
        print(f"Total Saved: ${discount:.2f}")
        print(f"Final Bill: ${total - discount:.2f}")
    else:
        print(f"Total: ${total:.2f}, Discount: $0")
else:
    print(f"Total: ${total:.2f}, Discount: $0")