import math
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
d=b**2-4*a*c
if a==0:
    print("Invalid input")
elif d>0:
    print("Roots are real")
    r1=-b+math.sqrt(d)/2*a
    r2=-b-math.sqrt(d)/2*a
    print(r1,r2,"are the roots")
elif d==0:
    print("Roots are real and equal")
    r1=-b/2*a
    print(r1,"is the root")
else:
    print("Roots are unequal")
    x=-b/2*a
    y=math.sqrt(math.fabs(d)/2*a)
    print(x,'+',y,'j')
    print(x,'-',y,'j')
