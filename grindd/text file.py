def create():
    o=open('report.txt','w')
    s=input('enter a string')
    o.write(s)
    o.close()
    o1=open('report.txt','r')
    r=o1.read()
    print(r)

def rev():
    o=open('report.txt','r')
    rev=''
    r=o.read()
    rl=r.split(' ')
    l=len(rl)
    for i in range(l):
        w=rl[i]
        print(w)
        l1=len(w)
        for j in range(l1-1,-1,-1):
            print(rl[i][j])
            rev=rev+str(rl[i][j])
            if j==-1:
                print(' ')
    print(rev)
            

print('file handling')
print('1.create')
print('2.reverse')
ch=int(input('Enter a choice'))
if ch==1:
    create()
elif ch==2:
    rev()
