def create():
    f1=open("report.txt","w")
    s=input("enter:")
    f1.write(s)
    f1.close()
    f2=open("report.txt","r")
    d=f2.read()
    print(d)
def reverse():
    m=""
    f=open("report.txt","r")
    k=f.readlines()
    for i in range(len(k)):
        s=k[i]
        for j in range(-1,-len(s)-1,-1):
            m+=s[j]
    print(m)
    f.close()
    g=open("reverse.txt","w")
    g.write(m)
    g.close()
def remove():
    b=""
    s=input("enter the word to be removed:")
    f1=open("report.txt","r")
    g=f1.readlines()
    for i in range(len(g)):
        l=g[i]
        for j in range(len(l)):
            if l[j]!=s:
                b+=str(l[j])
    print(b)
while True:
    print("1.create")
    print("2.reverse")
    print("3.remove")
    choice=int(input("enter choice:"))
    if choice==1:
        create()
    elif choice==2:
        reverse()
    elif choice==3:
        remove()
    y=input("continue:")
    if y=="q":
        break
