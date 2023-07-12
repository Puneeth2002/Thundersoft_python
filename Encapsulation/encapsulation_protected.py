#protected ( it will be accessed by single underscore)
#private ( it will be accessed by double underscore)

class Myclass:
    _x=10
    def __init__(self):
        print("Iam in constructor")
    def display(self):
        print("X value is",Myclass._x) #private attributes can be accessed with the functions of that class

obj=Myclass()
print("x value",obj._x)# no attribute error because protected attribute was declared outside
print("x value",Myclass._x) 
obj.display()
