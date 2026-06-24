def count_case(text):
    upper = 0
    lower = 0

    i = 0
    while i < len(text):
        ch = text[i]

        if 'A' <= ch <= 'Z':
            upper += 1
        elif 'a' <= ch <= 'z':
            lower += 1

        i += 1

    print("No. of upper case characters :", upper)
    print("No. of lower case characters :", lower)

count_case("The quick Brow Fox")