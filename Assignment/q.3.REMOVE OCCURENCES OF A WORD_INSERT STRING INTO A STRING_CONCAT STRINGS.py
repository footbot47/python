print("1.To remove all occurences of a given word")
print("2.To insert a string within another string in a given position")
print("3.To concatenate two strings in a third string")
choice=int(input("enter choice:"))
if choice not in [1,2,3]:
    print("invalid input")
s=input("enter a string:")
def remove(s):
    w=" "
    a=list()
    a=s.split()
    x=input("enter the word you want to remove :")
    d=[]
    l=[]
    if x in a:
        for i in range(len(a)):
            if a[i]==x:
                d.append(a[i])
            else:
                l.append(a[i])
    else:
        print(x,"not in the string")
    for j in range(0,len(l)):
        w=w+" "+l[j]
    return w
if choice==1:
    print("new string with the removed words",remove(s))

def insert(s):
    w=""
    pos=int(input("which position should the inserted word hold :"))
    word=input("enter the word to be inserted:")
    a=s.split()
    a.insert(pos-1,word)
    for i in range(0,len(a)):
        w=w+" "+a[i]
    return w
if choice==2:
    print("string with inserted string:",insert(s))

def concat(s):
    w=""
    s1=input("another string:")
    a=s.split()
    b=s1.split()
    for i in range(0,len(a)):
        w+=a[i]
    for j in range(0,len(b)):
        w+=b[j]
    return(w)
if choice==3:
    print("concatenated string=",concat(s))
#by pradipti class xii
    
        
    
                
                
            
        
