a=input("Enter a string")
s=0
if a.isalnum()==1:
    for i in range(len(a)):
        if a[i].isdigit()==1:
            print(a[i])
            s=s+int(a[i])
else:
    print("The string has no numbers")
print("The sum of the digits in",a,"is",s)
