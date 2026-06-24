text = input("Enter a string: ")

result = ""
i = 0

while i < len(text):
    ch = text[i]

    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)

    elif 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)

    else:
        result += ch

    i += 1

print(result)