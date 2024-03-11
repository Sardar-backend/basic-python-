a=int(input("enter"))
i=1
for i in range(1,a):
    b=a%i
    if b==0:
      print(i,"-",end='')
