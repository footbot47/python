a=int(input("Enter a number"))
p=0
n=0
while a!=0:
    if a==0:
        break
    elif a>0:
        p=p+1
    elif a<0:
        n=n+1
    a=int(input("Enter a number"))
print("Number of positive integers=",p)
print("Number of negative integers=",n)
