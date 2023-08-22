a={}
b={}
c=0
n=int(input("Number of values"))
for i in range(n):
    
            key=input("Enter key")
            val=input('Enter value')
            a[key]=val
d=list(a.values())
for i in range(0,len(d)):
    c=d.count(d[i])

if c>1:
    print('2 keys have the same values')
elif c==1:
    print('No key has the same value')

    
        
    
