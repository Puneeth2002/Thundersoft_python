f = open("C:text.txt","a")
print(f.write("This is the appending statement"))

f = open("C:text.txt","r")
for x in f:
    print(x)
