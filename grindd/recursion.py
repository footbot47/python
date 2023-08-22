def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

def s(l,n):
    if n==0:
        return l[0]
    else:
        return l[n]+s(l,n-1)

def fib(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
a='y'
while a=='y':
    print('1.factorial')
    print('2.sum')
    print('3.fibonacci')
    n=int(input('Enter n'))
    ch=int(input('Enter a choice'))
    if ch==1:
        ans=fact(n)
        print(ans)
        a=input('do you want to continue')
    elif ch==2:
        l1=eval(input('Enter a list'))
        ans=s(l1,n)
        print(ans)
        a=input('do you want to continue')

    elif ch==3:
        ans=fib(n)
        print(ans)
        for i in range(n):
            print(fib(i),end=',')
        a=input('do you want to continue')

    else:
        print('invalid')


        
        
