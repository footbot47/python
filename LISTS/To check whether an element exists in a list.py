a=eval(input("Enter a list of numbers"))
l=len(a)
e=int(input("Enter the element you want searched"))
for i in range(0,l):
    if a[i]==e:
        print("The given element exists in the list at index",i)
    else:
        print("The element does not exist in the list")
