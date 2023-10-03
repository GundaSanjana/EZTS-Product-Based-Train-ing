'''class MyClass:
    def __init__(self):
        self.a = input("enter the string: ")
        self.b = int(input("enter the num1: "))
        self.c = int(input("enter number 2: "))
    def m1(self):
        print(self.a[::-1])
        print(self.c**2)

    def display_res(self):
        print(len(self.a))
        print(self.b%self.c)

obj=MyClass()
obj.m1()
obj.display_res()'''


class MyClass:
    def __init__(self):
        self.a = input("enter the string: ")
        self.b = int(input("enter the num1: "))
        self.c = int(input("enter number 2: "))
    def m1(self,x,y):
        x=x[::-1]
        print(x)
        m=y**2
        print(m)

    def display_res(self):
        print(len(self.a))
        print((self.b) % (self.c))

obj=MyClass()
obj.m1("sanju",2)
obj.display_res()
