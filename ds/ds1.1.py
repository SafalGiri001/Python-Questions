student_records = {
    'id1': {'name': 'ram', 'email': 'ram124@gmail.com'},
    'id2': {'name': 'shyam', 'email': 'shyam001@gmail.com'}
}

name = input("Enter student name: ")

if student_records['id1']['name'] == name:
    print("Email:", student_records['id1']['email'])
elif student_records['id2']['name'] == name:
    print("Email:", student_records['id2']['email'])
else:
    print("contact not found")