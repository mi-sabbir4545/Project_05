# Multilevel Inheritance

'''class A:
    def display1(self):
        print("I am inside A class")


class B(A):
    # display1()
    def display2(self):
        print("I am inside B class")


class C(B):
    # display1()
    # display2()
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")

ob1 = C()
# ob1.display1()
# ob1.display2()
ob1.display3()'''

# multiple inheritance

class A:
    def display(self):
        print("I am inside A class")


class B:
    # display1()
    def display(self):
        print("I am inside B class")


class C(A,B):
    pass
    # display1()
    # display2()


ob1 = C()
# ob1.display1()
# ob1.display2()
ob1.display()