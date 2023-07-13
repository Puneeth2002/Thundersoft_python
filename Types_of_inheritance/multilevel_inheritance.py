class Base1:
    def display(self):
        print("\n Iam display method from base1 class")

class Base2(Base1):
    def display(self):
        print("\n Iam display method from base2 class")

class derived(Base2):
     print("\n Iam derived method from base2 class")


d=derived()
d.display()

print(derived.__mro__)
print(derived.mro())
