class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks


    def average(self):
        average = sum((self.marks))/len(self.marks)
        return average

s1 = Student("jod",[12,13,14])
print(s1.name,s1.marks)
print(s1.average())