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
obj2.x=100
print("X value is",obj2.x)

print("X value is",Myclass.x)
print("X value is",obj.x)


