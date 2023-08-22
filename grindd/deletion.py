def bins(l,a):
    beg=0
    last=len(l)-1
    while beg<=last:
        mid=(beg+last)//2
        if l[mid]==a:
            return a
        elif l[mid]>=a:
            last=mid-1
        else:
            beg=mid+1

l1=eval(input('Enter a list'))
a1=int(input('Enter number you want deleted'))
p=bins(l1,a1)
if p:
    for i in range(p-1,len(l1)-1):
        l1[i]=l1[i+1]
    l1.pop()
    print('The list after deletion=',l1)

else:
    print('The element was not found')

