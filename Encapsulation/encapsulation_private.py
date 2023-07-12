class Myclass:
    __x=10
    def __init__(self):
        print("Iam in constructor")
    def display(self):
        print("X value is",Myclass.__x)

obj=Myclass()
obj.display()
#print("X value is",Myclass.__x)
#print("X value is",obj.__x)

obj2=Myclass()
#print("X value is",obj2.__x)
Myclass.__x=100 #it will reflect for all the objects
obj2.__x=50 #it will reflect only to that object (obj2)
print("X value is",obj2.__x)

print("X value is",Myclass.__x)
print("X value is",obj.__x)
