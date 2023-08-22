#even and odd numbers
cnte=0
cnto=0
for a in range(1,11):
    n=int(input("Enter a number"))
    if n%2==0:
        cnte=cnte+1
    else:
        cnto=cnto+1
print(cnte,"is the number of even numbers")
print(cnto,"is the number of odd numbers")
