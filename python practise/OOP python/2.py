traffic_light = input("Enter traffic light color(red, green, yellow): ")
if traffic_light == "red":
    print("Stop")
elif traffic_light == "green":
    print("Go")
elif traffic_light == "yellow":
    print("Ready to go")
else:
    print("Not a valid traffic light color")


#match case
traffic_light = input("Enter traffic light color(red, green, yellow): ")
match traffic_light:
    case "red": print("Stop")
    case "green": print("Go")
    case "yellow": print("Ready to go")
    case _: print("Not a valid traffic light color")