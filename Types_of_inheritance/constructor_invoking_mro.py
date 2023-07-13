class Base:
    def __init__(self):
        print("\n Iam constructor from base class")
    def display(self):
        print("\n Iam display method from base class")

class child1(Base):
    def __init__(self):
        print("\n Iam constructor from child class1")
        super().__init__()
    def display(self):
        super().display()
        print("\n Iam display method from child1 class1")

class child2(Base):
    def __init__(self):       
        print("\n Iam constructor from child class2")
        super().__init__()
    def display(self):
        super().display()
        print("\n Iam display method from child class2")

class Grandchild(child1,child2):
    def __init__(self):
        print("\n Iam constructor from grand child class")
        super().__init__()
    def display(self):
        super().display()
        print("\n iam from display method from grandchild")
     


'''d=child1()
d.display()


print(child1.__mro__)
print(child1.mro())

d=child2()
d.display()

print(child2.__mro__)
print(child2.mro())
'''
d=Grandchild()
#d.display()

print(Grandchild.__mro__)
print(Grandchild.mro())
