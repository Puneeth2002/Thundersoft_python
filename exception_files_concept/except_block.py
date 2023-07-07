try:
 a = int(input("Enter Num1:"))
 b = int(input("Enter Num2:"))
 print("result is:", a * b)
 print("result is:", a / b)
 print("result is:", a + b)
 print("result is:", a - b)
except ZeroDivisionError as msg:
 print(msg)

