print("1.10^logx=x ")
print("2. root of(3^2+4^2)=5")
choice=int(input("enter choice:"))
if choice==1:
    x=int(input("enter x:"))
    if x>0:
        import math
        z=math.pow(10,math.log(x))
        if z==x:
            print("identity is verified as : LHS=",z,"= RHS,",x)
        else:
            print("identity is not verified as",z,"not equal to",x)
elif choice==2:
    import math
    z=math.sqrt(math.pow(3,2)+math.pow(4,2))
    if z==5:
        print("identity is verified")
#by pradipti class xii
