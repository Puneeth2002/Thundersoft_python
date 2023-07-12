class Myclass:
    x=10
    def __init__(self):
        print("Iam in constructor")
    def display(self):
        print("X value is",Myclass.x)

obj=Myclass()
obj.display()
print("X value is",Myclass.x)
print("X value is",obj.x)

obj2=Myclass()
print("X value is",obj2.x)
Myclass.x=100 #it will reflect for all the objects
obj2.x=50 #it will reflect only to that object (obj2)
print("X value is",obj2.x)

print("X value is",Myclass.x)
print("X value is",obj.x)
