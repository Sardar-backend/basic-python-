import os
import time
a=input("enter")
if a=="yes":
    time.sleep(5)
    os.system("shutdown/r")
elif a=="no":
    time.sleep(5)
    os.system("shutdown/s")
else:
    time.sleep(5)
    print("error")
