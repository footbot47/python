def create():
    o=open('new.txt','w')
    s=input('Enter a string')
    o.write(s)
    o.close()

def cntv():
    o=open('new.txt','r')
    cntv,cntd=0,0
    r=o.read()
    rl=list(r)
    l=len(rl)
    for i in range(l):
        if rl[i] in ('a','e','i','o','u'):
            cntv=cntv+1
        elif rl[i].isdigit():
            cntd=cntd+1
    print('The number of vowels',cntv)
    print('The number of digits',cntd)
    o.close()

def space():
    o=open('new.txt','r')
    s=''
    r=o.read()
    rl=list(r)
    l=len(rl)
    for i in range(l):
        if rl[i]==' ':
            s=s+'#'
        else:
            s=s+rl[i]
    print(s)

ans='y'
while ans=='y':

    print('text operations')
    print('1.create')
    print('2.count the vowels and digits')
    print('3.replace space with #')
    ch=int(input('Enter a choice'))
    if ch==1:
        create()
        ans=input('do you want to continue?')
    elif ch==2:
        cntv()
        ans=input('do you want to continue?')
    elif ch==3:
        space()
        ans=input('do you want to continue?')

    else:
        print('invalid input')
        ans=input('do you want to continue?')
        
        
    
