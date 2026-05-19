class_list =  {'Ram','Sita','Laxman'}
new_student= input("Enter the student's name: ")
if not new_student  in class_list:
    class_list.add(new_student)
    print(class_list)
else:
    print("Student already exist")