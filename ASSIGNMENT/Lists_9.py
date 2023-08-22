a=input("Enter a string")
a1=len(a)
s=a[0]
b=a[a1-1]
a2=a
a4=len(a2)
for i in range(0,a1):
    a[0]=a[0].upper()
    a[a1-1]=a[a1-1].upper()
    a[0]=a2[0]
    a[a1-1]=a2[a4-1]
print(a2)


    
    
