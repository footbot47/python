L=eval(input("Enter a list"))
L1=len(L)
for i in range(0,L1):
    if i<L1:
        L[i]=L[i]+L[i+1]
    elif i>=L1:
        break
print(L)
