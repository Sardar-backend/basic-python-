a=input("enter")
b=input("enter")
file=open("n.txt","w")
file.write(a)
file.write(b)
file=open("n.txt","r")
print(file.read())
