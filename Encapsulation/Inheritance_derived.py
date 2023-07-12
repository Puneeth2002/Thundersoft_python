class MyBase:
    def __init__(self):
        print("this is mybase class constructor")
    def BaseDisplay(self):
        print("this is my baseclass Display method")
class MyDerived(MyBase):
    def DerivedDisplay(self):
        print("this is my DerivedDisplay method")
obj1 =MyBase()
obj1.BaseDisplay()
obj2=MyDerived()
obj1.BaseDisplay()
obj2.DerivedDisplay()

