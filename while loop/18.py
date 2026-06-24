text = input("Enter a string: ")

result = ""
i = 0

while i < len(text):
    if text[i].lower() not in "aeiou":
        result += text[i]

    i += 1

print(result)