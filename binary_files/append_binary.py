f = open("C:text1.txt","a+")
print(f.write("This is the appending statement"))

f = open("C:text1.txt","r")
for x in f:
    print(x)
