class Base:
    def display(self):
        print("\n Iam display method from base1 class")

class child1(Base):
    def display(self):
        super().display()
        print("\n Iam display method from child1 class1")

class child2(Base):
    def display(self):
        super().display()
        print("\n Iam derived method from child2 class2")

class Grandchild(child1,child2):
    def display(self):
        print("\n iam from display method from grandchild")
     

d=child1()
d.display()


print(child1.__mro__)
print(child1.mro())

d=child2()
d.display()

print(child2.__mro__)
print(child2.mro())

d=Grandchild()
d.display()

print(Grandchild.__mro__)
print(Grandchild.mro())
