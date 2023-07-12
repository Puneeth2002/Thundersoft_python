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
