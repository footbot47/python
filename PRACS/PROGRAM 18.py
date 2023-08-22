a=eval(input("Enter the elements of the list"))
l=len(a)
maxe=a[0]
maxi=0
for i in range(l):
    if a[i]%2==0:
        if a[i]>maxe:
            maxe=a[i]
            maxi=i
print("The largest even element is",maxe)
