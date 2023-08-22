#Armstrong
a=int(input("Enter a number"))
a1=a
while a!=0:
    rem=a%10
    a=a+rem**3
    a=a1//10
if s==a:
    print("Armstrong number")
else:
    print("Not an armstrong number")
