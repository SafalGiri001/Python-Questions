sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
i = 0

while i < len(sentence):
    ch = sentence[i]

    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    i += 1

print("Vowels =", vowels)
print("Consonants =", consonants)