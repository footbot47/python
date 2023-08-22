a=eval(input("Enter a list"))
b=list(a)
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
    i=i-1
a.remove(a[0])
a.insert(0,b[-1])
print(a)
