line=input("Enter a string")
cntl=cntu=0
dcount=counta=0
for a in line:
    if a.islower():
        cntl=cntl+1
    elif a.isupper():
        cntu=cntu+1
    elif a.isdigit():
        dcount=dcount+1
    elif a.isalpha():
        counta=counta+1
print("No. of uppercase letters=",cntu)
print("No. of lowercase letters=",cntl)
print("No. of digits=",dcount)
print("No. of alphabets=",counta)
