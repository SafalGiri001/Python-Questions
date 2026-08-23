class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def average(self):
        avg = (self.mark1 + self.mark2 +self.mark3)/3
        print("Average", avg)
s1 = Student("Ram", 44 ,55,66)
print(s1.name)
s1.average()


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for value in self.marks:
            sum += value

        print("hi",self.name, "your average score is ", sum/3)
s1 = Student("Ram", [44 ,55,66])
print(s1.name)
s1.average()

