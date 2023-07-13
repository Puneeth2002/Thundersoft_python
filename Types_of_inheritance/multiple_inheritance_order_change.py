class Base1:
    def display(self):
        print("\n Iam display method from base1 class")

class Base2:
    def display(self):
        print("\n Iam display method from base2 class")

class derived(Base1,Base2):
     pass


d=derived()
d.display()
