t=eval(input("Enter tuple"))
a=list(t)
b=a[2::3]
c=[]
for i in b:
    d=i**3
    c.append(d)
print("Tuple=",tuple(c))
