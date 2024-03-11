a=input("enter")
if a=="ali":
    file=open("ali.txt","w")
    file.write("hello")
    file=open("ali.txt","r")
    print(file.read())
elif a=="reza":
    file=open("reza.txt","w")
    file.write("hello")
    file=open("reza.txt","r")
    print(file.read())
else:
    print("error")
