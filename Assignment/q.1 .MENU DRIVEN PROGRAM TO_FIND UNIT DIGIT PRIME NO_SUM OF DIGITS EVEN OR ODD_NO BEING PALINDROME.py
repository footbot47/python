print("1.The number in unit's place being a prime number")
print("2.sum of digits in a number being odd or even")
print("3.a number being a palindrome or not")
choice=int(input("enter choice in [1,2,3]:"))
if choice not in [1,2,3]:
    print("invalid choice")
def unit(x):
    s=str(x)
    cnt=0
    if int(s[-1])==0 or int(s[-1])==1:
        print(int(s[-1]),"is neither prime nor composite")
    elif int(s[-1])==2:
        print("2 is a prime number")
    else:
        for i in range(3,int(s[-1])):
            if int(s[-1])%i==0:
                continue
            elif int(s[-1])%i!=0:
                cnt+=1
    if cnt==len(range(3,int(s[-1]))):
        print("The unit's place digit is prime number")
        return(int(s[-1]))
    elif cnt!=len(range(3,int(s[-1]))):
        print("the unit's place digit is not prime")
        return(int(s[-1]))

if choice==1:
    x=int(input("enter a number:"))
    print(unit(x))


def s(x):
    st=str(x)
    sm=0
    for i in st:
        sm+=int(i)
    if sm%2==0:
        print("sum of digits is even")
        return(sm)
    else:
        print("sum of digits is odd")
        return(sm)
if choice==2:
    x=int(input("enter x:"))
    print(s(x))


def palin(x):
    rev=0
    a=x
    while x!=0:
        r=x%10
        x=x//10
        rev=rev*10+r
    if rev==a:
        print("palindrome number")
        return(rev)
    elif rev!=a:
        print("not a palindrome number!")
        return(rev)
if choice==3:
    x=int(input("enter x:"))
    print(palin(x))

  


