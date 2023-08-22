#My special series
n=int(input("Enter your range"))
a=1
b=1
c=2
print(a,b,c,end="")
for i in range(1,n):
    t=a+b*c
    print(t,end=" ")
    a=b
    b=c
    c=t

    

