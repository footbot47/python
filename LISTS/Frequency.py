a=eval(input("Enter the elements of the list"))
l=len(a)
cnt=0
el=int(input("Enter an element who's frequency you want checked"))
for i in range(0,l):
     if a[i]==el:
         cnt=cnt+1
print("The frequency of the element",el,"is",cnt)
