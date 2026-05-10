total = float(input("Enter total purchase amount: "))
member = input("Are you a member? (yes/no): ")

if total > 1000:
    if member == "yes":
        final = total * 0.8
    else:
        final = total * 0.9
else:
    final = total

print("Final Bill =", final)