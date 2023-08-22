a=input("Enter a string")
l=len(a)
s=0
if a.isalnum()==1:
    for i in range(l):
        if a[i].isdigit()==1:
            print(a[i])
            s=s+int(a[i])
else:
    print("The string has no digits")
print("The sum of the digits in the string=",s)

        
