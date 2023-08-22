a=eval(input("Enter the elements of the list "))
l=len(a)
mine=a[0]
mini=0
for i in range(1,l-1):
    if a[i]<mine:
        mine=a[i]
        mini=i
print("The list is=",a)
print("The smallest element",mine,"is at the index",mini)
