print("1.decimal number to binary")
print("2.binary to decimal nuber")
print("3.octal to binary number")
choice=int(input("enter choice in [1,2,3]:"))
def bin(x):
    l=[]
    s=""
    while x!=0:
        a=x%2
        l.append(a)
        x=x//2
    l.reverse()
    for i in range(len(l)):
        s+=str(l[i])
    return(int(s))
if choice==1:
    x=int(input("enter a decimal number:"))
    print("binary form of ",x,"=",bin(x))
def dec(x):
    s=""
    sm=0
    l=[]
    a=str(x)
    l=list(a)
    l.reverse()
    for i in range(0,len(l)):
        s+=str(int(l[i])*2**i)
    for j in range(len(s)):
        sm+=int(s[j])
    print("binary form of the decimal no:",x,"=")
    if ["0","1"] in l:
        return(int(sm))
    else:
        print(x,"is not a binary number")
        return
    
if choice==2:
    x=int(input("a binary number:"))
    print(dec(x))
def octbin(x):
    s=""
    octal={"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
    l=list(str(x))
    for i in l:
        if i in ["0","1","2","3","4","5","6","7"]:
            s+=(octal[i])
        elif i not in ["0","1","2","3","4","5","6","7"] :
            print(i,"is not an octal number")
            break
    if s=="":
        print("conversion not possible as it contains non octal value")
    else:
        return(int(s))
if choice==3:
    x=int(input("an octal number:"))
    print("the binary form of octal number",x,"=",octbin(x))
if choice not in[1,2,3]:
    print("invalid input")
#by pradipti class xii
    
    
        
        


        
    
    
