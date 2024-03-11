a=float(input("enter"))
b=float(input("enter"))
if a>80 and b<30:
    print("rain")
elif a>80 and b<10:
    print("show")
elif a<80 or b>30:
    print("warm")
