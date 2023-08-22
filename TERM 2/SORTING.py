l=[]
s=[]
l=eval(input('Enter 3 digit numbers'))
for k in range(0,len(l)):
    c=l[k]%10
    s+=[c,]
for i in range(0,len(l)):
    key=l[i]
    key1=s[i]
    j=i-1
    while j>0 and key<l[j]:
        s[j+1],s[j]=l[j+1],l[j]
        j=j-1
    else:
        s[j+1]=key
        l[j+1]=key1
print(l)
