class Student:
    name = "karan"
    def __init__(self):
        print(self)
        print("adding new student in database")

s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)

# class Student:
#     name = "karan"
#     def __init__(self, fullname):
#         self.name = fullname
#
#         print("adding new student in database")
#
# s1 = Student("karan")
# print(s1.name)
#
# s2 = Student("arjun")
# print(s2.name)


class Student:
    name = "karan"
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

        print("adding new student in database")

s1 = Student("karan", 53)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)