grades = {
    'ram' : 92,
    'sita' : 88
}
student_name = input("enter student name: ")
if student_name == 'ram':
    grade = grades['ram']
    print(grade)
elif student_name == 'sita':
    grade = grades['sita']
    print(grade)
else:
    print("grade is not available")