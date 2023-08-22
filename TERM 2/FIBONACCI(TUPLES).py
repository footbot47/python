n=int(input("Enter n"))
d=[0,1,]
a=0
b=1
for i in range(0,n+1):
    c=a+b
    d.append(c)
    a=b
    b=c
print(d)
