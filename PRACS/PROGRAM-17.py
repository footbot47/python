a=input("Enter a string")
l=len(a)
cnt=0
for i in range(l):
    print(a[i])
print("The string in reversed order:-")
for i in range(-1,(-l-1),-1):
    print(a[i])
inp=input("Enter a letter whose frequency you want checked")
for i in range(l):
    if inp==a[i]:
        cnt=cnt+1
print("The number of times",inp,"was repeated=",cnt)

    
