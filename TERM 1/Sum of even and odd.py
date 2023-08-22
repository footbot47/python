n=int(input("Enter the limit"))
ctr=1
so=se=0
while ctr<=n:
    if ctr%2==0:
        se=se+ctr
    else:
        so=so+ctr
    ctr=ctr+1
print("The sum of even integers is",se)
print("The sum of odd integers is",so)
