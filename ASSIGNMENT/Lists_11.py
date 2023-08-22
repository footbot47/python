L=eval(input("Enter the values"))
L1=len(L)
for i in range(0,L1):
    if i%2==0:
        L[i]=0.5(L[i])
    else:
        L[i]=2(L[i])
print(L)
