class Base:
    def display(self):
        print("\n Iam display method from base class")

class derived(Base):
     def display(self):
        print("\n Iam display method from derived class")


d=derived()
d.display()
