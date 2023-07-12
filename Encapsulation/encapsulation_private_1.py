class Myclass:
    __x=10
    def __init__(self):
        print("Iam in constructor")
    def display(self):
        print("X value is",Myclass.__x) #private attributes can be accessed with the functions of that class

obj=Myclass()
#print("x value",obj.__x) attribute error as private attribute was declared outside
#print("x value",Myclass.__x) attribute error
obj.display()
