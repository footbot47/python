a=int(input("Enter a number"))
lim=int(a/2)+1
for i in range(2,lim):
    rem=a%i
    if rem==0:
        print(a,"is not a prime number")
    else:
        print(a,"is a prime number")
        
