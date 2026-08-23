class Person :
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()

s1 = Person()
print(s1.welcome())