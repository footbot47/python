t=eval(input("Enter the tuple pairs"))
cnt=0
for (a,b) in t:
    if a%2==0 and b%2==0:
        cnt=cnt+1
print("The number of even tuples=",cnt)
