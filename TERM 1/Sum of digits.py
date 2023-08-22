a=int(input("Enter a number"))
s=0
while a!=0:
    rem=a%10
    s=s+rem
    a=a//10
print("Sum of digits=",s)
    
