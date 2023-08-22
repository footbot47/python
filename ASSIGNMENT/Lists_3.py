L=eval(input("Enter the values"))
L1=len(L)
for i in range(1,L1-1):
    e=min(L)
    del(e)
    print(L)
    mine=L[0]
    if L[i]<mine:
        mine=L[i]
print("The second smallest element is",mine)
