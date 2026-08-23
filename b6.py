questions =[
    "What is the capital of nepal? ",
    "what is 5 + 3?",
    "which language are we learning?"
]
answers = ["kathmandu", "8","python" ]
score = 0
for i in range (len(questions)):
    print("/nQuestions", i +1)
    print(questions[i])

    answer = input("your answer: ")

    if answer.lower() == answers[i].lower():
        print("correct! you guessed it right")
        score += 1
    else:
        print("wrong")


print("Quiz finished")
print (f'score: {score}')
