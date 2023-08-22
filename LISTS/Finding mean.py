a=eval(input("Enter the list "))
l=len(a)
m=0
s=0
for i in range(l):
    s=s+a[i]
m=s/l
print("The mean of the given list is",m)
