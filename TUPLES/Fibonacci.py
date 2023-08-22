a,b=0,1
fib=(a,b)
for i in range(0,10):
	a,b=b,a+b
	fib+=(b,)
print(fib)
a=int(input("Enter a value"))
a1=fib[a]
print(fib[a],"is the element")

