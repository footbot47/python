L=eval(input("Enter values"))
l1=len(L)
mine=L[0]
maxe=L[0]
for i in range(1,l1):
    if L[i]<mine:
        mine=L[i]
    if L[i]>maxe:
        maxe=L[i]
print("The minimum element is",mine)
print("The maximum element is",maxe)
rnge=maxe-mine
print("The range is",rnge)

    
