f = open("C:text1.txt","w+")
print(f.write("this will overrite everything"))
print(f.write("Hello , this is puneeth onboarded in thundersoft to pursue my internship"))

f = open("C:text1.txt","r")
for x in f:
    print(x)
