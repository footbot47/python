#read a string and print it in reverse
a=input("Enter a string")
print("The",a,"in reverse order is:")
lenght=len(a)
for i in range(-1,(-lenght-1),-1):
    print(a[i])
    
