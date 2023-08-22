a=input("Enter a string")
a1=len(a)
e=str('')
if a1<2:
    print(e)
else:
    d=a[0]+a[1]+a[a1-2]+a[a1-1]
    print(d,"is the required output")
