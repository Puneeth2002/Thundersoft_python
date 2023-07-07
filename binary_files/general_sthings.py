f = open("C:text.txt","r")
print(f.read())
print("file name is:",f.name)
print("file mode is:",f.mode)
print("is file readable?",f.readable())
print("is file writable?",f.writable())
print("is file closed?",f.closed())
