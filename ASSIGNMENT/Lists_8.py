L=eval(input("Enter values"))
L1=len(L)
for i in range(0,L1):
    L[i]=L[i+1]
    if i==L1-1:
        L[i]=L[0]
print(L)
        

    
