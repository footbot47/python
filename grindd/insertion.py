def fp(l,a):
    l.sort()
    s=len(l)
    if l[0]==a:
        return 0
    else:
        p=-1
        for i in range(s-1):
            if l[i]<=a and a<l[i+1]:
                p=i+1
                break
        if p==-1 and i<=s-1:
            p=s
        return p

def shift(l,p):
    l.append(None)
    s=len(l)
    i=s-1
    while i>p:
        l[i]=l[i-1]
        i=i-1


l=eval(input('ENTER LIST'))
a=int(input('enter a'))
pos=fp(l,a)
shift(l,pos)
l[pos]=a
print(l)
