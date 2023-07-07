f = open("C:text.txt","w")#overrite my statements
print(f.write("this will overrite everything"))
print(f.write("Hello , this is puneeth onboarded in thundersoft to pursue my internship"))

f = open("C:text.txt","r")
for x in f:
    print(x)
