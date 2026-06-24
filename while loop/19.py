text = input("Enter a string: ")

count = 0
i = 0

while i < len(text) - 1:
    if text[i:i+2] == "hi":
        count += 1

    i += 1

print("'hi' appears", count, "times")