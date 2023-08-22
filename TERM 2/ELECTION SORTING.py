election={}
ans='y'
names=""
values=0
while ans=='y':
    name=input("Enter party name")
    values=int(input("Enter the number of votes"))
    election[name]=values
    ans=input('Do you want to continue?(y/n)')

a=[]
b=[]
for i in election.keys():
    b+=[i,]
    a+=[election[i]]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        
        if a[j+1]>a[j]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[i]=temp
            n=b[i+1]
            b[i+1]=b[j]
            b[i]=n
print('Party','votes')
for p in range(0,len(a)):
    print(b[p],'    ',a[p])
    
    
