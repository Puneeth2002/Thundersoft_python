f=open("sample.txt",'w')
l=["sai\n","ram\n","mohan\n","durga\n"]
f.writelines(l)
print("List data written to the file")
f.close()
