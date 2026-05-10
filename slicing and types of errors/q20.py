earth = float(input("Earth weight: "))
planet = int(input("Planet number (1-7): "))

gravity = [0.38,0.91,0.38,2.34,1.06,0.92,1.19]

if 1 <= planet <= 7:
    print("Weight =", earth * gravity[planet-1])
else:
    print("Invalid planet number")