def create():
    o=open('marks.dat','w')
    roll=int(input('Enter the roll number'))
    n=input('Enter name')
    m=int(input('Enter marks'))
    f=str(roll)+'|'+n+'|'+str(m)
    o.write(f)
    o.close()

def append():
    o=open('marks.dat','a')
    roll=int(input('Enter the roll number'))
    n=input('Enter name')
    m=int(input('Enter marks'))
    f=str(roll)+'|'+n+'|'+str(m)
    o.write(f)

def display():
    o=open('marks.dat','r')
    r=o.read()
    print('The contents of the file are:-')
    print(r)

def search():
    x=input('Enter string that you want searched')
    o=open('marks.dat','r')
    r=o.read()
    if x in r:
        print('found')
    else:
        print('not found')

ans='y'
while ans=='y':
    print('1.create')
    print('2.append')
    print('3.display')
    print('4.search')
    ch=int(input('Enter your choice'))
    if ch==1:
        create()
        ans=input('do you want to continue?')
    elif ch==2:
        append()
        ans=input('do you want to continue?')
    elif ch==3:
        display()
        ans=input('do you want to continue?')
    elif ch==4:
        search()
        ans=input('do you want to continue?')
    else:
        ans=input('do you want to continue?')

