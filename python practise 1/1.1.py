student_marks = {"ram":93,"shyam":98,"hari":90}
result = student_marks.get("hira","students not found")
print(result)
print(student_marks.keys)

student_marks = {"ram":93,"shyam":98,"hari":90}
student_marks.get["sita"] = 75
print(student_marks)

#student_marks = {"ram":93,"shyam":98,"hari":90}
#student_marks["ram"]= 77
#student_marks.update(["sita":88, "laxman":73])
#print(student_marks)

#pop
student_marks = {"ram":93,"shyam":98,"hari":90}
student_marks.pop()
student_marks.popitem()
print(student_marks)

#keys values items

student_marks = {"ram":93,"shyam":98,"hari":90}
for i in student_marks:
    print(i)

for i in student_marks.keys():
    print(i)
for i in student_marks.values():
    print(i)
for i in student_marks.items():
    print(i)