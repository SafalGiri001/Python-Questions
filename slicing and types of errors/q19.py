total = float(input("Total amount: "))
member = input("Member? (True/False): ")

if total > 1000 and member == "True":
    total *= 0.8
elif total > 1000:
    total *= 0.9

print("Final Amount =", total)