NumberA=input()
heightA=input()
weightA=input()
ageA=input()
NumberB=input()
heightB=input()
weightB=input()
ageB=input()
y,n,m=0,0,0
class A:
    def __init__(self,NumberA,heightA,weightA,ageA):
       self.Number=NumberA
       self.height=heightA
       self.weight=weightA
       self.age=ageA
    def AverageclassA(self):
        a=(self.height).split(' ')
        b=(self.weight).split(' ')
        c=(self.age).split(' ')
        for i in a:
            y=y+int(i)
        g=y/self.Number
        for i in b:
            n=n+int(i)
        t=n/self.Number
        for i in c:
            m=m+int(i)
        r=m/self.Number
        return g,t,r
class B:
    def __init__(self,NumberB,heightB,weightB,ageB):
       self.Number=NumberB
       self.height=heightB
       self.weight=weightB
       self.age=ageB
    def AverageclassB(self):
        a=(self.height).split(' ')
        b=(self.weight).split(' ')
        c=(self.age).split(' ')
        for i in a:
            y=y+int(i)
        k=y/self.Number
        for i in b:
            n=n+int(i)
        q=n/self.Number
        for i in c:
            m=m+int(i)
        e=m/self.Number
        return y,n,e
obj1=A(NumberA,heightA,weightA,ageA)
obj2=B(NumberB,heightB,weightB,ageB)
print(obj1.AverageclassA())