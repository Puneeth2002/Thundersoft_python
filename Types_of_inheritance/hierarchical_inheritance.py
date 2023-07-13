class Base:
    def display(self):
        print("\n Iam display method from base1 class")

class child1(Base):
    def display(self):
        print("\n Iam display method from child1 class1")

class child2(Base):
     print("\n Iam derived method from child2 class2")


d=child1()
d.display()


print(child1.__mro__)
print(child1.mro())

d=child2()
d.display()

print(child2.__mro__)
print(child2.mro())
