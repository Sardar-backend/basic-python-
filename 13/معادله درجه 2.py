import cmath
a=float(input("enter"))
b=float(input("enter"))
c=float(input("enter"))
delta=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(delta))/(2*a)
root2=(-b+cmath.sqrt(delta))/(2*a)
print('The solution are{0}and{1}'.format(root1,root2))

    
