n=int(input("Enter n"))
x=int(input("Enter the value of x"))
s=0
fact=1
series=0
for i in range(1,n+1):
    if i%2==1:
        s=s+(x**i)
    else:
        s=s-(x**i)
    fact=fact*i
    series=s/fact
print(series)
