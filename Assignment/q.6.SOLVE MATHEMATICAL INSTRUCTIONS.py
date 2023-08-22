#mathematical instructions
print("1. 2-ye^2y+4y")
print("2. cosx/tanx+x")
print("3. |e^x-x^2-x|")
print("4. p+q(r+5)^4")
choice=int(input("enter choice:"))
if choice==2:
    x=int(input("enter value for x:"))
    def two(x):
        import math
        z=math.cos(x)/(math.tan(x)+x)
        return z
elif choice==1:
    y=int(input("enter y:"))
    def one(y):
        import math
        z=2-(y*(math.e)**(2*y))+4*y
        return z
elif choice==3:
    x=int(input("enter x:"))
    def three(x):
        import math
        z=math.pow(math.e,x)-math.pow(x,2)-x
        if z%10 in [-1,-2,-3,-4,-5,-6,-7,-8,-9,-0]:
            return(-z)
        else:
            return z
elif choice==4:
    p=int(input("enter p:"))
    q=int(input("enter q:"))
    r=int(input("enter r:"))
    def four(p,q,r):
        import math
        z=p+q*(math.pow((r+5),4))
        return z
if choice==1:
    print(one(y))
elif choice==2:
    print(two(x))
elif choice==3:
    print(three(x))
elif choice==4:
    print(four(p,q,r))
else:
    print("invalid choice")
#by pradipti class xii
    
    
    
    
    
