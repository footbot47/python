L=eval(input("Enter values"))
l1=len(L)
se=0
so=0
for i in range(0,l1):
    if i%2==0:
        se=se+L[i]
    else:
        so=so+L[i]
diff=se-so
print("The sum of the even indexed elements are",se)
print("The sum of the odd indexed elements are",so)
print("Sum of even-Sum off odd=",diff)

        
