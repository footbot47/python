a=input("Enter a string")
b='ly'
c='ing'
l=len(a)
if l>=3:
    if a.rstrip(c)==1:
        a=a+str(b)
        print(a)
    else:
        a=a+str(c)
        print(a)
else:
    print("Lenght of string is too small")
    
