quiz_data={
    'qn1':{
        'question':'which Phyton library is used for building desktop GUI?',
        'option':['NumPy', 'Tkinter', 'Pandas', 'Flask'],
        'answer':'Tkinter'
    },
        'qn2':{
        'question':'What is the result of 4==7 in Python?',
        'option':['True', 'False', 'Error', 'None'],
        'answer':'False'
    },
        'qns3' : {
        'question':'Which set method is used to check if two sets have no common items ?',
        'option':['issubset()', 'intersection()', 'isdisjoint()', 'difference()'],
        'answer':'isdisjoint()'
    }
}

score = 0
for key,value in quiz_data.items():
    print(key,' ',value['question'])
    for values in value['option']:
        print(value)
    user_input = input('Enter your answer: ')
    if user_input in value['answer']:
        score += 1
print(f'Your score is: {score}')
