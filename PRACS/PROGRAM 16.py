a=input("Enter your sentence")
l=len(a)
cntw=0
cnts=0
cntd=0
for i in range(l):
    if a[i].isalpha()==1:
        print("The word at the",i,"th place=",a[i])
        cntw=cntw+1
    if a[i].isspace()==1:
        cnts=cnts+1
    if a[i].isdigit()==1:
        cntd=cntd+1
print("The number of words=",cntw)
print("The number of characters=",cnts)
print("The percentage of alpha numeric characters are=",cntd/l*100)

        
        
