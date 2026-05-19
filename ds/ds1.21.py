valid_courses = {"python", "robotics", "java"}
hs_grades = list(range(9, 13))

name = input("Enter student name: ")
course = input("Enter course: ")
grade = int(input("Enter grade: "))

student_records = {
    "name": name,
    "course": course,
    "grade": grade
}


if course not in valid_courses:
    print(f"{name} selected an invalid course.")

else:

    if grade < 9:
        print("grade too low")
    elif grade > 12:
        print("grade too high")
    else:
        if course == "robotics" and grade == 9:
            print(f"{name} is not eligible for {course} grade too low")
        else:
            print(f"{name} is approved for {course}")