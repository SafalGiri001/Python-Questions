light = input("Enter light (red/yellow/green): ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready")
elif light == "green":
    print("Go")
else:
    print("Invalid light")