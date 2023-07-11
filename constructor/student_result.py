class student:
    def __init__(self,Sno,Sname,Smarks):
        self.rno=Sno
        self.name=Sname
        self.marks=Smarks
    def read_data(self):
        print("\n Enter student details:")
        self.rno=input("Enter Rollnumber:")
        self.name=input("Enter student name:")
        self.marks[0]=eval(input("Enter Marks in sub1:"))
        self.marks[1]=eval(input("Enter Marks in sub2:"))
        self.marks[2]=eval(input("Enter Marks in sub3:"))
        self.marks[3]=eval(input("Enter Marks in sub4:"))
        self.marks[4]=eval(input("Enter Marks in sub5:"))
        self.marks[5]=eval(input("Enter Marks in sub6:"))
    def calculate(self):
        self.total= self.marks[0]+self.marks[1]+self.marks[2]+self.marks[3]+self.marks[4]+self.marks[5]
        self.avg=self.total/6
        if ( self.marks[0]< 35 or self.marks[1]< 35 or self.marks[2]< 35 or self.marks[3]< 35 or self.marks[4]< 35 or self.marks[5]< 35 ):
            self.result="fail"
        elif self.avg>=60:
            self.result="First class"
        elif self.avg>=50:
            self.result="Second class"
        else: 
            self.result="Third class"
    def display(self):
        print("student rno is :",self.rno)
        print("student name is :",self.name)
        print("student marks is :",self.marks)
        print("student total marks is :",self.total)
        print("student avg marks is :",self.avg)
        print("student result is :",self.result)

s1=student("1","sai",[35,35,35,35,35,35])
s1.read_data()
s1.calculate()
s1.display
