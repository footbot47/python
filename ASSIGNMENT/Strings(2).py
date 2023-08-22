a=input("Enter a string")
l=len(a)
if l%4==0:
    for i in range(-1,-l,-1):
        print(a[i])
else:
    print(a,"is not a multiple of 4")
    

        
        
